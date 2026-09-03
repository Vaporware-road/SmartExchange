# RefundedPayment

> Source: [https://docs.aiogram.dev/en/latest/api/types/refunded_payment.html](https://docs.aiogram.dev/en/latest/api/types/refunded_payment.html)

*class* aiogram.types.refunded_payment.RefundedPayment(*\**, *currency: Literal['XTR'] = 'XTR'*, *total_amount: int*, *invoice_payload: str*, *telegram_payment_charge_id: str*, *provider_payment_charge_id: str | None = None*, *\*\*extra_data: Any*)
:   This object contains basic information about a refunded payment.

    Source: <https://core.telegram.org/bots/api#refundedpayment>

    currency*: Literal['XTR']*
    :   Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90). Currently, always ‘XTR’

    total_amount*: int*
    :   Total refunded price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45`, `total_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)

    invoice_payload*: str*
    :   Bot-specified invoice payload

    telegram_payment_charge_id*: str*
    :   Telegram payment identifier

    provider_payment_charge_id*: str | None*
    :   *Optional*. Provider payment identifier
