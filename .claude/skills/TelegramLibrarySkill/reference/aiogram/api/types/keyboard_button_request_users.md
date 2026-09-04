# KeyboardButtonRequestUsers

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_users.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_users.html)

*class* aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers(*\**, *request_id: int*, *user_is_bot: bool | None = None*, *user_is_premium: bool | None = None*, *max_quantity: int | None = None*, *request_name: bool | None = None*, *request_username: bool | None = None*, *request_photo: bool | None = None*, *\*\*extra_data: Any*)
:   This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. [More about requesting users »](https://core.telegram.org/bots/features#chat-and-user-selection)

    Source: <https://core.telegram.org/bots/api#keyboardbuttonrequestusers>

    request_id*: int*
    :   Signed 32-bit identifier of the request that will be received back in the [`aiogram.types.users_shared.UsersShared`](users_shared.html#aiogram.types.users_shared.UsersShared "aiogram.types.users_shared.UsersShared") object. Must be unique within the message

    user_is_bot*: bool | None*
    :   *Optional*. Pass `True` to request bots, pass `False` to request regular users. If not specified, no additional restrictions are applied

    user_is_premium*: bool | None*
    :   *Optional*. Pass `True` to request premium users, pass `False` to request non-premium users. If not specified, no additional restrictions are applied

    max_quantity*: int | None*
    :   *Optional*. The maximum number of users to be selected; 1-10. Defaults to 1

    request_name*: bool | None*
    :   *Optional*. Pass `True` to request the users’ first and last names

    request_username*: bool | None*
    :   *Optional*. Pass `True` to request the users’ usernames

    request_photo*: bool | None*
    :   *Optional*. Pass `True` to request the users’ photos
