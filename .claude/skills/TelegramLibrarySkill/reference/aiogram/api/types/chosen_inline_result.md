# ChosenInlineResult

> Source: [https://docs.aiogram.dev/en/latest/api/types/chosen_inline_result.html](https://docs.aiogram.dev/en/latest/api/types/chosen_inline_result.html)

*class* aiogram.types.chosen_inline_result.ChosenInlineResult(*\**, *result_id: str*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *query: str*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None = None*, *inline_message_id: str | None = None*, *\*\*extra_data: Any*)
:   Represents a [result](https://core.telegram.org/bots/api#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.
    **Note:** It is necessary to enable [inline feedback](https://core.telegram.org/bots/inline#collecting-feedback) via [@BotFather](https://t.me/botfather) in order to receive these objects in updates.

    Source: <https://core.telegram.org/bots/api#choseninlineresult>

    result_id*: str*
    :   The unique identifier for the result that was chosen

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   The user that chose the result

    query*: str*
    :   The query that was used to obtain the result

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None*
    :   *Optional*. Sender location, only for bots that require user location

    inline_message_id*: str | None*
    :   *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api#updating-messages) the message
