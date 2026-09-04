# ChatMemberLeft

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_member_left.html](https://docs.aiogram.dev/en/latest/api/types/chat_member_left.html)

*class* aiogram.types.chat_member_left.ChatMemberLeft(*\**, *status: Literal[ChatMemberStatus.LEFT] = ChatMemberStatus.LEFT*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that isn’t currently a member of the chat, but may join it themselves.

    Source: <https://core.telegram.org/bots/api#chatmemberleft>

    status*: Literal[ChatMemberStatus.LEFT]*
    :   The member’s status in the chat, always ‘left’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user
