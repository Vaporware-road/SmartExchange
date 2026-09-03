# getFile

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_file.html](https://docs.aiogram.dev/en/latest/api/methods/get_file.html)

Returns: `File`

*class* aiogram.methods.get_file.GetFile(*\**, *file_id: str*, *\*\*extra_data: Any*)
:   Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a [`aiogram.types.file.File`](../types/file.html#aiogram.types.file.File "aiogram.types.file.File") object is returned. The file can then be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`, where `<file_path>` is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [`aiogram.methods.get_file.GetFile`](#aiogram.methods.get_file.GetFile "aiogram.methods.get_file.GetFile") again.
    **Note:** This function may not preserve the original file name and MIME type. You should save the file’s MIME type and name (if available) when the File object is received.

    Source: <https://core.telegram.org/bots/api#getfile>

    file_id*: str*
    :   File identifier to get information about

## Usage

### As bot method

```
result: File = await bot.get_file(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_file import GetFile`
- alias: `from aiogram.methods import GetFile`

#### With specific bot

```
result: File = await bot(GetFile(...))
```
