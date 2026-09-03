# deleteStickerFromSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_sticker_from_set.html](https://docs.aiogram.dev/en/latest/api/methods/delete_sticker_from_set.html)

Returns: `bool`

*class* aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet(*\**, *sticker: str*, *\*\*extra_data: Any*)
:   Use this method to delete a sticker from a set created by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletestickerfromset>

    sticker*: str*
    :   File identifier of the sticker

## Usage

### As bot method

```
result: bool = await bot.delete_sticker_from_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_sticker_from_set import DeleteStickerFromSet`
- alias: `from aiogram.methods import DeleteStickerFromSet`

#### With specific bot

```
result: bool = await bot(DeleteStickerFromSet(...))
```

#### As reply into Webhook in handler

```
return DeleteStickerFromSet(...)
```

### As shortcut from received object

- [`aiogram.types.sticker.Sticker.delete_from_set()`](../types/sticker.html#aiogram.types.sticker.Sticker.delete_from_set "aiogram.types.sticker.Sticker.delete_from_set")
