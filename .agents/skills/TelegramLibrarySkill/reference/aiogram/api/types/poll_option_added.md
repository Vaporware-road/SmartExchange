# PollOptionAdded

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll_option_added.html](https://docs.aiogram.dev/en/latest/api/types/poll_option_added.html)

*class* aiogram.types.poll_option_added.PollOptionAdded(*\**, *option_persistent_id: str*, *option_text: str*, *poll_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | [InaccessibleMessage](inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage "aiogram.types.inaccessible_message.InaccessibleMessage") | None = None*, *option_text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about an option added to a poll.

    Source: <https://core.telegram.org/bots/api#polloptionadded>

    option_persistent_id*: str*
    :   Unique identifier of the added option

    option_text*: str*
    :   Option text

    poll_message*: MaybeInaccessibleMessageUnion | None*
    :   *Optional*. Message containing the poll to which the option was added, if known. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    option_text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the *option_text*
