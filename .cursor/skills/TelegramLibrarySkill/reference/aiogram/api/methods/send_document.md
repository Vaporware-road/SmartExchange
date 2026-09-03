# sendDocument

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_document.html](https://docs.aiogram.dev/en/latest/api/methods/send_document.html)

Returns: `Message`

*class* aiogram.methods.send_document.SendDocument(*\**, *chat_id: int | str*, *document: str | ~aiogram.types.input_file.InputFile*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to send general files. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    Source: <https://core.telegram.org/bots/api#senddocument>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    document*: InputFileUnion*
    :   File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    thumbnail*: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None*
    :   Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)

    caption*: str | None*
    :   Document caption (may also be used when resending documents by *file_id*), 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    disable_content_type_detection*: bool | None*
    :   Disables automatic server-side content type detection for files uploaded using multipart/form-data

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
result: Message = await bot.send_document(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_document import SendDocument`
- alias: `from aiogram.methods import SendDocument`

#### With specific bot

```
result: Message = await bot(SendDocument(...))
```

#### As reply into Webhook in handler

```
return SendDocument(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_document()`](../types/message.html#aiogram.types.message.Message.answer_document "aiogram.types.message.Message.answer_document")
- [`aiogram.types.message.Message.reply_document()`](../types/message.html#aiogram.types.message.Message.reply_document "aiogram.types.message.Message.reply_document")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_document()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_document "aiogram.types.chat_join_request.ChatJoinRequest.answer_document")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_document_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_document_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_document_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_document()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_document "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_document")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_document()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_document "aiogram.types.inaccessible_message.InaccessibleMessage.answer_document")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_document()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_document "aiogram.types.inaccessible_message.InaccessibleMessage.reply_document")
