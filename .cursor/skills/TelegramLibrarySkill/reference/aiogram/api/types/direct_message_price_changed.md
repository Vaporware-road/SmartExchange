# DirectMessagePriceChanged

> Source: [https://docs.aiogram.dev/en/latest/api/types/direct_message_price_changed.html](https://docs.aiogram.dev/en/latest/api/types/direct_message_price_changed.html)

*class* aiogram.types.direct_message_price_changed.DirectMessagePriceChanged(*\**, *are_direct_messages_enabled: bool*, *direct_message_star_count: int | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about a change in the price of direct messages sent to a channel chat.

    Source: <https://core.telegram.org/bots/api#directmessagepricechanged>

    are_direct_messages_enabled*: bool*
    :   `True`, if direct messages are enabled for the channel chat; `False` otherwise

    direct_message_star_count*: int | None*
    :   *Optional*. The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0
