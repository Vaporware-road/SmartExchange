# editMessageText

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_text.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_text.html)

Returns: `Message | bool`

*class* aiogram.methods.edit_message_text.EditMessageText(*\**, *text: str | None = None*, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *link_preview_options: ~aiogram.types.link_preview_options.LinkPreviewOptions | ~aiogram.client.default.Default | None = <Default('link_preview')>*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *rich_message: ~aiogram.types.input_rich_message.InputRichMessage | None = None*, *disable_web_page_preview: bool | ~aiogram.client.default.Default | None = <Default('link_preview_is_disabled')>*, *\*\*extra_data: ~typing.Any*)
:   Use this method to edit text, rich and [game](https://core.telegram.org/bots/api#games) messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

    Source: <https://core.telegram.org/bots/api#editmessagetext>

    text*: str | None*
    :   New text of the message, 1-4096 characters after entity parsing; required if *rich_message* isn’t specified

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message to edit

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    parse_mode*: str | Default | None*
    :   Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*

    link_preview_options*: [LinkPreviewOptions](../types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | Default | None*
    :   Link preview generation options for the message

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

    rich_message*: [InputRichMessage](../types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage") | None*
    :   New rich content of the message; required if *text* isn’t specified. Direct upload of new files isn’t supported when an inline message is edited

    disable_web_page_preview*: bool | Default | None*
    :   Disables link previews for links in this message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message | bool = await bot.edit_message_text(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_text import EditMessageText`
- alias: `from aiogram.methods import EditMessageText`

#### With specific bot

```
result: Message | bool = await bot(EditMessageText(...))
```

#### As reply into Webhook in handler

```
return EditMessageText(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_text()`](../types/message.html#aiogram.types.message.Message.edit_text "aiogram.types.message.Message.edit_text")
