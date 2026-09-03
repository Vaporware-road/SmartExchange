# SuggestedPostApprovalFailed

> Source: [https://docs.aiogram.dev/en/latest/api/types/suggested_post_approval_failed.html](https://docs.aiogram.dev/en/latest/api/types/suggested_post_approval_failed.html)

*class* aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed(*\**, *price: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice")*, *suggested_post_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about the failed approval of a suggested post. Currently, only caused by insufficient user funds at the time of approval.

    Source: <https://core.telegram.org/bots/api#suggestedpostapprovalfailed>

    price*: [SuggestedPostPrice](suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice")*
    :   Expected price of the post

    suggested_post_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the suggested post whose approval has failed. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply
