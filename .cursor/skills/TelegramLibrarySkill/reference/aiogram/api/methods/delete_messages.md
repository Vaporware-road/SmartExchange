# deleteMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_messages.html](https://docs.aiogram.dev/en/latest/api/methods/delete_messages.html)

Returns: `bool`

*class* aiogram.methods.delete_messages.DeleteMessages(*\**, *chat_id: int | str*, *message_ids: list[int]*, *\*\*extra_data: Any*)
:   Use this method to delete multiple messages simultaneously. If some of the specified messages can’t be found, they are skipped. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletemessages>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_ids*: list[int]*
    :   A JSON-serialized list of 1-100 identifiers of messages to delete. See [`aiogram.methods.delete_message.DeleteMessage`](delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage") for limitations on which messages can be deleted

## Usage

### As bot method

```
result: bool = await bot.delete_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_messages import DeleteMessages`
- alias: `from aiogram.methods import DeleteMessages`

#### With specific bot

```
result: bool = await bot(DeleteMessages(...))
```

#### As reply into Webhook in handler

```
return DeleteMessages(...)
```
