# Invoice

> Source: [https://docs.aiogram.dev/en/latest/api/types/invoice.html](https://docs.aiogram.dev/en/latest/api/types/invoice.html)

*class* aiogram.types.invoice.Invoice(*\**, *title: str*, *description: str*, *start_parameter: str*, *currency: str*, *total_amount: int*, *\*\*extra_data: Any*)
:   This object contains basic information about an invoice.

    Source: <https://core.telegram.org/bots/api#invoice>

    title*: str*
    :   Product name

    description*: str*
    :   Product description

    start_parameter*: str*
    :   Unique bot deep-linking parameter that can be used to generate this invoice

    currency*: str*
    :   Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)

    total_amount*: int*
    :   Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)
