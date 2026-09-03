# UniqueGiftModel

> Source: [https://docs.aiogram.dev/en/latest/api/types/unique_gift_model.html](https://docs.aiogram.dev/en/latest/api/types/unique_gift_model.html)

*class* aiogram.types.unique_gift_model.UniqueGiftModel(*\**, *name: str*, *sticker: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")*, *rarity_per_mille: int*, *rarity: str | None = None*, *\*\*extra_data: Any*)
:   This object describes the model of a unique gift.

    Source: <https://core.telegram.org/bots/api#uniquegiftmodel>

    name*: str*
    :   Name of the model

    sticker*: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker")*
    :   The sticker that represents the unique gift

    rarity_per_mille*: int*
    :   The number of unique gifts that receive this model for every 1000 gift upgrades. Always 0 for crafted gifts

    rarity*: str | None*
    :   *Optional*. Rarity of the model if it is a crafted model. Currently, can be ‘uncommon’, ‘rare’, ‘epic’, or ‘legendary’
