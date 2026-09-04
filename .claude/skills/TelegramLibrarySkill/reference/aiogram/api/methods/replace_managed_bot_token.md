# replaceManagedBotToken

> Source: [https://docs.aiogram.dev/en/latest/api/methods/replace_managed_bot_token.html](https://docs.aiogram.dev/en/latest/api/methods/replace_managed_bot_token.html)

Returns: `str`

*class* aiogram.methods.replace_managed_bot_token.ReplaceManagedBotToken(*\**, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to revoke the current token of a managed bot and generate a new one. Returns the new token as *String* on success.

    Source: <https://core.telegram.org/bots/api#replacemanagedbottoken>

    user_id*: int*
    :   User identifier of the managed bot whose token will be replaced

## Usage

### As bot method

```
result: str = await bot.replace_managed_bot_token(...)
```

### Method as object

Imports:

- `from aiogram.methods.replace_managed_bot_token import ReplaceManagedBotToken`
- alias: `from aiogram.methods import ReplaceManagedBotToken`

#### With specific bot

```
result: str = await bot(ReplaceManagedBotToken(...))
```

#### As reply into Webhook in handler

```
return ReplaceManagedBotToken(...)
```
