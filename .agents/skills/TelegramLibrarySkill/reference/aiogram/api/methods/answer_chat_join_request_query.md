# answerChatJoinRequestQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_chat_join_request_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_chat_join_request_query.html)

Returns: `bool`

*class* aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery(*\**, *chat_join_request_query_id: str*, *result: str*, *\*\*extra_data: Any*)
:   Use this method to process a received chat join request query. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#answerchatjoinrequestquery>

    chat_join_request_query_id*: str*
    :   Unique identifier of the join request query

    result*: str*
    :   Result of the query. Must be either ‘approve’ to allow the user to join the chat, ‘decline’ to disallow the user to join the chat, or ‘queue’ to leave the decision to other administrators

## Usage

### As bot method

```
result: bool = await bot.answer_chat_join_request_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_chat_join_request_query import AnswerChatJoinRequestQuery`
- alias: `from aiogram.methods import AnswerChatJoinRequestQuery`

#### With specific bot

```
result: bool = await bot(AnswerChatJoinRequestQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerChatJoinRequestQuery(...)
```

### As shortcut from received object

- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_query()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_query "aiogram.types.chat_join_request.ChatJoinRequest.answer_query")
