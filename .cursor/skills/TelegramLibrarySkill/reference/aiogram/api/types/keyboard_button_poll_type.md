# KeyboardButtonPollType

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button_poll_type.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button_poll_type.html)

*class* aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType(*\**, *type: str | None = None*, *\*\*extra_data: Any*)
:   This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    Source: <https://core.telegram.org/bots/api#keyboardbuttonpolltype>

    type*: str | None*
    :   *Optional*. If *quiz* is passed, the user will be allowed to create only polls in the quiz mode. If *regular* is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type
