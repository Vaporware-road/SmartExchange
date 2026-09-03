# editMessageLiveLocation

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_message_live_location.html](https://docs.aiogram.dev/en/latest/api/methods/edit_message_live_location.html)

Returns: `Message | bool`

*class* aiogram.methods.edit_message_live_location.EditMessageLiveLocation(*\**, *latitude: float*, *longitude: float*, *business_connection_id: str | None = None*, *chat_id: int | str | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *live_period: int | None = None*, *horizontal_accuracy: float | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit live location messages. A location can be edited until its *live_period* expires or editing is explicitly disabled by a call to [`aiogram.methods.stop_message_live_location.StopMessageLiveLocation`](stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation"). On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned.

    Source: <https://core.telegram.org/bots/api#editmessagelivelocation>

    latitude*: float*
    :   Latitude of new location

    longitude*: float*
    :   Longitude of new location

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    chat_id*: ChatIdUnion | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the message to edit

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

    live_period*: int | None*
    :   New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live_period* remains unchanged

    horizontal_accuracy*: float | None*
    :   The radius of uncertainty for the location, measured in meters; 0-1500

    heading*: int | None*
    :   Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified

    proximity_alert_radius*: int | None*
    :   The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Message | bool = await bot.edit_message_live_location(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_message_live_location import EditMessageLiveLocation`
- alias: `from aiogram.methods import EditMessageLiveLocation`

#### With specific bot

```
result: Message | bool = await bot(EditMessageLiveLocation(...))
```

#### As reply into Webhook in handler

```
return EditMessageLiveLocation(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.edit_live_location()`](../types/message.html#aiogram.types.message.Message.edit_live_location "aiogram.types.message.Message.edit_live_location")
