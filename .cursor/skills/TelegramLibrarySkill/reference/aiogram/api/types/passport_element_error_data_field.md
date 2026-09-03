# PassportElementErrorDataField

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_data_field.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_data_field.html)

*class* aiogram.types.passport_element_error_data_field.PassportElementErrorDataField(*\**, *source: Literal[PassportElementErrorType.DATA] = PassportElementErrorType.DATA*, *type: str*, *field_name: str*, *data_hash: str*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field’s value changes.

    Source: <https://core.telegram.org/bots/api#passportelementerrordatafield>

    source*: Literal[PassportElementErrorType.DATA]*
    :   Error source, must be *data*

    type*: str*
    :   The section of the user’s Telegram Passport which has the error, one of ‘personal_details’, ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’, ‘address’

    field_name*: str*
    :   Name of the data field which has the error

    data_hash*: str*
    :   Base64-encoded data hash

    message*: str*
    :   Error message
