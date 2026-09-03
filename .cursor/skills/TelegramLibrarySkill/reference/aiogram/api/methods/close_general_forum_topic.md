# closeGeneralForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/close_general_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/close_general_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.close_general_forum_topic.CloseGeneralForumTopic(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to close an open ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#closegeneralforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.close_general_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.close_general_forum_topic import CloseGeneralForumTopic`
- alias: `from aiogram.methods import CloseGeneralForumTopic`

#### With specific bot

```
result: bool = await bot(CloseGeneralForumTopic(...))
```

#### As reply into Webhook in handler

```
return CloseGeneralForumTopic(...)
```
