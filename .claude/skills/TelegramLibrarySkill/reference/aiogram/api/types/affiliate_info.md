# AffiliateInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/affiliate_info.html](https://docs.aiogram.dev/en/latest/api/types/affiliate_info.html)

*class* aiogram.types.affiliate_info.AffiliateInfo(*\**, *commission_per_mille: int*, *amount: int*, *affiliate_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *affiliate_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *nanostar_amount: int | None = None*, *\*\*extra_data: Any*)
:   Contains information about the affiliate that received a commission via this transaction.

    Source: <https://core.telegram.org/bots/api#affiliateinfo>

    commission_per_mille*: int*
    :   The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users

    amount*: int*
    :   Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds

    affiliate_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. The bot or the user that received an affiliate commission if it was received by a bot or a user

    affiliate_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. The chat that received an affiliate commission if it was received by a chat

    nanostar_amount*: int | None*
    :   *Optional*. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds
