# copyMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/copy_message.html](https://docs.aiogram.dev/en/latest/api/methods/copy_message.html)

Returns: `MessageId`

*class* aiogram.methods.copy_message.CopyMessage(*\**, *chat_id: int | str*, *from_chat_id: int | str*, *message_id: int*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *video_start_timestamp: ~datetime.datetime | ~datetime.timedelta | int | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can’t be copied. A quiz `aiogram.methods.poll.Poll` can be copied only if the value of the field *correct_option_id* is known to the bot. The method is analogous to the method [`aiogram.methods.forward_message.ForwardMessage`](forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage"), but the copied message doesn’t have a link to the original message. Returns the [`aiogram.types.message_id.MessageId`](../types/message_id.html#aiogram.types.message_id.MessageId "aiogram.types.message_id.MessageId") of the sent message on success.

    Source: <https://core.telegram.org/bots/api#copymessage>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    from_chat_id*: ChatIdUnion*
    :   Unique identifier for the chat where the original message was sent (or username of the target bot, supergroup or channel in the format `@username`)

    message_id*: int*
    :   Message identifier in the chat specified in *from_chat_id*

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    video_start_timestamp*: DateTimeUnion | None*
    :   New start timestamp for the copied video in the message

    caption*: str | None*
    :   New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept

    parse_mode*: str | Default | None*
    :   Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   Pass `True` if the caption must be shown above the message media. Ignored if a new caption isn’t specified

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; only available when copying to private chats

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: ReplyMarkupUnion | None*
    :   Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: MessageId = await bot.copy_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.copy_message import CopyMessage`
- alias: `from aiogram.methods import CopyMessage`

#### With specific bot

```
result: MessageId = await bot(CopyMessage(...))
```

#### As reply into Webhook in handler

```
return CopyMessage(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.copy_to()`](../types/message.html#aiogram.types.message.Message.copy_to "aiogram.types.message.Message.copy_to")
