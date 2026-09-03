# declineChatJoinRequest

> Source: [https://docs.aiogram.dev/en/latest/api/methods/decline_chat_join_request.html](https://docs.aiogram.dev/en/latest/api/methods/decline_chat_join_request.html)

Returns: `bool`

*class* aiogram.methods.decline_chat_join_request.DeclineChatJoinRequest(*\**, *chat_id: int | str*, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the *can_invite_users* administrator right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#declinechatjoinrequest>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

## Usage

### As bot method

```
result: bool = await bot.decline_chat_join_request(...)
```

### Method as object

Imports:

- `from aiogram.methods.decline_chat_join_request import DeclineChatJoinRequest`
- alias: `from aiogram.methods import DeclineChatJoinRequest`

#### With specific bot

```
result: bool = await bot(DeclineChatJoinRequest(...))
```

#### As reply into Webhook in handler

```
return DeclineChatJoinRequest(...)
```

### As shortcut from received object

- [`aiogram.types.chat_join_request.ChatJoinRequest.decline()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.decline "aiogram.types.chat_join_request.ChatJoinRequest.decline")
