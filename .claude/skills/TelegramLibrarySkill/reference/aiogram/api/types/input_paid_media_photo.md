# InputPaidMediaPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_paid_media_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_paid_media_photo.html)

*class* aiogram.types.input_paid_media_photo.InputPaidMediaPhoto(*\**, *type: Literal[InputPaidMediaType.PHOTO] = InputPaidMediaType.PHOTO*, *media: str | [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *\*\*extra_data: Any*)
:   The paid media to send is a photo.

    Source: <https://core.telegram.org/bots/api#inputpaidmediaphoto>

    type*: Literal[InputPaidMediaType.PHOTO]*
    :   Type of the media, must be *photo*

    media*: InputFileUnion*
    :   File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)
