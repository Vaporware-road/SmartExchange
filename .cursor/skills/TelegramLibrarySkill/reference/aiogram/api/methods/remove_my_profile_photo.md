# removeMyProfilePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/remove_my_profile_photo.html](https://docs.aiogram.dev/en/latest/api/methods/remove_my_profile_photo.html)

Returns: `bool`

*class* aiogram.methods.remove_my_profile_photo.RemoveMyProfilePhoto(*\*\*extra_data: Any*)
:   Removes the profile photo of the bot. Requires no parameters. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#removemyprofilephoto>

## Usage

### As bot method

```
result: bool = await bot.remove_my_profile_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.remove_my_profile_photo import RemoveMyProfilePhoto`
- alias: `from aiogram.methods import RemoveMyProfilePhoto`

#### With specific bot

```
result: bool = await bot(RemoveMyProfilePhoto(...))
```

#### As reply into Webhook in handler

```
return RemoveMyProfilePhoto(...)
```
