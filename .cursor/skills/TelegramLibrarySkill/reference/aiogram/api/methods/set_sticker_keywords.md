# setStickerKeywords

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_sticker_keywords.html](https://docs.aiogram.dev/en/latest/api/methods/set_sticker_keywords.html)

Returns: `bool`

*class* aiogram.methods.set_sticker_keywords.SetStickerKeywords(*\**, *sticker: str*, *keywords: list[str] | None = None*, *\*\*extra_data: Any*)
:   Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setstickerkeywords>

    sticker*: str*
    :   File identifier of the sticker

    keywords*: list[str] | None*
    :   A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters

## Usage

### As bot method

```
result: bool = await bot.set_sticker_keywords(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_sticker_keywords import SetStickerKeywords`
- alias: `from aiogram.methods import SetStickerKeywords`

#### With specific bot

```
result: bool = await bot(SetStickerKeywords(...))
```

#### As reply into Webhook in handler

```
return SetStickerKeywords(...)
```
