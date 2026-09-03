# PassportElementErrorUnspecified

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_element_error_unspecified.html](https://docs.aiogram.dev/en/latest/api/types/passport_element_error_unspecified.html)

*class* aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified(*\**, *source: Literal[PassportElementErrorType.UNSPECIFIED] = PassportElementErrorType.UNSPECIFIED*, *type: str*, *element_hash: str*, *message: str*, *\*\*extra_data: Any*)
:   Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    Source: <https://core.telegram.org/bots/api#passportelementerrorunspecified>

    source*: Literal[PassportElementErrorType.UNSPECIFIED]*
    :   Error source, must be *unspecified*

    type*: str*
    :   Type of element of the user’s Telegram Passport which has the issue

    element_hash*: str*
    :   Base64-encoded element hash

    message*: str*
    :   Error message
