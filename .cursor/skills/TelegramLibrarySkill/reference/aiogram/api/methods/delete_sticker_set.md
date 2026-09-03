# deleteStickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_sticker_set.html](https://docs.aiogram.dev/en/latest/api/methods/delete_sticker_set.html)

Returns: `bool`

*class* aiogram.methods.delete_sticker_set.DeleteStickerSet(*\**, *name: str*, *\*\*extra_data: Any*)
:   Use this method to delete a sticker set that was created by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletestickerset>

    name*: str*
    :   Sticker set name

## Usage

### As bot method

```
result: bool = await bot.delete_sticker_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_sticker_set import DeleteStickerSet`
- alias: `from aiogram.methods import DeleteStickerSet`

#### With specific bot

```
result: bool = await bot(DeleteStickerSet(...))
```

#### As reply into Webhook in handler

```
return DeleteStickerSet(...)
```
