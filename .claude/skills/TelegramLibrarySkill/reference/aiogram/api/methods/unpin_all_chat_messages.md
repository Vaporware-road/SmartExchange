# unpinAllChatMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unpin_all_chat_messages.html](https://docs.aiogram.dev/en/latest/api/methods/unpin_all_chat_messages.html)

Returns: `bool`

*class* aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to clear the list of pinned messages in a chat. In private chats and channel direct messages chats, no additional rights are required to unpin all pinned messages. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to unpin all pinned messages in groups and channels respectively. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unpinallchatmessages>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.unpin_all_chat_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.unpin_all_chat_messages import UnpinAllChatMessages`
- alias: `from aiogram.methods import UnpinAllChatMessages`

#### With specific bot

```
result: bool = await bot(UnpinAllChatMessages(...))
```

#### As reply into Webhook in handler

```
return UnpinAllChatMessages(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.unpin_all_messages()`](../types/chat.html#aiogram.types.chat.Chat.unpin_all_messages "aiogram.types.chat.Chat.unpin_all_messages")
