# MessageOriginUser

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_origin_user.html](https://docs.aiogram.dev/en/latest/api/types/message_origin_user.html)

*class* aiogram.types.message_origin_user.MessageOriginUser(*\**, *type: Literal[MessageOriginType.USER] = MessageOriginType.USER*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *sender_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   The message was originally sent by a known user.

    Source: <https://core.telegram.org/bots/api#messageoriginuser>

    type*: Literal[MessageOriginType.USER]*
    :   Type of the message origin, always ‘user’

    date*: DateTime*
    :   Date the message was sent originally in Unix time

    sender_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User that sent the message originally
