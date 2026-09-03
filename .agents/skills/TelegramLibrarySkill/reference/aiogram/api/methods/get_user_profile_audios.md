# getUserProfileAudios

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_user_profile_audios.html](https://docs.aiogram.dev/en/latest/api/methods/get_user_profile_audios.html)

Returns: `UserProfileAudios`

*class* aiogram.methods.get_user_profile_audios.GetUserProfileAudios(*\**, *user_id: int*, *offset: int | None = None*, *limit: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to get a list of profile audios for a user. Returns a [`aiogram.types.user_profile_audios.UserProfileAudios`](../types/user_profile_audios.html#aiogram.types.user_profile_audios.UserProfileAudios "aiogram.types.user_profile_audios.UserProfileAudios") object.

    Source: <https://core.telegram.org/bots/api#getuserprofileaudios>

    user_id*: int*
    :   Unique identifier of the target user

    offset*: int | None*
    :   Sequential number of the first audio to be returned. By default, all audios are returned

    limit*: int | None*
    :   Limits the number of audios to be retrieved. Values between 1-100 are accepted. Defaults to 100

## Usage

### As bot method

```
result: UserProfileAudios = await bot.get_user_profile_audios(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_user_profile_audios import GetUserProfileAudios`
- alias: `from aiogram.methods import GetUserProfileAudios`

#### With specific bot

```
result: UserProfileAudios = await bot(GetUserProfileAudios(...))
```

### As shortcut from received object

- [`aiogram.types.user.User.get_profile_audios()`](../types/user.html#aiogram.types.user.User.get_profile_audios "aiogram.types.user.User.get_profile_audios")
