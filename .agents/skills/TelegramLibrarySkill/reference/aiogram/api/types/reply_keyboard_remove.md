# ReplyKeyboardRemove

> Source: [https://docs.aiogram.dev/en/latest/api/types/reply_keyboard_remove.html](https://docs.aiogram.dev/en/latest/api/types/reply_keyboard_remove.html)

*class* aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove(*\**, *remove_keyboard: Literal[True] = True*, *selective: bool | None = None*, *\*\*extra_data: Any*)
:   Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see [`aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup`](reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup")). Not supported in channels and for messages sent on behalf of a business account.

    Source: <https://core.telegram.org/bots/api#replykeyboardremove>

    remove_keyboard*: Literal[True]*
    :   Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use *one_time_keyboard* in [`aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup`](reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup"))

    selective*: bool | None*
    :   *Optional*. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the *text* of the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object; 2) if the bot’s message is a reply to a message in the same chat and forum topic, sender of the original message
