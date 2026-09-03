# PhotoSize

> Source: [https://docs.aiogram.dev/en/latest/api/types/photo_size.html](https://docs.aiogram.dev/en/latest/api/types/photo_size.html)

*class* aiogram.types.photo_size.PhotoSize(*\**, *file_id: str*, *file_unique_id: str*, *width: int*, *height: int*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents one size of a photo or a [file](https://core.telegram.org/bots/api#document) / `aiogram.methods.sticker.Sticker` thumbnail.

    Source: <https://core.telegram.org/bots/api#photosize>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    width*: int*
    :   Photo width

    height*: int*
    :   Photo height

    file_size*: int | None*
    :   *Optional*. File size in bytes
