# removeUserVerification

> Source: [https://docs.aiogram.dev/en/latest/api/methods/remove_user_verification.html](https://docs.aiogram.dev/en/latest/api/methods/remove_user_verification.html)

Returns: `bool`

*class* aiogram.methods.remove_user_verification.RemoveUserVerification(*\**, *user_id: int*, *\*\*extra_data: Any*)
:   Removes verification from a user who is currently verified [on behalf of the organization](https://telegram.org/verify#third-party-verification) represented by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#removeuserverification>

    user_id*: int*
    :   Unique identifier of the target user

## Usage

### As bot method

```
result: bool = await bot.remove_user_verification(...)
```

### Method as object

Imports:

- `from aiogram.methods.remove_user_verification import RemoveUserVerification`
- alias: `from aiogram.methods import RemoveUserVerification`

#### With specific bot

```
result: bool = await bot(RemoveUserVerification(...))
```

#### As reply into Webhook in handler

```
return RemoveUserVerification(...)
```
