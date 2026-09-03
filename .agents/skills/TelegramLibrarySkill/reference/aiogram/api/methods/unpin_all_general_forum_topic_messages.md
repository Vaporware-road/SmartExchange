# unpinAllGeneralForumTopicMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unpin_all_general_forum_topic_messages.html](https://docs.aiogram.dev/en/latest/api/methods/unpin_all_general_forum_topic_messages.html)

Returns: `bool`

*class* aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the *can_pin_messages* administrator right in the supergroup. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.unpin_all_general_forum_topic_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.unpin_all_general_forum_topic_messages import UnpinAllGeneralForumTopicMessages`
- alias: `from aiogram.methods import UnpinAllGeneralForumTopicMessages`

#### With specific bot

```
result: bool = await bot(UnpinAllGeneralForumTopicMessages(...))
```

#### As reply into Webhook in handler

```
return UnpinAllGeneralForumTopicMessages(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.unpin_all_general_forum_topic_messages()`](../types/chat.html#aiogram.types.chat.Chat.unpin_all_general_forum_topic_messages "aiogram.types.chat.Chat.unpin_all_general_forum_topic_messages")
