# MessageId

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_id.html](https://docs.aiogram.dev/en/latest/api/types/message_id.html)

*class* aiogram.types.message_id.MessageId(*\**, *message_id: int*, *\*\*extra_data: Any*)
:   This object represents a unique message identifier.

    Source: <https://core.telegram.org/bots/api#messageid>

    message_id*: int*
    :   Unique message identifier. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent
