# giftPremiumSubscription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/gift_premium_subscription.html](https://docs.aiogram.dev/en/latest/api/methods/gift_premium_subscription.html)

Returns: `bool`

*class* aiogram.methods.gift_premium_subscription.GiftPremiumSubscription(*\**, *user_id: int*, *month_count: int*, *star_count: int*, *text: str | None = None*, *text_parse_mode: str | None = None*, *text_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Gifts a Telegram Premium subscription to the given user. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#giftpremiumsubscription>

    user_id*: int*
    :   Unique identifier of the target user who will receive a Telegram Premium subscription

    month_count*: int*
    :   Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12

    star_count*: int*
    :   Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months

    text*: str | None*
    :   Text that will be shown along with the service message about the subscription; 0-128 characters

    text_parse_mode*: str | None*
    :   Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Entities other than ‘bold’, ‘italic’, ‘underline’, ‘strikethrough’, ‘spoiler’, ‘custom_emoji’, and ‘date_time’ are ignored

    text_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than ‘bold’, ‘italic’, ‘underline’, ‘strikethrough’, ‘spoiler’, ‘custom_emoji’, and ‘date_time’ are ignored

## Usage

### As bot method

```
result: bool = await bot.gift_premium_subscription(...)
```

### Method as object

Imports:

- `from aiogram.methods.gift_premium_subscription import GiftPremiumSubscription`
- alias: `from aiogram.methods import GiftPremiumSubscription`

#### With specific bot

```
result: bool = await bot(GiftPremiumSubscription(...))
```

#### As reply into Webhook in handler

```
return GiftPremiumSubscription(...)
```
