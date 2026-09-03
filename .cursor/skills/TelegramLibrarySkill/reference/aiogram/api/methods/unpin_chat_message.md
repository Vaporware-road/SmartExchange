# unpinChatMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unpin_chat_message.html](https://docs.aiogram.dev/en/latest/api/methods/unpin_chat_message.html)

Returns: `bool`

*class* aiogram.methods.unpin_chat_message.UnpinChatMessage(*\**, *chat_id: int | str*, *business_connection_id: str | None = None*, *message_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to unpin messages in groups and channels respectively. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unpinchatmessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be unpinned

    message_id*: int | None*
    :   Identifier of the message to unpin. Required if *business_connection_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned

## Usage

### As bot method

```
result: bool = await bot.unpin_chat_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.unpin_chat_message import UnpinChatMessage`
- alias: `from aiogram.methods import UnpinChatMessage`

#### With specific bot

```
result: bool = await bot(UnpinChatMessage(...))
```

#### As reply into Webhook in handler

```
return UnpinChatMessage(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.unpin_message()`](../types/chat.html#aiogram.types.chat.Chat.unpin_message "aiogram.types.chat.Chat.unpin_message")
- [`aiogram.types.message.Message.unpin()`](../types/message.html#aiogram.types.message.Message.unpin "aiogram.types.message.Message.unpin")
