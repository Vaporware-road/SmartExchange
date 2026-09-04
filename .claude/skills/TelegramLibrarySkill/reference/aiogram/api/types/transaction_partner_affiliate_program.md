# TransactionPartnerAffiliateProgram

> Source: [https://docs.aiogram.dev/en/latest/api/types/transaction_partner_affiliate_program.html](https://docs.aiogram.dev/en/latest/api/types/transaction_partner_affiliate_program.html)

*class* aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram(*\**, *type: Literal[TransactionPartnerType.AFFILIATE_PROGRAM] = TransactionPartnerType.AFFILIATE_PROGRAM*, *commission_per_mille: int*, *sponsor_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *\*\*extra_data: Any*)
:   Describes the affiliate program that issued the affiliate commission received via this transaction.

    Source: <https://core.telegram.org/bots/api#transactionpartneraffiliateprogram>

    type*: Literal[TransactionPartnerType.AFFILIATE_PROGRAM]*
    :   Type of the transaction partner, always ‘affiliate_program’

    commission_per_mille*: int*
    :   The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users

    sponsor_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Information about the bot that sponsored the affiliate program
