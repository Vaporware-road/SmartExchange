# banChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/methods/ban_chat_member.html](https://docs.aiogram.dev/en/latest/api/methods/ban_chat_member.html)

Returns: `bool`

*class* aiogram.methods.ban_chat_member.BanChatMember(*\**, *chat_id: int | str*, *user_id: int*, *until_date: datetime | timedelta | int | None = None*, *revoke_messages: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless [unbanned](https://core.telegram.org/bots/api#unbanchatmember) first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#banchatmember>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target group or username of the target supergroup or channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    until_date*: DateTimeUnion | None*
    :   Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only

    revoke_messages*: bool | None*
    :   Pass `True` to delete all messages from the chat for the user that is being removed. If `False`, the user will be able to see messages in the group that were sent before the user was removed. Always `True` for supergroups and channels

## Usage

### As bot method

```
result: bool = await bot.ban_chat_member(...)
```

### Method as object

Imports:

- `from aiogram.methods.ban_chat_member import BanChatMember`
- alias: `from aiogram.methods import BanChatMember`

#### With specific bot

```
result: bool = await bot(BanChatMember(...))
```

#### As reply into Webhook in handler

```
return BanChatMember(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.ban()`](../types/chat.html#aiogram.types.chat.Chat.ban "aiogram.types.chat.Chat.ban")
