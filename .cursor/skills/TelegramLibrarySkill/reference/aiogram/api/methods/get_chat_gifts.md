# getChatGifts

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat_gifts.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat_gifts.html)

Returns: `OwnedGifts`

*class* aiogram.methods.get_chat_gifts.GetChatGifts(*\**, *chat_id: int | str*, *exclude_unsaved: bool | None = None*, *exclude_saved: bool | None = None*, *exclude_unlimited: bool | None = None*, *exclude_limited_upgradable: bool | None = None*, *exclude_limited_non_upgradable: bool | None = None*, *exclude_from_blockchain: bool | None = None*, *exclude_unique: bool | None = None*, *sort_by_price: bool | None = None*, *offset: str | None = None*, *limit: int | None = None*, *\*\*extra_data: Any*)
:   Returns the gifts owned by a chat. Returns [`aiogram.types.owned_gifts.OwnedGifts`](../types/owned_gifts.html#aiogram.types.owned_gifts.OwnedGifts "aiogram.types.owned_gifts.OwnedGifts") on success.

    Source: <https://core.telegram.org/bots/api#getchatgifts>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    exclude_unsaved*: bool | None*
    :   Pass `True` to exclude gifts that aren’t saved to the chat’s profile page. Always `True`, unless the bot has the *can_post_messages* administrator right in the channel

    exclude_saved*: bool | None*
    :   Pass `True` to exclude gifts that are saved to the chat’s profile page. Always `False`, unless the bot has the *can_post_messages* administrator right in the channel

    exclude_unlimited*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased an unlimited number of times

    exclude_limited_upgradable*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased a limited number of times and can be upgraded to unique

    exclude_limited_non_upgradable*: bool | None*
    :   Pass `True` to exclude gifts that can be purchased a limited number of times and can’t be upgraded to unique

    exclude_from_blockchain*: bool | None*
    :   Pass `True` to exclude gifts that were assigned from the TON blockchain and can’t be resold or transferred in Telegram

    exclude_unique*: bool | None*
    :   Pass `True` to exclude unique gifts

    sort_by_price*: bool | None*
    :   Pass `True` to sort results by gift price instead of send date. Sorting is applied before pagination

    offset*: str | None*
    :   Offset of the first entry to return as received from the previous request; use an empty string to get the first chunk of results

    limit*: int | None*
    :   The maximum number of gifts to be returned; 1-100. Defaults to 100

## Usage

### As bot method

```
result: OwnedGifts = await bot.get_chat_gifts(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat_gifts import GetChatGifts`
- alias: `from aiogram.methods import GetChatGifts`

#### With specific bot

```
result: OwnedGifts = await bot(GetChatGifts(...))
```
