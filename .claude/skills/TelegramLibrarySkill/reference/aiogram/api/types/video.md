# Video

> Source: [https://docs.aiogram.dev/en/latest/api/types/video.html](https://docs.aiogram.dev/en/latest/api/types/video.html)

*class* aiogram.types.video.Video(*\**, *file_id: str*, *file_unique_id: str*, *width: int*, *height: int*, *duration: int*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *cover: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *start_timestamp: datetime | None = None*, *qualities: list[[VideoQuality](video_quality.html#aiogram.types.video_quality.VideoQuality "aiogram.types.video_quality.VideoQuality")] | None = None*, *file_name: str | None = None*, *mime_type: str | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a video file.

    Source: <https://core.telegram.org/bots/api#video>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    width*: int*
    :   Video width as defined by the sender

    height*: int*
    :   Video height as defined by the sender

    duration*: int*
    :   Duration of the video in seconds as defined by the sender

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Video thumbnail

    cover*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Available sizes of the cover of the video in the message

    start_timestamp*: datetime.datetime | None*
    :   *Optional*. Timestamp in seconds from which the video will play in the message

    qualities*: list[[VideoQuality](video_quality.html#aiogram.types.video_quality.VideoQuality "aiogram.types.video_quality.VideoQuality")] | None*
    :   *Optional*. List of available qualities of the video

    file_name*: str | None*
    :   *Optional*. Original filename as defined by the sender

    mime_type*: str | None*
    :   *Optional*. MIME type of the file as defined by the sender

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value
