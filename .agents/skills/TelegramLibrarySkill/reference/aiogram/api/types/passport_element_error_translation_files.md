# PassportElementErrorTranslationFiles

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_translation_files.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_translation_files.html)

*class* aiogram.types.passport_element_error_translation_files.PassportElementErrorTranslationFiles(*\**, *source: Literal[PassportElementErrorType.TRANSLATION_FILES] = PassportElementErrorType.TRANSLATION_FILES*, *type: str*, *file_hashes: list[str]*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    Source: <https://core.telegram.org/bots/api#passportelementerrortranslationfiles>

    source*: Literal[PassportElementErrorType.TRANSLATION_FILES]*
    :   Error source, must be *translation_files*

    type*: str*
    :   Type of element of the user’s Telegram Passport which has the issue, one of ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’, ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’, ‘temporary_registration’

    file_hashes*: list[str]*
    :   List of base64-encoded file hashes

    message*: str*
    :   Error message
