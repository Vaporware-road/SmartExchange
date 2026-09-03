# How to upload file?

> Source: [https://docs.aiogram.dev/en/latest/api/upload_file.html](https://docs.aiogram.dev/en/latest/api/upload_file.html)

As says [official Telegram Bot API documentation](https://core.telegram.org/bots/api#sending-files)
there are three ways to send files (photos, stickers, audio, media, etc.):

If the file is already stored somewhere on the Telegram servers or file is available by the URL,
you don’t need to reupload it.

But if you need to upload a new file just use subclasses of [InputFile](types/input_file.html).

Here are the three different available builtin types of input file:

- [`aiogram.types.input_file.FSInputFile`](#aiogram.types.input_file.FSInputFile "aiogram.types.input_file.FSInputFile") - [uploading from file system](#upload-from-file-system)
- [`aiogram.types.input_file.BufferedInputFile`](#aiogram.types.input_file.BufferedInputFile "aiogram.types.input_file.BufferedInputFile") - [uploading from buffer](#upload-from-buffer)
- [`aiogram.types.input_file.URLInputFile`](#aiogram.types.input_file.URLInputFile "aiogram.types.input_file.URLInputFile") - [uploading from URL](#upload-from-url)

Warning

**Be respectful to Telegram**

Instances of InputFile are reusable.
That means you can create an instance of InputFile and send it multiple times. However, Telegram does not recommend doing this. Instead, once you upload a file, save its file_id and reuse that later.

## Upload from file system

By first step you will need to import InputFile wrapper:

```
from aiogram.types import FSInputFile
```

Then you can use it:

```
cat = FSInputFile("cat.png")
agenda = FSInputFile("my-document.pdf", filename="agenda-2019-11-19.pdf")
```

*class* aiogram.types.input_file.FSInputFile(*path: str | Path*, *filename: str | None = None*, *chunk_size: int = 65536*)
:   __init__(*path: str | Path*, *filename: str | None = None*, *chunk_size: int = 65536*)
    :   Represents object for uploading files from filesystem

        Parameters:
        :   - **path** – Path to file
            - **filename** – Filename to be propagated to telegram.
              By default, will be parsed from path
            - **chunk_size** – Uploading chunk size

## Upload from buffer

Files can be also passed from buffer
(For example you generate image using [Pillow](https://pillow.readthedocs.io/en/stable/)
and you want to send it to Telegram):

Import wrapper:

```
from aiogram.types import BufferedInputFile
```

And then you can use it:

```
text_file = BufferedInputFile(b"Hello, world!", filename="file.txt")
```

*class* aiogram.types.input_file.BufferedInputFile(*file: bytes*, *filename: str*, *chunk_size: int = 65536*)
:   __init__(*file: bytes*, *filename: str*, *chunk_size: int = 65536*)
    :   Represents object for uploading files from filesystem

        Parameters:
        :   - **file** – Bytes
            - **filename** – Filename to be propagated to telegram.
            - **chunk_size** – Uploading chunk size

## Upload from url

If you need to upload a file from another server, but the direct link is bound to your server’s IP,
or you want to bypass native [upload limits](https://core.telegram.org/bots/api#sending-files)
by URL, you can use [`aiogram.types.input_file.URLInputFile`](#aiogram.types.input_file.URLInputFile "aiogram.types.input_file.URLInputFile").

Import wrapper:

```
from aiogram.types import URLInputFile
```

And then you can use it:

```
image = URLInputFile(
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    filename="python-logo.png"
)
```

*class* aiogram.types.input_file.URLInputFile(*url: str*, *headers: dict[str, Any] | None = None*, *filename: str | None = None*, *chunk_size: int = 65536*, *timeout: int = 30*, *bot: Bot | None = None*)
