# createInvoiceLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/create_invoice_link.html](https://docs.aiogram.dev/en/latest/api/methods/create_invoice_link.html)

Returns: `str`

*class* aiogram.methods.create_invoice_link.CreateInvoiceLink(*\**, *title: str*, *description: str*, *payload: str*, *currency: str*, *prices: list[[LabeledPrice](../types/labeled_price.html#aiogram.types.labeled_price.LabeledPrice "aiogram.types.labeled_price.LabeledPrice")]*, *business_connection_id: str | None = None*, *provider_token: str | None = None*, *subscription_period: int | None = None*, *max_tip_amount: int | None = None*, *suggested_tip_amounts: list[int] | None = None*, *provider_data: str | None = None*, *photo_url: str | None = None*, *photo_size: int | None = None*, *photo_width: int | None = None*, *photo_height: int | None = None*, *need_name: bool | None = None*, *need_phone_number: bool | None = None*, *need_email: bool | None = None*, *need_shipping_address: bool | None = None*, *send_phone_number_to_provider: bool | None = None*, *send_email_to_provider: bool | None = None*, *is_flexible: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to create a link for an invoice. Returns the created invoice link as *String* on success.

    Source: <https://core.telegram.org/bots/api#createinvoicelink>

    title*: str*
    :   Product name, 1-32 characters

    description*: str*
    :   Product description, 1-255 characters

    payload*: str*
    :   Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes

    currency*: str*
    :   Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)

    prices*: list[[LabeledPrice](../types/labeled_price.html#aiogram.types.labeled_price.LabeledPrice "aiogram.types.labeled_price.LabeledPrice")]*
    :   Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the link will be created. For payments in [Telegram Stars](https://t.me/BotNews/90) only

    provider_token*: str | None*
    :   Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)

    subscription_period*: int | None*
    :   The number of seconds the subscription will be active for before the next payment. The currency must be set to ‘XTR’ (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 10000 Telegram Stars

    max_tip_amount*: int | None*
    :   The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)

    suggested_tip_amounts*: list[int] | None*
    :   A JSON-serialized Array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*

    provider_data*: str | None*
    :   JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider

    photo_url*: str | None*
    :   URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service

    photo_size*: int | None*
    :   Photo size in bytes

    photo_width*: int | None*
    :   Photo width

    photo_height*: int | None*
    :   Photo height

    need_name*: bool | None*
    :   Pass `True` if you require the user’s full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_phone_number*: bool | None*
    :   Pass `True` if you require the user’s phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_email*: bool | None*
    :   Pass `True` if you require the user’s email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_shipping_address*: bool | None*
    :   Pass `True` if you require the user’s shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    send_phone_number_to_provider*: bool | None*
    :   Pass `True` if the user’s phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    send_email_to_provider*: bool | None*
    :   Pass `True` if the user’s email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    is_flexible*: bool | None*
    :   Pass `True` if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

## Usage

### As bot method

```
result: str = await bot.create_invoice_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.create_invoice_link import CreateInvoiceLink`
- alias: `from aiogram.methods import CreateInvoiceLink`

#### With specific bot

```
result: str = await bot(CreateInvoiceLink(...))
```

#### As reply into Webhook in handler

```
return CreateInvoiceLink(...)
```
