# sendMediaGroup

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_media_group.html](https://docs.aiogram.dev/en/latest/api/methods/send_media_group.html)

Returns: `list[Message]`

*class* aiogram.methods.send_media_group.SendMediaGroup(*\*, chat_id: int | str, media: list[~aiogram.types.input_media_audio.InputMediaAudio | ~aiogram.types.input_media_document.InputMediaDocument | ~aiogram.types.input_media_live_photo.InputMediaLivePhoto | ~aiogram.types.input_media_photo.InputMediaPhoto | ~aiogram.types.input_media_video.InputMediaVideo], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*extra_data: ~typing.Any*)
:   Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") objects that were sent is returned.

    Source: <https://core.telegram.org/bots/api#sendmediagroup>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    media*: list[MediaUnion]*
    :   A JSON-serialized Array describing messages to be sent, must include 2-10 items

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat

    disable_notification*: bool | None*
    :   Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent messages from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the messages are a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: list[Message] = await bot.send_media_group(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_media_group import SendMediaGroup`
- alias: `from aiogram.methods import SendMediaGroup`

#### With specific bot

```
result: list[Message] = await bot(SendMediaGroup(...))
```

#### As reply into Webhook in handler

```
return SendMediaGroup(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_media_group()`](../types/message.html#aiogram.types.message.Message.answer_media_group "aiogram.types.message.Message.answer_media_group")
- [`aiogram.types.message.Message.reply_media_group()`](../types/message.html#aiogram.types.message.Message.reply_media_group "aiogram.types.message.Message.reply_media_group")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group "aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_media_group()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_media_group "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_media_group")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_media_group()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_media_group "aiogram.types.inaccessible_message.InaccessibleMessage.answer_media_group")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_media_group()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_media_group "aiogram.types.inaccessible_message.InaccessibleMessage.reply_media_group")
