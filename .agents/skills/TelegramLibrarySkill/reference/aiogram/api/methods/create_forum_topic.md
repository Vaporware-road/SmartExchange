# createForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/methods/create_forum_topic.html](https://docs.aiogram.dev/en/latest/api/methods/create_forum_topic.html)

Returns: `ForumTopic`

*class* aiogram.methods.create_forum_topic.CreateForumTopic(*\**, *chat_id: int | str*, *name: str*, *icon_color: int | None = None*, *icon_custom_emoji_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to create a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator right. Returns information about the created topic as a [`aiogram.types.forum_topic.ForumTopic`](../types/forum_topic.html#aiogram.types.forum_topic.ForumTopic "aiogram.types.forum_topic.ForumTopic") object.

    Source: <https://core.telegram.org/bots/api#createforumtopic>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    name*: str*
    :   Topic name, 1-128 characters

    icon_color*: int | None*
    :   Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F)

    icon_custom_emoji_id*: str | None*
    :   Unique identifier of the custom emoji shown as the topic icon. Use [`aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers`](get_forum_topic_icon_stickers.html#aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers "aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers") to get all allowed custom emoji identifiers

## Usage

### As bot method

```
result: ForumTopic = await bot.create_forum_topic(...)
```

### Method as object

Imports:

- `from aiogram.methods.create_forum_topic import CreateForumTopic`
- alias: `from aiogram.methods import CreateForumTopic`

#### With specific bot

```
result: ForumTopic = await bot(CreateForumTopic(...))
```

#### As reply into Webhook in handler

```
return CreateForumTopic(...)
```
