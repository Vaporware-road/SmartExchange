# setMessageReaction

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_message_reaction.html](https://docs.aiogram.dev/en/latest/api/methods/set_message_reaction.html)

Returns: `bool`

*class* aiogram.methods.set_message_reaction.SetMessageReaction(*\**, *chat_id: int | str*, *message_id: int*, *reaction: list[Annotated[[ReactionTypeEmoji](../types/reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](../types/reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](../types/reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]] | None = None*, *is_big: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the chosen reactions on a message. Service messages of some types can’t be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can’t use paid reactions. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmessagereaction>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int*
    :   Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead

    reaction*: list[Annotated[[ReactionTypeEmoji](../types/reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](../types/reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](../types/reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]] | None*
    :   A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can’t be used by bots

    is_big*: bool | None*
    :   Pass `True` to set the reaction with a big animation

## Usage

### As bot method

```
result: bool = await bot.set_message_reaction(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_message_reaction import SetMessageReaction`
- alias: `from aiogram.methods import SetMessageReaction`

#### With specific bot

```
result: bool = await bot(SetMessageReaction(...))
```

#### As reply into Webhook in handler

```
return SetMessageReaction(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.react()`](../types/message.html#aiogram.types.message.Message.react "aiogram.types.message.Message.react")
