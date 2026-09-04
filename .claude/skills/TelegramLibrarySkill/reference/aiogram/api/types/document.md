# Document

> Source: [https://docs.aiogram.dev/en/latest/api/types/document.html](https://docs.aiogram.dev/en/latest/api/types/document.html)

*class* aiogram.types.document.Document(*\**, *file_id: str*, *file_unique_id: str*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *file_name: str | None = None*, *mime_type: str | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a general file (as opposed to [photos](https://core.telegram.org/bots/api#photosize), [voice messages](https://core.telegram.org/bots/api#voice) and [audio files](https://core.telegram.org/bots/api#audio)).

    Source: <https://core.telegram.org/bots/api#document>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Document thumbnail as defined by the sender

    file_name*: str | None*
    :   *Optional*. Original filename as defined by the sender

    mime_type*: str | None*
    :   *Optional*. MIME type of the file as defined by the sender

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value
