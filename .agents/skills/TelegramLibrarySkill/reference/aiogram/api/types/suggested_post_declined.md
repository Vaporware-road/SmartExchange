# SuggestedPostDeclined

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_declined.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_declined.html)

*class* aiogram.types.suggested_post_declined.SuggestedPostDeclined(*\**, *suggested_post_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *comment: str | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about the rejection of a suggested post.

    Source: <https://core.telegram.org/bots/api#suggestedpostdeclined>

    suggested_post_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the suggested post. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    comment*: str | None*
    :   *Optional*. Comment with which the post was declined
