"""
Customer-bot conversation FSM.

Customer menus use Telegram *reply keyboards* (button panel under the input),
not inline message buttons. Tapping a button sends its label as text; we map
labels back to internal action tokens.
"""

from __future__ import annotations

import logging
from decimal import Decimal, InvalidOperation

from django.db.models import Count, Q
from django.utils import timezone

from ..models import (
    BotSession,
    CustomerProfile,
    ExchangeRequest,
    PriceAlert,
    TelegramBot,
)
from . import currency_catalog
from .admin_conversation import (
    go_admin_menu,
    handle_admin_action,
    handle_admin_text,
    resolve_admin_label,
)
from .admin_notify import notify_staff_of_exchange_request

logger = logging.getLogger(__name__)

DEFAULT_EXCHANGE_TTL_MINUTES = 5

# ── internal action tokens (mapped from reply-keyboard labels) ───────────────
CB_MENU_PROFILE = "menu:profile"
CB_MENU_EXCHANGE = "menu:exchange"
CB_MENU_NOTIFICATIONS = "menu:notifications"
CB_MENU_HOME = "menu:home"

CB_PROFILE_HISTORY = "profile:history"
CB_PROFILE_MOST = "profile:most"
CB_PROFILE_ID = "profile:id"
CB_PROFILE_BACK = "profile:back"
CB_PROFILE_RUNNING = "profile:running"
CB_PROFILE_CANCEL_PREFIX = "profile:cancel:"

CB_EXCH_CONFIRM = "exch:confirm"
CB_EXCH_EDIT = "exch:edit"
CB_EXCH_EDIT_SOURCE = "exch:ef:source"
CB_EXCH_EDIT_TARGET = "exch:ef:target"
CB_EXCH_EDIT_AMOUNT = "exch:ef:amount"
CB_EXCH_CANCEL = "exch:cancel"
CB_EXCH_SUMMARY = "exch:summary"

CB_ALERT_INC = "alert:inc"
CB_ALERT_DEC = "alert:dec"
CB_ALERT_CONFIRM = "alert:confirm"
CB_ALERT_EDIT = "alert:edit"
CB_ALERT_EDIT_SOURCE = "alert:ef:source"
CB_ALERT_EDIT_TARGET = "alert:ef:target"
CB_ALERT_EDIT_PRICE = "alert:ef:price"
CB_ALERT_CANCEL = "alert:cancel"
CB_ALERT_SUMMARY = "alert:summary"

# Visible reply-keyboard labels (shown in the Telegram button panel)
BTN_PROFILE = "Customer profile"
BTN_EXCHANGE = "Registering for exchange"
BTN_NOTIFICATIONS = "Notification System"
BTN_HOME = "Back to menu"
BTN_CANCEL = "Cancel"
BTN_BACK = "Back"
BTN_HISTORY = "History Of Requests"
BTN_RUNNING = "Current running exchanges"
BTN_MOST = "Most Requested Currencies"
BTN_ID = "ID"
BTN_CONFIRM = "Confirm"
BTN_EDIT = "Edit"
BTN_EXCH_SOURCE = "Source currency"
BTN_EXCH_TARGET = "Target currency"
BTN_EXCH_AMOUNT = "Amount"
BTN_BACK_SUMMARY = "Back to summary"
BTN_ALERT_INC = "Price increase Alert"
BTN_ALERT_DEC = "Price Decrease Alert"
BTN_ALERT_SOURCE = "Source currency"
BTN_ALERT_TARGET = "Target currency"
BTN_ALERT_PRICE = "Target price"
BTN_PREV = "◀ Prev"
BTN_NEXT = "Next ▶"

LABEL_TO_CB: dict[str, str] = {
    BTN_PROFILE: CB_MENU_PROFILE,
    BTN_EXCHANGE: CB_MENU_EXCHANGE,
    BTN_NOTIFICATIONS: CB_MENU_NOTIFICATIONS,
    BTN_HOME: CB_MENU_HOME,
    BTN_CANCEL: CB_MENU_HOME,
    BTN_BACK: CB_PROFILE_BACK,
    BTN_HISTORY: CB_PROFILE_HISTORY,
    BTN_RUNNING: CB_PROFILE_RUNNING,
    BTN_MOST: CB_PROFILE_MOST,
    BTN_ID: CB_PROFILE_ID,
    BTN_CONFIRM: CB_EXCH_CONFIRM,  # disambiguated by state below
    BTN_EDIT: CB_EXCH_EDIT,
    BTN_EXCH_SOURCE: CB_EXCH_EDIT_SOURCE,
    BTN_EXCH_TARGET: CB_EXCH_EDIT_TARGET,
    BTN_EXCH_AMOUNT: CB_EXCH_EDIT_AMOUNT,
    BTN_BACK_SUMMARY: CB_EXCH_SUMMARY,
    BTN_ALERT_INC: CB_ALERT_INC,
    BTN_ALERT_DEC: CB_ALERT_DEC,
}

