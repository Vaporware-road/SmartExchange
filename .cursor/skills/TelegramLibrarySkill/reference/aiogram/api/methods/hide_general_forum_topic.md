# hideGeneralForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/hide_general_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/hide_general_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.hide_general_forum_topic.HideGeneralForumTopic(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to hide the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. The topic will be automatically closed if it was open. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#hidegeneralforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.hide_general_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.hide_general_forum_topic import HideGeneralForumTopic`
- alias: `from aiogram.methods import HideGeneralForumTopic`

#### With specific bot

```
result: bool = await bot(HideGeneralForumTopic(...))
```

#### As reply into Webhook in handler

```
return HideGeneralForumTopic(...)
```
