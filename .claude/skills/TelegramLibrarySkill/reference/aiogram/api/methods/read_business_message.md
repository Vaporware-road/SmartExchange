# readBusinessMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/read_business_message.html](https://docs.aiogram.dev/en/latest/api/methods/read_business_message.html)

Returns: `bool`

*class* aiogram.methods.read_business_message.ReadBusinessMessage(*\**, *business_connection_id: str*, *chat_id: int*, *message_id: int*, *\*\*extra_data: Any*)
:   Marks incoming message as read on behalf of a business account. Requires the *can_read_messages* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#readbusinessmessage>

    business_connection_id*: str*
    :   Unique identifier of the business connection on behalf of which to read the message

    chat_id*: int*
    :   Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours

    message_id*: int*
    :   Unique identifier of the message to mark as read

## Usage

### As bot method

```
result: bool = await bot.read_business_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.read_business_message import ReadBusinessMessage`
- alias: `from aiogram.methods import ReadBusinessMessage`

#### With specific bot

```
result: bool = await bot(ReadBusinessMessage(...))
```

#### As reply into Webhook in handler

```
return ReadBusinessMessage(...)
```
