# StarTransaction

> Source: [https://docs.aiogram.dev/en/latest/api/types/star_transaction.html](https://docs.aiogram.dev/en/latest/api/types/star_transaction.html)

*class* aiogram.types.star_transaction.StarTransaction(*\**, *id: str*, *amount: int*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *nanostar_amount: int | None = None*, *source: Annotated[[TransactionPartnerUser](transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser") | [TransactionPartnerChat](transaction_partner_chat.html#aiogram.types.transaction_partner_chat.TransactionPartnerChat "aiogram.types.transaction_partner_chat.TransactionPartnerChat") | [TransactionPartnerAffiliateProgram](transaction_partner_affiliate_program.html#aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram "aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram") | [TransactionPartnerFragment](transaction_partner_fragment.html#aiogram.types.transaction_partner_fragment.TransactionPartnerFragment "aiogram.types.transaction_partner_fragment.TransactionPartnerFragment") | [TransactionPartnerTelegramAds](transaction_partner_telegram_ads.html#aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds "aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds") | [TransactionPartnerTelegramApi](transaction_partner_telegram_api.html#aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi "aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi") | [TransactionPartnerOther](transaction_partner_other.html#aiogram.types.transaction_partner_other.TransactionPartnerOther "aiogram.types.transaction_partner_other.TransactionPartnerOther"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *receiver: Annotated[[TransactionPartnerUser](transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser") | [TransactionPartnerChat](transaction_partner_chat.html#aiogram.types.transaction_partner_chat.TransactionPartnerChat "aiogram.types.transaction_partner_chat.TransactionPartnerChat") | [TransactionPartnerAffiliateProgram](transaction_partner_affiliate_program.html#aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram "aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram") | [TransactionPartnerFragment](transaction_partner_fragment.html#aiogram.types.transaction_partner_fragment.TransactionPartnerFragment "aiogram.types.transaction_partner_fragment.TransactionPartnerFragment") | [TransactionPartnerTelegramAds](transaction_partner_telegram_ads.html#aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds "aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds") | [TransactionPartnerTelegramApi](transaction_partner_telegram_api.html#aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi "aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi") | [TransactionPartnerOther](transaction_partner_other.html#aiogram.types.transaction_partner_other.TransactionPartnerOther "aiogram.types.transaction_partner_other.TransactionPartnerOther"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *\*\*extra_data: Any*)
:   Describes a Telegram Star transaction. Note that if the buyer initiates a chargeback with the payment provider from whom they acquired Stars (e.g., Apple, Google) following this transaction, the refunded Stars will be deducted from the bot’s balance. This is outside of Telegram’s control.

    Source: <https://core.telegram.org/bots/api#startransaction>

    id*: str*
    :   Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with *SuccessfulPayment.telegram_payment_charge_id* for successful incoming payments from users

    amount*: int*
    :   Integer amount of Telegram Stars transferred by the transaction

    date*: DateTime*
    :   Date the transaction was created in Unix time

    nanostar_amount*: int | None*
    :   *Optional*. The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999

    source*: TransactionPartnerUnion | None*
    :   *Optional*. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions

    receiver*: TransactionPartnerUnion | None*
    :   *Optional*. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions
