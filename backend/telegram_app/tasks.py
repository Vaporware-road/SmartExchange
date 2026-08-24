from celery import shared_task

from .models import TelegramBot
from .services.alert_checker import check_price_alerts
from .services.analytics_service import (
    snapshot_channel_members_for_bot,
    snapshot_customer_growth_for_bot,
    snapshot_daily_usage_for_bot,
)
from .services.auto_post import run_due_auto_posts
from .services.reengage_service import run_due_campaigns


@shared_task(name="telegram_app.auto_post_due_configs")
def auto_post_due_configs_task():
    """Celery beat entry: publish due AutoPostConfig records on their schedule."""
    return run_due_auto_posts()


@shared_task(name="telegram_app.check_price_alerts")
def check_price_alerts_task():
    """Celery beat entry: compare board prices to active customer alerts."""
    return check_price_alerts()


@shared_task(name="telegram_app.snapshot_daily_bot_usage")
def snapshot_daily_bot_usage_task():
    """Nightly: persist daily active user counts per bot."""
    results = {}
    for bot in TelegramBot.objects.filter(is_active=True):
        count = snapshot_daily_usage_for_bot(bot)
        results[bot.id] = count
    return results


@shared_task(name="telegram_app.snapshot_customer_growth")
def snapshot_customer_growth_task():
    """Nightly: persist new bot DM user counts per bot."""
    results = {}
    for bot in TelegramBot.objects.filter(is_active=True):
        count = snapshot_customer_growth_for_bot(bot)
        results[bot.id] = count
    return results


@shared_task(name="telegram_app.snapshot_channel_members")
def snapshot_channel_members_task():
    """Nightly: sample channel subscriber counts where bot is admin."""
    results = {}
    for bot in TelegramBot.objects.filter(is_active=True):
        results[bot.id] = snapshot_channel_members_for_bot(bot)
    return results


@shared_task(name="telegram_app.run_due_reengage_campaigns")
def run_due_reengage_campaigns_task():
    """Check and run periodic re-engage campaigns."""
    return run_due_campaigns()
