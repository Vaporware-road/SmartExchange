# getStarTransactions

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_star_transactions.html](https://docs.aiogram.dev/en/latest/api/methods/get_star_transactions.html)

Returns: `StarTransactions`

*class* aiogram.methods.get_star_transactions.GetStarTransactions(*\**, *offset: int | None = None*, *limit: int | None = None*, *\*\*extra_data: Any*)
:   Returns the bot’s Telegram Star transactions in chronological order. On success, returns a [`aiogram.types.star_transactions.StarTransactions`](../types/star_transactions.html#aiogram.types.star_transactions.StarTransactions "aiogram.types.star_transactions.StarTransactions") object.

    Source: <https://core.telegram.org/bots/api#getstartransactions>

    offset*: int | None*
    :   Number of transactions to skip in the response

    limit*: int | None*
    :   The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100

## Usage

### As bot method

```
result: StarTransactions = await bot.get_star_transactions(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_star_transactions import GetStarTransactions`
- alias: `from aiogram.methods import GetStarTransactions`

#### With specific bot

```
result: StarTransactions = await bot(GetStarTransactions(...))
```
