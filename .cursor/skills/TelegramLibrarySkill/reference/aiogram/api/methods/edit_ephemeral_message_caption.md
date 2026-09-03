# editEphemeralMessageCaption

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_caption.html](https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_caption.html)

Returns: `bool`

*class* aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption(*\**, *chat_id: int | str*, *receiver_user_id: int*, *ephemeral_message_id: int*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit the caption of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

    Source: <https://core.telegram.org/bots/api#editephemeralmessagecaption>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    receiver_user_id*: int*
    :   Identifier of the user who received the message

    ephemeral_message_id*: int*
    :   Identifier of the ephemeral message to edit

    caption*: str | None*
    :   New caption of the message, 0-1024 characters after entities parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: bool = await bot.edit_ephemeral_message_caption(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_ephemeral_message_caption import EditEphemeralMessageCaption`
- alias: `from aiogram.methods import EditEphemeralMessageCaption`

#### With specific bot

```
result: bool = await bot(EditEphemeralMessageCaption(...))
```

#### As reply into Webhook in handler

```
return EditEphemeralMessageCaption(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_ephemeral_caption()`](../types/message.html#aiogram.types.message.Message.edit_ephemeral_caption "aiogram.types.message.Message.edit_ephemeral_caption")
