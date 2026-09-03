# SuggestedPostParameters

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_parameters.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_parameters.html)

*class* aiogram.types.suggested_post_parameters.SuggestedPostParameters(*\**, *price: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None = None*, *send_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *\*\*extra_data: Any*)
:   Contains parameters of a post that is being suggested by the bot.

    Source: <https://core.telegram.org/bots/api#suggestedpostparameters>

    price*: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") | None*
    :   *Optional*. Proposed price for the post. If the field is omitted, then the post is unpaid

    send_date*: DateTime | None*
    :   *Optional*. Proposed send date of the post. If specified, then the date must be between 300 second and 2678400 seconds (30 days) in the future. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user who approves it
