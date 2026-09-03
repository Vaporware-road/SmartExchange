# Audio

> Source: [https://docs.aiogram.dev/en/latest/api/types/audio.html](https://docs.aiogram.dev/en/latest/api/types/audio.html)

*class* aiogram.types.audio.Audio(*\**, *file_id: str*, *file_unique_id: str*, *duration: int*, *performer: str | None = None*, *title: str | None = None*, *file_name: str | None = None*, *mime_type: str | None = None*, *file_size: int | None = None*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *\*\*extra_data: Any*)
:   This object represents an audio file to be treated as music by the Telegram clients.

    Source: <https://core.telegram.org/bots/api#audio>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    duration*: int*
    :   Duration of the audio in seconds as defined by the sender

    performer*: str | None*
    :   *Optional*. Performer of the audio as defined by the sender or by audio tags

    title*: str | None*
    :   *Optional*. Title of the audio as defined by the sender or by audio tags

    file_name*: str | None*
    :   *Optional*. Original filename as defined by the sender

    mime_type*: str | None*
    :   *Optional*. MIME type of the file as defined by the sender

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Thumbnail of the album cover to which the music file belongs
