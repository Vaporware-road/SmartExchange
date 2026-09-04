# setStickerEmojiList

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_sticker_emoji_list.html](https://docs.aiogram.dev/en/latest/api/methods/set_sticker_emoji_list.html)

Returns: `bool`

*class* aiogram.methods.set_sticker_emoji_list.SetStickerEmojiList(*\**, *sticker: str*, *emoji_list: list[str]*, *\*\*extra_data: Any*)
:   Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setstickeremojilist>

    sticker*: str*
    :   File identifier of the sticker

    emoji_list*: list[str]*
    :   A JSON-serialized list of 1-20 emoji associated with the sticker

## Usage

### As bot method

```
result: bool = await bot.set_sticker_emoji_list(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_sticker_emoji_list import SetStickerEmojiList`
- alias: `from aiogram.methods import SetStickerEmojiList`

#### With specific bot

```
result: bool = await bot(SetStickerEmojiList(...))
```

#### As reply into Webhook in handler

```
return SetStickerEmojiList(...)
```
