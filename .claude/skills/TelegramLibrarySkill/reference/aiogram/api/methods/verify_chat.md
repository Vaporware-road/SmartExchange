# verifyChat

> Source: [https://docs.aiogram.dev/en/latest/api/methods/verify_chat.html](https://docs.aiogram.dev/en/latest/api/methods/verify_chat.html)

Returns: `bool`

*class* aiogram.methods.verify_chat.VerifyChat(*\**, *chat_id: int | str*, *custom_description: str | None = None*, *\*\*extra_data: Any*)
:   Verifies a chat [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#verifychat>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. Channel direct messages chats can’t be verified

    custom_description*: str | None*
    :   Custom description for the verification; 0-70 characters. Must be empty if the organization isn’t allowed to provide a custom verification description

## Usage

### As bot method

```
result: bool = await bot.verify_chat(...)
```

### Method as object

Imports:

- `from aiogram.methods.verify_chat import VerifyChat`
- alias: `from aiogram.methods import VerifyChat`

#### With specific bot

```
result: bool = await bot(VerifyChat(...))
```

#### As reply into Webhook in handler

```
return VerifyChat(...)
```
