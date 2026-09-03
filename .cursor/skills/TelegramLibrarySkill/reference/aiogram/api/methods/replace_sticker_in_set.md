# replaceStickerInSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/replace_sticker_in_set.html](https://docs.aiogram.dev/en/latest/api/methods/replace_sticker_in_set.html)

Returns: `bool`

*class* aiogram.methods.replace_sticker_in_set.ReplaceStickerInSet(*\**, *user_id: int*, *name: str*, *old_sticker: str*, *sticker: [InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")*, *\*\*extra_data: Any*)
:   Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling [`aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet`](delete_sticker_from_set.html#aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet "aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet"), then [`aiogram.methods.add_sticker_to_set.AddStickerToSet`](add_sticker_to_set.html#aiogram.methods.add_sticker_to_set.AddStickerToSet "aiogram.methods.add_sticker_to_set.AddStickerToSet"), then [`aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet`](set_sticker_position_in_set.html#aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet "aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet"). Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#replacestickerinset>

    user_id*: int*
    :   User identifier of the sticker set owner

    name*: str*
    :   Sticker set name

    old_sticker*: str*
    :   File identifier of the replaced sticker

    sticker*: [InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")*
    :   A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged

## Usage

### As bot method

```
result: bool = await bot.replace_sticker_in_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.replace_sticker_in_set import ReplaceStickerInSet`
- alias: `from aiogram.methods import ReplaceStickerInSet`

#### With specific bot

```
result: bool = await bot(ReplaceStickerInSet(...))
```

#### As reply into Webhook in handler

```
return ReplaceStickerInSet(...)
```
