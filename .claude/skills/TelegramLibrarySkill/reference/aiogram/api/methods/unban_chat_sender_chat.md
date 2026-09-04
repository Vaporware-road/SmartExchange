# unbanChatSenderChat

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unban_chat_sender_chat.html](https://docs.aiogram.dev/en/latest/api/methods/unban_chat_sender_chat.html)

Returns: `bool`

*class* aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat(*\**, *chat_id: int | str*, *sender_chat_id: int*, *\*\*extra_data: Any*)
:   Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unbanchatsenderchat>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    sender_chat_id*: int*
    :   Unique identifier of the target sender chat

## Usage

### As bot method

```
result: bool = await bot.unban_chat_sender_chat(...)
```

### Method as object

Imports:

- `from aiogram.methods.unban_chat_sender_chat import UnbanChatSenderChat`
- alias: `from aiogram.methods import UnbanChatSenderChat`

#### With specific bot

```
result: bool = await bot(UnbanChatSenderChat(...))
```

#### As reply into Webhook in handler

```
return UnbanChatSenderChat(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.unban_sender_chat()`](../types/chat.html#aiogram.types.chat.Chat.unban_sender_chat "aiogram.types.chat.Chat.unban_sender_chat")
