# editEphemeralMessageText

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_text.html](https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_text.html)

Returns: `bool`

*class* aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText(*\**, *chat_id: int | str*, *receiver_user_id: int*, *ephemeral_message_id: int*, *text: str*, *parse_mode: str | None = None*, *entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *link_preview_options: [LinkPreviewOptions](../types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit an ephemeral text message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

    Source: <https://core.telegram.org/bots/api#editephemeralmessagetext>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    receiver_user_id*: int*
    :   Identifier of the user who received the message

    ephemeral_message_id*: int*
    :   Identifier of the ephemeral message to edit

    text*: str*
    :   New text of the message, 1-4096 characters after entity parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*

    link_preview_options*: [LinkPreviewOptions](../types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None*
    :   Link preview generation options for the message

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: bool = await bot.edit_ephemeral_message_text(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_ephemeral_message_text import EditEphemeralMessageText`
- alias: `from aiogram.methods import EditEphemeralMessageText`

#### With specific bot

```
result: bool = await bot(EditEphemeralMessageText(...))
```

#### As reply into Webhook in handler

```
return EditEphemeralMessageText(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_ephemeral_text()`](../types/message.html#aiogram.types.message.Message.edit_ephemeral_text "aiogram.types.message.Message.edit_ephemeral_text")
