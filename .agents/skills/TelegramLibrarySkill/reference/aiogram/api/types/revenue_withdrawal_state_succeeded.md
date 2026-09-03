# RevenueWithdrawalStateSucceeded

> Source: [https://docs.aiogram.dev/en/latest/api/types/revenue_withdrawal_state_succeeded.html](https://docs.aiogram.dev/en/latest/api/types/revenue_withdrawal_state_succeeded.html)

*class* aiogram.types.revenue_withdrawal_state_succeeded.RevenueWithdrawalStateSucceeded(*\**, *type: Literal[RevenueWithdrawalStateType.SUCCEEDED] = RevenueWithdrawalStateType.SUCCEEDED*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *url: str*, *\*\*extra_data: Any*)
:   The withdrawal succeeded.

    Source: <https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded>

    type*: Literal[RevenueWithdrawalStateType.SUCCEEDED]*
    :   Type of the state, always ‘succeeded’

    date*: DateTime*
    :   Date the withdrawal was completed in Unix time

    url*: str*
    :   An HTTPS URL that can be used to see transaction details
