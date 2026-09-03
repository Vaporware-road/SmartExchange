# ForumTopic

> Source: [https://docs.aiogram.dev/en/latest/api/types/forum_topic.html](https://docs.aiogram.dev/en/latest/api/types/forum_topic.html)

*class* aiogram.types.forum_topic.ForumTopic(*\**, *message_thread_id: int*, *name: str*, *icon_color: int*, *icon_custom_emoji_id: str | None = None*, *is_name_implicit: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a forum topic.

    Source: <https://core.telegram.org/bots/api#forumtopic>

    message_thread_id*: int*
    :   Unique identifier of the forum topic

    name*: str*
    :   Name of the topic

    icon_color*: int*
    :   Color of the topic icon in RGB format

    icon_custom_emoji_id*: str | None*
    :   *Optional*. Unique identifier of the custom emoji shown as the topic icon

    is_name_implicit*: bool | None*
    :   *Optional*. `True`, if the name of the topic wasn’t specified explicitly by its creator and likely needs to be changed by the bot
