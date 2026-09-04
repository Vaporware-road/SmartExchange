# getStickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_sticker_set.html](https://docs.aiogram.dev/en/latest/api/methods/get_sticker_set.html)

Returns: `StickerSet`

*class* aiogram.methods.get_sticker_set.GetStickerSet(*\**, *name: str*, *\*\*extra_data: Any*)
:   Use this method to get a sticker set. On success, a [`aiogram.types.sticker_set.StickerSet`](../types/sticker_set.html#aiogram.types.sticker_set.StickerSet "aiogram.types.sticker_set.StickerSet") object is returned.

    Source: <https://core.telegram.org/bots/api#getstickerset>

    name*: str*
    :   Name of the sticker set

## Usage

### As bot method

```
result: StickerSet = await bot.get_sticker_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_sticker_set import GetStickerSet`
- alias: `from aiogram.methods import GetStickerSet`

#### With specific bot

```
result: StickerSet = await bot(GetStickerSet(...))
```
