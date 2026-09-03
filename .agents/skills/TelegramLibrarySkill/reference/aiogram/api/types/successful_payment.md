# SuccessfulPayment

> Source: [https://docs.aiogram.dev/en/latest/api/types/successful_payment.html](https://docs.aiogram.dev/en/latest/api/types/successful_payment.html)

*class* aiogram.types.successful_payment.SuccessfulPayment(*\**, *currency: str*, *total_amount: int*, *invoice_payload: str*, *telegram_payment_charge_id: str*, *provider_payment_charge_id: str*, *subscription_expiration_date: int | None = None*, *is_recurring: bool | None = None*, *is_first_recurring: bool | None = None*, *shipping_option_id: str | None = None*, *order_info: [OrderInfo](order_info.html#aiogram.types.order_info.OrderInfo "aiogram.types.order_info.OrderInfo") | None = None*, *\*\*extra_data: Any*)
:   This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram’s control.

    Source: <https://core.telegram.org/bots/api#successfulpayment>

    currency*: str*
    :   Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)

    total_amount*: int*
    :   Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)

    invoice_payload*: str*
    :   Bot-specified invoice payload

    telegram_payment_charge_id*: str*
    :   Telegram payment identifier

    provider_payment_charge_id*: str*
    :   Provider payment identifier

    subscription_expiration_date*: int | None*
    :   *Optional*. Expiration date of the subscription, in Unix time; for recurring payments only

    is_recurring*: bool | None*
    :   *Optional*. `True`, if the payment is a recurring payment for a subscription

    is_first_recurring*: bool | None*
    :   *Optional*. `True`, if the payment is the first payment for a subscription

    shipping_option_id*: str | None*
    :   *Optional*. Identifier of the shipping option chosen by the user

    order_info*: [OrderInfo](order_info.html#aiogram.types.order_info.OrderInfo "aiogram.types.order_info.OrderInfo") | None*
    :   *Optional*. Order information provided by the user
