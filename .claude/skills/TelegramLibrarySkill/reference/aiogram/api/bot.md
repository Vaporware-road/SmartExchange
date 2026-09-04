# Bot

> Source: [https://docs.aiogram.dev/en/latest/api/bot.html](https://docs.aiogram.dev/en/latest/api/bot.html)

Bot instance can be created from `aiogram.Bot` (`from aiogram import Bot`) and
you can’t use methods without instance of bot with configured token.

This class has aliases for all methods and named in `lower_camel_case`.

For example `sendMessage` named `send_message` and has the same specification with all class-based methods.

Warning

A full list of methods can be found in the appropriate section of the documentation

*class* aiogram.client.bot.Bot(*token: str*, *session: [BaseSession](session/base.html#aiogram.client.session.base.BaseSession "aiogram.client.session.base.BaseSession") | None = None*, *default: [DefaultBotProperties](defaults.html#aiogram.client.default.DefaultBotProperties "aiogram.client.default.DefaultBotProperties") | None = None*, *\*\*kwargs: Any*)
:   Bases: `object`

    __init__(*token: str*, *session: [BaseSession](session/base.html#aiogram.client.session.base.BaseSession "aiogram.client.session.base.BaseSession") | None = None*, *default: [DefaultBotProperties](defaults.html#aiogram.client.default.DefaultBotProperties "aiogram.client.default.DefaultBotProperties") | None = None*, *\*\*kwargs: Any*) → None
    :   Bot class

        Parameters:
        :   - **token** – Telegram Bot token [Obtained from @BotFather](https://t.me/BotFather)
            - **session** – HTTP Client session (For example AiohttpSession).
              If not specified it will be automatically created.
            - **default** – Default bot properties.
              If specified it will be propagated into the API methods at runtime.

        Raises:
        :   **TokenValidationError** – When token has invalid format this exception will be raised

    *property* token*: str*

    *property* id*: int*
    :   Get bot ID from token

        Returns:

    context(*auto_close: bool = True*) → AsyncIterator[Bot]
    :   Generate bot context

        Parameters:
        :   **auto_close** – close session on exit

        Returns:

    *async* me() → [User](types/user.html#aiogram.types.user.User "aiogram.types.user.User")
    :   Cached alias for getMe method

        Returns:

    *async* download_file(*file_path: str | Path*, *destination: BinaryIO | Path | str | None = None*, *timeout: int = 30*, *chunk_size: int = 65536*, *seek: bool = True*) → BinaryIO | None
    :   Download file by file_path to destination.

        If you want to automatically create destination (`io.BytesIO`) use default
        value of destination and handle result of this method.

        Parameters:
        :   - **file_path** – File path on Telegram server (You can get it from `aiogram.types.File`)
            - **destination** – Filename, file path or instance of `io.IOBase`. For e.g. `io.BytesIO`, defaults to None
            - **timeout** – Total timeout in seconds, defaults to 30
            - **chunk_size** – File chunks size, defaults to 64 kb
            - **seek** – Go to start of file when downloading is finished. Used only for destination with `typing.BinaryIO` type, defaults to True

    *async* download(*file: str | Downloadable*, *destination: BinaryIO | Path | str | None = None*, *timeout: int = 30*, *chunk_size: int = 65536*, *seek: bool = True*) → BinaryIO | None
    :   Download file by file_id or Downloadable object to destination.

        If you want to automatically create destination (`io.BytesIO`) use default
        value of destination and handle result of this method.

        Parameters:
        :   - **file** – file_id or Downloadable object
            - **destination** – Filename, file path or instance of `io.IOBase`. For e.g. `io.BytesIO`, defaults to None
            - **timeout** – Total timeout in seconds, defaults to 30
            - **chunk_size** – File chunks size, defaults to 64 kb
            - **seek** – Go to start of file when downloading is finished. Used only for destination with `typing.BinaryIO` type, defaults to True
