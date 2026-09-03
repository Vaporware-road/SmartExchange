# deleteMessageReaction

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_message_reaction.html](https://docs.aiogram.dev/en/latest/api/methods/delete_message_reaction.html)

Returns: `bool`

*class* aiogram.methods.delete_message_reaction.DeleteMessageReaction(*\**, *chat_id: int | str*, *message_id: int*, *user_id: int | None = None*, *actor_chat_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to remove a reaction from a message in a group or a supergroup chat. The bot must have the ‘can_delete_messages’ administrator right in the chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletemessagereaction>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    message_id*: int*
    :   Identifier of the target message

    user_id*: int | None*
    :   Identifier of the user whose reaction will be removed, if the reaction was added by a user

    actor_chat_id*: int | None*
    :   Identifier of the chat whose reaction will be removed, if the reaction was added by a chat

## Usage

### As bot method

```
result: bool = await bot.delete_message_reaction(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_message_reaction import DeleteMessageReaction`
- alias: `from aiogram.methods import DeleteMessageReaction`

#### With specific bot

```
result: bool = await bot(DeleteMessageReaction(...))
```

#### As reply into Webhook in handler

```
return DeleteMessageReaction(...)
```