MAIN_MENU_BUTTONS = [
    [{"text": BTN_PROFILE}],
    [{"text": BTN_EXCHANGE}],
    [{"text": BTN_NOTIFICATIONS}],
]

MAIN_MENU_TEXT = (
    "Welcome. Choose an option from the keyboard below "
    "(or open the Menu button next to the message field):\n\n"
    "1. Customer profile\n"
    "2. Registering for exchange\n"
    "3. Notification System"
)

CANCEL_ROW = [[{"text": BTN_CANCEL}]]

CMD_PROFILE = "/profile"
CMD_EXCHANGE = "/exchange"
CMD_NOTIFICATIONS = "/notifications"
CMD_ADMIN = "/admin"


def _btn(*labels: str) -> list[list[dict[str, str]]]:
    return [[{"text": label}] for label in labels]


def _reply(text: str, *, buttons=None, remove_keyboard: bool = False) -> dict:
    """Customer menus use the bottom reply-keyboard panel."""
    return {
        "text": text,
        "buttons": buttons,
        "keyboard": "reply",
        "remove_keyboard": remove_keyboard,
        "edit_previous": False,
        "message_id": None,
    }


def _normalize_command(text: str | None) -> str | None:
    raw = (text or "").strip()
    if not raw.startswith("/"):
        return None
    cmd = raw.split()[0].lower()
    if "@" in cmd:
        cmd = cmd.split("@", 1)[0]
    return cmd


def _persist(session: BotSession, *, fields: list[str]) -> None:
    update = list(dict.fromkeys(fields + ["last_activity", "updated_at"]))
    session.save(update_fields=update)


def _ctx(session: BotSession) -> dict:
    return dict(session.context or {})


def _set_ctx(session: BotSession, ctx: dict) -> None:
    session.context = ctx


def _draft(session: BotSession) -> dict:
    ctx = _ctx(session)
    draft = ctx.get("draft")
    if not isinstance(draft, dict):
        draft = {}
        ctx["draft"] = draft
        _set_ctx(session, ctx)
    return draft


def _clear_draft(session: BotSession) -> None:
    ctx = _ctx(session)
    ctx.pop("draft", None)
    _set_ctx(session, ctx)


def _parse_decimal(raw: str) -> Decimal | None:
    try:
        value = Decimal(str(raw).strip().replace(",", ""))
    except (InvalidOperation, AttributeError):
        return None
    if value <= 0:
        return None
    return value


def _resolve_label_action(session: BotSession, text: str) -> str | None:
    """Map a reply-keyboard label (or currency code) to an internal action token."""
    label = (text or "").strip()
    if not label:
        return None

    state = session.state
    draft = _draft(session)

    if label == BTN_CONFIRM:
        if state in (
            BotSession.State.ALERT_SUMMARY,
            BotSession.State.ALERT_MENU,
            BotSession.State.ALERT_SOURCE,
            BotSession.State.ALERT_TARGET,
            BotSession.State.ALERT_PRICE,
        ) or (draft.get("flow") == "alert"):
            return CB_ALERT_CONFIRM
        return CB_EXCH_CONFIRM

    # "Cancel #123" — cancel a running exchange from the profile list
    if label.startswith("Cancel #"):
        try:
            req_id = int(label.split("#", 1)[1].strip().split()[0])
            return f"{CB_PROFILE_CANCEL_PREFIX}{req_id}"
        except (IndexError, ValueError):
            pass

    if label == BTN_EDIT:
        if state == BotSession.State.ALERT_SUMMARY or draft.get("flow") == "alert":
            return CB_ALERT_EDIT
        return CB_EXCH_EDIT

    if label == BTN_BACK_SUMMARY:
        if state.startswith("ALERT") or draft.get("flow") == "alert":
            return CB_ALERT_SUMMARY
        return CB_EXCH_SUMMARY

    if label in (BTN_EXCH_SOURCE, BTN_ALERT_SOURCE) and (
        state.startswith("ALERT") or draft.get("flow") == "alert"
    ):
        return CB_ALERT_EDIT_SOURCE
    if label in (BTN_EXCH_TARGET, BTN_ALERT_TARGET) and (
        state.startswith("ALERT") or draft.get("flow") == "alert"
    ):
        return CB_ALERT_EDIT_TARGET
    if label == BTN_ALERT_PRICE and (
        state.startswith("ALERT") or draft.get("flow") == "alert"
    ):
        return CB_ALERT_EDIT_PRICE

    if label in LABEL_TO_CB:
        return LABEL_TO_CB[label]

    # Currency picker pagination / select / typed fuzzy match
    if state in (
        BotSession.State.EXCHANGE_SOURCE,
        BotSession.State.EXCHANGE_TARGET,
        BotSession.State.ALERT_SOURCE,
        BotSession.State.ALERT_TARGET,
    ):
        page = int(draft.get("currency_page") or 0)
        if label == BTN_PREV:
            return currency_catalog.encode_prev_callback(page)
        if label == BTN_NEXT:
            return currency_catalog.encode_next_callback(page)
        guessed = currency_catalog.guess_currency(label)
        if guessed is not None:
            return currency_catalog.encode_select_callback(guessed.code)

    return None


