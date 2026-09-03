# InputMediaLivePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_live_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_media_live_photo.html)

*class* aiogram.types.input_media_live_photo.InputMediaLivePhoto(*\**, *type: Literal[InputMediaType.LIVE_PHOTO] = InputMediaType.LIVE_PHOTO*, *media: str*, *photo: str*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *has_spoiler: bool | None = None*, *\*\*extra_data: Any*)
:   Represents a live photo to be sent.

    Source: <https://core.telegram.org/bots/api#inputmedialivephoto>

    type*: Literal[InputMediaType.LIVE_PHOTO]*
    :   Type of the media, must be *live_photo*

    media*: str*
    :   Video of the live photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported

    photo*: str*
    :   The static photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported

    caption*: str | None*
    :   *Optional*. Caption of the live photo to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | None*
    :   *Optional*. Mode for parsing entities in the live photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    has_spoiler*: bool | None*
    :   *Optional*. Pass `True` if the live photo needs to be covered with a spoiler animation
