# Base

> Source: [https://docs.aiogram.dev/en/latest/api/session/base.html](https://docs.aiogram.dev/en/latest/api/session/base.html)

Abstract session for all client sessions

*class* aiogram.client.session.base.BaseSession(*api: ~aiogram.client.telegram.TelegramAPIServer = TelegramAPIServer(base='https://api.telegram.org/bot{token}/{method}', file='https://api.telegram.org/file/bot{token}/{path}', is_local=False, wrap_local_file=<aiogram.client.telegram.BareFilesPathWrapper object>), json_loads: ~collections.abc.Callable[[...], ~typing.Any] = <function loads>, json_dumps: ~collections.abc.Callable[[...], str] = <function dumps>, timeout: float = 60.0*)
:   This is base class for all HTTP sessions in aiogram.

    If you want to create your own session, you must inherit from this class.

    check_response(*bot: Bot*, *method: TelegramMethod[TelegramType]*, *status_code: int*, *content: str*) → Response[TelegramType]
    :   Check response status

    *abstract async* close() → None
    :   Close client session

    *abstract async* make_request(*bot: Bot*, *method: TelegramMethod[TelegramType]*, *timeout: int | None = None*) → TelegramType
    :   Make request to Telegram Bot API

        Parameters:
        :   - **bot** – Bot instance
            - **method** – Method instance
            - **timeout** – Request timeout

        Returns:

        Raises:
        :   **TelegramApiError** –

    prepare_value(*value: Any*, *bot: Bot*, *files: dict[str, Any]*, *_dumps_json: bool = True*) → Any
    :   Prepare value before send

    *abstract async* stream_content(*url: str*, *headers: dict[str, Any] | None = None*, *timeout: int = 30*, *chunk_size: int = 65536*, *raise_for_status: bool = True*) → AsyncGenerator[bytes, None]
    :   Stream reader
