# GiveawayCompleted

> Source: [https://docs.aiogram.dev/en/latest/api/types/giveaway_completed.html](https://docs.aiogram.dev/en/latest/api/types/giveaway_completed.html)

*class* aiogram.types.giveaway_completed.GiveawayCompleted(*\**, *winner_count: int*, *unclaimed_prize_count: int | None = None*, *giveaway_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *is_star_giveaway: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a service message about the completion of a giveaway without public winners.

    Source: <https://core.telegram.org/bots/api#giveawaycompleted>

    winner_count*: int*
    :   Number of winners in the giveaway

    unclaimed_prize_count*: int | None*
    :   *Optional*. Number of undistributed prizes

    giveaway_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message with the giveaway that was completed, if it wasn’t deleted

    is_star_giveaway*: bool | None*
    :   *Optional*. `True`, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway
