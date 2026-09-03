# forwardMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/forward_message.html](https://docs.aiogram.dev/en/latest/api/methods/forward_message.html)

Returns: `Message`

*class* aiogram.methods.forward_message.ForwardMessage(*\**, *chat_id: int | str*, *from_chat_id: int | str*, *message_id: int*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *video_start_timestamp: ~datetime.datetime | ~datetime.timedelta | int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to forward messages of any kind. Service messages and messages with protected content can’t be forwarded. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#forwardmessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    from_chat_id*: ChatIdUnion*
    :   Unique identifier for the chat where the original message was sent (or username of the target bot, supergroup or channel in the format `@username`)

    message_id*: int*
    :   Message identifier in the chat specified in *from_chat_id*

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat

    video_start_timestamp*: DateTimeUnion | None*
    :   New start timestamp for the forwarded video in the message

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the forwarded message from forwarding and saving

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; only available when forwarding to private chats

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only

## Usage

### As bot method

```
result: Message = await bot.forward_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.forward_message import ForwardMessage`
- alias: `from aiogram.methods import ForwardMessage`

#### With specific bot

```
result: Message = await bot(ForwardMessage(...))
```

#### As reply into Webhook in handler

```
return ForwardMessage(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.forward()`](../types/message.html#aiogram.types.message.Message.forward "aiogram.types.message.Message.forward")
