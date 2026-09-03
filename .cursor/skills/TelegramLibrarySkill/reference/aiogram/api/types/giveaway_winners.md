# GiveawayWinners

> Source: [https://docs.aiogram.dev/en/latest/api/types/giveaway_winners.html](https://docs.aiogram.dev/en/latest/api/types/giveaway_winners.html)

*class* aiogram.types.giveaway_winners.GiveawayWinners(*\**, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *giveaway_message_id: int*, *winners_selection_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *winner_count: int*, *winners: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")]*, *additional_chat_count: int | None = None*, *prize_star_count: int | None = None*, *premium_subscription_month_count: int | None = None*, *unclaimed_prize_count: int | None = None*, *only_new_members: bool | None = None*, *was_refunded: bool | None = None*, *prize_description: str | None = None*, *\*\*extra_data: Any*)
:   This object represents a message about the completion of a giveaway with public winners.

    Source: <https://core.telegram.org/bots/api#giveawaywinners>

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   The chat that created the giveaway

    giveaway_message_id*: int*
    :   Identifier of the message with the giveaway in the chat

    winners_selection_date*: DateTime*
    :   Point in time (Unix timestamp) when winners of the giveaway were selected

    winner_count*: int*
    :   Total number of winners in the giveaway

    winners*: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")]*
    :   List of up to 100 winners of the giveaway

    additional_chat_count*: int | None*
    :   *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway

    prize_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only

    premium_subscription_month_count*: int | None*
    :   *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only

    unclaimed_prize_count*: int | None*
    :   *Optional*. Number of undistributed prizes

    only_new_members*: bool | None*
    :   *Optional*. `True`, if only users who had joined the chats after the giveaway started were eligible to win

    was_refunded*: bool | None*
    :   *Optional*. `True`, if the giveaway was canceled because the payment for it was refunded

    prize_description*: str | None*
    :   *Optional*. Description of additional giveaway prize
