# editMessageMedia

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_media.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_media.html)

Returns: `Message | bool`

*class* aiogram.methods.edit_message_media.EditMessageMedia(*\**, *media: [InputMediaAnimation](../types/input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation") | [InputMediaAudio](../types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaDocument](../types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument") | [InputMediaLivePhoto](../types/input_media_live_photo.html#aiogram.types.input_media_live_photo.InputMediaLivePhoto "aiogram.types.input_media_live_photo.InputMediaLivePhoto") | [InputMediaPhoto](../types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](../types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo")*, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can’t be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

    Source: <https://core.telegram.org/bots/api#editmessagemedia>

    media*: InputMediaUnion*
    :   A JSON-serialized object for the new media content of the message

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message to edit

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message | bool = await bot.edit_message_media(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_media import EditMessageMedia`
- alias: `from aiogram.methods import EditMessageMedia`

#### With specific bot

```
result: Message | bool = await bot(EditMessageMedia(...))
```

#### As reply into Webhook in handler

```
return EditMessageMedia(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_media()`](../types/message.html#aiogram.types.message.Message.edit_media "aiogram.types.message.Message.edit_media")
