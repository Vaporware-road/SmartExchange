# forwardMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/forward_messages.html](https://docs.aiogram.dev/en/latest/api/methods/forward_messages.html)

Returns: `list[MessageId]`

*class* aiogram.methods.forward_messages.ForwardMessages(*\**, *chat_id: int | str*, *from_chat_id: int | str*, *message_ids: list[int]*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to forward multiple messages of any kind. If some of the specified messages can’t be found or forwarded, they are skipped. Service messages and messages with protected content can’t be forwarded. Album grouping is kept for forwarded messages. On success, an Array of [`aiogram.types.message_id.MessageId`](../types/message_id.html#aiogram.types.message_id.MessageId "aiogram.types.message_id.MessageId") of the sent messages is returned.

    Source: <https://core.telegram.org/bots/api#forwardmessages>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    from_chat_id*: int | str*
    :   Unique identifier for the chat where the original messages were sent (or username of the target bot, supergroup or channel in the format `@username`)

    message_ids*: list[int]*
    :   A JSON-serialized list of 1-100 identifiers of messages in the chat *from_chat_id* to forward. The identifiers must be specified in a strictly increasing order

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat

    disable_notification*: bool | None*
    :   Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | None*
    :   Protects the contents of the forwarded messages from forwarding and saving

## Usage

### As bot method

```
result: list[MessageId] = await bot.forward_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.forward_messages import ForwardMessages`
- alias: `from aiogram.methods import ForwardMessages`

#### With specific bot

```
result: list[MessageId] = await bot(ForwardMessages(...))
```

#### As reply into Webhook in handler

```
return ForwardMessages(...)
```
