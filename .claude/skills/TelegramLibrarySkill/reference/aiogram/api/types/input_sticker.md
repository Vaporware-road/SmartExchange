# InputSticker

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_sticker.html](https://docs.aiogram.dev/en/latest/api/types/input_sticker.html)

*class* aiogram.types.input_sticker.InputSticker(*\**, *sticker: str | [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *format: str*, *emoji_list: list[str]*, *mask_position: [MaskPosition](mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None = None*, *keywords: list[str] | None = None*, *\*\*extra_data: Any*)
:   This object describes a sticker to be added to a sticker set.

    Source: <https://core.telegram.org/bots/api#inputsticker>

    sticker*: InputFileUnion*
    :   The added sticker. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new file using multipart/form-data under <file_attach_name> name. Animated and video stickers can’t be uploaded via HTTP URL. [More information on Sending Files »](../upload_file.html#sending-files)

    format*: str*
    :   Format of the added sticker, must be one of ‘static’ for a **.WEBP** or **.PNG** image, ‘animated’ for a **.TGS** animation, ‘video’ for a **.WEBM** video

    emoji_list*: list[str]*
    :   List of 1-20 emoji associated with the sticker

    mask_position*: [MaskPosition](mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None*
    :   *Optional*. Position where the mask should be placed on faces. For ‘mask’ stickers only

    keywords*: list[str] | None*
    :   *Optional*. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For ‘regular’ and ‘custom_emoji’ stickers only
