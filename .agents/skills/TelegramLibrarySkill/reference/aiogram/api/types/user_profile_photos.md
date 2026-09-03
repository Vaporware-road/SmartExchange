# UserProfilePhotos

> Source: [https://docs.aiogram.dev/en/latest/api/types/user_profile_photos.html](https://docs.aiogram.dev/en/latest/api/types/user_profile_photos.html)

*class* aiogram.types.user_profile_photos.UserProfilePhotos(*\**, *total_count: int*, *photos: list[list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]]*, *\*\*extra_data: Any*)
:   This object represent a user’s profile pictures.

    Source: <https://core.telegram.org/bots/api#userprofilephotos>

    total_count*: int*
    :   Total number of profile pictures the target user has

    photos*: list[list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]]*
    :   Requested profile pictures (in up to 4 sizes each)
