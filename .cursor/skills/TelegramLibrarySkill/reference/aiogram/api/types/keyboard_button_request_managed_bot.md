# KeyboardButtonRequestManagedBot

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_managed_bot.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_managed_bot.html)

*class* aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot(*\**, *request_id: int*, *suggested_name: str | None = None*, *suggested_username: str | None = None*, *\*\*extra_data: Any*)
:   This object defines the parameters for the creation of a managed bot. Information about the created bot will be shared with the bot using the update *managed_bot* and a [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") with the field *managed_bot_created*.

    Source: <https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot>

    request_id*: int*
    :   Signed 32-bit identifier of the request. Must be unique within the message

    suggested_name*: str | None*
    :   *Optional*. Suggested name for the bot

    suggested_username*: str | None*
    :   *Optional*. Suggested username for the bot
