# ChatMemberBanned

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_member_banned.html](https://docs.aiogram.dev/en/latest/api/types/chat_member_banned.html)

*class* aiogram.types.chat_member_banned.ChatMemberBanned(*\**, *status: Literal[ChatMemberStatus.KICKED] = ChatMemberStatus.KICKED*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *until_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *\*\*extra_data: Any*)
:   Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that was banned in the chat and can’t return to the chat or view chat messages.

    Source: <https://core.telegram.org/bots/api#chatmemberbanned>

    status*: Literal[ChatMemberStatus.KICKED]*
    :   The member’s status in the chat, always ‘kicked’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user

    until_date*: DateTime*
    :   Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever
