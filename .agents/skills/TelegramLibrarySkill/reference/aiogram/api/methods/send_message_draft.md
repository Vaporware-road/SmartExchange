# sendMessageDraft

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_message_draft.html](https://docs.aiogram.dev/en/latest/api/methods/send_message_draft.html)

Returns: `bool`

*class* aiogram.methods.send_message_draft.SendMessageDraft(*\**, *chat_id: int*, *draft_id: int*, *message_thread_id: int | None = None*, *text: str | None = None*, *parse_mode: str | None = None*, *entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Use this method to stream a partial message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you **must** call [`aiogram.methods.send_message.SendMessage`](send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage") with the complete message to persist it in the user’s chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#sendmessagedraft>

    chat_id*: int*
    :   Unique identifier for the target private chat

    draft_id*: int*
    :   Unique identifier of the message draft; must be non-zero. Changes to drafts with the same identifier are animated

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread

    text*: str | None*
    :   Text of the message to be sent, 0-4096 characters after entities parsing. Pass an empty text to show a ‘Thinking…’ placeholder

    parse_mode*: str | None*
    :   Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*

## Usage

### As bot method

```
result: bool = await bot.send_message_draft(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_message_draft import SendMessageDraft`
- alias: `from aiogram.methods import SendMessageDraft`

#### With specific bot

```
result: bool = await bot(SendMessageDraft(...))
```

#### As reply into Webhook in handler

```
return SendMessageDraft(...)
```
