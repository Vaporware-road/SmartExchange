"""
Dev long-polling for customer Telegram bots when HTTPS webhook is unavailable.

Uses one persistent asyncio loop + aiogram Bot/Dispatcher per token.

Usage:
  python manage.py poll_telegram_bots
  python manage.py poll_telegram_bots --bot-id 1 --once
  python manage.py poll_telegram_bots --register-webhooks
"""

from __future__ import annotations

import asyncio
import signal

from aiogram.exceptions import TelegramAPIError, TelegramConflictError
from django.core.management.base import BaseCommand

from telegram_app.bot.factory import close_cached_bots, get_bot_and_dispatcher
from telegram_app.models import TelegramBot
from telegram_app.services.dispatcher import sync_webhooks_from_site_settings


def bots_one_per_token(bots: list[TelegramBot]) -> tuple[list[TelegramBot], list[tuple[TelegramBot, TelegramBot]]]:
    """Telegram allows one getUpdates client per BotFather token.

    Keep the lowest-id row for each distinct token; return skipped (duplicate, keeper) pairs.
    """
    keepers: list[TelegramBot] = []
    skipped: list[tuple[TelegramBot, TelegramBot]] = []
    seen: dict[str, TelegramBot] = {}
    for bot in bots:
        token = (bot.get_plain_token() or "").strip()
        if not token:
            continue
        keeper = seen.get(token)
        if keeper is not None:
            skipped.append((bot, keeper))
            continue
        seen[token] = bot
        keepers.append(bot)
    return keepers, skipped


class Command(BaseCommand):
    help = (
        "Poll getUpdates for active customer bots (clears webhook first), "
        "or register HTTPS webhooks from SiteSettings.telegram_webhook_base_url."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--bot-id",
            type=int,
            default=None,
            help="Only poll / register this bot id.",
        )
        parser.add_argument(
            "--once",
            action="store_true",
            help="Fetch one getUpdates batch per bot then exit.",
        )
        parser.add_argument(
            "--timeout",
            type=int,
            default=25,
            help="Long-poll timeout seconds (1-50).",
        )
        parser.add_argument(
            "--register-webhooks",
            action="store_true",
            help="Call setWebhook for active bots using SiteSettings base URL, then exit.",
        )

    def handle(self, *args, **options):
        if options["register_webhooks"]:
            results = sync_webhooks_from_site_settings()
            if not results:
                self.stdout.write(
                    self.style.WARNING(
                        "No webhooks registered (set SiteSettings.telegram_webhook_base_url to https://...)."
                    )
                )
                return
            for row in results:
                style = self.style.SUCCESS if row.get("ok") else self.style.ERROR
                self.stdout.write(
                    style(
                        f"bot_id={row.get('bot_id')} ok={row.get('ok')} "
                        f"url={row.get('url')} detail={row.get('detail')}"
                    )
                )
            return

        qs = TelegramBot.objects.filter(is_active=True).order_by("id")
        requested_id = options["bot_id"]
        if requested_id is not None:
            qs = qs.filter(pk=requested_id)
        bots = list(qs)
        if not bots:
            self.stderr.write(self.style.ERROR("No active Telegram bots found."))
            return

        if requested_id is None:
            bots, skipped = bots_one_per_token(bots)
            for duplicate, keeper in skipped:
                self.stderr.write(
                    self.style.WARNING(
                        f"Skipping bot_id={duplicate.pk} ({duplicate.name!r}): same BotFather "
                        f"token as bot_id={keeper.pk} ({keeper.name!r}). Telegram allows only "
                        "one getUpdates client per token. Give this bot its own token, or "
                        f"poll one of them with --bot-id {keeper.pk}."
                    )
                )
            if not bots:
                self.stderr.write(self.style.ERROR("No unique bot tokens to poll."))
                return
        else:
            token = (bots[0].get_plain_token() or "").strip()
            siblings = [
                other
                for other in TelegramBot.objects.filter(is_active=True).exclude(pk=requested_id)
                if token and (other.get_plain_token() or "").strip() == token
            ]
            if siblings:
                names = ", ".join(f"bot_id={b.pk} ({b.name!r})" for b in siblings)
                self.stderr.write(
                    self.style.WARNING(
                        f"bot_id={requested_id} shares a BotFather token with {names}. "
                        "Do not run another poller for those rows."
                    )
                )

        stop = {"flag": False}

        def _stop(*_args):
            stop["flag"] = True

        signal.signal(signal.SIGINT, _stop)
        signal.signal(signal.SIGTERM, _stop)

        timeout = max(1, min(50, int(options["timeout"])))
        once = bool(options["once"])

        self.stdout.write(
            self.style.SUCCESS(f"Polling {len(bots)} bot(s). Ctrl+C to stop.")
        )
        asyncio.run(self._poll_all(bots, timeout=timeout, once=once, stop=stop))
        self.stdout.write("Polling stopped.")

    async def _poll_all(self, bots, *, timeout: int, once: bool, stop: dict):
        try:
            await asyncio.gather(
                *(
                    self._poll_one(bot, timeout=timeout, once=once, stop=stop)
                    for bot in bots
                )
            )
        finally:
            await close_cached_bots()

    async def _poll_one(
        self, bot_row: TelegramBot, *, timeout: int, once: bool, stop: dict
    ):
        bot, dp = get_bot_and_dispatcher(bot_row)
        offsets: dict[int, int | None] = {bot_row.pk: None}
        try:
            await bot.delete_webhook(drop_pending_updates=True)
            self.stdout.write(f"Cleared webhook for bot_id={bot_row.pk}")
        except Exception as exc:
            self.stderr.write(
                self.style.ERROR(f"deleteWebhook bot_id={bot_row.pk} failed: {exc}")
            )
            return

        while not stop["flag"]:
            try:
                updates = await bot.get_updates(
                    offset=offsets[bot_row.pk],
                    timeout=timeout,
                    limit=100,
                )
            except TelegramConflictError as exc:
                self.stderr.write(
                    f"getUpdates bot_id={bot_row.pk} conflict: {exc}. "
                    "Another process is already polling this token "
                    "(second poller, duplicate bot row, or a remote instance). "
                    "Retrying in 5s."
                )
                await asyncio.sleep(5)
                continue
            except TelegramAPIError as exc:
                self.stderr.write(f"getUpdates bot_id={bot_row.pk} failed: {exc}")
                await asyncio.sleep(1)
                continue
            except Exception as exc:
                self.stderr.write(f"getUpdates bot_id={bot_row.pk} failed: {exc}")
                await asyncio.sleep(1)
                continue

            for update in updates:
                offsets[bot_row.pk] = update.update_id + 1
                try:
                    fresh = await asyncio.to_thread(
                        lambda: TelegramBot.objects.filter(
                            pk=bot_row.pk, is_active=True
                        ).first()
                    )
                    if fresh is None:
                        continue
                    dp["django_bot"] = fresh
                    await dp.feed_update(bot, update)
                except Exception as exc:
                    self.stderr.write(
                        f"process_update bot_id={bot_row.pk} error: {exc}"
                    )

            if once:
                break
