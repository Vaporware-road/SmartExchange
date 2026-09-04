# editGeneralForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_general_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/edit_general_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.edit_general_forum_topic.EditGeneralForumTopic(*\**, *chat_id: int | str*, *name: str*, *\*\*extra_data: Any*)
:   Use this method to edit the name of the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#editgeneralforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    name*: str*
    :   New topic name, 1-128 characters

## Usage

### As bot method

```
result: bool = await bot.edit_general_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_general_forum_topic import EditGeneralForumTopic`
- alias: `from aiogram.methods import EditGeneralForumTopic`

#### With specific bot

```
result: bool = await bot(EditGeneralForumTopic(...))
```

#### As reply into Webhook in handler

```
return EditGeneralForumTopic(...)
```
