# VideoNote

> Source: [https://docs.aiogram.dev/en/latest/api/types/video_note.html](https://docs.aiogram.dev/en/latest/api/types/video_note.html)

*class* aiogram.types.video_note.VideoNote(*\**, *file_id: str*, *file_unique_id: str*, *length: int*, *duration: int*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope) (available in Telegram apps as of [v.4.0](https://telegram.org/blog/video-messages-and-telescope)).

    Source: <https://core.telegram.org/bots/api#videonote>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    length*: int*
    :   Video width and height (diameter of the video message) as defined by the sender

    duration*: int*
    :   Duration of the video in seconds as defined by the sender

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Video thumbnail

    file_size*: int | None*
    :   *Optional*. File size in bytes
