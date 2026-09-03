# ShippingQuery

> Source: [https://docs.aiogram.dev/en/latest/api/types/shipping_query.html](https://docs.aiogram.dev/en/latest/api/types/shipping_query.html)

*class* aiogram.types.shipping_query.ShippingQuery(*\**, *id: str*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *invoice_payload: str*, *shipping_address: [ShippingAddress](shipping_address.html#aiogram.types.shipping_address.ShippingAddress "aiogram.types.shipping_address.ShippingAddress")*, *\*\*extra_data: Any*)
:   This object contains information about an incoming shipping query.

    Source: <https://core.telegram.org/bots/api#shippingquery>

    id*: str*
    :   Unique query identifier

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User who sent the query

    invoice_payload*: str*
    :   Bot-specified invoice payload

    shipping_address*: [ShippingAddress](shipping_address.html#aiogram.types.shipping_address.ShippingAddress "aiogram.types.shipping_address.ShippingAddress")*
    :   User specified shipping address

    answer(*ok: bool*, *shipping_options: list[[ShippingOption](shipping_option.html#aiogram.types.shipping_option.ShippingOption "aiogram.types.shipping_option.ShippingOption")] | None = None*, *error_message: str | None = None*, *\*\*kwargs: Any*) → [AnswerShippingQuery](../methods/answer_shipping_query.html#aiogram.methods.answer_shipping_query.AnswerShippingQuery "aiogram.methods.answer_shipping_query.AnswerShippingQuery")
    :   Shortcut for method [`aiogram.methods.answer_shipping_query.AnswerShippingQuery`](../methods/answer_shipping_query.html#aiogram.methods.answer_shipping_query.AnswerShippingQuery "aiogram.methods.answer_shipping_query.AnswerShippingQuery")
        will automatically fill method attributes:

        - `shipping_query_id`

        If you sent an invoice requesting a shipping address and the parameter *is_flexible* was specified, the Bot API will send an [`aiogram.types.update.Update`](update.html#aiogram.types.update.Update "aiogram.types.update.Update") with a *shipping_query* field to the bot. Use this method to reply to shipping queries. On success, `True` is returned.

        Source: <https://core.telegram.org/bots/api#answershippingquery>

        Parameters:
        :   - **ok** – Pass `True` if delivery to the specified address is possible and `False` if there are any problems (for example, if delivery to the specified address is not possible)
            - **shipping_options** – Required if *ok* is `True`. A JSON-serialized Array of available shipping options
            - **error_message** – Required if *ok* is `False`. Error message in human readable form that explains why it is impossible to complete the order (e.g. ‘Sorry, delivery to your desired address is unavailable’). Telegram will display this message to the user

        Returns:
        :   instance of method [`aiogram.methods.answer_shipping_query.AnswerShippingQuery`](../methods/answer_shipping_query.html#aiogram.methods.answer_shipping_query.AnswerShippingQuery "aiogram.methods.answer_shipping_query.AnswerShippingQuery")
