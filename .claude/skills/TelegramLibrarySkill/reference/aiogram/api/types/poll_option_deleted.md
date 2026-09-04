# PollOptionDeleted

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll_option_deleted.html](https://docs.aiogram.dev/en/latest/api/types/poll_option_deleted.html)

*class* aiogram.types.poll_option_deleted.PollOptionDeleted(*\**, *option_persistent_id: str*, *option_text: str*, *poll_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | [InaccessibleMessage](inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage "aiogram.types.inaccessible_message.InaccessibleMessage") | None = None*, *option_text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about an option deleted from a poll.

    Source: <https://core.telegram.org/bots/api#polloptiondeleted>

    option_persistent_id*: str*
    :   Unique identifier of the deleted option

    option_text*: str*
    :   Option text

    poll_message*: MaybeInaccessibleMessageUnion | None*
    :   *Optional*. Message containing the poll from which the option was deleted, if known. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    option_text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the *option_text*
