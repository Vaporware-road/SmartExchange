# TransactionPartnerTelegramApi

> Source: [https://docs.aiogram.dev/en/latest/api/types/transaction_partner_telegram_api.html](https://docs.aiogram.dev/en/latest/api/types/transaction_partner_telegram_api.html)

*class* aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi(*\**, *type: Literal[TransactionPartnerType.TELEGRAM_API] = TransactionPartnerType.TELEGRAM_API*, *request_count: int*, *\*\*extra_data: Any*)
:   Describes a transaction with payment for [paid broadcasting](https://core.telegram.org/bots/api#paid-broadcasts).

    Source: <https://core.telegram.org/bots/api#transactionpartnertelegramapi>

    type*: Literal[TransactionPartnerType.TELEGRAM_API]*
    :   Type of the transaction partner, always ‘telegram_api’

    request_count*: int*
    :   The number of successful requests that exceeded regular limits and were therefore billed
