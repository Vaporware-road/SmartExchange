# deleteEphemeralMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_ephemeral_message.html](https://docs.aiogram.dev/en/latest/api/methods/delete_ephemeral_message.html)

Returns: `bool`

*class* aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage(*\**, *chat_id: int | str*, *receiver_user_id: int*, *ephemeral_message_id: int*, *\*\*extra_data: Any*)
:   Use this method to delete an ephemeral message. Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deleteephemeralmessage>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    receiver_user_id*: int*
    :   Identifier of the user who received the message

    ephemeral_message_id*: int*
    :   Identifier of the ephemeral message to delete

## Usage

### As bot method

```
result: bool = await bot.delete_ephemeral_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_ephemeral_message import DeleteEphemeralMessage`
- alias: `from aiogram.methods import DeleteEphemeralMessage`

#### With specific bot

```
result: bool = await bot(DeleteEphemeralMessage(...))
```

#### As reply into Webhook in handler

```
return DeleteEphemeralMessage(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.delete_ephemeral()`](../types/message.html#aiogram.types.message.Message.delete_ephemeral "aiogram.types.message.Message.delete_ephemeral")
