# editEphemeralMessageMedia

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_media.html](https://docs.aiogram.dev/en/latest/api/methods/edit_ephemeral_message_media.html)

Returns: `bool`

*class* aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia(*\**, *chat_id: int | str*, *receiver_user_id: int*, *ephemeral_message_id: int*, *media: [InputMediaAnimation](../types/input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation") | [InputMediaAudio](../types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaDocument](../types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument") | [InputMediaLivePhoto](../types/input_media_live_photo.html#aiogram.types.input_media_live_photo.InputMediaLivePhoto "aiogram.types.input_media_live_photo.InputMediaLivePhoto") | [InputMediaPhoto](../types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](../types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo")*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit the media of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

    Source: <https://core.telegram.org/bots/api#editephemeralmessagemedia>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    receiver_user_id*: int*
    :   Identifier of the user who received the message

    ephemeral_message_id*: int*
    :   Identifier of the ephemeral message to edit

    media*: Annotated[[InputMediaAnimation](../types/input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation") | [InputMediaAudio](../types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaDocument](../types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument") | [InputMediaLivePhoto](../types/input_media_live_photo.html#aiogram.types.input_media_live_photo.InputMediaLivePhoto "aiogram.types.input_media_live_photo.InputMediaLivePhoto") | [InputMediaPhoto](../types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](../types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]*
    :   A JSON-serialized object for the new media content of the message. A new file can’t be uploaded; use a previously uploaded file via its file_id or specify a URL

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: bool = await bot.edit_ephemeral_message_media(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_ephemeral_message_media import EditEphemeralMessageMedia`
- alias: `from aiogram.methods import EditEphemeralMessageMedia`

#### With specific bot

```
result: bool = await bot(EditEphemeralMessageMedia(...))
```

#### As reply into Webhook in handler

```
return EditEphemeralMessageMedia(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_ephemeral_media()`](../types/message.html#aiogram.types.message.Message.edit_ephemeral_media "aiogram.types.message.Message.edit_ephemeral_media")
