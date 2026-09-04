# UniqueGiftInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/unique_gift_info.html](https://docs.aiogram.dev/en/latest/api/types/unique_gift_info.html)

*class* aiogram.types.unique_gift_info.UniqueGiftInfo(*\**, *gift: [UniqueGift](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")*, *origin: str*, *last_resale_currency: str | None = None*, *last_resale_amount: int | None = None*, *owned_gift_id: str | None = None*, *transfer_star_count: int | None = None*, *next_transfer_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *last_resale_star_count: int | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about a unique gift that was sent or received.

    Source: <https://core.telegram.org/bots/api#uniquegiftinfo>

    gift*: [UniqueGift](unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift")*
    :   Information about the gift

    origin*: str*
    :   Origin of the gift. Currently, either ‘upgrade’ for gifts upgraded from regular gifts, ‘transfer’ for gifts transferred from other users or channels, ‘resale’ for gifts bought from other users, ‘gifted_upgrade’ for upgrades purchased after the gift was sent, or ‘offer’ for gifts bought or sold through gift purchase offers

    last_resale_currency*: str | None*
    :   *Optional*. For gifts bought from other users, the currency in which the payment for the gift was done. Currently, one of ‘XTR’ for Telegram Stars or ‘TON’ for TON grams

    last_resale_amount*: int | None*
    :   *Optional*. For gifts bought from other users, the price paid for the gift in either Telegram Stars or nanograms

    owned_gift_id*: str | None*
    :   *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts

    transfer_star_count*: int | None*
    :   *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift

    next_transfer_date*: DateTime | None*
    :   *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now

    last_resale_star_count*: int | None*
    :   *Optional*. For gifts bought from other users, the price paid for the gift

        Deprecated since version API:9.3: <https://core.telegram.org/bots/api-changelog#december-31-2025>
