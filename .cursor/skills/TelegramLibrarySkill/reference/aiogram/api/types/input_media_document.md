# InputMediaDocument

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_document.html](https://docs.aiogram.dev/en/latest/api/types/input_media_document.html)

*class* aiogram.types.input_media_document.InputMediaDocument(*\**, *type: ~typing.Literal[InputMediaType.DOCUMENT] = InputMediaType.DOCUMENT*, *media: str | ~aiogram.types.input_file.InputFile*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a general file to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediadocument>

    type*: Literal[InputMediaType.DOCUMENT]*
    :   Type of the media, must be *document*

    media*: InputFileUnion*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    thumbnail*: [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None*
    :   *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)

    caption*: str | None*
    :   *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    disable_content_type_detection*: bool | None*
    :   *Optional*. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always `True`, if the document is sent as part of an album
