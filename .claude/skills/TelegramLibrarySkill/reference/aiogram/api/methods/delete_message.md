# deleteMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_message.html](https://docs.aiogram.dev/en/latest/api/methods/delete_message.html)

Returns: `bool`

*class* aiogram.methods.delete_message.DeleteMessage(*\**, *chat_id: int | str*, *message_id: int*, *\*\*extra_data: Any*)
:   Use this method to delete a message, including service messages, with the following limitations:

    - A message can only be deleted if it was sent less than 48 hours ago.
    - Service messages about a supergroup, channel, or forum topic creation can’t be deleted.
    - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
    - Bots can delete outgoing messages in private chats, groups, and supergroups.
    - Bots can delete incoming messages in private chats.
    - Bots granted *can_post_messages* permissions can delete outgoing messages in channels.
    - If the bot is an administrator of a group, it can delete any message there.
    - If the bot has *can_delete_messages* administrator right in a supergroup or a channel, it can delete any message there.
    - If the bot has *can_manage_direct_messages* administrator right in a channel, it can delete any message in the corresponding direct messages chat.

    Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletemessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int*
    :   Identifier of the message to delete

## Usage

### As bot method

```
result: bool = await bot.delete_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_message import DeleteMessage`
- alias: `from aiogram.methods import DeleteMessage`

#### With specific bot

```
result: bool = await bot(DeleteMessage(...))
```

#### As reply into Webhook in handler

```
return DeleteMessage(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.delete_message()`](../types/chat.html#aiogram.types.chat.Chat.delete_message "aiogram.types.chat.Chat.delete_message")
- [`aiogram.types.message.Message.delete()`](../types/message.html#aiogram.types.message.Message.delete "aiogram.types.message.Message.delete")
