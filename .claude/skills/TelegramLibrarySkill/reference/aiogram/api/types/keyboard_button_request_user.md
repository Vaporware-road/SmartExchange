# KeyboardButtonRequestUser

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_user.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_user.html)

*class* aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser(*\**, *request_id: int*, *user_is_bot: bool | None = None*, *user_is_premium: bool | None = None*, *\*\*extra_data: Any*)
:   This object defines the criteria used to request a suitable user. The identifier of the selected user will be shared with the bot when the corresponding button is pressed. [More about requesting users »](https://core.telegram.org/bots/features#chat-and-user-selection)

    Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    Source: <https://core.telegram.org/bots/api#keyboardbuttonrequestuser>

    request_id*: int*
    :   Signed 32-bit identifier of the request, which will be received back in the [`aiogram.types.user_shared.UserShared`](user_shared.html#aiogram.types.user_shared.UserShared "aiogram.types.user_shared.UserShared") object. Must be unique within the message

    user_is_bot*: bool | None*
    :   *Optional*. Pass `True` to request a bot, pass `False` to request a regular user. If not specified, no additional restrictions are applied

    user_is_premium*: bool | None*
    :   *Optional*. Pass `True` to request a premium user, pass `False` to request a non-premium user. If not specified, no additional restrictions are applied
