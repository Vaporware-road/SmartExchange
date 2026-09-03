# editEphemeralMessageReplyMarkup

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_reply_markup.html](https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_reply_markup.html)

Returns: `bool`

*class* aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup(*\**, *chat_id: int | str*, *receiver_user_id: int*, *ephemeral_message_id: int*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit only the reply markup of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

    Source: <https://core.telegram.org/bots/api#editephemeralmessagereplymarkup>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    receiver_user_id*: int*
    :   Identifier of the user who received the message

    ephemeral_message_id*: int*
    :   Identifier of the ephemeral message to edit

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: bool = await bot.edit_ephemeral_message_reply_markup(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_ephemeral_message_reply_markup import EditEphemeralMessageReplyMarkup`
- alias: `from aiogram.methods import EditEphemeralMessageReplyMarkup`

#### With specific bot

```
result: bool = await bot(EditEphemeralMessageReplyMarkup(...))
```

#### As reply into Webhook in handler

```
return EditEphemeralMessageReplyMarkup(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_ephemeral_reply_markup()`](../types/message.html#aiogram.types.message.Message.edit_ephemeral_reply_markup "aiogram.types.message.Message.edit_ephemeral_reply_markup")
