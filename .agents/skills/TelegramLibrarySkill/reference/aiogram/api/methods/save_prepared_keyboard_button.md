# savePreparedKeyboardButton

> Source: [https://docs.aiogram.dev/en/latest/api/methods/save_prepared_keyboard_button.html](https://docs.aiogram.dev/en/latest/api/methods/save_prepared_keyboard_button.html)

Returns: `PreparedKeyboardButton`

*class* aiogram.methods.save_prepared_keyboard_button.SavePreparedKeyboardButton(*\**, *user_id: int*, *button: [KeyboardButton](../types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")*, *\*\*extra_data: Any*)
:   Stores a keyboard button that can be used by a user within a Mini App. Returns a [`aiogram.types.prepared_keyboard_button.PreparedKeyboardButton`](../types/prepared_keyboard_button.html#aiogram.types.prepared_keyboard_button.PreparedKeyboardButton "aiogram.types.prepared_keyboard_button.PreparedKeyboardButton") object.

    Source: <https://core.telegram.org/bots/api#savepreparedkeyboardbutton>

    user_id*: int*
    :   Unique identifier of the target user that can use the button

    button*: [KeyboardButton](../types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")*
    :   A JSON-serialized object describing the button to be saved. The button must be of the type *request_users*, *request_chat*, or *request_managed_bot*

## Usage

### As bot method

```
result: PreparedKeyboardButton = await bot.save_prepared_keyboard_button(...)
```

### Method as object

Imports:

- `from aiogram.methods.save_prepared_keyboard_button import SavePreparedKeyboardButton`
- alias: `from aiogram.methods import SavePreparedKeyboardButton`

#### With specific bot

```
result: PreparedKeyboardButton = await bot(SavePreparedKeyboardButton(...))
```

#### As reply into Webhook in handler

```
return SavePreparedKeyboardButton(...)
```
