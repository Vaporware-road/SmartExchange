# setCustomEmojiStickerSetThumbnail

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_custom_emoji_sticker_set_thumbnail.html](https://docs.aiogram.dev/en/latest/api/methods/set_custom_emoji_sticker_set_thumbnail.html)

Returns: `bool`

*class* aiogram.methods.set_custom_emoji_sticker_set_thumbnail.SetCustomEmojiStickerSetThumbnail(*\**, *name: str*, *custom_emoji_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to set the thumbnail of a custom emoji sticker set. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail>

    name*: str*
    :   Sticker set name

    custom_emoji_id*: str | None*
    :   Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail

## Usage

### As bot method

```
result: bool = await bot.set_custom_emoji_sticker_set_thumbnail(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_custom_emoji_sticker_set_thumbnail import SetCustomEmojiStickerSetThumbnail`
- alias: `from aiogram.methods import SetCustomEmojiStickerSetThumbnail`

#### With specific bot

```
result: bool = await bot(SetCustomEmojiStickerSetThumbnail(...))
```

#### As reply into Webhook in handler

```
return SetCustomEmojiStickerSetThumbnail(...)
```
