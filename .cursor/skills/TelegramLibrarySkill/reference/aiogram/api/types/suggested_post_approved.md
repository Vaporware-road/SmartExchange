# SuggestedPostApproved

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_approved.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_approved.html)

*class* aiogram.types.suggested_post_approved.SuggestedPostApproved(*\**, *send_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *suggested_post_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *price: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about the approval of a suggested post.

    Source: <https://core.telegram.org/bots/api#suggestedpostapproved>

    send_date*: DateTime*
    :   Date when the post will be published

    suggested_post_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the suggested post. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    price*: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None*
    :   *Optional*. Amount paid for the post