def _currency_keyboard(page: int, *, cancel_label: str = BTN_CANCEL) -> tuple[str, list]:
    items, page_index, has_prev, has_next = currency_catalog.paginate(page)
    total_pages = max(1, currency_catalog.page_count())
    lines = [f"Choose a currency (page {page_index + 1}/{total_pages}):"]
    rows: list[list[dict[str, str]]] = []
    pair: list[dict[str, str]] = []
    for cur in items:
        pair.append({"text": cur.code})
        if len(pair) == 2:
            rows.append(pair)
            pair = []
    if pair:
        rows.append(pair)
    nav: list[dict[str, str]] = []
    if has_prev:
        nav.append({"text": BTN_PREV})
    if has_next:
        nav.append({"text": BTN_NEXT})
    if nav:
        rows.append(nav)
    rows.append([{"text": cancel_label}])
    return "\n".join(lines), rows


def _exchange_currency_picker(*, role: str) -> tuple[str, list]:
    """
    Exchange and alert flows: top-10 most used currencies + Cancel.
    User may also type a code/name (typos are guessed).
    """
    top = currency_catalog.top_exchanged_currencies(10)
    lines = [
        f"Select {role} currency",
        "",
        "Top 10 most exchanged — tap one, or type a code/name",
        "(typos are OK, e.g. \"dolr\" → USD):",
        "",
    ]
    for i, cur in enumerate(top, start=1):
        lines.append(f"{i}. {cur.code} — {cur.name}")
    rows: list[list[dict[str, str]]] = []
    pair: list[dict[str, str]] = []
    for cur in top:
        pair.append({"text": cur.code})
        if len(pair) == 2:
            rows.append(pair)
            pair = []
    if pair:
        rows.append(pair)
    rows.append([{"text": BTN_CANCEL}])
    return "\n".join(lines), rows


