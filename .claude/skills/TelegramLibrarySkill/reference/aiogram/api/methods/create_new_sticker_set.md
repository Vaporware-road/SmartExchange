# createNewStickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/create_new_sticker_set.html](https://docs.aiogram.dev/en/latest/api/methods/create_new_sticker_set.html)

Returns: `bool`

*class* aiogram.methods.create_new_sticker_set.CreateNewStickerSet(*\**, *user_id: int*, *name: str*, *title: str*, *stickers: list[[InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")]*, *sticker_type: str | None = None*, *needs_repainting: bool | None = None*, *sticker_format: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#createnewstickerset>

    user_id*: int*
    :   User identifier of created sticker set owner

    name*: str*
    :   Short name of sticker set, to be used in `t.me/addstickers/` URLs (e.g., *animals*). Can contain only English letters, digits and underscores. Must begin with a letter, can’t contain consecutive underscores and must end in `"_by_<bot_username>"`. `<bot_username>` is case insensitive. 1-64 characters

    title*: str*
    :   Sticker set title, 1-64 characters

    stickers*: list[[InputSticker](../types/input_sticker.html#aiogram.types.input_sticker.InputSticker "aiogram.types.input_sticker.InputSticker")]*
    :   A JSON-serialized list of 1-50 initial stickers to be added to the sticker set

    sticker_type*: str | None*
    :   Type of stickers in the set, pass ‘regular’, ‘mask’, or ‘custom_emoji’. By default, a regular sticker set is created

    needs_repainting*: bool | None*
    :   Pass `True` if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only

    sticker_format*: str | None*
    :   Format of stickers in the set, must be one of ‘static’, ‘animated’, ‘video’

        Deprecated since version API:7.2: <https://core.telegram.org/bots/api-changelog#march-31-2024>

## Usage

### As bot method

```
result: bool = await bot.create_new_sticker_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.create_new_sticker_set import CreateNewStickerSet`
- alias: `from aiogram.methods import CreateNewStickerSet`

#### With specific bot

```
result: bool = await bot(CreateNewStickerSet(...))
```

#### As reply into Webhook in handler

```
return CreateNewStickerSet(...)
```
