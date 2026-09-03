# editMessageReplyMarkup

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_reply_markup.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_reply_markup.html)

Returns: `Message | bool`

*class* aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup(*\**, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

    Source: <https://core.telegram.org/bots/api#editmessagereplymarkup>

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message to edit

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message | bool = await bot.edit_message_reply_markup(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_reply_markup import EditMessageReplyMarkup`
- alias: `from aiogram.methods import EditMessageReplyMarkup`

#### With specific bot

```
result: Message | bool = await bot(EditMessageReplyMarkup(...))
```

#### As reply into Webhook in handler

```
return EditMessageReplyMarkup(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_reply_markup()`](../types/message.html#aiogram.types.message.Message.edit_reply_markup "aiogram.types.message.Message.edit_reply_markup")
- [`aiogram.types.message.Message.delete_reply_markup()`](../types/message.html#aiogram.types.message.Message.delete_reply_markup "aiogram.types.message.Message.delete_reply_markup")
