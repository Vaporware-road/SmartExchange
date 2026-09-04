# editMessageChecklist

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_checklist.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_checklist.html)

Returns: `Message`

*class* aiogram.methods.edit_message_checklist.EditMessageChecklist(*\**, *business_connection_id: str*, *chat_id: int | str*, *message_id: int*, *checklist: [InputChecklist](../types/input_checklist.html#aiogram.types.input_checklist.InputChecklist "aiogram.types.input_checklist.InputChecklist")*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit a checklist on behalf of a connected business account. On success, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#editmessagechecklist>

    business_connection_id*: str*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot in the format `@username`

    message_id*: int*
    :   Unique identifier for the target message

    checklist*: [InputChecklist](../types/input_checklist.html#aiogram.types.input_checklist.InputChecklist "aiogram.types.input_checklist.InputChecklist")*
    :   A JSON-serialized object for the new checklist

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for the new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) for the message

## Usage

### As bot method

```
result: Message = await bot.edit_message_checklist(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_checklist import EditMessageChecklist`
- alias: `from aiogram.methods import EditMessageChecklist`

#### With specific bot

```
result: Message = await bot(EditMessageChecklist(...))
```

#### As reply into Webhook in handler

```
return EditMessageChecklist(...)
```
