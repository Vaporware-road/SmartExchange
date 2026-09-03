# InputPaidMediaVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_paid_media_video.html](https://docs.aiogram.dev/en/latest/api/types/input_paid_media_video.html)

*class* aiogram.types.input_paid_media_video.InputPaidMediaVideo(*\**, *type: Literal[InputPaidMediaType.VIDEO] = InputPaidMediaType.VIDEO*, *media: str | [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *thumbnail: [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None = None*, *cover: str | [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None = None*, *start_timestamp: datetime | timedelta | int | None = None*, *width: int | None = None*, *height: int | None = None*, *duration: int | None = None*, *supports_streaming: bool | None = None*, *\*\*extra_data: Any*)
:   The paid media to send is a video.

    Source: <https://core.telegram.org/bots/api#inputpaidmediavideo>

    type*: Literal[InputPaidMediaType.VIDEO]*
    :   Type of the media, must be *video*

    media*: InputFileUnion*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    thumbnail*: [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None*
    :   *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)

    cover*: InputFileUnion | None*
    :   *Optional*. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    start_timestamp*: DateTimeUnion | None*
    :   *Optional*. Start timestamp for the video in the message

    width*: int | None*
    :   *Optional*. Video width

    height*: int | None*
    :   *Optional*. Video height

    duration*: int | None*
    :   *Optional*. Video duration in seconds

    supports_streaming*: bool | None*
    :   *Optional*. Pass `True` if the uploaded video is suitable for streaming
