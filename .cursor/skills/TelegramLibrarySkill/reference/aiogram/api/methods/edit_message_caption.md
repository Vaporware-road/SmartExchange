# editMessageCaption

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_caption.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_caption.html)

Returns: `Message | bool`

*class* aiogram.methods.edit_message_caption.EditMessageCaption(*\**, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

    Source: <https://core.telegram.org/bots/api#editmessagecaption>

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message to edit

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    caption*: str | None*
    :   New caption of the message, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   Pass `True` if the caption must be shown above the message media. Supported only for animation, photo and video messages

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message | bool = await bot.edit_message_caption(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_caption import EditMessageCaption`
- alias: `from aiogram.methods import EditMessageCaption`

#### With specific bot

```
result: Message | bool = await bot(EditMessageCaption(...))
```

#### As reply into Webhook in handler

```
return EditMessageCaption(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_caption()`](../types/message.html#aiogram.types.message.Message.edit_caption "aiogram.types.message.Message.edit_caption")
