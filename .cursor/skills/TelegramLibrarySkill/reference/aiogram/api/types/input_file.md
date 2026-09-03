# InputFile

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_file.html](https://docs.aiogram.dev/en/latest/api/types/input_file.html)

*class* aiogram.types.input_file.InputFile(*filename: str | None = None*, *chunk_size: int = 65536*)
:   This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    Source: <https://core.telegram.org/bots/api#inputfile>

    *abstract async* read(*bot: Bot*) → AsyncGenerator[bytes, None]

*class* aiogram.types.input_file.BufferedInputFile(*file: bytes*, *filename: str*, *chunk_size: int = 65536*)
:   *classmethod* from_file(*path: str | Path*, *filename: str | None = None*, *chunk_size: int = 65536*) → [BufferedInputFile](../upload_file.html#aiogram.types.input_file.BufferedInputFile "aiogram.types.input_file.BufferedInputFile")
    :   Create buffer from file

        Parameters:
        :   - **path** – Path to file
            - **filename** – Filename to be propagated to telegram.
              By default, will be parsed from path
            - **chunk_size** – Uploading chunk size

        Returns:
        :   instance of [`BufferedInputFile`](../upload_file.html#aiogram.types.input_file.BufferedInputFile "aiogram.types.input_file.BufferedInputFile")

    *async* read(*bot: Bot*) → AsyncGenerator[bytes, None]

*class* aiogram.types.input_file.FSInputFile(*path: str | Path*, *filename: str | None = None*, *chunk_size: int = 65536*)
:   *async* read(*bot: Bot*) → AsyncGenerator[bytes, None]

*class* aiogram.types.input_file.URLInputFile(*url: str*, *headers: dict[str, Any] | None = None*, *filename: str | None = None*, *chunk_size: int = 65536*, *timeout: int = 30*, *bot: Bot | None = None*)
:   *async* read(*bot: Bot*) → AsyncGenerator[bytes, None]
