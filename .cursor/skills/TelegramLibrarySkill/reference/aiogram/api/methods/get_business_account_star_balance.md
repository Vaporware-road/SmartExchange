# getBusinessAccountStarBalance

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_business_account_star_balance.html](https://docs.aiogram.dev/en/latest/api/methods/get_business_account_star_balance.html)

Returns: `StarAmount`

*class* aiogram.methods.get_business_account_star_balance.GetBusinessAccountStarBalance(*\**, *business_connection_id: str*, *\*\*extra_data: Any*)
:   Returns the amount of Telegram Stars owned by a managed business account. Requires the *can_view_gifts_and_stars* business bot right. Returns [`aiogram.types.star_amount.StarAmount`](../types/star_amount.html#aiogram.types.star_amount.StarAmount "aiogram.types.star_amount.StarAmount") on success.

    Source: <https://core.telegram.org/bots/api#getbusinessaccountstarbalance>

    business_connection_id*: str*
    :   Unique identifier of the business connection

## Usage

### As bot method

```
result: StarAmount = await bot.get_business_account_star_balance(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_business_account_star_balance import GetBusinessAccountStarBalance`
- alias: `from aiogram.methods import GetBusinessAccountStarBalance`

#### With specific bot

```
result: StarAmount = await bot(GetBusinessAccountStarBalance(...))
```
