# removeBusinessAccountProfilePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/remove_business_account_profile_photo.html](https://docs.aiogram.dev/en/latest/api/methods/remove_business_account_profile_photo.html)

Returns: `bool`

*class* aiogram.methods.remove_business_account_profile_photo.RemoveBusinessAccountProfilePhoto(*\**, *business_connection_id: str*, *is_public: bool | None = None*, *\*\*extra_data: Any*)
:   Removes the current profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#removebusinessaccountprofilephoto>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    is_public*: bool | None*
    :   Pass `True` to remove the public photo, which is visible even if the main photo is hidden by the business account’s privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo

## Usage

### As bot method

```
result: bool = await bot.remove_business_account_profile_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.remove_business_account_profile_photo import RemoveBusinessAccountProfilePhoto`
- alias: `from aiogram.methods import RemoveBusinessAccountProfilePhoto`

#### With specific bot

```
result: bool = await bot(RemoveBusinessAccountProfilePhoto(...))
```

#### As reply into Webhook in handler

```
return RemoveBusinessAccountProfilePhoto(...)
```
