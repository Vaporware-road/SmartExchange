# InputRichMessageMedia

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_message_media.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_message_media.html)

*class* aiogram.types.input_rich_message_media.InputRichMessageMedia(*\**, *id: str*, *media: [InputMediaAnimation](input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation") | [InputMediaAudio](input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaPhoto](input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo") | [InputMediaVoiceNote](input_media_voice_note.html#aiogram.types.input_media_voice_note.InputMediaVoiceNote "aiogram.types.input_media_voice_note.InputMediaVoiceNote")*, *\*\*extra_data: Any*)
:   Describes a media element embedded in an outgoing rich message.

    Source: <https://core.telegram.org/bots/api#inputrichmessagemedia>

    id*: str*
    :   Unique identifier of the media used in a `tg://photo?id=`, `tg://video?id=`, or `tg://audio?id=` link. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed

    media*: InputRichMessageMediaUnion*
    :   The media to be sent. Everything except the media itself and its properties is ignored
