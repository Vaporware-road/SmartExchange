# OwnedGiftUnique

> Source: [https://docs.aiogram.dev/en/latest/api/types/owned_gift_unique.html](https://docs.aiogram.dev/en/latest/api/types/owned_gift_unique.html)

*class* aiogram.types.owned_gift_unique.OwnedGiftUnique(*\**, *type: Literal[OwnedGiftType.UNIQUE] = OwnedGiftType.UNIQUE*, *gift: [UniqueGift](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")*, *send_date: int*, *owned_gift_id: str | None = None*, *sender_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *is_saved: bool | None = None*, *can_be_transferred: bool | None = None*, *transfer_star_count: int | None = None*, *next_transfer_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *\*\*extra_data: Any*)
:   Describes a unique gift received and owned by a user or a chat.

    Source: <https://core.telegram.org/bots/api#ownedgiftunique>

    type*: Literal[OwnedGiftType.UNIQUE]*
    :   Type of the gift, always ‘unique’

    gift*: [UniqueGift](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")*
    :   Information about the unique gift

    send_date*: int*
    :   Date the gift was sent in Unix time

    owned_gift_id*: str | None*
    :   *Optional*. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only

    sender_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Sender of the gift if it is a known user

    is_saved*: bool | None*
    :   *Optional*. `True`, if the gift is displayed on the account’s profile page; for gifts received on behalf of business accounts only

    can_be_transferred*: bool | None*
    :   *Optional*. `True`, if the gift can be transferred to another owner; for gifts received on behalf of business accounts only

    transfer_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift

    next_transfer_date*: DateTime | None*
    :   *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now
