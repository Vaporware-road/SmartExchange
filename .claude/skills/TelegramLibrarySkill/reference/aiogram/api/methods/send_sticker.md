# sendSticker

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_sticker.html](https://docs.aiogram.dev/en/latest/api/methods/send_sticker.html)

Returns: `Message`

*class* aiogram.methods.send_sticker.SendSticker(*\**, *chat_id: int | str*, *sticker: str | ~aiogram.types.input_file.InputFile*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendsticker>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    sticker*: InputFileUnion*
    :   Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Video and animated stickers can’t be sent via an HTTP URL

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    emoji*: str | None*
    :   Emoji associated with the sticker; only for just uploaded stickers

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: ReplyMarkupUnion | None*
    :   Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

    receiver_user_id*: int | None*
    :   For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details

    callback_query_id*: str | None*
    :   For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_sticker(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_sticker import SendSticker`
- alias: `from aiogram.methods import SendSticker`

#### With specific bot

```
result: Message = await bot(SendSticker(...))
```

#### As reply into Webhook in handler

```
return SendSticker(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_sticker()`](../types/message.html#aiogram.types.message.Message.answer_sticker "aiogram.types.message.Message.answer_sticker")
- [`aiogram.types.message.Message.reply_sticker()`](../types/message.html#aiogram.types.message.Message.reply_sticker "aiogram.types.message.Message.reply_sticker")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker "aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_sticker()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_sticker "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_sticker")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_sticker()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_sticker "aiogram.types.inaccessible_message.InaccessibleMessage.answer_sticker")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_sticker()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_sticker "aiogram.types.inaccessible_message.InaccessibleMessage.reply_sticker")