class ConversationEngine:
    """State machine for customer Telegram conversations (reply keyboards)."""

    def __init__(self, bot: TelegramBot):
        self.bot = bot

    def get_or_create_session(self, telegram_user_id: int) -> BotSession:
        session, _ = BotSession.objects.get_or_create(
            telegram_user_id=telegram_user_id,
            bot=self.bot,
            defaults={"state": BotSession.State.START, "context": {}},
        )
        return session

    def _customer(self, session: BotSession) -> CustomerProfile | None:
        return CustomerProfile.objects.filter(
            telegram_user_id=session.telegram_user_id
        ).first()

    def process_update(
        self,
        session: BotSession,
        text: str | None = None,
        callback_data: str | None = None,
        message_id: int | None = None,
    ) -> dict:
        session.last_activity = timezone.now()

        # Reply-keyboard taps arrive as plain text messages.
        if callback_data is None and text and not text.strip().lower().startswith("/"):
            admin_mapped = resolve_admin_label(text)
            if admin_mapped is not None:
                callback_data = admin_mapped
                text = None
            else:
                mapped = _resolve_label_action(session, text)
                if mapped is not None:
                    callback_data = mapped
                    text = None

        cmd = _normalize_command(text)
        if cmd in ("/start", CMD_ADMIN):
            admin_home = go_admin_menu(session)
            if admin_home is not None:
                return admin_home
            if cmd == CMD_ADMIN:
                return _reply(
                    "You are not registered as an admin for this bot.\n"
                    "Ask a developer to set your numeric Telegram ID on a "
                    "super_admin or management account that owns this bot.",
                    buttons=MAIN_MENU_BUTTONS,
                )
            return self._go_main_menu(session)
        if cmd == CMD_PROFILE:
            return self._show_profile(session)
        if cmd == CMD_EXCHANGE:
            return self._start_exchange(session)
        if cmd == CMD_NOTIFICATIONS:
            return self._show_alert_menu(session)

        # In-bot admin panel (staff Telegram IDs — no login button)
        if (
            callback_data
            and str(callback_data).startswith("admin:")
        ) or str(session.state).startswith("ADMIN"):
            if text and not callback_data:
                text_result = handle_admin_text(session, text)
                if text_result is not None:
                    return text_result
            admin_result = handle_admin_action(session, callback_data)
            if isinstance(admin_result, dict) and admin_result.get("_switch_customer"):
                return self._go_main_menu(session)
            if admin_result is not None:
                return admin_result

        if callback_data == CB_MENU_HOME:
            # Staff landing on "Back to menu" from customer flows → admin home
            admin_home = go_admin_menu(session)
            if admin_home is not None:
                return admin_home
            return self._go_main_menu(session)

        if callback_data == CB_MENU_PROFILE:
            return self._show_profile(session)

        if callback_data == CB_MENU_EXCHANGE:
            return self._start_exchange(session)

        if callback_data == CB_MENU_NOTIFICATIONS:
            return self._show_alert_menu(session)

        if session.state == BotSession.State.PROFILE or callback_data in (
            CB_PROFILE_HISTORY,
            CB_PROFILE_MOST,
            CB_PROFILE_ID,
            CB_PROFILE_BACK,
            CB_PROFILE_RUNNING,
            CB_MENU_PROFILE,
        ) or (callback_data or "").startswith(CB_PROFILE_CANCEL_PREFIX):
            handled = self._handle_profile(session, text, callback_data)
            if handled is not None:
                return handled

        catalog_cb = currency_catalog.decode_catalog_callback(callback_data or "")
        if catalog_cb is not None:
            handled = self._handle_currency_callback(session, catalog_cb)
            if handled is not None:
                return handled

        if session.state in (
            BotSession.State.EXCHANGE_SOURCE,
            BotSession.State.EXCHANGE_TARGET,
            BotSession.State.EXCHANGE_AMOUNT,
            BotSession.State.EXCHANGE_PRICE,
            BotSession.State.EXCHANGE_TTL,
            BotSession.State.EXCHANGE_SUMMARY,
        ) or (callback_data or "").startswith("exch:"):
            handled = self._handle_exchange(session, text, callback_data)
            if handled is not None:
                return handled

        if session.state in (
            BotSession.State.ALERT_MENU,
            BotSession.State.ALERT_SOURCE,
            BotSession.State.ALERT_TARGET,
            BotSession.State.ALERT_PRICE,
            BotSession.State.ALERT_SUMMARY,
        ) or (callback_data or "").startswith("alert:"):
            handled = self._handle_alert(session, text, callback_data)
            if handled is not None:
                return handled

        if session.state in (BotSession.State.START, BotSession.State.MAIN_MENU):
            return self._go_main_menu(session)

        return self._go_main_menu(session)

    def _go_main_menu(self, session: BotSession) -> dict:
        _clear_draft(session)
        session.state = BotSession.State.MAIN_MENU
        _persist(session, fields=["state", "context"])
        return _reply(MAIN_MENU_TEXT, buttons=MAIN_MENU_BUTTONS)

    def _show_profile(self, session: BotSession) -> dict:
        session.state = BotSession.State.PROFILE
        _persist(session, fields=["state"])
        customer = self._customer(session)
        tag = customer.tag if customer else CustomerProfile.Tag.GLOBAL
        body = f"Customer profile\nTag: {tag}"
        buttons = _btn(BTN_HISTORY, BTN_RUNNING, BTN_MOST, BTN_ID, BTN_HOME)
        return _reply(body, buttons=buttons)

    def _list_running_exchanges(self, customer: CustomerProfile) -> list[ExchangeRequest]:
        qs = ExchangeRequest.objects.filter(
            customer=customer,
            status=ExchangeRequest.Status.NEW,
        ).filter(Q(bot=self.bot) | Q(bot__isnull=True)).order_by("-created_at")[:40]
        return [req for req in qs if req.is_running()][:10]

    def _cancel_button_label(self, req: ExchangeRequest) -> str:
        return f"Cancel #{req.pk}"

    def _show_running_exchanges(self, session: BotSession) -> dict:
        session.state = BotSession.State.PROFILE
        _persist(session, fields=["state"])
        customer = self._customer(session)
        back = _btn(BTN_BACK)
        if customer is None:
            return _reply("No running exchanges.", buttons=back)
        running = self._list_running_exchanges(customer)
        if not running:
            return _reply("No running exchanges.", buttons=back)
        lines = ["Current running exchanges:", "Tap Cancel #id to cancel one.", ""]
        rows: list[list[dict[str, str]]] = []
        for req in running:
            mins_left = max(
                0,
                int((req.expires_at() - timezone.now()).total_seconds() // 60),
            )
            lines.append(
                f"#{req.pk} {req.source_currency}→{req.target_currency} "
                f"{req.amount} · ~{mins_left}m left · {req.status}"
            )
            rows.append([{"text": self._cancel_button_label(req)}])
        rows.append([{"text": BTN_BACK}])
        return _reply("\n".join(lines), buttons=rows)

    def _cancel_running_exchange(self, session: BotSession, req_id: int) -> dict:
        customer = self._customer(session)
        if customer is None:
            return self._show_running_exchanges(session)
        req = (
            ExchangeRequest.objects.filter(
                pk=req_id,
                customer=customer,
            )
            .filter(Q(bot=self.bot) | Q(bot__isnull=True))
            .first()
        )
        if req is None or not req.is_running():
            out = self._show_running_exchanges(session)
            out["text"] = "That exchange is not running (or already ended).\n\n" + (
                out["text"] or ""
            )
            return out
        req.status = ExchangeRequest.Status.CANCELLED
        req.save(update_fields=["status", "updated_at"])
        out = self._show_running_exchanges(session)
        out["text"] = (
            f"Cancelled #{req.pk} ({req.source_currency}→{req.target_currency}).\n\n"
            + (out["text"] or "")
        )
        return out

    def _handle_profile(
        self, session: BotSession, text: str | None, callback_data: str | None
    ) -> dict | None:
        if callback_data == CB_MENU_PROFILE or callback_data == CB_PROFILE_BACK:
            return self._show_profile(session)

        if callback_data == CB_PROFILE_RUNNING:
            return self._show_running_exchanges(session)

        if callback_data and callback_data.startswith(CB_PROFILE_CANCEL_PREFIX):
            try:
                req_id = int(callback_data[len(CB_PROFILE_CANCEL_PREFIX) :])
            except ValueError:
                return self._show_running_exchanges(session)
            return self._cancel_running_exchange(session, req_id)

        back = _btn(BTN_BACK)
        if callback_data == CB_PROFILE_ID:
            return _reply(
                f"Your Telegram ID: {session.telegram_user_id}",
                buttons=back,
            )

        if callback_data == CB_PROFILE_HISTORY:
            customer = self._customer(session)
            if customer is None:
                return _reply("No requests yet.", buttons=back)
            qs = ExchangeRequest.objects.filter(customer=customer).order_by("-created_at")[
                :10
            ]
            if not qs:
                return _reply("No requests yet.", buttons=back)
            lines = ["History Of Requests:"]
            for req in qs:
                price_bit = (
                    f" @ {req.price_at_request}"
                    if req.price_at_request is not None
                    else ""
                )
                lines.append(
                    f"• {req.source_currency}→{req.target_currency} "
                    f"{req.amount}{price_bit} ({req.status})"
                )
            return _reply("\n".join(lines), buttons=back)

        if callback_data == CB_PROFILE_MOST:
            customer = self._customer(session)
            if customer is None:
                return _reply("No data yet.", buttons=back)
            rows = (
                ExchangeRequest.objects.filter(customer=customer)
                .values("source_currency", "target_currency")
                .annotate(c=Count("id"))
                .order_by("-c")[:5]
            )
            if not rows:
                return _reply("No data yet.", buttons=back)
            lines = ["Most Requested Currencies:"]
            for row in rows:
                lines.append(
                    f"• {row['source_currency']}→{row['target_currency']} ({row['c']})"
                )
            return _reply("\n".join(lines), buttons=back)

        if callback_data == CB_MENU_HOME:
            return self._go_main_menu(session)

        return self._show_profile(session)

    def _start_exchange(self, session: BotSession) -> dict:
        draft = _draft(session)
        draft.clear()
        draft["flow"] = "exchange"
        session.state = BotSession.State.EXCHANGE_SOURCE
        _persist(session, fields=["state", "context"])
        body, buttons = _exchange_currency_picker(role="source")
        return _reply(body, buttons=buttons)

    def _ask_currency(
        self, session: BotSession, *, prompt: str, page: int
    ) -> dict:
        draft = _draft(session)
        # Exchange and alert flows share top-10 + type-to-guess.
        if draft.get("flow") in ("exchange", "alert") or session.state in (
            BotSession.State.EXCHANGE_SOURCE,
            BotSession.State.EXCHANGE_TARGET,
            BotSession.State.ALERT_SOURCE,
            BotSession.State.ALERT_TARGET,
        ):
            role = (
                "source"
                if session.state
                in (
                    BotSession.State.EXCHANGE_SOURCE,
                    BotSession.State.ALERT_SOURCE,
                )
                else "target"
            )
            body, buttons = _exchange_currency_picker(role=role)
            return _reply(body, buttons=buttons)
        draft["currency_page"] = page
        _persist(session, fields=["context"])
        body, buttons = _currency_keyboard(page)
        return _reply(f"{prompt}\n{body}", buttons=buttons)

    def _handle_currency_callback(self, session: BotSession, catalog_cb) -> dict | None:
        kind = catalog_cb.kind
        draft = _draft(session)
        page = int(draft.get("currency_page") or 0)

        if kind == "page":
            page = int(catalog_cb.page or 0)
        elif kind == "select":
            code = catalog_cb.code
            if session.state == BotSession.State.EXCHANGE_SOURCE:
                draft["source_currency"] = code
                if draft.get("editing") == "source":
                    draft.pop("editing", None)
                    return self._show_exchange_summary(session)
                session.state = BotSession.State.EXCHANGE_TARGET
                draft["currency_page"] = 0
                _persist(session, fields=["state", "context"])
                cur = currency_catalog.get_currency(code)
                label = f"{cur.code} — {cur.name}" if cur else code
                body, buttons = _exchange_currency_picker(role="target")
                return _reply(
                    f"Source set to {label}.\n\n{body}",
                    buttons=buttons,
                )
            if session.state == BotSession.State.EXCHANGE_TARGET:
                draft["target_currency"] = code
                if draft.get("editing") == "target":
                    draft.pop("editing", None)
                    return self._show_exchange_summary(session)
                session.state = BotSession.State.EXCHANGE_AMOUNT
                _persist(session, fields=["state", "context"])
                cur = currency_catalog.get_currency(code)
                label = f"{cur.code} — {cur.name}" if cur else code
                return _reply(
                    f"Target set to {label}.\nEnter amount:",
                    buttons=CANCEL_ROW,
                )
            if session.state == BotSession.State.ALERT_SOURCE:
                draft["source_currency"] = code
                if draft.get("editing") == "source":
                    draft.pop("editing", None)
                    return self._show_alert_summary(session)
                session.state = BotSession.State.ALERT_TARGET
                draft["currency_page"] = 0
                _persist(session, fields=["state", "context"])
                cur = currency_catalog.get_currency(code)
                label = f"{cur.code} — {cur.name}" if cur else code
                body, buttons = _exchange_currency_picker(role="target")
                return _reply(
                    f"Source set to {label}.\n\n{body}",
                    buttons=buttons,
                )
            if session.state == BotSession.State.ALERT_TARGET:
                draft["target_currency"] = code
                if draft.get("editing") == "target":
                    draft.pop("editing", None)
                    return self._show_alert_summary(session)
                session.state = BotSession.State.ALERT_PRICE
                _persist(session, fields=["state", "context"])
                cur = currency_catalog.get_currency(code)
                label = f"{cur.code} — {cur.name}" if cur else code
                return _reply(
                    f"Target set to {label}.\nEnter target price:",
                    buttons=CANCEL_ROW,
                )
            return None
        else:
            return None

        if session.state in (
            BotSession.State.EXCHANGE_SOURCE,
            BotSession.State.ALERT_SOURCE,
        ):
            prompt = "Select source currency:"
        else:
            prompt = "Select target currency:"
        return self._ask_currency(session, prompt=prompt, page=page)

    def _show_exchange_summary(self, session: BotSession) -> dict:
        draft = _draft(session)
        session.state = BotSession.State.EXCHANGE_SUMMARY
        _persist(session, fields=["state", "context"])
        body = (
            "Exchange request summary:\n"
            f"Source: {draft.get('source_currency')}\n"
            f"Target: {draft.get('target_currency')}\n"
            f"Amount: {draft.get('amount')}"
        )
        buttons = [
            [{"text": BTN_CONFIRM}, {"text": BTN_EDIT}],
            [{"text": BTN_CANCEL}],
        ]
        return _reply(body, buttons=buttons)

    def _recover_legacy_exchange_price_ttl(self, session: BotSession) -> dict | None:
        """Sessions stuck on removed price/TTL steps resume at summary or amount."""
        if session.state not in (
            BotSession.State.EXCHANGE_PRICE,
            BotSession.State.EXCHANGE_TTL,
        ):
            return None
        draft = _draft(session)
        draft.pop("price_at_request", None)
        draft.pop("ttl_minutes", None)
        draft.pop("editing", None)
        if (
            draft.get("source_currency")
            and draft.get("target_currency")
            and draft.get("amount")
        ):
            return self._show_exchange_summary(session)
        session.state = BotSession.State.EXCHANGE_AMOUNT
        _persist(session, fields=["state", "context"])
        return _reply("Enter amount:", buttons=CANCEL_ROW)

    def _handle_exchange(
        self, session: BotSession, text: str | None, callback_data: str | None
    ) -> dict | None:
        draft = _draft(session)

        recovered = self._recover_legacy_exchange_price_ttl(session)
        if recovered is not None:
            return recovered

        if callback_data == CB_EXCH_CANCEL or callback_data == CB_MENU_HOME:
            return self._go_main_menu(session)

        if callback_data == CB_EXCH_EDIT:
            buttons = _btn(
                BTN_EXCH_SOURCE,
                BTN_EXCH_TARGET,
                BTN_EXCH_AMOUNT,
                BTN_BACK_SUMMARY,
            )
            return _reply("What do you want to edit?", buttons=buttons)

        if callback_data == CB_EXCH_SUMMARY:
            return self._show_exchange_summary(session)

        if callback_data == CB_EXCH_EDIT_SOURCE:
            draft["editing"] = "source"
            draft["currency_page"] = 0
            session.state = BotSession.State.EXCHANGE_SOURCE
            _persist(session, fields=["state", "context"])
            return self._ask_currency(session, prompt="Select source currency:", page=0)

        if callback_data == CB_EXCH_EDIT_TARGET:
            draft["editing"] = "target"
            draft["currency_page"] = 0
            session.state = BotSession.State.EXCHANGE_TARGET
            _persist(session, fields=["state", "context"])
            return self._ask_currency(session, prompt="Select target currency:", page=0)

        if callback_data == CB_EXCH_EDIT_AMOUNT:
            draft["editing"] = "amount"
            session.state = BotSession.State.EXCHANGE_AMOUNT
            _persist(session, fields=["state", "context"])
            return _reply("Enter amount:", buttons=CANCEL_ROW)

        if callback_data == CB_EXCH_CONFIRM:
            if session.state != BotSession.State.EXCHANGE_SUMMARY:
                return self._show_exchange_summary(session)
            return self._confirm_exchange(session)

        if session.state == BotSession.State.EXCHANGE_AMOUNT and text:
            amount = _parse_decimal(text)
            if amount is None:
                return _reply(
                    "Invalid amount. Enter a positive number:",
                    buttons=CANCEL_ROW,
                )
            draft["amount"] = str(amount)
            draft.pop("editing", None)
            return self._show_exchange_summary(session)

        if session.state in (
            BotSession.State.EXCHANGE_SOURCE,
            BotSession.State.EXCHANGE_TARGET,
        ):
            if text:
                role = (
                    "source"
                    if session.state == BotSession.State.EXCHANGE_SOURCE
                    else "target"
                )
                body, buttons = _exchange_currency_picker(role=role)
                return _reply(
                    f"Could not understand \"{text.strip()}\". "
                    f"Tap a top currency or type a clearer code/name.\n\n{body}",
                    buttons=buttons,
                )
            role = (
                "source"
                if session.state == BotSession.State.EXCHANGE_SOURCE
                else "target"
            )
            body, buttons = _exchange_currency_picker(role=role)
            return _reply(body, buttons=buttons)

        return None

    def _bot_ttl_minutes(self) -> int:
        ttl = getattr(self.bot, "default_exchange_ttl_minutes", None)
        try:
            value = int(ttl) if ttl is not None else DEFAULT_EXCHANGE_TTL_MINUTES
        except (TypeError, ValueError):
            value = DEFAULT_EXCHANGE_TTL_MINUTES
        return value if value >= 1 else DEFAULT_EXCHANGE_TTL_MINUTES

    def _confirm_exchange(self, session: BotSession) -> dict:
        draft = _draft(session)
        customer = self._customer(session)
        if customer is None:
            customer = CustomerProfile.objects.create(
                telegram_user_id=session.telegram_user_id
            )
        try:
            req = ExchangeRequest.objects.create(
                customer=customer,
                bot=self.bot,
                source_currency=str(draft["source_currency"]),
                target_currency=str(draft["target_currency"]),
                amount=Decimal(str(draft["amount"])),
                price_at_request=None,
                ttl_minutes=self._bot_ttl_minutes(),
                status=ExchangeRequest.Status.NEW,
            )
            currency_catalog.clear_currency_cache()
        except Exception:
            logger.exception("exchange confirm failed user=%s", session.telegram_user_id)
            return _reply(
                "Could not save the request. Please try again.",
                buttons=MAIN_MENU_BUTTONS,
            )

        try:
            notify_staff_of_exchange_request(req, bot=self.bot)
        except Exception:
            logger.exception("admin_notify crashed request_id=%s", req.pk)

        _clear_draft(session)
        session.state = BotSession.State.MAIN_MENU
        _persist(session, fields=["state", "context"])
        return _reply(
            "The Operator will contact you very soon",
            buttons=MAIN_MENU_BUTTONS,
        )

    def _show_alert_menu(self, session: BotSession) -> dict:
        session.state = BotSession.State.ALERT_MENU
        _clear_draft(session)
        _persist(session, fields=["state", "context"])
        buttons = _btn(BTN_ALERT_INC, BTN_ALERT_DEC, BTN_HOME)
        return _reply(
            "Notification System\nChoose an alert type:",
            buttons=buttons,
        )

    def _start_alert(self, session: BotSession, *, direction: str) -> dict:
        draft = _draft(session)
        draft.clear()
        draft["flow"] = "alert"
        draft["direction"] = direction
        draft["currency_page"] = 0
        session.state = BotSession.State.ALERT_SOURCE
        _persist(session, fields=["state", "context"])
        if direction == PriceAlert.Direction.INCREASE:
            intro = "If the price Grow upper than the target the bot will Alarm you"
        else:
            intro = "If the price fall lower than the target the bot will Alarm you"
        body, buttons = _exchange_currency_picker(role="source")
        return _reply(f"{intro}\n\n{body}", buttons=buttons)

    def _show_alert_summary(self, session: BotSession) -> dict:
        draft = _draft(session)
        session.state = BotSession.State.ALERT_SUMMARY
        _persist(session, fields=["state", "context"])
        body = (
            "Alert summary:\n"
            f"Direction: {draft.get('direction')}\n"
            f"Source: {draft.get('source_currency')}\n"
            f"Target: {draft.get('target_currency')}\n"
            f"Target price: {draft.get('target_price')}"
        )
        buttons = [
            [{"text": BTN_CONFIRM}, {"text": BTN_EDIT}],
            [{"text": BTN_CANCEL}],
        ]
        return _reply(body, buttons=buttons)

    def _handle_alert(
        self, session: BotSession, text: str | None, callback_data: str | None
    ) -> dict | None:
        draft = _draft(session)

        if callback_data == CB_ALERT_CANCEL or callback_data == CB_MENU_HOME:
            return self._go_main_menu(session)

        if callback_data == CB_ALERT_INC:
            return self._start_alert(
                session, direction=PriceAlert.Direction.INCREASE
            )
        if callback_data == CB_ALERT_DEC:
            return self._start_alert(
                session, direction=PriceAlert.Direction.DECREASE
            )

        if callback_data == CB_ALERT_EDIT:
            buttons = _btn(
                BTN_ALERT_SOURCE,
                BTN_ALERT_TARGET,
                BTN_ALERT_PRICE,
                BTN_BACK_SUMMARY,
            )
            return _reply("What do you want to edit?", buttons=buttons)

        if callback_data == CB_ALERT_SUMMARY:
            return self._show_alert_summary(session)

        if callback_data == CB_ALERT_EDIT_SOURCE:
            draft["editing"] = "source"
            draft["currency_page"] = 0
            session.state = BotSession.State.ALERT_SOURCE
            _persist(session, fields=["state", "context"])
            return self._ask_currency(session, prompt="Select source currency:", page=0)

        if callback_data == CB_ALERT_EDIT_TARGET:
            draft["editing"] = "target"
            draft["currency_page"] = 0
            session.state = BotSession.State.ALERT_TARGET
            _persist(session, fields=["state", "context"])
            return self._ask_currency(session, prompt="Select target currency:", page=0)

        if callback_data == CB_ALERT_EDIT_PRICE:
            draft["editing"] = "price"
            session.state = BotSession.State.ALERT_PRICE
            _persist(session, fields=["state", "context"])
            return _reply("Enter target price:", buttons=CANCEL_ROW)

        if callback_data == CB_ALERT_CONFIRM:
            if session.state != BotSession.State.ALERT_SUMMARY:
                return self._show_alert_summary(session)
            return self._confirm_alert(session)

        if session.state == BotSession.State.ALERT_PRICE and text:
            price = _parse_decimal(text)
            if price is None:
                return _reply(
                    "Invalid price. Enter a positive number:",
                    buttons=CANCEL_ROW,
                )
            draft["target_price"] = str(price)
            draft.pop("editing", None)
            return self._show_alert_summary(session)

        if session.state == BotSession.State.ALERT_MENU:
            return self._show_alert_menu(session)

        if session.state in (
            BotSession.State.ALERT_SOURCE,
            BotSession.State.ALERT_TARGET,
        ):
            if text:
                role = (
                    "source"
                    if session.state == BotSession.State.ALERT_SOURCE
                    else "target"
                )
                body, buttons = _exchange_currency_picker(role=role)
                return _reply(
                    f"Could not understand \"{text.strip()}\". "
                    f"Tap a top currency or type a clearer code/name.\n\n{body}",
                    buttons=buttons,
                )
            role = (
                "source"
                if session.state == BotSession.State.ALERT_SOURCE
                else "target"
            )
            body, buttons = _exchange_currency_picker(role=role)
            return _reply(body, buttons=buttons)

        return None

    def _confirm_alert(self, session: BotSession) -> dict:
        draft = _draft(session)
        customer = self._customer(session)
        if customer is None:
            customer = CustomerProfile.objects.create(
                telegram_user_id=session.telegram_user_id
            )
        try:
            PriceAlert.objects.create(
                customer=customer,
                direction=str(draft["direction"]),
                source_currency=str(draft["source_currency"]),
                target_currency=str(draft["target_currency"]),
                target_price=Decimal(str(draft["target_price"])),
                is_active=True,
            )
        except Exception:
            logger.exception("alert confirm failed user=%s", session.telegram_user_id)
            return _reply(
                "Could not save the alert. Please try again.",
                buttons=MAIN_MENU_BUTTONS,
            )

        _clear_draft(session)
        session.state = BotSession.State.MAIN_MENU
        _persist(session, fields=["state", "context"])
        return _reply(
            "Confirmed.\n\n" + MAIN_MENU_TEXT,
            buttons=MAIN_MENU_BUTTONS,
        )
