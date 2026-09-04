# UsersShared

> Source: [https://docs.aiogram.dev/en/latest/api/types/users_shared.html](https://docs.aiogram.dev/en/latest/api/types/users_shared.html)

*class* aiogram.types.users_shared.UsersShared(*\**, *request_id: int*, *users: list[[SharedUser](shared_user.html#aiogram.types.shared_user.SharedUser "aiogram.types.shared_user.SharedUser")]*, *user_ids: list[int] | None = None*, *\*\*extra_data: Any*)
:   This object contains information about the users whose identifiers were shared with the bot using a [`aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers`](keyboard_button_request_users.html#aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers "aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers") button.

    Source: <https://core.telegram.org/bots/api#usersshared>

    request_id*: int*
    :   Identifier of the request

    users*: list[[SharedUser](shared_user.html#aiogram.types.shared_user.SharedUser "aiogram.types.shared_user.SharedUser")]*
    :   Information about users shared with the bot

    user_ids*: list[int] | None*
    :   Identifiers of the shared users. These numbers may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting them. But they have at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the users and could be unable to use these identifiers, unless the users are already known to the bot by some other means

        Deprecated since version API:7.2: <https://core.telegram.org/bots/api-changelog#march-31-2024>
