# verifyUser

> Source: [https://docs.aiogram.dev/en/latest/api/methods/verify_user.html](https://docs.aiogram.dev/en/latest/api/methods/verify_user.html)

Returns: `bool`

*class* aiogram.methods.verify_user.VerifyUser(*\**, *user_id: int*, *custom_description: str | None = None*, *\*\*extra_data: Any*)
:   Verifies a user [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#verifyuser>

    user_id*: int*
    :   Unique identifier of the target user

    custom_description*: str | None*
    :   Custom description for the verification; 0-70 characters. Must be empty if the organization isn’t allowed to provide a custom verification description

## Usage

### As bot method

```
result: bool = await bot.verify_user(...)
```

### Method as object

Imports:

- `from aiogram.methods.verify_user import VerifyUser`
- alias: `from aiogram.methods import VerifyUser`

#### With specific bot

```
result: bool = await bot(VerifyUser(...))
```

#### As reply into Webhook in handler

```
return VerifyUser(...)
```
