# MessageOriginChat

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_origin_chat.html](https://docs.aiogram.dev/en/latest/api/types/message_origin_chat.html)

*class* aiogram.types.message_origin_chat.MessageOriginChat(*\**, *type: Literal[MessageOriginType.CHAT] = MessageOriginType.CHAT*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *sender_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *author_signature: str | None = None*, *\*\*extra_data: Any*)
:   The message was originally sent on behalf of a chat to a group chat.

    Source: <https://core.telegram.org/bots/api#messageoriginchat>

    type*: Literal[MessageOriginType.CHAT]*
    :   Type of the message origin, always ‘chat’

    date*: DateTime*
    :   Date the message was sent originally in Unix time

    sender_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Chat that sent the message originally

    author_signature*: str | None*
    :   *Optional*. For messages originally sent by an anonymous chat administrator, original message author signature
