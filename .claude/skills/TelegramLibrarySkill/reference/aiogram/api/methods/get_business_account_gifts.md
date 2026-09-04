# getBusinessAccountGifts

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_business_account_gifts.html](https://docs.aiogram.dev/en/latest/api/methods/get_business_account_gifts.html)

Returns: `OwnedGifts`

*class* aiogram.methods.get_business_account_gifts.GetBusinessAccountGifts(*\**, *business_connection_id: str*, *exclude_unsaved: bool | None = None*, *exclude_saved: bool | None = None*, *exclude_unlimited: bool | None = None*, *exclude_limited_upgradable: bool | None = None*, *exclude_limited_non_upgradable: bool | None = None*, *exclude_unique: bool | None = None*, *exclude_from_blockchain: bool | None = None*, *sort_by_price: bool | None = None*, *offset: str | None = None*, *limit: int | None = None*, *exclude_limited: bool | None = None*, *\*\*extra_data: Any*)
:   Returns the gifts received and owned by a managed business account. Requires the *can_view_gifts_and_stars* business bot right. Returns [`aiogram.types.owned_gifts.OwnedGifts`](../types/owned_gifts.html#aiogram.types.owned_gifts.OwnedGifts "aiogram.types.owned_gifts.OwnedGifts") on success.

    Source: <https://core.telegram.org/bots/api#getbusinessaccountgifts>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    exclude_unsaved*: bool | None*
    :   Pass `True` to exclude gifts that aren’t saved to the account’s profile page

    exclude_saved*: bool | None*
    :   Pass `True` to exclude gifts that are saved to the account’s profile page

    exclude_unlimited*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased an unlimited number of times

    exclude_limited_upgradable*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased a limited number of times and can be upgraded to unique

    exclude_limited_non_upgradable*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased a limited number of times and can’t be upgraded to unique

    exclude_unique*: bool | None*
    :   Pass `True` to exclude unique gifts

    exclude_from_blockchain*: bool | None*
    :   Pass `True` to exclude gifts that were assigned from the TON blockchain and can’t be resold or transferred in Telegram

    sort_by_price*: bool | None*
    :   Pass `True` to sort results by gift price instead of send date. Sorting is applied before pagination

    offset*: str | None*
    :   Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

    limit*: int | None*
    :   The maximum number of gifts to be returned; 1-100. Defaults to 100

    exclude_limited*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased a limited number of times

        Deprecated since version API:9.3: <https://core.telegram.org/bots/api-changelog#december-31-2025>

## Usage

### As bot method

```
result: OwnedGifts = await bot.get_business_account_gifts(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_business_account_gifts import GetBusinessAccountGifts`
- alias: `from aiogram.methods import GetBusinessAccountGifts`

#### With specific bot

```
result: OwnedGifts = await bot(GetBusinessAccountGifts(...))
```
