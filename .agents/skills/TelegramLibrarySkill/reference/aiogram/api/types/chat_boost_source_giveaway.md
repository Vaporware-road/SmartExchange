# ChatBoostSourceGiveaway

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_giveaway.html](https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_giveaway.html)

*class* aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway(*\**, *source: Literal[ChatBoostSourceType.GIVEAWAY] = ChatBoostSourceType.GIVEAWAY*, *giveaway_message_id: int*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *prize_star_count: int | None = None*, *is_unclaimed: bool | None = None*, *\*\*extra_data: Any*)
:   The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and *prize_star_count* / 500 times for one year for Telegram Star giveaways.

    Source: <https://core.telegram.org/bots/api#chatboostsourcegiveaway>

    source*: Literal[ChatBoostSourceType.GIVEAWAY]*
    :   Source of the boost, always ‘giveaway’

    giveaway_message_id*: int*
    :   Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn’t sent yet

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. User that won the prize in the giveaway if any; for Telegram Premium giveaways only

    prize_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only

    is_unclaimed*: bool | None*
    :   *Optional*. `True`, if the giveaway was completed, but there was no user to win the prize
