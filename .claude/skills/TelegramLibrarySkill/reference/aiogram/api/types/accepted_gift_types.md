# AcceptedGiftTypes

> Source: [https://docs.aiogram.dev/en/latest/api/types/accepted_gift_types.html](https://docs.aiogram.dev/en/latest/api/types/accepted_gift_types.html)

*class* aiogram.types.accepted_gift_types.AcceptedGiftTypes(*\**, *unlimited_gifts: bool*, *limited_gifts: bool*, *unique_gifts: bool*, *premium_subscription: bool*, *gifts_from_channels: bool*, *\*\*extra_data: Any*)
:   This object describes the types of gifts that can be gifted to a user or a chat.

    Source: <https://core.telegram.org/bots/api#acceptedgifttypes>

    unlimited_gifts*: bool*
    :   `True`, if unlimited regular gifts are accepted

    limited_gifts*: bool*
    :   `True`, if limited regular gifts are accepted

    unique_gifts*: bool*
    :   `True`, if unique gifts or gifts that can be upgraded to unique for free are accepted

    premium_subscription*: bool*
    :   `True`, if a Telegram Premium subscription is accepted

    gifts_from_channels*: bool*
    :   `True`, if transfers of unique gifts from channels are accepted
