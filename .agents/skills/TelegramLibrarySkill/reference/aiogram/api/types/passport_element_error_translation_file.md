# PassportElementErrorTranslationFile

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_translation_file.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_translation_file.html)

*class* aiogram.types.passport_element_error_translation_file.PassportElementErrorTranslationFile(*\**, *source: Literal[PassportElementErrorType.TRANSLATION_FILE] = PassportElementErrorType.TRANSLATION_FILE*, *type: str*, *file_hash: str*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    Source: <https://core.telegram.org/bots/api#passportelementerrortranslationfile>

    source*: Literal[PassportElementErrorType.TRANSLATION_FILE]*
    :   Error source, must be *translation_file*

    type*: str*
    :   Type of element of the user’s Telegram Passport which has the issue, one of ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’, ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’, ‘temporary_registration’

    file_hash*: str*
    :   Base64-encoded file hash

    message*: str*
    :   Error message
