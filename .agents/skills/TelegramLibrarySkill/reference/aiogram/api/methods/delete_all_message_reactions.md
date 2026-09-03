# deleteAllMessageReactions

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_all_message_reactions.html](https://docs.aiogram.dev/en/latest/api/methods/delete_all_message_reactions.html)

Returns: `bool`

*class* aiogram.methods.delete_all_message_reactions.DeleteAllMessageReactions(*\**, *chat_id: int | str*, *user_id: int | None = None*, *actor_chat_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat. The bot must have the ‘can_delete_messages’ administrator right in the chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deleteallmessagereactions>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    user_id*: int | None*
    :   Identifier of the user whose reactions will be removed, if the reactions were added by a user

    actor_chat_id*: int | None*
    :   Identifier of the chat whose reactions will be removed, if the reactions were added by a chat

## Usage

### As bot method

```
result: bool = await bot.delete_all_message_reactions(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_all_message_reactions import DeleteAllMessageReactions`
- alias: `from aiogram.methods import DeleteAllMessageReactions`

#### With specific bot

```
result: bool = await bot(DeleteAllMessageReactions(...))
```

#### As reply into Webhook in handler

```
return DeleteAllMessageReactions(...)
```
