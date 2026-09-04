# ChatMemberOwner

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_member_owner.html](https://docs.aiogram.dev/en/latest/api/types/chat_member_owner.html)

*class* aiogram.types.chat_member_owner.ChatMemberOwner(*\**, *status: Literal[ChatMemberStatus.CREATOR] = ChatMemberStatus.CREATOR*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *is_anonymous: bool*, *custom_title: str | None = None*, *\*\*extra_data: Any*)
:   Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that owns the chat and has all administrator privileges.

    Source: <https://core.telegram.org/bots/api#chatmemberowner>

    status*: Literal[ChatMemberStatus.CREATOR]*
    :   The member’s status in the chat, always ‘creator’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user

    is_anonymous*: bool*
    :   `True`, if the user’s presence in the chat is hidden

    custom_title*: str | None*
    :   *Optional*. Custom title for this user
