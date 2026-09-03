# MessageOriginHiddenUser

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_origin_hidden_user.html](https://docs.aiogram.dev/en/latest/api/types/message_origin_hidden_user.html)

*class* aiogram.types.message_origin_hidden_user.MessageOriginHiddenUser(*\**, *type: Literal[MessageOriginType.HIDDEN_USER] = MessageOriginType.HIDDEN_USER*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *sender_user_name: str*, *\*\*extra_data: Any*)
:   The message was originally sent by an unknown user.

    Source: <https://core.telegram.org/bots/api#messageoriginhiddenuser>

    type*: Literal[MessageOriginType.HIDDEN_USER]*
    :   Type of the message origin, always ‘hidden_user’

    date*: _datetime_serializer, return_type=int, when_used=unless-none)]*
    :   Date the message was sent originally in Unix time

    sender_user_name*: str*
    :   Name of the user that sent the message originally
