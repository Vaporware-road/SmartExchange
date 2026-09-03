# setStickerPositionInSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_sticker_position_in_set.html](https://docs.aiogram.dev/en/latest/api/methods/set_sticker_position_in_set.html)

Returns: `bool`

*class* aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet(*\**, *sticker: str*, *position: int*, *\*\*extra_data: Any*)
:   Use this method to move a sticker in a set created by the bot to a specific position. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setstickerpositioninset>

    sticker*: str*
    :   File identifier of the sticker

    position*: int*
    :   New sticker position in the set, zero-based

## Usage

### As bot method

```
result: bool = await bot.set_sticker_position_in_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_sticker_position_in_set import SetStickerPositionInSet`
- alias: `from aiogram.methods import SetStickerPositionInSet`

#### With specific bot

```
result: bool = await bot(SetStickerPositionInSet(...))
```

#### As reply into Webhook in handler

```
return SetStickerPositionInSet(...)
```

### As shortcut from received object

- [`aiogram.types.sticker.Sticker.set_position_in_set()`](../types/sticker.html#aiogram.types.sticker.Sticker.set_position_in_set "aiogram.types.sticker.Sticker.set_position_in_set")
