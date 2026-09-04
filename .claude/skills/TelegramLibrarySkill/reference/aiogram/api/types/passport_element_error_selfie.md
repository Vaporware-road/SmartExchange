# PassportElementErrorSelfie

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_selfie.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_selfie.html)

*class* aiogram.types.passport_element_error_selfie.PassportElementErrorSelfie(*\**, *source: Literal[PassportElementErrorType.SELFIE] = PassportElementErrorType.SELFIE*, *type: str*, *file_hash: str*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    Source: <https://core.telegram.org/bots/api#passportelementerrorselfie>

    source*: Literal[PassportElementErrorType.SELFIE]*
    :   Error source, must be *selfie*

    type*: str*
    :   The section of the user’s Telegram Passport which has the issue, one of ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’

    file_hash*: str*
    :   Base64-encoded hash of the file with the selfie

    message*: str*
    :   Error message
