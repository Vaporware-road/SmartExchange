# TransactionPartnerChat

> Source: [https://docs.aiogram.dev/en/latest/api/types/transaction_partner_chat.html](https://docs.aiogram.dev/en/latest/api/types/transaction_partner_chat.html)

*class* aiogram.types.transaction_partner_chat.TransactionPartnerChat(*\**, *type: Literal[TransactionPartnerType.CHAT] = TransactionPartnerType.CHAT*, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *gift: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") | None = None*, *\*\*extra_data: Any*)
:   Describes a transaction with a chat.

    Source: <https://core.telegram.org/bots/api#transactionpartnerchat>

    type*: Literal[TransactionPartnerType.CHAT]*
    :   Type of the transaction partner, always ‘chat’

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Information about the chat

    gift*: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") | None*
    :   *Optional*. The gift sent to the chat by the bot
