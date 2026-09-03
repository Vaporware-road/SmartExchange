# ChatMemberMember

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_member_member.html](https://docs.aiogram.dev/en/latest/api/types/chat_member_member.html)

*class* aiogram.types.chat_member_member.ChatMemberMember(*\**, *status: Literal[ChatMemberStatus.MEMBER] = ChatMemberStatus.MEMBER*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *tag: str | None = None*, *until_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *\*\*extra_data: Any*)
:   Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that has no additional privileges or restrictions.

    Source: <https://core.telegram.org/bots/api#chatmembermember>

    status*: Literal[ChatMemberStatus.MEMBER]*
    :   The member’s status in the chat, always ‘member’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user

    tag*: str | None*
    :   *Optional*. Tag of the member

    until_date*: DateTime | None*
    :   *Optional*. Date when the user’s subscription will expire; Unix time
