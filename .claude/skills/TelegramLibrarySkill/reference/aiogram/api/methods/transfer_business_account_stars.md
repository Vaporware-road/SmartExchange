# transferBusinessAccountStars

> Source: [https://docs.aiogram.dev/en/latest/api/methods/transfer_business_account_stars.html](https://docs.aiogram.dev/en/latest/api/methods/transfer_business_account_stars.html)

Returns: `bool`

*class* aiogram.methods.transfer_business_account_stars.TransferBusinessAccountStars(*\**, *business_connection_id: str*, *star_count: int*, *\*\*extra_data: Any*)
:   Transfers Telegram Stars from the business account balance to the bot’s balance. Requires the *can_transfer_stars* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#transferbusinessaccountstars>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    star_count*: int*
    :   Number of Telegram Stars to transfer; 1-10000

## Usage

### As bot method

```
result: bool = await bot.transfer_business_account_stars(...)
```

### Method as object

Imports:

- `from aiogram.methods.transfer_business_account_stars import TransferBusinessAccountStars`
- alias: `from aiogram.methods import TransferBusinessAccountStars`

#### With specific bot

```
result: bool = await bot(TransferBusinessAccountStars(...))
```

#### As reply into Webhook in handler

```
return TransferBusinessAccountStars(...)
```
