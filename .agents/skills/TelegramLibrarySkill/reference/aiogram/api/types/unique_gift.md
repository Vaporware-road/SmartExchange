# UniqueGift

> Source: [https://docs.aiogram.dev/en/latest/api/types/unique_gift.html](https://docs.aiogram.dev/en/latest/api/types/unique_gift.html)

*class* aiogram.types.unique_gift.UniqueGift(*\**, *gift_id: str*, *base_name: str*, *name: str*, *number: int*, *model: [UniqueGiftModel](unique_gift_model.html#aiogram.types.unique_gift_model.UniqueGiftModel "aiogram.types.unique_gift_model.UniqueGiftModel")*, *symbol: [UniqueGiftSymbol](unique_gift_symbol.html#aiogram.types.unique_gift_symbol.UniqueGiftSymbol "aiogram.types.unique_gift_symbol.UniqueGiftSymbol")*, *backdrop: [UniqueGiftBackdrop](unique_gift_backdrop.html#aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop "aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop")*, *is_premium: bool | None = None*, *is_burned: bool | None = None*, *is_from_blockchain: bool | None = None*, *colors: [UniqueGiftColors](unique_gift_colors.html#aiogram.types.unique_gift_colors.UniqueGiftColors "aiogram.types.unique_gift_colors.UniqueGiftColors") | None = None*, *publisher_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *\*\*extra_data: Any*)
:   This object describes a unique gift that was upgraded from a regular gift.

    Source: <https://core.telegram.org/bots/api#uniquegift>

    gift_id*: str*
    :   Identifier of the regular gift from which the gift was upgraded

    base_name*: str*
    :   Human-readable name of the regular gift from which this unique gift was upgraded

    name*: str*
    :   Unique name of the gift. This name can be used in `https://t.me/nft/...` links and story areas

    number*: int*
    :   Unique number of the upgraded gift among gifts upgraded from the same regular gift

    model*: [UniqueGiftModel](unique_gift_model.html#aiogram.types.unique_gift_model.UniqueGiftModel "aiogram.types.unique_gift_model.UniqueGiftModel")*
    :   Model of the gift

    symbol*: [UniqueGiftSymbol](unique_gift_symbol.html#aiogram.types.unique_gift_symbol.UniqueGiftSymbol "aiogram.types.unique_gift_symbol.UniqueGiftSymbol")*
    :   Symbol of the gift

    backdrop*: [UniqueGiftBackdrop](unique_gift_backdrop.html#aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop "aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop")*
    :   Backdrop of the gift

    is_premium*: bool | None*
    :   *Optional*. `True`, if the original regular gift was exclusively purchaseable by Telegram Premium subscribers

    is_burned*: bool | None*
    :   *Optional*. `True`, if the gift was used to craft another gift and isn’t available anymore

    is_from_blockchain*: bool | None*
    :   *Optional*. `True`, if the gift is assigned from the TON blockchain and can’t be resold or transferred in Telegram

    colors*: [UniqueGiftColors](unique_gift_colors.html#aiogram.types.unique_gift_colors.UniqueGiftColors "aiogram.types.unique_gift_colors.UniqueGiftColors") | None*
    :   *Optional*. The color scheme that can be used by the gift’s owner for the chat’s name, replies to messages and link previews; for business account gifts and gifts that are currently on sale only

    publisher_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Information about the chat that published the gift
