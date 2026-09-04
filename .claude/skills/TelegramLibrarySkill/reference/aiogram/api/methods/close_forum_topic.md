# closeForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/close_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/close_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.close_forum_topic.CloseForumTopic(*\**, *chat_id: int | str*, *message_thread_id: int*, *\*\*extra_data: Any*)
:   Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#closeforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_thread_id*: int*
    :   Unique identifier for the target message thread of the forum topic

## Usage

### As bot method

```
result: bool = await bot.close_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.close_forum_topic import CloseForumTopic`
- alias: `from aiogram.methods import CloseForumTopic`

#### With specific bot

```
result: bool = await bot(CloseForumTopic(...))
```

#### As reply into Webhook in handler

```
return CloseForumTopic(...)
```
