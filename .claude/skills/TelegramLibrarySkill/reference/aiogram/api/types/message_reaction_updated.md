# MessageReactionUpdated

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_reaction_updated.html](https://docs.aiogram.dev/en/latest/api/types/message_reaction_updated.html)

*class* aiogram.types.message_reaction_updated.MessageReactionUpdated(*\**, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_id: int*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *old_reaction: list[Annotated[[ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]]*, *new_reaction: list[Annotated[[ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]]*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *actor_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *\*\*extra_data: Any*)
:   This object represents a change of a reaction on a message performed by a user.

    Source: <https://core.telegram.org/bots/api#messagereactionupdated>

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   The chat containing the message the user reacted to

    message_id*: int*
    :   Unique identifier of the message inside the chat

    date*: DateTime*
    :   Date of the change in Unix time

    old_reaction*: list[ReactionTypeUnion]*
    :   Previous list of reaction types that were set by the user

    new_reaction*: list[ReactionTypeUnion]*
    :   New list of reaction types that have been set by the user

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. The user that changed the reaction, if the user isn’t anonymous

    actor_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. The chat on behalf of which the reaction was changed, if the user is anonymous
