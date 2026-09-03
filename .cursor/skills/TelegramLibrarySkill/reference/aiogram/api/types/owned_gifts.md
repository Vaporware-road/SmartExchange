# OwnedGifts

> Source: [https://docs.aiogram.dev/en/latest/api/types/owned_gifts.html](https://docs.aiogram.dev/en/latest/api/types/owned_gifts.html)

*class* aiogram.types.owned_gifts.OwnedGifts(*\**, *total_count: int*, *gifts: list[Annotated[[OwnedGiftRegular](owned_gift_regular.html#aiogram.types.owned_gift_regular.OwnedGiftRegular "aiogram.types.owned_gift_regular.OwnedGiftRegular") | [OwnedGiftUnique](owned_gift_unique.html#aiogram.types.owned_gift_unique.OwnedGiftUnique "aiogram.types.owned_gift_unique.OwnedGiftUnique"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]]*, *next_offset: str | None = None*, *\*\*extra_data: Any*)
:   Contains the list of gifts received and owned by a user or a chat.

    Source: <https://core.telegram.org/bots/api#ownedgifts>

    total_count*: int*
    :   The total number of gifts owned by the user or the chat

    gifts*: list[OwnedGiftUnion]*
    :   The list of gifts

    next_offset*: str | None*
    :   *Optional*. Offset for the next request. If empty, then there are no more results
