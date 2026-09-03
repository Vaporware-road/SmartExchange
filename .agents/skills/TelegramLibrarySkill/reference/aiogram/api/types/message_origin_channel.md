# MessageOriginChannel

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_origin_channel.html](https://docs.aiogram.dev/en/latest/api/types/message_origin_channel.html)

*class* aiogram.types.message_origin_channel.MessageOriginChannel(*\**, *type: Literal[MessageOriginType.CHANNEL] = MessageOriginType.CHANNEL*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_id: int*, *author_signature: str | None = None*, *\*\*extra_data: Any*)
:   The message was originally sent to a channel chat.

    Source: <https://core.telegram.org/bots/api#messageoriginchannel>

    type*: Literal[MessageOriginType.CHANNEL]*
    :   Type of the message origin, always ‘channel’

    date*: DateTime*
    :   Date the message was sent originally in Unix time

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Channel chat to which the message was originally sent

    message_id*: int*
    :   Unique message identifier inside the chat

    author_signature*: str | None*
    :   *Optional*. Signature of the original post author
