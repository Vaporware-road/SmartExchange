# Voice

> Source: [https://docs.aiogram.dev/en/latest/api/types/voice.html](https://docs.aiogram.dev/en/latest/api/types/voice.html)

*class* aiogram.types.voice.Voice(*\**, *file_id: str*, *file_unique_id: str*, *duration: int*, *mime_type: str | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a voice note.

    Source: <https://core.telegram.org/bots/api#voice>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    duration*: int*
    :   Duration of the audio in seconds as defined by the sender

    mime_type*: str | None*
    :   *Optional*. MIME type of the file as defined by the sender

    file_size*: int | None*
    :   *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value
