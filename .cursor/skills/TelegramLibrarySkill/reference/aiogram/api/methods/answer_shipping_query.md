# answerShippingQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_shipping_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_shipping_query.html)

Returns: `bool`

*class* aiogram.methods.answer_shipping_query.AnswerShippingQuery(*\**, *shipping_query_id: str*, *ok: bool*, *shipping_options: list[[ShippingOption](../types/shipping_option.html#aiogram.types.shipping_option.ShippingOption "aiogram.types.shipping_option.ShippingOption")] | None = None*, *error_message: str | None = None*, *\*\*extra_data: Any*)
:   If you sent an invoice requesting a shipping address and the parameter *is_flexible* was specified, the Bot API will send an [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") with a *shipping_query* field to the bot. Use this method to reply to shipping queries. On success, `True` is returned.

    Source: <https://core.telegram.org/bots/api#answershippingquery>

    shipping_query_id*: str*
    :   Unique identifier for the query to be answered

    ok*: bool*
    :   Pass `True` if delivery to the specified address is possible and `False` if there are any problems (for example, if delivery to the specified address is not possible)

    shipping_options*: list[[ShippingOption](../types/shipping_option.html#aiogram.types.shipping_option.ShippingOption "aiogram.types.shipping_option.ShippingOption")] | None*
    :   Required if *ok* is `True`. A JSON-serialized Array of available shipping options

    error_message*: str | None*
    :   Required if *ok* is `False`. Error message in human readable form that explains why it is impossible to complete the order (e.g. ‘Sorry, delivery to your desired address is unavailable’). Telegram will display this message to the user

## Usage

### As bot method

```
result: bool = await bot.answer_shipping_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_shipping_query import AnswerShippingQuery`
- alias: `from aiogram.methods import AnswerShippingQuery`

#### With specific bot

```
result: bool = await bot(AnswerShippingQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerShippingQuery(...)
```

### As shortcut from received object

- [`aiogram.types.shipping_query.ShippingQuery.answer()`](../types/shipping_query.html#aiogram.types.shipping_query.ShippingQuery.answer "aiogram.types.shipping_query.ShippingQuery.answer")
