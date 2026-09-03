# ReactionCount

> Source: [https://docs.aiogram.dev/en/latest/api/types/reaction_count.html](https://docs.aiogram.dev/en/latest/api/types/reaction_count.html)

*class* aiogram.types.reaction_count.ReactionCount(*\**, *type: [ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid")*, *total_count: int*, *\*\*extra_data: Any*)
:   Represents a reaction added to a message along with the number of times it was added.

    Source: <https://core.telegram.org/bots/api#reactioncount>

    type*: ReactionTypeUnion*
    :   Type of the reaction

    total_count*: int*
    :   Number of times the reaction was added
