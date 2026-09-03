# addStickerToSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/add_sticker_to_set.html](https://docs.aiogram.dev/en/latest/api/methods/add_sticker_to_set.html)

Returns: `bool`

*class* aiogram.methods.add_sticker_to_set.AddStickerToSet(*\**, *user_id: int*, *name: str*, *sticker: [InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")*, *\*\*extra_data: Any*)
:   Use this method to add a new sticker to a set created by the bot. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#addstickertoset>

    user_id*: int*
    :   User identifier of sticker set owner

    name*: str*
    :   Sticker set name

    sticker*: [InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")*
    :   A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn’t changed

## Usage

### As bot method

```
result: bool = await bot.add_sticker_to_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.add_sticker_to_set import AddStickerToSet`
- alias: `from aiogram.methods import AddStickerToSet`

#### With specific bot

```
result: bool = await bot(AddStickerToSet(...))
```

#### As reply into Webhook in handler

```
return AddStickerToSet(...)
```
