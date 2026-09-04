# setBusinessAccountUsername

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_business_account_username.html](https://docs.aiogram.dev/en/latest/api/methods/set_business_account_username.html)

Returns: `bool`

*class* aiogram.methods.set_business_account_username.SetBusinessAccountUsername(*\**, *business_connection_id: str*, *username: str | None = None*, *\*\*extra_data: Any*)
:   Changes the username of a managed business account. Requires the *can_change_username* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setbusinessaccountusername>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    username*: str | None*
    :   The new value of the username for the business account; 0-32 characters

## Usage

### As bot method

```
result: bool = await bot.set_business_account_username(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_business_account_username import SetBusinessAccountUsername`
- alias: `from aiogram.methods import SetBusinessAccountUsername`

#### With specific bot

```
result: bool = await bot(SetBusinessAccountUsername(...))
```

#### As reply into Webhook in handler

```
return SetBusinessAccountUsername(...)
```
