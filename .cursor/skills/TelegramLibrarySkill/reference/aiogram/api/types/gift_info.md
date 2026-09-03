# GiftInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/gift_info.html](https://docs.aiogram.dev/en/latest/api/types/gift_info.html)

*class* aiogram.types.gift_info.GiftInfo(*\**, *gift: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift")*, *owned_gift_id: str | None = None*, *convert_star_count: int | None = None*, *prepaid_upgrade_star_count: int | None = None*, *is_upgrade_separate: bool | None = None*, *can_be_upgraded: bool | None = None*, *text: str | None = None*, *entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *is_private: bool | None = None*, *unique_gift_number: int | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about a regular gift that was sent or received.

    Source: <https://core.telegram.org/bots/api#giftinfo>

    gift*: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift")*
    :   Information about the gift

    owned_gift_id*: str | None*
    :   *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts

    convert_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible

    prepaid_upgrade_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that were prepaid for the ability to upgrade the gift

    is_upgrade_separate*: bool | None*
    :   *Optional*. `True`, if the gift’s upgrade was purchased after the gift was sent

    can_be_upgraded*: bool | None*
    :   *Optional*. `True`, if the gift can be upgraded to a unique gift

    text*: str | None*
    :   *Optional*. Text of the message that was added to the gift

    entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the text

    is_private*: bool | None*
    :   *Optional*. `True`, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them

    unique_gift_number*: int | None*
    :   *Optional*. Unique number reserved for this gift when upgraded. See the *number* field in [`aiogram.types.unique_gift.UniqueGift`](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")
