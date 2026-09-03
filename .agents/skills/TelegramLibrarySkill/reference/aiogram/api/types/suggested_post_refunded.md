# SuggestedPostRefunded

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_refunded.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_refunded.html)

*class* aiogram.types.suggested_post_refunded.SuggestedPostRefunded(*\**, *reason: str*, *suggested_post_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about a payment refund for a suggested post.

    Source: <https://core.telegram.org/bots/api#suggestedpostrefunded>

    reason*: str*
    :   Reason for the refund. Currently, one of ‘post_deleted’ if the post was deleted within 24 hours of being posted or removed from scheduled messages without being posted, or ‘payment_refunded’ if the payer refunded their payment

    suggested_post_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the suggested post. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply
