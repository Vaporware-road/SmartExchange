# ChatBoost

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_boost.html](https://docs.aiogram.dev/en/latest/api/types/chat_boost.html)

*class* aiogram.types.chat_boost.ChatBoost(*\**, *boost_id: str*, *add_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *expiration_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *source: [ChatBoostSourcePremium](chat_boost_source_premium.html#aiogram.types.chat_boost_source_premium.ChatBoostSourcePremium "aiogram.types.chat_boost_source_premium.ChatBoostSourcePremium") | [ChatBoostSourceGiftCode](chat_boost_source_gift_code.html#aiogram.types.chat_boost_source_gift_code.ChatBoostSourceGiftCode "aiogram.types.chat_boost_source_gift_code.ChatBoostSourceGiftCode") | [ChatBoostSourceGiveaway](chat_boost_source_giveaway.html#aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway "aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway")*, *\*\*extra_data: Any*)
:   This object contains information about a chat boost.

    Source: <https://core.telegram.org/bots/api#chatboost>

    boost_id*: str*
    :   Unique identifier of the boost

    add_date*: DateTime*
    :   Point in time (Unix timestamp) when the chat was boosted

    expiration_date*: DateTime*
    :   Point in time (Unix timestamp) when the boost will automatically expire, unless the booster’s Telegram Premium subscription is prolonged

    source*: ChatBoostSourceUnion*
    :   Source of the added boost
