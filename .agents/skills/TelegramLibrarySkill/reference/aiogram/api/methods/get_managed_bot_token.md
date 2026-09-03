# getManagedBotToken

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_managed_bot_token.html](https://docs.aiogram.dev/en/latest/api/methods/get_managed_bot_token.html)

Returns: `str`

*class* aiogram.methods.get_managed_bot_token.GetManagedBotToken(*\**, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to get the token of a managed bot. Returns the token as *String* on success.

    Source: <https://core.telegram.org/bots/api#getmanagedbottoken>

    user_id*: int*
    :   User identifier of the managed bot whose token will be returned

## Usage

### As bot method

```
result: str = await bot.get_managed_bot_token(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_managed_bot_token import GetManagedBotToken`
- alias: `from aiogram.methods import GetManagedBotToken`

#### With specific bot

```
result: str = await bot(GetManagedBotToken(...))
```
