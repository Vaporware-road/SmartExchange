# BotSubscriptionUpdated

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_subscription_updated.html](https://docs.aiogram.dev/en/latest/api/types/bot_subscription_updated.html)

*class* aiogram.types.bot_subscription_updated.BotSubscriptionUpdated(*\**, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *invoice_payload: str*, *state: str*, *\*\*extra_data: Any*)
:   This object contains information about changes to a user payment subscription toward the current bot.

    Source: <https://core.telegram.org/bots/api#botsubscriptionupdated>

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User who subscribed for payments toward the bot

    invoice_payload*: str*
    :   Bot-specified invoice payload

    state*: str*
    :   The new state of the subscription. Currently, it can be one of ‘canceled’ if the user canceled the subscription, ‘active’ if the user re-enabled a previously canceled subscription, or ‘failed’ if payment for the subscription failed
