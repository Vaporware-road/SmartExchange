# setBusinessAccountProfilePhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_business_account_profile_photo.html](https://docs.aiogram.dev/en/latest/api/methods/set_business_account_profile_photo.html)

Returns: `bool`

*class* aiogram.methods.set_business_account_profile_photo.SetBusinessAccountProfilePhoto(*\**, *business_connection_id: str*, *photo: [InputProfilePhotoStatic](../types/input_profile_photo_static.html#aiogram.types.input_profile_photo_static.InputProfilePhotoStatic "aiogram.types.input_profile_photo_static.InputProfilePhotoStatic") | [InputProfilePhotoAnimated](../types/input_profile_photo_animated.html#aiogram.types.input_profile_photo_animated.InputProfilePhotoAnimated "aiogram.types.input_profile_photo_animated.InputProfilePhotoAnimated")*, *is_public: bool | None = None*, *\*\*extra_data: Any*)
:   Changes the profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setbusinessaccountprofilephoto>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    photo*: InputProfilePhotoUnion*
    :   The new profile photo to set

    is_public*: bool | None*
    :   Pass `True` to set the public photo, which will be visible even if the main photo is hidden by the business account’s privacy settings. An account can have only one public photo

## Usage

### As bot method

```
result: bool = await bot.set_business_account_profile_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_business_account_profile_photo import SetBusinessAccountProfilePhoto`
- alias: `from aiogram.methods import SetBusinessAccountProfilePhoto`

#### With specific bot

```
result: bool = await bot(SetBusinessAccountProfilePhoto(...))
```

#### As reply into Webhook in handler

```
return SetBusinessAccountProfilePhoto(...)
```
