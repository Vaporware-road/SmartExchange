# InputMediaPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_media_photo.html)

*class* aiogram.types.input_media_photo.InputMediaPhoto(*\**, *type: ~typing.Literal[InputMediaType.PHOTO] = InputMediaType.PHOTO*, *media: str | ~aiogram.types.input_file.InputFile*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a photo to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediaphoto>

    type*: Literal[InputMediaType.PHOTO]*
    :   Type of the media, must be *photo*

    media*: InputFileUnion*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    caption*: str | None*
    :   *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    has_spoiler*: bool | None*
    :   *Optional*. Pass `True` if the photo needs to be covered with a spoiler animation
