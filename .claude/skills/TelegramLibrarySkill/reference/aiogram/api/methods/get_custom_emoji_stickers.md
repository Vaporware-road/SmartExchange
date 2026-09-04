# getCustomEmojiStickers

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_custom_emoji_stickers.html](https://docs.aiogram.dev/en/latest/api/methods/get_custom_emoji_stickers.html)

Returns: `list[Sticker]`

*class* aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers(*\**, *custom_emoji_ids: list[str]*, *\*\*extra_data: Any*)
:   Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of [`aiogram.types.sticker.Sticker`](../types/sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") objects.

    Source: <https://core.telegram.org/bots/api#getcustomemojistickers>

    custom_emoji_ids*: list[str]*
    :   A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified

## Usage

### As bot method

```
result: list[Sticker] = await bot.get_custom_emoji_stickers(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_custom_emoji_stickers import GetCustomEmojiStickers`
- alias: `from aiogram.methods import GetCustomEmojiStickers`

#### With specific bot

```
result: list[Sticker] = await bot(GetCustomEmojiStickers(...))
```
