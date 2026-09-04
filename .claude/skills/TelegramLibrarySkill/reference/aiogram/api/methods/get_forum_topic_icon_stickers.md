# getForumTopicIconStickers

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_forum_topic_icon_stickers.html](https://docs.aiogram.dev/en/latest/api/methods/get_forum_topic_icon_stickers.html)

Returns: `list[Sticker]`

*class* aiogram.methods.get_forum_topic_icon_stickers.GetForumTopicIconStickers(*\*\*extra_data: Any*)
:   Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of [`aiogram.types.sticker.Sticker`](../types/sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") objects.

    Source: <https://core.telegram.org/bots/api#getforumtopiciconstickers>

## Usage

### As bot method

```
result: list[Sticker] = await bot.get_forum_topic_icon_stickers(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_forum_topic_icon_stickers import GetForumTopicIconStickers`
- alias: `from aiogram.methods import GetForumTopicIconStickers`

#### With specific bot

```
result: list[Sticker] = await bot(GetForumTopicIconStickers(...))
```
