# ChatBoostSourceGiftCode

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_gift_code.html](https://docs.aiogram.dev/en/latest/api/types/chat_boost_source_gift_code.html)

*class* aiogram.types.chat_boost_source_gift_code.ChatBoostSourceGiftCode(*\**, *source: Literal[ChatBoostSourceType.GIFT_CODE] = ChatBoostSourceType.GIFT_CODE*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

    Source: <https://core.telegram.org/bots/api#chatboostsourcegiftcode>

    source*: Literal[ChatBoostSourceType.GIFT_CODE]*
    :   Source of the boost, always ‘gift_code’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User for which the gift code was created
