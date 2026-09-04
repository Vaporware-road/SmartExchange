# VideoQuality

> Source: [https://docs.aiogram.dev/en/latest/api/types/video_quality.html](https://docs.aiogram.dev/en/latest/api/types/video_quality.html)

*class* aiogram.types.video_quality.VideoQuality(*\**, *file_id: str*, *file_unique_id: str*, *width: int*, *height: int*, *codec: str*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a video file of a specific quality.

    Source: <https://core.telegram.org/bots/api#videoquality>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    width*: int*
    :   Video width

    height*: int*
    :   Video height

    codec*: str*
    :   Codec that was used to encode the video, for example, ‘h264’, ‘h265’, or ‘av01’

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value
