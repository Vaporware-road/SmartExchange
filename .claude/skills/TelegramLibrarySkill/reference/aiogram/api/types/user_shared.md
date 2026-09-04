# UserShared

> Source: [https://docs.aiogram.dev/en/latest/api/types/user_shared.html](https://docs.aiogram.dev/en/latest/api/types/user_shared.html)

*class* aiogram.types.user_shared.UserShared(*\**, *request_id: int*, *user_id: int*, *\*\*extra_data: Any*)
:   This object contains information about the user whose identifier was shared with the bot using a [`aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser`](keyboard_button_request_user.html#aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser "aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser") button.

    Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    Source: <https://core.telegram.org/bots/api#usershared>

    request_id*: int*
    :   Identifier of the request

    user_id*: int*
    :   Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means
