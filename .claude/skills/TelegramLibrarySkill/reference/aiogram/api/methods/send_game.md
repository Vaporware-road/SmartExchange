# sendGame

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_game.html](https://docs.aiogram.dev/en/latest/api/methods/send_game.html)

Returns: `Message`

*class* aiogram.methods.send_game.SendGame(*\**, *chat_id: int | str*, *game_short_name: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Use this method to send a game. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendgame>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot in the format `@username`. Games can’t be sent to channel direct messages chats and channel chats

    game_short_name*: str*
    :   Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather)

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_game(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_game import SendGame`
- alias: `from aiogram.methods import SendGame`

#### With specific bot

```
result: Message = await bot(SendGame(...))
```

#### As reply into Webhook in handler

```
return SendGame(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_game()`](../types/message.html#aiogram.types.message.Message.answer_game "aiogram.types.message.Message.answer_game")
- [`aiogram.types.message.Message.reply_game()`](../types/message.html#aiogram.types.message.Message.reply_game "aiogram.types.message.Message.reply_game")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_game()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_game "aiogram.types.chat_join_request.ChatJoinRequest.answer_game")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_game_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_game_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_game_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_game()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_game "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_game")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_game()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_game "aiogram.types.inaccessible_message.InaccessibleMessage.answer_game")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_game()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_game "aiogram.types.inaccessible_message.InaccessibleMessage.reply_game")
