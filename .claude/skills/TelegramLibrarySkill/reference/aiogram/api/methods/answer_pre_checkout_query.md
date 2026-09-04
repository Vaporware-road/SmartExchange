# answerPreCheckoutQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_pre_checkout_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_pre_checkout_query.html)

Returns: `bool`

*class* aiogram.methods.answer_pre_checkout_query.AnswerPreCheckoutQuery(*\**, *pre_checkout_query_id: str*, *ok: bool*, *error_message: str | None = None*, *\*\*extra_data: Any*)
:   Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") with the field *pre_checkout_query*. Use this method to respond to such pre-checkout queries. On success, `True` is returned. **Note:** The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

    Source: <https://core.telegram.org/bots/api#answerprecheckoutquery>

    pre_checkout_query_id*: str*
    :   Unique identifier for the query to be answered

    ok*: bool*
    :   Specify `True` if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use `False` if there are any problems

    error_message*: str | None*
    :   Required if *ok* is `False`. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. “Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!”). Telegram will display this message to the user

## Usage

### As bot method

```
result: bool = await bot.answer_pre_checkout_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_pre_checkout_query import AnswerPreCheckoutQuery`
- alias: `from aiogram.methods import AnswerPreCheckoutQuery`

#### With specific bot

```
result: bool = await bot(AnswerPreCheckoutQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerPreCheckoutQuery(...)
```

### As shortcut from received object

- [`aiogram.types.pre_checkout_query.PreCheckoutQuery.answer()`](../types/pre_checkout_query.html#aiogram.types.pre_checkout_query.PreCheckoutQuery.answer "aiogram.types.pre_checkout_query.PreCheckoutQuery.answer")
