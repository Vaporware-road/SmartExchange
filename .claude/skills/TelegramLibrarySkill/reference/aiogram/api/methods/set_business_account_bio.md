# setBusinessAccountBio

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_business_account_bio.html](https://docs.aiogram.dev/en/latest/api/methods/set_business_account_bio.html)

Returns: `bool`

*class* aiogram.methods.set_business_account_bio.SetBusinessAccountBio(*\**, *business_connection_id: str*, *bio: str | None = None*, *\*\*extra_data: Any*)
:   Changes the bio of a managed business account. Requires the *can_change_bio* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setbusinessaccountbio>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    bio*: str | None*
    :   The new value of the bio for the business account; 0-140 characters

## Usage

### As bot method

```
result: bool = await bot.set_business_account_bio(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_business_account_bio import SetBusinessAccountBio`
- alias: `from aiogram.methods import SetBusinessAccountBio`

#### With specific bot

```
result: bool = await bot(SetBusinessAccountBio(...))
```

#### As reply into Webhook in handler

```
return SetBusinessAccountBio(...)
```
