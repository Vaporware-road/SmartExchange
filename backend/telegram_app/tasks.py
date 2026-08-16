from celery import shared_task

from .services.alert_checker import check_price_alerts


@shared_task(name="telegram_app.check_price_alerts")
def check_price_alerts_task():
    """Celery beat entry: compare board prices to active customer alerts."""
    return check_price_alerts()
