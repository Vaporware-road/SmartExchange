# removeChatVerification

> Source: [https://docs.aiogram.dev/en/latest/api/methods/remove_chat_verification.html](https://docs.aiogram.dev/en/latest/api/methods/remove_chat_verification.html)

Returns: `bool`

*class* aiogram.methods.remove_chat_verification.RemoveChatVerification(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Removes verification from a chat that is currently verified [on behalf of the organization](https://telegram.org/verify#third-party-verification) represented by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#removechatverification>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot or channel in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.remove_chat_verification(...)
```

### Method as object

Imports:

- `from aiogram.methods.remove_chat_verification import RemoveChatVerification`
- alias: `from aiogram.methods import RemoveChatVerification`

#### With specific bot

```
result: bool = await bot(RemoveChatVerification(...))
```

#### As reply into Webhook in handler

```
return RemoveChatVerification(...)
```
