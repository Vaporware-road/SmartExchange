# unpinAllForumTopicMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unpin_all_forum_topic_messages.html](https://docs.aiogram.dev/en/latest/api/methods/unpin_all_forum_topic_messages.html)

Returns: `bool`

*class* aiogram.methods.unpin_all_forum_topic_messages.UnpinAllForumTopicMessages(*\**, *chat_id: int | str*, *message_thread_id: int*, *\*\*extra_data: Any*)
:   Use this method to clear the list of pinned messages in a forum topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can_pin_messages* administrator right in the supergroup. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unpinallforumtopicmessages>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_thread_id*: int*
    :   Unique identifier for the target message thread of the forum topic

## Usage

### As bot method

```
result: bool = await bot.unpin_all_forum_topic_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.unpin_all_forum_topic_messages import UnpinAllForumTopicMessages`
- alias: `from aiogram.methods import UnpinAllForumTopicMessages`

#### With specific bot

```
result: bool = await bot(UnpinAllForumTopicMessages(...))
```

#### As reply into Webhook in handler

```
return UnpinAllForumTopicMessages(...)
```
