# getMyStarBalance

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_star_balance.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_star_balance.html)

Returns: `StarAmount`

*class* aiogram.methods.get_my_star_balance.GetMyStarBalance(*\*\*extra_data: Any*)
:   A method to get the current Telegram Stars balance of the bot. Requires no parameters. On success, returns a [`aiogram.types.star_amount.StarAmount`](../types/star_amount.html#aiogram.types.star_amount.StarAmount "aiogram.types.star_amount.StarAmount") object.

    Source: <https://core.telegram.org/bots/api#getmystarbalance>

## Usage

### As bot method

```
result: StarAmount = await bot.get_my_star_balance(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_star_balance import GetMyStarBalance`
- alias: `from aiogram.methods import GetMyStarBalance`

#### With specific bot

```
result: StarAmount = await bot(GetMyStarBalance(...))
```
