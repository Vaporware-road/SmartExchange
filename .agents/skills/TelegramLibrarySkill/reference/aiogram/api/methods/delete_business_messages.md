# deleteBusinessMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_business_messages.html](https://docs.aiogram.dev/en/latest/api/methods/delete_business_messages.html)

Returns: `bool`

*class* aiogram.methods.delete_business_messages.DeleteBusinessMessages(*\**, *business_connection_id: str*, *message_ids: list[int]*, *\*\*extra_data: Any*)
:   Delete messages on behalf of a business account. Requires the *can_delete_sent_messages* business bot right to delete messages sent by the bot itself, or the *can_delete_all_messages* business bot right to delete any message. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletebusinessmessages>

    business_connection_id*: str*
    :   Unique identifier of the business connection on behalf of which to delete the messages

    message_ids*: list[int]*
    :   A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See [`aiogram.methods.delete_message.DeleteMessage`](delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage") for limitations on which messages can be deleted

## Usage

### As bot method

```
result: bool = await bot.delete_business_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_business_messages import DeleteBusinessMessages`
- alias: `from aiogram.methods import DeleteBusinessMessages`

#### With specific bot

```
result: bool = await bot(DeleteBusinessMessages(...))
```

#### As reply into Webhook in handler

```
return DeleteBusinessMessages(...)
```
