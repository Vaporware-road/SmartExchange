"""
Utility functions for logging application events.
"""
import json

from .models import Log


def _serialize_details(details):
    """Normalize details for DB: dict -> JSON string; str/None unchanged."""
    if details is None:
        return None
    if isinstance(details, dict):
        return json.dumps(details, ensure_ascii=False, default=str)
    return details


def log_event(level='INFO', source='system', message='', details=None, user=None):
    """
    Create a log entry in the database.

    ``details`` may be a str or a dict (stored as JSON for structured logs).
    """
    return Log.objects.create(
        level=level,
        source=source,
        message=message,
        details=_serialize_details(details),
        user=user,
    )


def log_structured(
    level='INFO',
    source='system',
    message='',
    *,
    event=None,
    user=None,
    **fields,
):
    """
    Persist a structured log row: ``details`` is JSON ``{ "event": ..., ... }``.
    """
    payload = {}
    if event is not None:
        payload['event'] = event
    for key, value in fields.items():
        if value is not None:
            payload[key] = value
    details = payload if payload else None
    return log_event(
        level=level,
        source=source,
        message=message,
        details=details,
        user=user,
    )


def log_telegram_event(level='INFO', message='', details=None, user=None):
    """Convenience function to log Telegram events."""
    return log_event(level=level, source='telegram', message=message, details=details, user=user)


def log_finalize_event(level='INFO', message='', details=None, user=None):
    """Convenience function to log Finalize events."""
    return log_event(level=level, source='finalize', message=message, details=details, user=user)


def log_price_publisher_event(level='INFO', message='', details=None, user=None):
    """Convenience function to log Price Publisher events."""
    return log_event(level=level, source='price_publisher', message=message, details=details, user=user)


def log_template_editor_event(level='INFO', message='', details=None, user=None):
    """Convenience function to log Template Editor events."""
    return log_event(level=level, source='template_editor', message=message, details=details, user=user)
