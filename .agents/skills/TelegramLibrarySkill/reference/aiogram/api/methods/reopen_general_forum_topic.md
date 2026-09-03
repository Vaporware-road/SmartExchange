# reopenGeneralForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/reopen_general_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/reopen_general_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.reopen_general_forum_topic.ReopenGeneralForumTopic(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to reopen a closed ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. The topic will be automatically unhidden if it was hidden. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#reopengeneralforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.reopen_general_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.reopen_general_forum_topic import ReopenGeneralForumTopic`
- alias: `from aiogram.methods import ReopenGeneralForumTopic`

#### With specific bot

```
result: bool = await bot(ReopenGeneralForumTopic(...))
```

#### As reply into Webhook in handler

```
return ReopenGeneralForumTopic(...)
```
