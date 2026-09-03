# PassportElementErrorFrontSide

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_front_side.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_front_side.html)

*class* aiogram.types.passport_element_error_front_side.PassportElementErrorFrontSide(*\**, *source: Literal[PassportElementErrorType.FRONT_SIDE] = PassportElementErrorType.FRONT_SIDE*, *type: str*, *file_hash: str*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    Source: <https://core.telegram.org/bots/api#passportelementerrorfrontside>

    source*: Literal[PassportElementErrorType.FRONT_SIDE]*
    :   Error source, must be *front_side*

    type*: str*
    :   The section of the user’s Telegram Passport which has the issue, one of ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’

    file_hash*: str*
    :   Base64-encoded hash of the file with the front side of the document

    message*: str*
    :   Error message
