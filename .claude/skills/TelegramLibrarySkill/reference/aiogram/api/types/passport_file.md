# PassportFile

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_file.html](https://docs.aiogram.dev/en/latest/api/types/passport_file.html)

*class* aiogram.types.passport_file.PassportFile(*\**, *file_id: str*, *file_unique_id: str*, *file_size: int*, *file_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *\*\*extra_data: Any*)
:   This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don’t exceed 10MB.

    Source: <https://core.telegram.org/bots/api#passportfile>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    file_size*: int*
    :   File size in bytes

    file_date*: DateTime*
    :   Unix time when the file was uploaded
