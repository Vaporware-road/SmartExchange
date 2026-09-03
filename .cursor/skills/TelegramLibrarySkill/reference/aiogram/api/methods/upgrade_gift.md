# upgradeGift

> Source: [https://docs.aiogram.dev/en/latest/api/methods/upgrade_gift.html](https://docs.aiogram.dev/en/latest/api/methods/upgrade_gift.html)

Returns: `bool`

*class* aiogram.methods.upgrade_gift.UpgradeGift(*\**, *business_connection_id: str*, *owned_gift_id: str*, *keep_original_details: bool | None = None*, *star_count: int | None = None*, *\*\*extra_data: Any*)
:   Upgrades a given regular gift to a unique gift. Requires the *can_transfer_and_upgrade_gifts* business bot right. Additionally requires the *can_transfer_stars* business bot right if the upgrade is paid. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#upgradegift>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    owned_gift_id*: str*
    :   Unique identifier of the regular gift that should be upgraded to a unique one

    keep_original_details*: bool | None*
    :   Pass `True` to keep the original gift text, sender and receiver in the upgraded gift

    star_count*: int | None*
    :   The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If `gift.prepaid_upgrade_star_count > 0`, then pass 0, otherwise, the *can_transfer_stars* business bot right is required and `gift.upgrade_star_count` must be passed

## Usage

### As bot method

```
result: bool = await bot.upgrade_gift(...)
```

### Method as object

Imports:

- `from aiogram.methods.upgrade_gift import UpgradeGift`
- alias: `from aiogram.methods import UpgradeGift`

#### With specific bot

```
result: bool = await bot(UpgradeGift(...))
```

#### As reply into Webhook in handler

```
return UpgradeGift(...)
```
