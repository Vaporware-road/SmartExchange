# unbanChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unban_chat_member.html](https://docs.aiogram.dev/en/latest/api/methods/unban_chat_member.html)

Returns: `bool`

*class* aiogram.methods.unban_chat_member.UnbanChatMember(*\**, *chat_id: int | str*, *user_id: int*, *only_if_banned: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to unban a previously banned user in a supergroup or channel. The user will **not** return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be **removed** from the chat. If you don’t want this, use the parameter *only_if_banned*. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unbanchatmember>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target group or username of the target supergroup or channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    only_if_banned*: bool | None*
    :   Do nothing if the user is not banned

## Usage

### As bot method

```
result: bool = await bot.unban_chat_member(...)
```

### Method as object

Imports:

- `from aiogram.methods.unban_chat_member import UnbanChatMember`
- alias: `from aiogram.methods import UnbanChatMember`

#### With specific bot

```
result: bool = await bot(UnbanChatMember(...))
```

#### As reply into Webhook in handler

```
return UnbanChatMember(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.unban()`](../types/chat.html#aiogram.types.chat.Chat.unban "aiogram.types.chat.Chat.unban")
