# Giveaway

> Source: [https://docs.aiogram.dev/en/latest/api/types/giveaway.html](https://docs.aiogram.dev/en/latest/api/types/giveaway.html)

*class* aiogram.types.giveaway.Giveaway(*\**, *chats: list[[Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")]*, *winners_selection_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *winner_count: int*, *only_new_members: bool | None = None*, *has_public_winners: bool | None = None*, *prize_description: str | None = None*, *country_codes: list[str] | None = None*, *prize_star_count: int | None = None*, *premium_subscription_month_count: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a message about a scheduled giveaway.

    Source: <https://core.telegram.org/bots/api#giveaway>

    chats*: list[[Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")]*
    :   The list of chats which the user must join to participate in the giveaway

    winners_selection_date*: DateTime*
    :   Point in time (Unix timestamp) when winners of the giveaway will be selected

    winner_count*: int*
    :   The number of users which are supposed to be selected as winners of the giveaway

    only_new_members*: bool | None*
    :   *Optional*. `True`, if only users who join the chats after the giveaway started should be eligible to win

    has_public_winners*: bool | None*
    :   *Optional*. `True`, if the list of giveaway winners will be visible to everyone

    prize_description*: str | None*
    :   *Optional*. Description of additional giveaway prize

    country_codes*: list[str] | None*
    :   *Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways

    prize_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only

    premium_subscription_month_count*: int | None*
    :   *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only
