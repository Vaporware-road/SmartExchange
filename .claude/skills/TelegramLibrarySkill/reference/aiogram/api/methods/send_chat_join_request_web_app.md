# sendChatJoinRequestWebApp

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_chat_join_request_web_app.html](https://docs.aiogram.dev/en/latest/api/methods/send_chat_join_request_web_app.html)

Returns: `bool`

*class* aiogram.methods.send_chat_join_request_web_app.SendChatJoinRequestWebApp(*\**, *chat_join_request_query_id: str*, *web_app_url: str*, *\*\*extra_data: Any*)
:   Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome. Call [`aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery`](answer_chat_join_request_query.html#aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery "aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery") to resolve the join request query based on the user interaction with the Mini App. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#sendchatjoinrequestwebapp>

    chat_join_request_query_id*: str*
    :   Unique identifier of the join request query

    web_app_url*: str*
    :   An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-mini-apps)

## Usage

### As bot method

```
result: bool = await bot.send_chat_join_request_web_app(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_chat_join_request_web_app import SendChatJoinRequestWebApp`
- alias: `from aiogram.methods import SendChatJoinRequestWebApp`

#### With specific bot

```
result: bool = await bot(SendChatJoinRequestWebApp(...))
```

#### As reply into Webhook in handler

```
return SendChatJoinRequestWebApp(...)
```

### As shortcut from received object

- [`aiogram.types.chat_join_request.ChatJoinRequest.send_webapp()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.send_webapp "aiogram.types.chat_join_request.ChatJoinRequest.send_webapp")
