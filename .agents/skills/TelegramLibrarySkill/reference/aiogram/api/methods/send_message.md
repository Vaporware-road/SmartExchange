# sendMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_message.html](https://docs.aiogram.dev/en/latest/api/methods/send_message.html)

Returns: `Message`

*class* aiogram.methods.send_message.SendMessage(*\**, *chat_id: int | str*, *text: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *link_preview_options: ~aiogram.types.link_preview_options.LinkPreviewOptions | ~aiogram.client.default.Default | None = <Default('link_preview')>*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *disable_web_page_preview: bool | ~aiogram.client.default.Default | None = <Default('link_preview_is_disabled')>*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to send text messages. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendmessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    text*: str*
    :   Text of the message to be sent, 1-4096 characters after entities parsing

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    parse_mode*: str | Default | None*
    :   Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*

    link_preview_options*: [LinkPreviewOptions](../types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | Default | None*
    :   Link preview generation options for the message

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

    disable_web_page_preview*: bool | Default | None*
    :   Disables link previews for links in this message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_message import SendMessage`
- alias: `from aiogram.methods import SendMessage`

#### With specific bot

```
result: Message = await bot(SendMessage(...))
```

#### As reply into Webhook in handler

```
return SendMessage(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer()`](../types/message.html#aiogram.types.message.Message.answer "aiogram.types.message.Message.answer")
- [`aiogram.types.message.Message.reply()`](../types/message.html#aiogram.types.message.Message.reply "aiogram.types.message.Message.reply")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer "aiogram.types.chat_join_request.ChatJoinRequest.answer")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer "aiogram.types.chat_member_updated.ChatMemberUpdated.answer")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer "aiogram.types.inaccessible_message.InaccessibleMessage.answer")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply "aiogram.types.inaccessible_message.InaccessibleMessage.reply")
