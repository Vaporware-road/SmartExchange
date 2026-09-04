# banChatSenderChat

> Source: [https://docs.aiogram.dev/en/latest/api/methods/ban_chat_sender_chat.html](https://docs.aiogram.dev/en/latest/api/methods/ban_chat_sender_chat.html)

Returns: `bool`

*class* aiogram.methods.ban_chat_sender_chat.BanChatSenderChat(*\**, *chat_id: int | str*, *sender_chat_id: int*, *\*\*extra_data: Any*)
:   Use this method to ban a channel chat in a supergroup or a channel. Until the chat is [unbanned](https://core.telegram.org/bots/api#unbanchatsenderchat), the owner of the banned chat won’t be able to send messages on behalf of **any of their channels**. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#banchatsenderchat>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    sender_chat_id*: int*
    :   Unique identifier of the target sender chat

## Usage

### As bot method

```
result: bool = await bot.ban_chat_sender_chat(...)
```

### Method as object

Imports:

- `from aiogram.methods.ban_chat_sender_chat import BanChatSenderChat`
- alias: `from aiogram.methods import BanChatSenderChat`

#### With specific bot

```
result: bool = await bot(BanChatSenderChat(...))
```

#### As reply into Webhook in handler

```
return BanChatSenderChat(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.ban_sender_chat()`](../types/chat.html#aiogram.types.chat.Chat.ban_sender_chat "aiogram.types.chat.Chat.ban_sender_chat")
