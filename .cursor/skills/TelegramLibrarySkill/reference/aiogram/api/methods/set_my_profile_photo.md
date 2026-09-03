# setMyProfilePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_profile_photo.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_profile_photo.html)

Returns: `bool`

*class* aiogram.methods.set_my_profile_photo.SetMyProfilePhoto(*\**, *photo: [InputProfilePhotoStatic](../types/input_profile_photo_static.html#aiogram.types.input_profile_photo_static.InputProfilePhotoStatic "aiogram.types.input_profile_photo_static.InputProfilePhotoStatic") | [InputProfilePhotoAnimated](../types/input_profile_photo_animated.html#aiogram.types.input_profile_photo_animated.InputProfilePhotoAnimated "aiogram.types.input_profile_photo_animated.InputProfilePhotoAnimated")*, *\*\*extra_data: Any*)
:   Changes the profile photo of the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmyprofilephoto>

    photo*: InputProfilePhotoUnion*
    :   The new profile photo to set

## Usage

### As bot method

```
result: bool = await bot.set_my_profile_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_profile_photo import SetMyProfilePhoto`
- alias: `from aiogram.methods import SetMyProfilePhoto`

#### With specific bot

```
result: bool = await bot(SetMyProfilePhoto(...))
```

#### As reply into Webhook in handler

```
return SetMyProfilePhoto(...)
```
