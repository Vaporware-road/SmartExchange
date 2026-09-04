# deleteForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/delete_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.delete_forum_topic.DeleteForumTopic(*\**, *chat_id: int | str*, *message_thread_id: int*, *\*\*extra_data: Any*)
:   Use this method to delete a forum topic along with all its messages in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can_delete_messages* administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deleteforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_thread_id*: int*
    :   Unique identifier for the target message thread of the forum topic

## Usage

### As bot method

```
result: bool = await bot.delete_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_forum_topic import DeleteForumTopic`
- alias: `from aiogram.methods import DeleteForumTopic`

#### With specific bot

```
result: bool = await bot(DeleteForumTopic(...))
```

#### As reply into Webhook in handler

```
return DeleteForumTopic(...)
```
