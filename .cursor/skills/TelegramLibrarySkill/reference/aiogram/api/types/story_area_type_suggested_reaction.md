# StoryAreaTypeSuggestedReaction

> Source: [https://docs.aiogram.dev/en/latest/api/types/story_area_type_suggested_reaction.html](https://docs.aiogram.dev/en/latest/api/types/story_area_type_suggested_reaction.html)

*class* aiogram.types.story_area_type_suggested_reaction.StoryAreaTypeSuggestedReaction(*\**, *type: Literal[StoryAreaTypeType.SUGGESTED_REACTION] = StoryAreaTypeType.SUGGESTED_REACTION*, *reaction_type: [ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid")*, *is_dark: bool | None = None*, *is_flipped: bool | None = None*, *\*\*extra_data: Any*)
:   Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

    Source: <https://core.telegram.org/bots/api#storyareatypesuggestedreaction>

    type*: Literal[StoryAreaTypeType.SUGGESTED_REACTION]*
    :   Type of the area, always ‘suggested_reaction’

    reaction_type*: ReactionTypeUnion*
    :   Type of the reaction

    is_dark*: bool | None*
    :   *Optional*. Pass `True` if the reaction area has a dark background

    is_flipped*: bool | None*
    :   *Optional*. Pass `True` if reaction area corner is flipped
