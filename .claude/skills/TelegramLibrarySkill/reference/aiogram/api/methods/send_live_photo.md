# sendLivePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_live_photo.html](https://docs.aiogram.dev/en/latest/api/methods/send_live_photo.html)

Returns: `Message`

*class* aiogram.methods.send_live_photo.SendLivePhoto(*\**, *chat_id: int | str*, *live_photo: str | [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *photo: str | [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | [ReplyKeyboardMarkup](../types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") | [ReplyKeyboardRemove](../types/reply_keyboard_remove.html#aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove "aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove") | [ForceReply](../types/force_reply.html#aiogram.types.force_reply.ForceReply "aiogram.types.force_reply.ForceReply") | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to send live photos. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendlivephoto>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

    live_photo*: str | [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*
    :   Live photo video to send. The video must be no longer than 10 seconds and must not exceed 10 MB in size. Pass a file_id as String to send a video that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported

    photo*: str | [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*
    :   The static photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending live photos by a URL is currently unsupported

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    caption*: str | None*
    :   Video caption (may also be used when resending videos by *file_id*), 0-1024 characters after entities parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | None*
    :   Pass `True` if the caption must be shown above the message media

    has_spoiler*: bool | None*
    :   Pass `True` if the video needs to be covered with a spoiler animation

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

    receiver_user_id*: int | None*
    :   For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details

    callback_query_id*: str | None*
    :   For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any

## Usage

### As bot method

```
result: Message = await bot.send_live_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_live_photo import SendLivePhoto`
- alias: `from aiogram.methods import SendLivePhoto`

#### With specific bot

```
result: Message = await bot(SendLivePhoto(...))
```

#### As reply into Webhook in handler

```
return SendLivePhoto(...)
```
