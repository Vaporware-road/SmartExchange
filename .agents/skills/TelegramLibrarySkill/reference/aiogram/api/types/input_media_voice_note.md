# InputMediaVoiceNote

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_voice_note.html](https://docs.aiogram.dev/en/latest/api/types/input_media_voice_note.html)

*class* aiogram.types.input_media_voice_note.InputMediaVoiceNote(*\**, *type: Literal['voice_note'] = 'voice_note'*, *media: str*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *duration: int | None = None*, *\*\*extra_data: Any*)
:   Represents a voice message file to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediavoicenote>

    type*: Literal['voice_note']*
    :   Type of the media, must be *voice_note*

    media*: str*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    caption*: str | None*
    :   *Optional*. Caption of the voice message to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | None*
    :   *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    duration*: int | None*
    :   *Optional*. Duration of the voice message in seconds
