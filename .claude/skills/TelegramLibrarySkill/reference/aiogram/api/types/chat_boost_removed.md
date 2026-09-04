# ChatBoostRemoved

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_boost_removed.html](https://docs.aiogram.dev/en/latest/api/types/chat_boost_removed.html)

*class* aiogram.types.chat_boost_removed.ChatBoostRemoved(*\**, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *boost_id: str*, *remove_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *source: [ChatBoostSourcePremium](chat_boost_source_premium.html#aiogram.types.chat_boost_source_premium.ChatBoostSourcePremium "aiogram.types.chat_boost_source_premium.ChatBoostSourcePremium") | [ChatBoostSourceGiftCode](chat_boost_source_gift_code.html#aiogram.types.chat_boost_source_gift_code.ChatBoostSourceGiftCode "aiogram.types.chat_boost_source_gift_code.ChatBoostSourceGiftCode") | [ChatBoostSourceGiveaway](chat_boost_source_giveaway.html#aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway "aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway")*, *\*\*extra_data: Any*)
:   This object represents a boost removed from a chat.

    Source: <https://core.telegram.org/bots/api#chatboostremoved>

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Chat which was boosted

    boost_id*: str*
    :   Unique identifier of the boost

    remove_date*: DateTime*
    :   Point in time (Unix timestamp) when the boost was removed

    source*: ChatBoostSourceUnion*
    :   Source of the removed boost
