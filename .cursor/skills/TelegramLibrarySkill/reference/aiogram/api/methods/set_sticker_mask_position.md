# setStickerMaskPosition

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_sticker_mask_position.html](https://docs.aiogram.dev/en/latest/api/methods/set_sticker_mask_position.html)

Returns: `bool`

*class* aiogram.methods.set_sticker_mask_position.SetStickerMaskPosition(*\**, *sticker: str*, *mask_position: [MaskPosition](../types/mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the [mask position](https://core.telegram.org/bots/api#maskposition) of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setstickermaskposition>

    sticker*: str*
    :   File identifier of the sticker

    mask_position*: [MaskPosition](../types/mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None*
    :   A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position

## Usage

### As bot method

```
result: bool = await bot.set_sticker_mask_position(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_sticker_mask_position import SetStickerMaskPosition`
- alias: `from aiogram.methods import SetStickerMaskPosition`

#### With specific bot

```
result: bool = await bot(SetStickerMaskPosition(...))
```

#### As reply into Webhook in handler

```
return SetStickerMaskPosition(...)
```
