# WebhookInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/webhook_info.html](https://docs.aiogram.dev/en/latest/api/types/webhook_info.html)

*class* aiogram.types.webhook_info.WebhookInfo(*\**, *url: str*, *has_custom_certificate: bool*, *pending_update_count: int*, *ip_address: str | None = None*, *last_error_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *last_error_message: str | None = None*, *last_synchronization_error_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *max_connections: int | None = None*, *allowed_updates: list[str] | None = None*, *\*\*extra_data: Any*)
:   Describes the current status of a webhook.

    Source: <https://core.telegram.org/bots/api#webhookinfo>

    url*: str*
    :   Webhook URL, may be empty if webhook is not set up

    has_custom_certificate*: bool*
    :   `True`, if a custom certificate was provided for webhook certificate checks

    pending_update_count*: int*
    :   Number of updates awaiting delivery

    ip_address*: str | None*
    :   *Optional*. Currently used webhook IP address

    last_error_date*: DateTime | None*
    :   *Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook

    last_error_message*: str | None*
    :   *Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook

    last_synchronization_error_date*: DateTime | None*
    :   *Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters

    max_connections*: int | None*
    :   *Optional*. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery

    allowed_updates*: list[str] | None*
    :   *Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat_member*, *message_reaction*, and *message_reaction_count*
