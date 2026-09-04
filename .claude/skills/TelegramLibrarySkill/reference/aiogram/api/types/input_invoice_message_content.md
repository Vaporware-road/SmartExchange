# InputInvoiceMessageContent

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_invoice_message_content.html](https://docs.aiogram.dev/en/latest/api/types/input_invoice_message_content.html)

*class* aiogram.types.input_invoice_message_content.InputInvoiceMessageContent(*\**, *title: str*, *description: str*, *payload: str*, *currency: str*, *prices: list[[LabeledPrice](labeled_price.html#aiogram.types.labeled_price.LabeledPrice "aiogram.types.labeled_price.LabeledPrice")]*, *provider_token: str | None = None*, *max_tip_amount: int | None = None*, *suggested_tip_amounts: list[int] | None = None*, *provider_data: str | None = None*, *photo_url: str | None = None*, *photo_size: int | None = None*, *photo_width: int | None = None*, *photo_height: int | None = None*, *need_name: bool | None = None*, *need_phone_number: bool | None = None*, *need_email: bool | None = None*, *need_shipping_address: bool | None = None*, *send_phone_number_to_provider: bool | None = None*, *send_email_to_provider: bool | None = None*, *is_flexible: bool | None = None*, *\*\*extra_data: Any*)
:   Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of an invoice message to be sent as the result of an inline query.

    Source: <https://core.telegram.org/bots/api#inputinvoicemessagecontent>

    title*: str*
    :   Product name, 1-32 characters

    description*: str*
    :   Product description, 1-255 characters

    payload*: str*
    :   Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes

    currency*: str*
    :   Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)

    prices*: list[[LabeledPrice](labeled_price.html#aiogram.types.labeled_price.LabeledPrice "aiogram.types.labeled_price.LabeledPrice")]*
    :   Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)

    provider_token*: str | None*
    :   *Optional*. Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)

    max_tip_amount*: int | None*
    :   *Optional*. The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)

    suggested_tip_amounts*: list[int] | None*
    :   *Optional*. A JSON-serialized Array of suggested amounts of tip in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*

    provider_data*: str | None*
    :   *Optional*. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider

    photo_url*: str | None*
    :   *Optional*. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service

    photo_size*: int | None*
    :   *Optional*. Photo size in bytes

    photo_width*: int | None*
    :   *Optional*. Photo width

    photo_height*: int | None*
    :   *Optional*. Photo height

    need_name*: bool | None*
    :   *Optional*. Pass `True` if you require the user’s full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_phone_number*: bool | None*
    :   *Optional*. Pass `True` if you require the user’s phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_email*: bool | None*
    :   *Optional*. Pass `True` if you require the user’s email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    need_shipping_address*: bool | None*
    :   *Optional*. Pass `True` if you require the user’s shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    send_phone_number_to_provider*: bool | None*
    :   *Optional*. Pass `True` if the user’s phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    send_email_to_provider*: bool | None*
    :   *Optional*. Pass `True` if the user’s email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)

    is_flexible*: bool | None*
    :   *Optional*. Pass `True` if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
