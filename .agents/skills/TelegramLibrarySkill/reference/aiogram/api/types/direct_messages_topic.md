# DirectMessagesTopic

> Source: [https://docs.aiogram.dev/en/latest/api/types/direct_messages_topic.html](https://docs.aiogram.dev/en/latest/api/types/direct_messages_topic.html)

*class* aiogram.types.direct_messages_topic.DirectMessagesTopic(*\**, *topic_id: int*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *\*\*extra_data: Any*)
:   Describes a topic of a direct messages chat.

    Source: <https://core.telegram.org/bots/api#directmessagestopic>

    topic_id*: int*
    :   Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Information about the user that created the topic. Currently, it is always present
