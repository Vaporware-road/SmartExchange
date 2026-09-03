# getUserPersonalChatMessages

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_user_personal_chat_messages.html](https://docs.aiogram.dev/en/latest/api/methods/get_user_personal_chat_messages.html)

Returns: `list[Message]`

*class* aiogram.methods.get_user_personal_chat_messages.GetUserPersonalChatMessages(*\**, *user_id: int*, *limit: int*, *\*\*extra_data: Any*)
:   Use this method to get the last messages from the personal chat (i.e., the chat currently added to their profile) of a given user. On success, an Array of [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") objects is returned.

    Source: <https://core.telegram.org/bots/api#getuserpersonalchatmessages>

    user_id*: int*
    :   Unique identifier for the target user

    limit*: int*
    :   The maximum number of messages to return; 1-20

## Usage

### As bot method

```
result: list[Message] = await bot.get_user_personal_chat_messages(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_user_personal_chat_messages import GetUserPersonalChatMessages`
- alias: `from aiogram.methods import GetUserPersonalChatMessages`

#### With specific bot

```
result: list[Message] = await bot(GetUserPersonalChatMessages(...))
```
