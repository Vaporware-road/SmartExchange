# TransactionPartnerFragment

> Source: [https://docs.aiogram.dev/en/latest/api/types/transaction_partner_fragment.html](https://docs.aiogram.dev/en/latest/api/types/transaction_partner_fragment.html)

*class* aiogram.types.transaction_partner_fragment.TransactionPartnerFragment(*\**, *type: Literal[TransactionPartnerType.FRAGMENT] = TransactionPartnerType.FRAGMENT*, *withdrawal_state: Annotated[[RevenueWithdrawalStatePending](revenue_withdrawal_state_pending.html#aiogram.types.revenue_withdrawal_state_pending.RevenueWithdrawalStatePending "aiogram.types.revenue_withdrawal_state_pending.RevenueWithdrawalStatePending") | [RevenueWithdrawalStateSucceeded](revenue_withdrawal_state_succeeded.html#aiogram.types.revenue_withdrawal_state_succeeded.RevenueWithdrawalStateSucceeded "aiogram.types.revenue_withdrawal_state_succeeded.RevenueWithdrawalStateSucceeded") | [RevenueWithdrawalStateFailed](revenue_withdrawal_state_failed.html#aiogram.types.revenue_withdrawal_state_failed.RevenueWithdrawalStateFailed "aiogram.types.revenue_withdrawal_state_failed.RevenueWithdrawalStateFailed"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *\*\*extra_data: Any*)
:   Describes a withdrawal transaction with Fragment.

    Source: <https://core.telegram.org/bots/api#transactionpartnerfragment>

    type*: Literal[TransactionPartnerType.FRAGMENT]*
    :   Type of the transaction partner, always ‘fragment’

    withdrawal_state*: RevenueWithdrawalStateUnion | None*
    :   *Optional*. State of the transaction if the transaction is outgoing
