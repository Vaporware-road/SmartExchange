# setStickerSetTitle

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_sticker_set_title.html](https://docs.aiogram.dev/en/latest/api/methods/set_sticker_set_title.html)

Returns: `bool`

*class* aiogram.methods.set_sticker_set_title.SetStickerSetTitle(*\**, *name: str*, *title: str*, *\*\*extra_data: Any*)
:   Use this method to set the title of a created sticker set. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setstickersettitle>

    name*: str*
    :   Sticker set name

    title*: str*
    :   Sticker set title, 1-64 characters

## Usage

### As bot method

```
result: bool = await bot.set_sticker_set_title(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_sticker_set_title import SetStickerSetTitle`
- alias: `from aiogram.methods import SetStickerSetTitle`

#### With specific bot

```
result: bool = await bot(SetStickerSetTitle(...))
```

#### As reply into Webhook in handler

```
return SetStickerSetTitle(...)
```
