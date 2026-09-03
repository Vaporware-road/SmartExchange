# SharedUser

> Source: [https://docs.aiogram.dev/en/latest/api/types/shared_user.html](https://docs.aiogram.dev/en/latest/api/types/shared_user.html)

*class* aiogram.types.shared_user.SharedUser(*\**, *user_id: int*, *first_name: str | None = None*, *last_name: str | None = None*, *username: str | None = None*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *\*\*extra_data: Any*)
:   This object contains information about a user that was shared with the bot using a [`aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers`](keyboard_button_request_users.html#aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers "aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers") button.

    Source: <https://core.telegram.org/bots/api#shareduser>

    user_id*: int*
    :   Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means

    first_name*: str | None*
    :   *Optional*. First name of the user, if the name was requested by the bot

    last_name*: str | None*
    :   *Optional*. Last name of the user, if the name was requested by the bot

    username*: str | None*
    :   *Optional*. Username of the user, if the username was requested by the bot

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Available sizes of the chat photo, if the photo was requested by the bot
