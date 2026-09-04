# sendChecklist

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_checklist.html](https://docs.aiogram.dev/en/latest/api/methods/send_checklist.html)

Returns: `Message`

*class* aiogram.methods.send_checklist.SendChecklist(*\**, *business_connection_id: str*, *chat_id: int | str*, *checklist: [InputChecklist](../types/input_checklist.html#aiogram.types.input_checklist.InputChecklist "aiogram.types.input_checklist.InputChecklist")*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *message_effect_id: str | None = None*, *reply_parameters: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to send a checklist on behalf of a connected business account. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendchecklist>

    business_connection_id*: str*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot in the format `@username`

    checklist*: [InputChecklist](../types/input_checklist.html#aiogram.types.input_checklist.InputChecklist "aiogram.types.input_checklist.InputChecklist")*
    :   A JSON-serialized object for the checklist to send

    disable_notification*: bool | None*
    :   Sends the message silently. Users will receive a notification with no sound

    protect_content*: bool | None*
    :   Protects the contents of the sent message from forwarding and saving

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   A JSON-serialized object for description of the message to reply to

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message = await bot.send_checklist(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_checklist import SendChecklist`
- alias: `from aiogram.methods import SendChecklist`

#### With specific bot

```
result: Message = await bot(SendChecklist(...))
```

#### As reply into Webhook in handler

```
return SendChecklist(...)
```
