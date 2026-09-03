# StickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/types/sticker_set.html](https://docs.aiogram.dev/en/latest/api/types/sticker_set.html)

*class* aiogram.types.sticker_set.StickerSet(*\**, *name: str*, *title: str*, *sticker_type: str*, *stickers: list[[Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")]*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *is_animated: bool | None = None*, *is_video: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a sticker set.

    Source: <https://core.telegram.org/bots/api#stickerset>

    name*: str*
    :   Sticker set name

    title*: str*
    :   Sticker set title

    sticker_type*: str*
    :   Type of stickers in the set, currently one of ‘regular’, ‘mask’, ‘custom_emoji’

    stickers*: list[[Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")]*
    :   List of all set stickers

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format

    is_animated*: bool | None*
    :   `True`, if the sticker set contains [animated stickers](https://telegram.org/blog/animated-stickers)

        Deprecated since version API:7.2: <https://core.telegram.org/bots/api-changelog#march-31-2024>

    is_video*: bool | None*
    :   `True`, if the sticker set contains [video stickers](https://telegram.org/blog/video-stickers-better-reactions)

        Deprecated since version API:7.2: <https://core.telegram.org/bots/api-changelog#march-31-2024>
