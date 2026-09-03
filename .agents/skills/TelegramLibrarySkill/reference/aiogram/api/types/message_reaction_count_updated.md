# MessageReactionCountUpdated

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_reaction_count_updated.html](https://docs.aiogram.dev/en/latest/api/types/message_reaction_count_updated.html)

*class* aiogram.types.message_reaction_count_updated.MessageReactionCountUpdated(*\**, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_id: int*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *reactions: list[[ReactionCount](reaction_count.html#aiogram.types.reaction_count.ReactionCount "aiogram.types.reaction_count.ReactionCount")]*, *\*\*extra_data: Any*)
:   This object represents reaction changes on a message with anonymous reactions.

    Source: <https://core.telegram.org/bots/api#messagereactioncountupdated>

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   The chat containing the message

    message_id*: int*
    :   Unique message identifier inside the chat

    date*: DateTime*
    :   Date of the change in Unix time

    reactions*: list[[ReactionCount](reaction_count.html#aiogram.types.reaction_count.ReactionCount "aiogram.types.reaction_count.ReactionCount")]*
    :   List of reactions that are present on the message
