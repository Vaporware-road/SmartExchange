# editForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/edit_forum_topic.html)

Returns: `bool`

*class* aiogram.methods.edit_forum_topic.EditForumTopic(*\**, *chat_id: int | str*, *message_thread_id: int*, *name: str | None = None*, *icon_custom_emoji_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit name and icon of a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#editforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_thread_id*: int*
    :   Unique identifier for the target message thread of the forum topic

    name*: str | None*
    :   New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept

    icon_custom_emoji_id*: str | None*
    :   New unique identifier of the custom emoji shown as the topic icon. Use [`aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers`](get_forum_topic_icon_stickers.html#aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers "aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers") to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept

## Usage

### As bot method

```
result: bool = await bot.edit_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_forum_topic import EditForumTopic`
- alias: `from aiogram.methods import EditForumTopic`

#### With specific bot

```
result: bool = await bot(EditForumTopic(...))
```

#### As reply into Webhook in handler

```
return EditForumTopic(...)
```
