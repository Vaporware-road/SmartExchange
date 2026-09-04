# UserRating

> Source: [https://docs.aiogram.dev/en/latest/api/types/user_rating.html](https://docs.aiogram.dev/en/latest/api/types/user_rating.html)

*class* aiogram.types.user_rating.UserRating(*\**, *level: int*, *rating: int*, *current_level_rating: int*, *next_level_rating: int | None = None*, *\*\*extra_data: Any*)
:   This object describes the rating of a user based on their Telegram Star spendings.

    Source: <https://core.telegram.org/bots/api#userrating>

    level*: int*
    :   Current level of the user, indicating their reliability when purchasing digital goods and services. A higher level suggests a more trustworthy customer; a negative level is likely reason for concern

    rating*: int*
    :   Numerical value of the user’s rating; the higher the rating, the better

    current_level_rating*: int*
    :   The rating value required to get the current level

    next_level_rating*: int | None*
    :   *Optional*. The rating value required to get to the next level; omitted if the maximum level was reached
