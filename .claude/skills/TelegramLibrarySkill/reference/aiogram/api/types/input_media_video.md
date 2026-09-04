# InputMediaVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_video.html](https://docs.aiogram.dev/en/latest/api/types/input_media_video.html)

*class* aiogram.types.input_media_video.InputMediaVideo(*\**, *type: ~typing.Literal[InputMediaType.VIDEO] = InputMediaType.VIDEO*, *media: str | ~aiogram.types.input_file.InputFile*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *cover: str | ~aiogram.types.input_file.InputFile | None = None*, *start_timestamp: ~datetime.datetime | ~datetime.timedelta | int | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *width: int | None = None*, *height: int | None = None*, *duration: int | None = None*, *supports_streaming: bool | None = None*, *has_spoiler: bool | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a video to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediavideo>

    type*: Literal[InputMediaType.VIDEO]*
    :   Type of the media, must be *video*

    media*: InputFileUnion*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    thumbnail*: [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None*
    :   *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)

    cover*: InputFileUnion | None*
    :   *Optional*. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    start_timestamp*: DateTimeUnion | None*
    :   *Optional*. Start timestamp for the video in the message

    caption*: str | None*
    :   *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    width*: int | None*
    :   *Optional*. Video width

    height*: int | None*
    :   *Optional*. Video height

    duration*: int | None*
    :   *Optional*. Video duration in seconds

    supports_streaming*: bool | None*
    :   *Optional*. Pass `True` if the uploaded video is suitable for streaming

    has_spoiler*: bool | None*
    :   *Optional*. Pass `True` if the video needs to be covered with a spoiler animation
