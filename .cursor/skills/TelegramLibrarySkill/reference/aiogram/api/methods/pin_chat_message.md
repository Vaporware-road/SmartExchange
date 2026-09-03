# pinChatMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/pin_chat_message.html](https://docs.aiogram.dev/en/latest/api/methods/pin_chat_message.html)

Returns: `bool`

*class* aiogram.methods.pin_chat_message.PinChatMessage(*\**, *chat_id: int | str*, *message_id: int*, *business_connection_id: str | None = None*, *disable_notification: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to pin messages in groups and channels respectively. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#pinchatmessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    message_id*: int*
    :   Identifier of a message to pin

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be pinned

    disable_notification*: bool | None*
    :   Pass `True` if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats

## Usage

### As bot method

```
result: bool = await bot.pin_chat_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.pin_chat_message import PinChatMessage`
- alias: `from aiogram.methods import PinChatMessage`

#### With specific bot

```
result: bool = await bot(PinChatMessage(...))
```

#### As reply into Webhook in handler

```
return PinChatMessage(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.pin_message()`](../types/chat.html#aiogram.types.chat.Chat.pin_message "aiogram.types.chat.Chat.pin_message")
- [`aiogram.types.message.Message.pin()`](../types/message.html#aiogram.types.message.Message.pin "aiogram.types.message.Message.pin")
