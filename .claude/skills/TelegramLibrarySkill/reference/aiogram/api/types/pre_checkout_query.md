# PreCheckoutQuery

> Source: [https://docs.aiogram.dev/en/latest/api/types/pre_checkout_query.html](https://docs.aiogram.dev/en/latest/api/types/pre_checkout_query.html)

*class* aiogram.types.pre_checkout_query.PreCheckoutQuery(*\**, *id: str*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *currency: str*, *total_amount: int*, *invoice_payload: str*, *shipping_option_id: str | None = None*, *order_info: [OrderInfo](order_info.html#aiogram.types.order_info.OrderInfo "aiogram.types.order_info.OrderInfo") | None = None*, *\*\*extra_data: Any*)
:   This object contains information about an incoming pre-checkout query.

    Source: <https://core.telegram.org/bots/api#precheckoutquery>

    id*: str*
    :   Unique query identifier

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User who sent the query

    currency*: str*
    :   Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)

    total_amount*: int*
    :   Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)

    invoice_payload*: str*
    :   Bot-specified invoice payload

    shipping_option_id*: str | None*
    :   *Optional*. Identifier of the shipping option chosen by the user

    order_info*: [OrderInfo](order_info.html#aiogram.types.order_info.OrderInfo "aiogram.types.order_info.OrderInfo") | None*
    :   *Optional*. Order information provided by the user

    answer(*ok: bool*, *error_message: str | None = None*, *\*\*kwargs: Any*) → [AnswerPreCheckoutQuery](../methods/answer_pre_checkout_query.html#aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery "aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery")
    :   Shortcut for method [`aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery`](../methods/answer_pre_checkout_query.html#aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery "aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery")
        will automatically fill method attributes:

        - `pre_checkout_query_id`

        Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an [`aiogram.types.update.Update`](update.html#aiogram.types.update.Update "aiogram.types.update.Update") with the field *pre_checkout_query*. Use this method to respond to such pre-checkout queries. On success, `True` is returned. **Note:** The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        Source: <https://core.telegram.org/bots/api#answerprecheckoutquery>

        Parameters:
        :   - **ok** – Specify `True` if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use `False` if there are any problems
            - **error_message** – Required if *ok* is `False`. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. “Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!”). Telegram will display this message to the user

        Returns:
        :   instance of method [`aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery`](../methods/answer_pre_checkout_query.html#aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery "aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery")
