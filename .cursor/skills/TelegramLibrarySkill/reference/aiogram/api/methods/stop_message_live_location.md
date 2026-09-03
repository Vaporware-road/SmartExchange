# stopMessageLiveLocation

> Source: [https://docs.aiogram.dev/en/latest/api/methods/stop_message_live_location.html](https://docs.aiogram.dev/en/latest/api/methods/stop_message_live_location.html)

Returns: `Message | bool`

*class* aiogram.methods.stop_message_live_location.StopMessageLiveLocation(*\**, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to stop updating a live location message before *live_period* expires. On success, if the message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned.

    Source: <https://core.telegram.org/bots/api#stopmessagelivelocation>

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message with live location to stop

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message | bool = await bot.stop_message_live_location(...)
```

### Method as object

Imports:

- `from aiogram.methods.stop_message_live_location import StopMessageLiveLocation`
- alias: `from aiogram.methods import StopMessageLiveLocation`

#### With specific bot

```
result: Message | bool = await bot(StopMessageLiveLocation(...))
```

#### As reply into Webhook in handler

```
return StopMessageLiveLocation(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.stop_live_location()`](../types/message.html#aiogram.types.message.Message.stop_live_location "aiogram.types.message.Message.stop_live_location")
