# StarAmount

> Source: [https://docs.aiogram.dev/en/latest/api/types/star_amount.html](https://docs.aiogram.dev/en/latest/api/types/star_amount.html)

*class* aiogram.types.star_amount.StarAmount(*\**, *amount: int*, *nanostar_amount: int | None = None*, *\*\*extra_data: Any*)
:   Describes an amount of Telegram Stars.

    Source: <https://core.telegram.org/bots/api#staramount>

    amount*: int*
    :   Integer amount of Telegram Stars, rounded to 0; can be negative

    nanostar_amount*: int | None*
    :   *Optional*. The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if *amount* is non-positive
