# LivePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/live_photo.html](https://docs.aiogram.dev/en/latest/api/types/live_photo.html)

*class* aiogram.types.live_photo.LivePhoto(*\**, *file_id: str*, *file_unique_id: str*, *width: int*, *height: int*, *duration: int*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *mime_type: str | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a live photo.

    Source: <https://core.telegram.org/bots/api#livephoto>

    file_id*: str*
    :   Identifier for the video file which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for the video file which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    width*: int*
    :   Video width as defined by the sender

    height*: int*
    :   Video height as defined by the sender

    duration*: int*
    :   Duration of the video in seconds as defined by the sender

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Available sizes of the corresponding static photo

    mime_type*: str | None*
    :   *Optional*. MIME type of the file as defined by the sender

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value
