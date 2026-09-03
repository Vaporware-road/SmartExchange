# transferGift

> Source: [https://docs.aiogram.dev/en/latest/api/methods/transfer_gift.html](https://docs.aiogram.dev/en/latest/api/methods/transfer_gift.html)

Returns: `bool`

*class* aiogram.methods.transfer_gift.TransferGift(*\**, *business_connection_id: str*, *owned_gift_id: str*, *new_owner_chat_id: int*, *star_count: int | None = None*, *\*\*extra_data: Any*)
:   Transfers an owned unique gift to another user. Requires the *can_transfer_and_upgrade_gifts* business bot right. Requires *can_transfer_stars* business bot right if the transfer is paid. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#transfergift>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    owned_gift_id*: str*
    :   Unique identifier of the regular gift that should be transferred

    new_owner_chat_id*: int*
    :   Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours

    star_count*: int | None*
    :   The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the *can_transfer_stars* business bot right is required

## Usage

### As bot method

```
result: bool = await bot.transfer_gift(...)
```

### Method as object

Imports:

- `from aiogram.methods.transfer_gift import TransferGift`
- alias: `from aiogram.methods import TransferGift`

#### With specific bot

```
result: bool = await bot(TransferGift(...))
```

#### As reply into Webhook in handler

```
return TransferGift(...)
```
