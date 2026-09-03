# sendPaidMedia

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_paid_media.html](https://docs.aiogram.dev/en/latest/api/methods/send_paid_media.html)

Returns: `Message`

*class* aiogram.methods.send_paid_media.SendPaidMedia(*\**, *chat_id: int | str*, *star_count: int*, *media: list[Annotated[[InputPaidMediaLivePhoto](../types/input_paid_media_live_photo.html#aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto "aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto") | [InputPaidMediaPhoto](../types/input_paid_media_photo.html#aiogram.types.input_paid_media_photo.InputPaidMediaPhoto "aiogram.types.input_paid_media_photo.InputPaidMediaPhoto") | [InputPaidMediaVideo](../types/input_paid_media_video.html#aiogram.types.input_paid_media_video.InputPaidMediaVideo "aiogram.types.input_paid_media_video.InputPaidMediaVideo"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]]*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *payload: str | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *suggested_post_parameters: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | [ReplyKeyboardMarkup](../types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") | [ReplyKeyboardRemove](../types/reply_keyboard_remove.html#aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove "aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove") | [ForceReply](../types/force_reply.html#aiogram.types.force_reply.ForceReply "aiogram.types.force_reply.ForceReply") | None = None*, *\*\*extra_data: Any*)
:   Use this method to send paid media. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendpaidmedia>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat’s balance. Otherwise, they will be credited to the bot’s balance

    star_count*: int*
    :   The number of Telegram Stars that must be paid to buy access to the media; 1-25000

    media*: list[InputPaidMediaUnion]*
    :   A JSON-serialized Array describing the media to be sent; up to 10 items

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    payload*: str | None*
    :   Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes

    caption*: str | None*
    :   Media caption, 0-1024 characters after entities parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the media caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | None*
    :   Pass `True` if the caption must be shown above the message media

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: ReplyMarkupUnion | None*
    :   Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

## Usage

### As bot method

```
result: Message = await bot.send_paid_media(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_paid_media import SendPaidMedia`
- alias: `from aiogram.methods import SendPaidMedia`

#### With specific bot

```
result: Message = await bot(SendPaidMedia(...))
```

#### As reply into Webhook in handler

```
return SendPaidMedia(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_paid_media()`](../types/message.html#aiogram.types.message.Message.answer_paid_media "aiogram.types.message.Message.answer_paid_media")
- [`aiogram.types.message.Message.reply_paid_media()`](../types/message.html#aiogram.types.message.Message.reply_paid_media "aiogram.types.message.Message.reply_paid_media")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_paid_media()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_paid_media "aiogram.types.inaccessible_message.InaccessibleMessage.answer_paid_media")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_paid_media()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_paid_media "aiogram.types.inaccessible_message.InaccessibleMessage.reply_paid_media")
