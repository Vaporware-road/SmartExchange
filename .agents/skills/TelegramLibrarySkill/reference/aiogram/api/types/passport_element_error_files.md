# PassportElementErrorFiles

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_files.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_files.html)

*class* aiogram.types.passport_element_error_files.PassportElementErrorFiles(*\**, *source: Literal[PassportElementErrorType.FILES] = PassportElementErrorType.FILES*, *type: str*, *file_hashes: list[str]*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    Source: <https://core.telegram.org/bots/api#passportelementerrorfiles>

    source*: Literal[PassportElementErrorType.FILES]*
    :   Error source, must be *files*

    type*: str*
    :   The section of the user’s Telegram Passport which has the issue, one of ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’, ‘temporary_registration’

    file_hashes*: list[str]*
    :   List of base64-encoded file hashes

    message*: str*
    :   Error message
