# leaveChat

> Source: [https://docs.aiogram.dev/en/latest/api/methods/leave_chat.html](https://docs.aiogram.dev/en/latest/api/methods/leave_chat.html)

Returns: `bool`

*class* aiogram.methods.leave_chat.LeaveChat(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method for your bot to leave a group, supergroup or channel. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#leavechat>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup or channel in the format `@username`. Channel direct messages chats aren’t supported; leave the corresponding channel instead

## Usage

### As bot method

```
result: bool = await bot.leave_chat(...)
```

### Method as object

Imports:

- `from aiogram.methods.leave_chat import LeaveChat`
- alias: `from aiogram.methods import LeaveChat`

#### With specific bot

```
result: bool = await bot(LeaveChat(...))
```

#### As reply into Webhook in handler

```
return LeaveChat(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.leave()`](../types/chat.html#aiogram.types.chat.Chat.leave "aiogram.types.chat.Chat.leave")
