# ReplyKeyboardMarkup

> Source: [https://docs.aiogram.dev/en/latest/api/types/reply_keyboard_markup.html](https://docs.aiogram.dev/en/latest/api/types/reply_keyboard_markup.html)

*class* aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup(*\**, *keyboard: list[list[[KeyboardButton](keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")]]*, *is_persistent: bool | None = None*, *resize_keyboard: bool | None = None*, *one_time_keyboard: bool | None = None*, *input_field_placeholder: str | None = None*, *selective: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a [custom keyboard](https://core.telegram.org/bots/features#keyboards) with reply options (see [Introduction to bots](https://core.telegram.org/bots/features#keyboards) for details and examples). Not supported in channels and for messages sent on behalf of a business account.

    Source: <https://core.telegram.org/bots/api#replykeyboardmarkup>

    keyboard*: list[list[[KeyboardButton](keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")]]*
    :   Array of button rows, each represented by an Array of [`aiogram.types.keyboard_button.KeyboardButton`](keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton") objects

    is_persistent*: bool | None*
    :   *Optional*. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to `False`, in which case the custom keyboard can be hidden and opened with a keyboard icon

    resize_keyboard*: bool | None*
    :   *Optional*. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to `False`, in which case the custom keyboard is always of the same height as the app’s standard keyboard

    one_time_keyboard*: bool | None*
    :   *Optional*. Requests clients to hide the keyboard as soon as it’s been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to `False`

    input_field_placeholder*: str | None*
    :   *Optional*. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters

    selective*: bool | None*
    :   *Optional*. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the *text* of the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object; 2) if the bot’s message is a reply to a message in the same chat and forum topic, sender of the original message
