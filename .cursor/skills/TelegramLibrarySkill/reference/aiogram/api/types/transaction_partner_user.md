# TransactionPartnerUser

> Source: [https://docs.aiogram.dev/en/latest/api/types/transaction_partner_user.html](https://docs.aiogram.dev/en/latest/api/types/transaction_partner_user.html)

*class* aiogram.types.transaction_partner_user.TransactionPartnerUser(*\**, *type: Literal[TransactionPartnerType.USER] = TransactionPartnerType.USER*, *transaction_type: str*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *affiliate: [AffiliateInfo](affiliate_info.html#aiogram.types.affiliate_info.AffiliateInfo "aiogram.types.affiliate_info.AffiliateInfo") | None = None*, *invoice_payload: str | None = None*, *subscription_period: int | None = None*, *paid_media: list[Annotated[[PaidMediaLivePhoto](paid_media_live_photo.html#aiogram.types.paid_media_live_photo.PaidMediaLivePhoto "aiogram.types.paid_media_live_photo.PaidMediaLivePhoto") | [PaidMediaPhoto](paid_media_photo.html#aiogram.types.paid_media_photo.PaidMediaPhoto "aiogram.types.paid_media_photo.PaidMediaPhoto") | [PaidMediaPreview](paid_media_preview.html#aiogram.types.paid_media_preview.PaidMediaPreview "aiogram.types.paid_media_preview.PaidMediaPreview") | [PaidMediaVideo](paid_media_video.html#aiogram.types.paid_media_video.PaidMediaVideo "aiogram.types.paid_media_video.PaidMediaVideo"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]] | None = None*, *paid_media_payload: str | None = None*, *gift: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") | None = None*, *premium_subscription_duration: int | None = None*, *\*\*extra_data: Any*)
:   Describes a transaction with a user.

    Source: <https://core.telegram.org/bots/api#transactionpartneruser>

    type*: Literal[TransactionPartnerType.USER]*
    :   Type of the transaction partner, always ‘user’

    transaction_type*: str*
    :   Type of the transaction, currently one of ‘invoice_payment’ for payments via invoices, ‘paid_media_payment’ for payments for paid media, ‘gift_purchase’ for gifts sent by the bot, ‘premium_purchase’ for Telegram Premium subscriptions gifted by the bot, ‘business_account_transfer’ for direct transfers from managed business accounts

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user

    affiliate*: [AffiliateInfo](affiliate_info.html#aiogram.types.affiliate_info.AffiliateInfo "aiogram.types.affiliate_info.AffiliateInfo") | None*
    :   *Optional*. Information about the affiliate that received a commission via this transaction. Can be available only for ‘invoice_payment’ and ‘paid_media_payment’ transactions

    invoice_payload*: str | None*
    :   *Optional*. Bot-specified invoice payload. Can be available only for ‘invoice_payment’ transactions

    subscription_period*: int | None*
    :   *Optional*. The duration of the paid subscription. Can be available only for ‘invoice_payment’ transactions

    paid_media*: list[PaidMediaUnion] | None*
    :   *Optional*. Information about the paid media bought by the user; for ‘paid_media_payment’ transactions only

    paid_media_payload*: str | None*
    :   *Optional*. Bot-specified paid media payload. Can be available only for ‘paid_media_payment’ transactions

    gift*: [Gift](gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") | None*
    :   *Optional*. The gift sent to the user by the bot; for ‘gift_purchase’ transactions only

    premium_subscription_duration*: int | None*
    :   *Optional*. Number of months the gifted Telegram Premium subscription will be active for; for ‘premium_purchase’ transactions only
