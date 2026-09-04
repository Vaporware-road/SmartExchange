# SuggestedPostInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_info.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_info.html)

*class* aiogram.types.suggested_post_info.SuggestedPostInfo(*\**, *state: str*, *price: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None = None*, *send_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *\*\*extra_data: Any*)
:   Contains information about a suggested post.

    Source: <https://core.telegram.org/bots/api#suggestedpostinfo>

    state*: str*
    :   State of the suggested post. Currently, it can be one of ‘pending’, ‘approved’, ‘declined’

    price*: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None*
    :   *Optional*. Proposed price of the post. If the field is omitted, then the post is unpaid

    send_date*: DateTime | None*
    :   *Optional*. Proposed send date of the post. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user or administrator who approves it
