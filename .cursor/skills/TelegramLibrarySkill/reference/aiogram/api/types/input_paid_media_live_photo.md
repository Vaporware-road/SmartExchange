# InputPaidMediaLivePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_paid_media_live_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_paid_media_live_photo.html)

*class* aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto(*\**, *type: Literal[InputPaidMediaType.LIVE_PHOTO] = InputPaidMediaType.LIVE_PHOTO*, *media: str*, *photo: str*, *\*\*extra_data: Any*)
:   The paid media to send is a live photo.

    Source: <https://core.telegram.org/bots/api#inputpaidmedialivephoto>

    type*: Literal[InputPaidMediaType.LIVE_PHOTO]*
    :   Type of the media, must be *live_photo*

    media*: str*
    :   Video of the live photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported

    photo*: str*
    :   The static photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported
