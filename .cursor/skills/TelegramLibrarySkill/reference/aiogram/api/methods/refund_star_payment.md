# refundStarPayment

> Source: [https://docs.aiogram.dev/en/latest/api/methods/refund_star_payment.html](https://docs.aiogram.dev/en/latest/api/methods/refund_star_payment.html)

Returns: `bool`

*class* aiogram.methods.refund_star_payment.RefundStarPayment(*\**, *user_id: int*, *telegram_payment_charge_id: str*, *\*\*extra_data: Any*)
:   Refunds a successful payment in [Telegram Stars](https://t.me/BotNews/90). Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#refundstarpayment>

    user_id*: int*
    :   Identifier of the user whose payment will be refunded

    telegram_payment_charge_id*: str*
    :   Telegram payment identifier

## Usage

### As bot method

```
result: bool = await bot.refund_star_payment(...)
```

### Method as object

Imports:

- `from aiogram.methods.refund_star_payment import RefundStarPayment`
- alias: `from aiogram.methods import RefundStarPayment`

#### With specific bot

```
result: bool = await bot(RefundStarPayment(...))
```

#### As reply into Webhook in handler

```
return RefundStarPayment(...)
```
