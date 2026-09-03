# WebApp

> Source: [https://docs.aiogram.dev/en/latest/utils/web_app.html](https://docs.aiogram.dev/en/latest/utils/web_app.html)

Telegram Bot API 6.0 announces a revolution in the development of chatbots using WebApp feature.

You can read more details on it in the official [blog](https://telegram.org/blog/notifications-bots#bot-revolution)
and [documentation](https://core.telegram.org/bots/webapps).

aiogram implements simple utils to remove headache with the data validation from Telegram WebApp on the backend side.

## Usage

For example from frontend you will pass `application/x-www-form-urlencoded` POST request
with `_auth` field in body and wants to return User info inside response as `application/json`

```
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

async def check_data_handler(request: Request):
    bot: Bot = request.app["bot"]

    data = await request.post()  # application/x-www-form-urlencoded
    try:
        data = safe_parse_webapp_init_data(token=bot.token, init_data=data["_auth"])
    except ValueError:
        return json_response({"ok": False, "err": "Unauthorized"}, status=401)
    return json_response({"ok": True, "data": data.user.dict()})
```

## Functions

aiogram.utils.web_app.check_webapp_signature(*token: str*, *init_data: str*) → bool
:   Check incoming WebApp init data signature

    Source: <https://core.telegram.org/bots/webapps#validating-data-received-via-the-web-app>

    Parameters:
    :   - **token** – bot Token
        - **init_data** – data from frontend to be validated

    Returns:

aiogram.utils.web_app.parse_webapp_init_data(*init_data: str, \*, loads: ~collections.abc.Callable[[...], ~typing.Any] = <function loads>*) → [WebAppInitData](#aiogram.utils.web_app.WebAppInitData "aiogram.utils.web_app.WebAppInitData")
:   Parse WebApp init data and return it as WebAppInitData object

    This method doesn’t make any security check, so you shall not trust to this data,
    use `safe_parse_webapp_init_data` instead.

    Parameters:
    :   - **init_data** – data from frontend to be parsed
        - **loads**

    Returns:

aiogram.utils.web_app.safe_parse_webapp_init_data(*token: str, init_data: str, \*, loads: ~collections.abc.Callable[[...], ~typing.Any] = <function loads>*) → [WebAppInitData](#aiogram.utils.web_app.WebAppInitData "aiogram.utils.web_app.WebAppInitData")
:   Validate raw WebApp init data and return it as WebAppInitData object

    Raise `ValueError` when data is invalid

    Parameters:
    :   - **token** – bot token
        - **init_data** – data from frontend to be parsed and validated
        - **loads**

    Returns:

## Types

*class* aiogram.utils.web_app.WebAppInitData(*\*\*extra_data: Any*)
:   This object contains data that is transferred to the Web App when it is opened.
    It is empty if the Web App was launched from a keyboard button.

    Source: <https://core.telegram.org/bots/webapps#webappinitdata>

    query_id*: str | None*
    :   A unique identifier for the Web App session, required for sending messages
        via the answerWebAppQuery method.

    user*: [WebAppUser](#aiogram.utils.web_app.WebAppUser "aiogram.utils.web_app.WebAppUser") | None*
    :   An object containing data about the current user.

    receiver*: [WebAppUser](#aiogram.utils.web_app.WebAppUser "aiogram.utils.web_app.WebAppUser") | None*
    :   An object containing data about the chat partner of the current user in the chat where
        the bot was launched via the attachment menu.
        Returned only for Web Apps launched via the attachment menu.

    chat*: [WebAppChat](#aiogram.utils.web_app.WebAppChat "aiogram.utils.web_app.WebAppChat") | None*
    :   An object containing data about the chat where the bot was launched via the attachment menu.
        Returned for supergroups, channels, and group chats – only for Web Apps launched via the
        attachment menu.

    chat_type*: str | None*
    :   Type of the chat from which the Web App was opened.
        Can be either “sender” for a private chat with the user opening the link,
        “private”, “group”, “supergroup”, or “channel”.
        Returned only for Web Apps launched from direct links.

    chat_instance*: str | None*
    :   Global identifier, uniquely corresponding to the chat from which the Web App was opened.
        Returned only for Web Apps launched from a direct link.

    start_param*: str | None*
    :   The value of the startattach parameter, passed via link.
        Only returned for Web Apps when launched from the attachment menu via link.
        The value of the start_param parameter will also be passed in the GET-parameter
        tgWebAppStartParam, so the Web App can load the correct interface right away.

    can_send_after*: int | None*
    :   Time in seconds, after which a message can be sent via the answerWebAppQuery method.

    auth_date*: datetime*
    :   Unix time when the form was opened.

    hash*: str*
    :   A hash of all passed parameters, which the bot server can use to check their validity.

*class* aiogram.utils.web_app.WebAppUser(*\*\*extra_data: Any*)
:   This object contains the data of the Web App user.

    Source: <https://core.telegram.org/bots/webapps#webappuser>

    id*: int*
    :   A unique identifier for the user or bot. This number may have more than 32 significant bits
        and some programming languages may have difficulty/silent defects in interpreting it.
        It has at most 52 significant bits, so a 64-bit integer or a double-precision float type
        is safe for storing this identifier.

    is_bot*: bool | None*
    :   True, if this user is a bot. Returns in the receiver field only.

    first_name*: str*
    :   First name of the user or bot.

    last_name*: str | None*
    :   Last name of the user or bot.

    username*: str | None*
    :   Username of the user or bot.

    language_code*: str | None*
    :   IETF language tag of the user’s language. Returns in user field only.

    is_premium*: bool | None*
    :   True, if this user is a Telegram Premium user.

    added_to_attachment_menu*: bool | None*
    :   True, if this user added the bot to the attachment menu.

    allows_write_to_pm*: bool | None*
    :   True, if this user allowed the bot to message them.

    photo_url*: str | None*
    :   URL of the user’s profile photo. The photo can be in .jpeg or .svg formats.
        Only returned for Web Apps launched from the attachment menu.

*class* aiogram.utils.web_app.WebAppChat(*\*\*extra_data: Any*)
:   This object represents a chat.

    Source: <https://core.telegram.org/bots/webapps#webappchat>

    id*: int*
    :   Unique identifier for this chat. This number may have more than 32 significant bits
        and some programming languages may have difficulty/silent defects in interpreting it.
        But it has at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier.

    type*: str*
    :   Type of chat, can be either “group”, “supergroup” or “channel”

    title*: str*
    :   Title of the chat

    username*: str | None*
    :   Username of the chat

    photo_url*: str | None*
    :   URL of the chat’s photo. The photo can be in .jpeg or .svg formats.
        Only returned for Web Apps launched from the attachment menu.
