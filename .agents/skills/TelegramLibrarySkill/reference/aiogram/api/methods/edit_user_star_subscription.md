# editUserStarSubscription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_user_star_subscription.html](https://docs.aiogram.dev/en/latest/api/methods/edit_user_star_subscription.html)

Returns: `bool`

*class* aiogram.methods.edit_user_star_subscription.EditUserStarSubscription(*\**, *user_id: int*, *telegram_payment_charge_id: str*, *is_canceled: bool*, *\*\*extra_data: Any*)
:   Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#edituserstarsubscription>

    user_id*: int*
    :   Identifier of the user whose subscription will be edited

    telegram_payment_charge_id*: str*
    :   Telegram payment identifier for the subscription

    is_canceled*: bool*
    :   Pass `True` to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass `False` to allow the user to re-enable a subscription that was previously canceled by the bot

## Usage

### As bot method

```
result: bool = await bot.edit_user_star_subscription(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_user_star_subscription import EditUserStarSubscription`
- alias: `from aiogram.methods import EditUserStarSubscription`

#### With specific bot

```
result: bool = await bot(EditUserStarSubscription(...))
```

#### As reply into Webhook in handler

```
return EditUserStarSubscription(...)
```
