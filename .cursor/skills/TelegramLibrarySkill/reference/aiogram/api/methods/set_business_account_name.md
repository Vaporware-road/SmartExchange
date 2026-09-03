# setBusinessAccountName

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_business_account_name.html](https://docs.aiogram.dev/en/latest/api/methods/set_business_account_name.html)

Returns: `bool`

*class* aiogram.methods.set_business_account_name.SetBusinessAccountName(*\**, *business_connection_id: str*, *first_name: str*, *last_name: str | None = None*, *\*\*extra_data: Any*)
:   Changes the first and last name of a managed business account. Requires the *can_change_name* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setbusinessaccountname>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    first_name*: str*
    :   The new value of the first name for the business account; 1-64 characters

    last_name*: str | None*
    :   The new value of the last name for the business account; 0-64 characters

## Usage

### As bot method

```
result: bool = await bot.set_business_account_name(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_business_account_name import SetBusinessAccountName`
- alias: `from aiogram.methods import SetBusinessAccountName`

#### With specific bot

```
result: bool = await bot(SetBusinessAccountName(...))
```

#### As reply into Webhook in handler

```
return SetBusinessAccountName(...)
```
