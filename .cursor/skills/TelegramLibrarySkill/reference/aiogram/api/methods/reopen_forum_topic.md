# reopenForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/reopen_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/reopen_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.reopen_forum_topic.ReopenForumTopic(*\**, *chat_id: int | str*, *message_thread_id: int*, *\*\*extra_data: Any*)
:   Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#reopenforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_thread_id*: int*
    :   Unique identifier for the target message thread of the forum topic

## Usage

### As bot method

```
result: bool = await bot.reopen_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.reopen_forum_topic import ReopenForumTopic`
- alias: `from aiogram.methods import ReopenForumTopic`

#### With specific bot

```
result: bool = await bot(ReopenForumTopic(...))
```

#### As reply into Webhook in handler

```
return ReopenForumTopic(...)
```
