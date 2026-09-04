# PollOption

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll_option.html](https://docs.aiogram.dev/en/latest/api/types/poll_option.html)

*class* aiogram.types.poll_option.PollOption(*\**, *persistent_id: str*, *text: str*, *voter_count: int*, *text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *media: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None = None*, *added_by_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *added_by_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *addition_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *\*\*extra_data: Any*)
:   This object contains information about one answer option in a poll.

    Source: <https://core.telegram.org/bots/api#polloption>

    persistent_id*: str*
    :   Unique identifier of the option, persistent on option addition and deletion

    text*: str*
    :   Option text, 1-100 characters

    voter_count*: int*
    :   Number of users who voted for this option; may be 0 if unknown

    text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the option *text*. Currently, only custom emoji entities are allowed in poll option texts

    media*: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None*
    :   *Optional*. Media added to the poll option

    added_by_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. User who added the option; omitted if the option wasn’t added by a user after poll creation

    added_by_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Chat that added the option; omitted if the option wasn’t added by a chat after poll creation

    addition_date*: DateTime | None*
    :   *Optional*. Point in time (Unix timestamp) when the option was added; omitted if the option existed in the original poll
