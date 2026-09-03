# ChatBoostSourcePremium

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_premium.html](https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_premium.html)

*class* aiogram.types.chat_boost_source_premium.ChatBoostSourcePremium(*\**, *source: Literal[ChatBoostSourceType.PREMIUM] = ChatBoostSourceType.PREMIUM*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

    Source: <https://core.telegram.org/bots/api#chatboostsourcepremium>

    source*: Literal[ChatBoostSourceType.PREMIUM]*
    :   Source of the boost, always ‘premium’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User that boosted the chat
