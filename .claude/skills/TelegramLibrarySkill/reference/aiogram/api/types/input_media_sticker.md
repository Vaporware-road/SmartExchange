# InputMediaSticker

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_sticker.html](https://docs.aiogram.dev/en/latest/api/types/input_media_sticker.html)

*class* aiogram.types.input_media_sticker.InputMediaSticker(*\**, *type: Literal[InputMediaType.STICKER] = InputMediaType.STICKER*, *media: str*, *emoji: str | None = None*, *\*\*extra_data: Any*)
:   Represents a sticker file to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediasticker>

    type*: Literal[InputMediaType.STICKER]*
    :   Type of the media, must be *sticker*

    media*: str*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a .WEBP sticker from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)

    emoji*: str | None*
    :   *Optional*. Emoji associated with the sticker; only for just uploaded stickers
