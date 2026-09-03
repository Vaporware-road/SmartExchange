# sendDice

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_dice.html](https://docs.aiogram.dev/en/latest/api/methods/send_dice.html)

Returns: `Message`

*class* aiogram.methods.send_dice.SendDice(*\**, *chat_id: int | str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to send an animated emoji that will display a random value. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#senddice>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    emoji*: str | None*
    :   Emoji on which the dice throw animation is based. Currently, must be one of ‘🎲’, ‘🎯’, ‘🏀’, ‘⚽’, ‘🎳’, or ‘🎰’. Dice can have values 1-6 for ‘🎲’, ‘🎯’ and ‘🎳’, values 1-5 for ‘🏀’ and ‘⚽’, and values 1-64 for ‘🎰’. Defaults to ‘🎲’

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding

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

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_dice(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_dice import SendDice`
- alias: `from aiogram.methods import SendDice`

#### With specific bot

```
result: Message = await bot(SendDice(...))
```

#### As reply into Webhook in handler

```
return SendDice(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_dice()`](../types/message.html#aiogram.types.message.Message.answer_dice "aiogram.types.message.Message.answer_dice")
- [`aiogram.types.message.Message.reply_dice()`](../types/message.html#aiogram.types.message.Message.reply_dice "aiogram.types.message.Message.reply_dice")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_dice()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_dice "aiogram.types.chat_join_request.ChatJoinRequest.answer_dice")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_dice_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_dice_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_dice_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_dice()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_dice "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_dice")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_dice()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_dice "aiogram.types.inaccessible_message.InaccessibleMessage.answer_dice")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_dice()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_dice "aiogram.types.inaccessible_message.InaccessibleMessage.reply_dice")
