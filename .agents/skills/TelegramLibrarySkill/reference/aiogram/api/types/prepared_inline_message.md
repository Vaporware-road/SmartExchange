# PreparedInlineMessage

> Source: [https://docs.aiogram.dev/en/latest/api/types/prepared_inline_message.html](https://docs.aiogram.dev/en/latest/api/types/prepared_inline_message.html)

*class* aiogram.types.prepared_inline_message.PreparedInlineMessage(*\**, *id: str*, *expiration_date: datetime | timedelta | int*, *\*\*extra_data: Any*)
:   Describes an inline message to be sent by a user of a Mini App.

    Source: <https://core.telegram.org/bots/api#preparedinlinemessage>

    id*: str*
    :   Unique identifier of the prepared message

    expiration_date*: DateTimeUnion*
    :   Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used
