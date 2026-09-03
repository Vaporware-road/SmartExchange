# sendRichMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_rich_message.html](https://docs.aiogram.dev/en/latest/api/methods/send_rich_message.html)

Returns: `Message`

*class* aiogram.methods.send_rich_message.SendRichMessage(*\**, *chat_id: int | str*, *rich_message: [InputRichMessage](../types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | [ReplyKeyboardMarkup](../types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") | [ReplyKeyboardRemove](../types/reply_keyboard_remove.html#aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove "aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove") | [ForceReply](../types/force_reply.html#aiogram.types.force_reply.ForceReply "aiogram.types.force_reply.ForceReply") | None = None*, *\*\*extra_data: Any*)
:   Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendrichmessage>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    rich_message*: [InputRichMessage](../types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*
    :   The message to be sent

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent. Bot can send rich messages on behalf of a business account only if the corresponding user can send rich messages

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | [ReplyKeyboardMarkup](../types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") | [ReplyKeyboardRemove](../types/reply_keyboard_remove.html#aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove "aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove") | [ForceReply](../types/force_reply.html#aiogram.types.force_reply.ForceReply "aiogram.types.force_reply.ForceReply") | None*
    :   Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

## Usage

### As bot method

```
result: Message = await bot.send_rich_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_rich_message import SendRichMessage`
- alias: `from aiogram.methods import SendRichMessage`

#### With specific bot

```
result: Message = await bot(SendRichMessage(...))
```

#### As reply into Webhook in handler

```
return SendRichMessage(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_rich()`](../types/message.html#aiogram.types.message.Message.answer_rich "aiogram.types.message.Message.answer_rich")
- [`aiogram.types.message.Message.reply_rich()`](../types/message.html#aiogram.types.message.Message.reply_rich "aiogram.types.message.Message.reply_rich")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_rich()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_rich "aiogram.types.inaccessible_message.InaccessibleMessage.answer_rich")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_rich()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_rich "aiogram.types.inaccessible_message.InaccessibleMessage.reply_rich")
