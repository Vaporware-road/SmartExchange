# ChatPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_photo.html](https://docs.aiogram.dev/en/latest/api/types/chat_photo.html)

*class* aiogram.types.chat_photo.ChatPhoto(*\**, *small_file_id: str*, *small_file_unique_id: str*, *big_file_id: str*, *big_file_unique_id: str*, *\*\*extra_data: Any*)
:   This object represents a chat photo.

    Source: <https://core.telegram.org/bots/api#chatphoto>

    small_file_id*: str*
    :   File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed

    small_file_unique_id*: str*
    :   Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    big_file_id*: str*
    :   File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed

    big_file_unique_id*: str*
    :   Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file
