# uploadStickerFile

> Source: [https://docs.aiogram.dev/en/latest/api/methods/upload_sticker_file.html](https://docs.aiogram.dev/en/latest/api/methods/upload_sticker_file.html)

Returns: `File`

*class* aiogram.methods.upload_sticker_file.UploadStickerFile(*\**, *user_id: int*, *sticker: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *sticker_format: str*, *\*\*extra_data: Any*)
:   Use this method to upload a file with a sticker for later use in the [`aiogram.methods.create_new_sticker_set.CreateNewStickerSet`](create_new_sticker_set.html#aiogram.methods.create_new_sticker_set.CreateNewStickerSet "aiogram.methods.create_new_sticker_set.CreateNewStickerSet"), [`aiogram.methods.add_sticker_to_set.AddStickerToSet`](add_sticker_to_set.html#aiogram.methods.add_sticker_to_set.AddStickerToSet "aiogram.methods.add_sticker_to_set.AddStickerToSet"), or [`aiogram.methods.replace_sticker_in_set.ReplaceStickerInSet`](replace_sticker_in_set.html#aiogram.methods.replace_sticker_in_set.ReplaceStickerInSet "aiogram.methods.replace_sticker_in_set.ReplaceStickerInSet") methods (the file can be used multiple times). Returns the uploaded [`aiogram.types.file.File`](../types/file.html#aiogram.types.file.File "aiogram.types.file.File") on success.

    Source: <https://core.telegram.org/bots/api#uploadstickerfile>

    user_id*: int*
    :   User identifier of sticker file owner

    sticker*: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*
    :   A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See [https://core.telegram.org/stickers <https://core.telegram.org/stickers>`_`https://core.telegram.org/stickers](https://core.telegram.org/stickers) for technical requirements. [More information on Sending Files »](../upload_file.html#sending-files)

    sticker_format*: str*
    :   Format of the sticker, must be one of ‘static’, ‘animated’, ‘video’

## Usage

### As bot method

```
result: File = await bot.upload_sticker_file(...)
```

### Method as object

Imports:

- `from aiogram.methods.upload_sticker_file import UploadStickerFile`
- alias: `from aiogram.methods import UploadStickerFile`

#### With specific bot

```
result: File = await bot(UploadStickerFile(...))
```
