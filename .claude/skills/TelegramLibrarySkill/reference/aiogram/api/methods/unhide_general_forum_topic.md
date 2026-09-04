# unhideGeneralForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/unhide_general_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/unhide_general_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.unhide_general_forum_topic.UnhideGeneralForumTopic(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to unhide the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#unhidegeneralforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.unhide_general_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.unhide_general_forum_topic import UnhideGeneralForumTopic`
- alias: `from aiogram.methods import UnhideGeneralForumTopic`

#### With specific bot

```
result: bool = await bot(UnhideGeneralForumTopic(...))
```

#### As reply into Webhook in handler

```
return UnhideGeneralForumTopic(...)
```
