# OwnedGiftRegular

> Source: [https://docs.aiogram.dev/en/latest/api/types/owned_gift_regular.html](https://docs.aiogram.dev/en/latest/api/types/owned_gift_regular.html)

*class* aiogram.types.owned_gift_regular.OwnedGiftRegular(*\**, *type: Literal[OwnedGiftType.REGULAR] = OwnedGiftType.REGULAR*, *gift: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift")*, *send_date: int*, *owned_gift_id: str | None = None*, *sender_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *text: str | None = None*, *entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *is_private: bool | None = None*, *is_saved: bool | None = None*, *can_be_upgraded: bool | None = None*, *was_refunded: bool | None = None*, *convert_star_count: int | None = None*, *prepaid_upgrade_star_count: int | None = None*, *is_upgrade_separate: bool | None = None*, *unique_gift_number: int | None = None*, *\*\*extra_data: Any*)
:   Describes a regular gift owned by a user or a chat.

    Source: <https://core.telegram.org/bots/api#ownedgiftregular>

    type*: Literal[OwnedGiftType.REGULAR]*
    :   Type of the gift, always ‘regular’

    gift*: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift")*
    :   Information about the regular gift

    send_date*: int*
    :   Date the gift was sent in Unix time

    owned_gift_id*: str | None*
    :   *Optional*. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only

    sender_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Sender of the gift if it is a known user

    text*: str | None*
    :   *Optional*. Text of the message that was added to the gift

    entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the text

    is_private*: bool | None*
    :   *Optional*. `True`, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them

    is_saved*: bool | None*
    :   *Optional*. `True`, if the gift is displayed on the account’s profile page; for gifts received on behalf of business accounts only

    can_be_upgraded*: bool | None*
    :   *Optional*. `True`, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only

    was_refunded*: bool | None*
    :   *Optional*. `True`, if the gift was refunded and isn’t available anymore

    convert_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars; for gifts received on behalf of business accounts only

    prepaid_upgrade_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that were paid for the ability to upgrade the gift

    is_upgrade_separate*: bool | None*
    :   *Optional*. `True`, if the gift’s upgrade was purchased after the gift was sent; for gifts received on behalf of business accounts only

    unique_gift_number*: int | None*
    :   *Optional*. Unique number reserved for this gift when upgraded. See the *number* field in [`aiogram.types.unique_gift.UniqueGift`](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")
