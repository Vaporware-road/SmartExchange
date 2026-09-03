# sendRichMessageDraft

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_rich_message_draft.html](https://docs.aiogram.dev/en/latest/api/methods/send_rich_message_draft.html)

Returns: `bool`

*class* aiogram.methods.send_rich_message_draft.SendRichMessageDraft(*\**, *chat_id: int*, *draft_id: int*, *rich_message: [InputRichMessage](../types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *message_thread_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to stream a partial rich message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you **must** call [`aiogram.methods.send_rich_message.SendRichMessage`](send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage") with the complete message to persist it in the user’s chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#sendrichmessagedraft>

    chat_id*: int*
    :   Unique identifier for the target private chat

    draft_id*: int*
    :   Unique identifier of the message draft; must be non-zero. Changes to drafts with the same identifier are animated

    rich_message*: [InputRichMessage](../types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*
    :   The partial message to be streamed. Direct upload of new files isn’t supported

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread

## Usage

### As bot method

```
result: bool = await bot.send_rich_message_draft(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_rich_message_draft import SendRichMessageDraft`
- alias: `from aiogram.methods import SendRichMessageDraft`

#### With specific bot

```
result: bool = await bot(SendRichMessageDraft(...))
```

#### As reply into Webhook in handler

```
return SendRichMessageDraft(...)
```
