# Gift

> Source: [https://docs.aiogram.dev/en/latest/api/types/gift.html](https://docs.aiogram.dev/en/latest/api/types/gift.html)

*class* aiogram.types.gift.Gift(*\**, *id: str*, *sticker: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")*, *star_count: int*, *upgrade_star_count: int | None = None*, *is_premium: bool | None = None*, *has_colors: bool | None = None*, *total_count: int | None = None*, *remaining_count: int | None = None*, *personal_total_count: int | None = None*, *personal_remaining_count: int | None = None*, *background: [GiftBackground](gift_background.html#aiogram.types.gift_background.GiftBackground "aiogram.types.gift_background.GiftBackground") | None = None*, *unique_gift_variant_count: int | None = None*, *publisher_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *\*\*extra_data: Any*)
:   This object represents a gift that can be sent by the bot.

    Source: <https://core.telegram.org/bots/api#gift>

    id*: str*
    :   Unique identifier of the gift

    sticker*: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")*
    :   The sticker that represents the gift

    star_count*: int*
    :   The number of Telegram Stars that must be paid to send the sticker

    upgrade_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars that must be paid to upgrade the gift to a unique one

    is_premium*: bool | None*
    :   *Optional*. `True`, if the gift can only be purchased by Telegram Premium subscribers

    has_colors*: bool | None*
    :   *Optional*. `True`, if the gift can be used (after being upgraded) to customize a user’s appearance

    total_count*: int | None*
    :   *Optional*. The total number of gifts of this type that can be sent by all users; for limited gifts only

    remaining_count*: int | None*
    :   *Optional*. The number of remaining gifts of this type that can be sent by all users; for limited gifts only

    personal_total_count*: int | None*
    :   *Optional*. The total number of gifts of this type that can be sent by the bot; for limited gifts only

    personal_remaining_count*: int | None*
    :   *Optional*. The number of remaining gifts of this type that can be sent by the bot; for limited gifts only

    background*: [GiftBackground](gift_background.html#aiogram.types.gift_background.GiftBackground "aiogram.types.gift_background.GiftBackground") | None*
    :   *Optional*. Background of the gift

    unique_gift_variant_count*: int | None*
    :   *Optional*. The total number of different unique gifts that can be obtained by upgrading the gift

    publisher_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Information about the chat that published the gift
