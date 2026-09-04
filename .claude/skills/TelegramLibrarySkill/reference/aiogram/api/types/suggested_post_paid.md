# SuggestedPostPaid

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_paid.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_paid.html)

*class* aiogram.types.suggested_post_paid.SuggestedPostPaid(*\**, *currency: str*, *suggested_post_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *amount: int | None = None*, *star_amount: [StarAmount](star_amount.html#aiogram.types.star_amount.StarAmount "aiogram.types.star_amount.StarAmount") | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about a successful payment for a suggested post.

    Source: <https://core.telegram.org/bots/api#suggestedpostpaid>

    currency*: str*
    :   Currency in which the payment was made. Currently, one of ‘XTR’ for Telegram Stars or ‘TON’ for TON grams

    suggested_post_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the suggested post. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    amount*: int | None*
    :   *Optional*. The amount of the currency that was received by the channel in nanograms; for payments in TON grams only

    star_amount*: [StarAmount](star_amount.html#aiogram.types.star_amount.StarAmount "aiogram.types.star_amount.StarAmount") | None*
    :   *Optional*. The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only
