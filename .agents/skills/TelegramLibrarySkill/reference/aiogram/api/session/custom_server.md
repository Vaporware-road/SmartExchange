# Use Custom API server

> Source: [https://docs.aiogram.dev/en/latest/api/session/custom_server.html](https://docs.aiogram.dev/en/latest/api/session/custom_server.html)

For example, if you want to use self-hosted API server:

```
session = AiohttpSession(
    api=TelegramAPIServer.from_base('http://localhost:8082')
)
bot = Bot(..., session=session)
```

*class* aiogram.client.telegram.TelegramAPIServer(*base: str*, *file: str*, *is_local: bool = False*, *wrap_local_file: ~aiogram.client.telegram.FilesPathWrapper = <aiogram.client.telegram.BareFilesPathWrapper object>*)
:   Base config for API Endpoints

    api_url(*token: str*, *method: str*) → str
    :   Generate URL for API methods

        Parameters:
        :   - **token** – Bot token
            - **method** – API method name (case insensitive)

        Returns:
        :   URL

    base*: str*
    :   Base URL

    file*: str*
    :   Files URL

    file_url(*token: str*, *path: str | Path*) → str
    :   Generate URL for downloading files

        Parameters:
        :   - **token** – Bot token
            - **path** – file path

        Returns:
        :   URL

    *classmethod* from_base(*base: str*, *\*\*kwargs: Any*) → [TelegramAPIServer](#aiogram.client.telegram.TelegramAPIServer "aiogram.client.telegram.TelegramAPIServer")
    :   Use this method to auto-generate TelegramAPIServer instance from base URL

        Parameters:
        :   **base** – Base URL

        Returns:
        :   instance of [`TelegramAPIServer`](#aiogram.client.telegram.TelegramAPIServer "aiogram.client.telegram.TelegramAPIServer")

    is_local*: bool* *= False*
    :   Mark this server is
        in [local mode](https://core.telegram.org/bots/api#using-a-local-bot-api-server).

    wrap_local_file*: FilesPathWrapper* *= <aiogram.client.telegram.BareFilesPathWrapper object>*
    :   Callback to wrap files path in local mode
