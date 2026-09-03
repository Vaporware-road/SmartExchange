# getUserProfilePhotos

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_user_profile_photos.html](https://docs.aiogram.dev/en/latest/api/methods/get_user_profile_photos.html)

Returns: `UserProfilePhotos`

*class* aiogram.methods.get_user_profile_photos.GetUserProfilePhotos(*\**, *user_id: int*, *offset: int | None = None*, *limit: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to get a list of profile pictures for a user. Returns a [`aiogram.types.user_profile_photos.UserProfilePhotos`](../types/user_profile_photos.html#aiogram.types.user_profile_photos.UserProfilePhotos "aiogram.types.user_profile_photos.UserProfilePhotos") object.

    Source: <https://core.telegram.org/bots/api#getuserprofilephotos>

    user_id*: int*
    :   Unique identifier of the target user

    offset*: int | None*
    :   Sequential number of the first photo to be returned. By default, all photos are returned

    limit*: int | None*
    :   Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100

## Usage

### As bot method

```
result: UserProfilePhotos = await bot.get_user_profile_photos(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_user_profile_photos import GetUserProfilePhotos`
- alias: `from aiogram.methods import GetUserProfilePhotos`

#### With specific bot

```
result: UserProfilePhotos = await bot(GetUserProfilePhotos(...))
```

### As shortcut from received object

- [`aiogram.types.user.User.get_profile_photos()`](../types/user.html#aiogram.types.user.User.get_profile_photos "aiogram.types.user.User.get_profile_photos")
