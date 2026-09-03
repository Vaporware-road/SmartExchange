# sendInvoice

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_invoice.html](https://docs.aiogram.dev/en/latest/api/methods/send_invoice.html)

Returns: `Message`

*class* aiogram.methods.send_invoice.SendInvoice(*\*, chat_id: int | str, title: str, description: str, payload: str, currency: str, prices: list[~aiogram.types.labeled_price.LabeledPrice], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: ~aiogram.types.suggested_post_parameters.SuggestedPostParameters | None = None, reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None, reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*extra_data: ~typing.Any*)
:   Use this method to send invoices. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendinvoice>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

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

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    direct_messages_topic_id*: int | None*
    :   Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat

    provider_token*: str | None*
    :   Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)

    max_tip_amount*: int | None*
    :   The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)

    suggested_tip_amounts*: list[int] | None*
    :   A JSON-serialized Array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*

    start_parameter*: str | None*
    :   Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter

    provider_data*: str | None*
    :   JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider

    photo_url*: str | None*
    :   URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for

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

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    suggested_post_parameters*: [SuggestedPostParameters](../types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None*
    :   A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Pay `total price`’ button will be shown. If not empty, the first button must be a Pay button

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_invoice(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_invoice import SendInvoice`
- alias: `from aiogram.methods import SendInvoice`

#### With specific bot

```
result: Message = await bot(SendInvoice(...))
```

#### As reply into Webhook in handler

```
return SendInvoice(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_invoice()`](../types/message.html#aiogram.types.message.Message.answer_invoice "aiogram.types.message.Message.answer_invoice")
- [`aiogram.types.message.Message.reply_invoice()`](../types/message.html#aiogram.types.message.Message.reply_invoice "aiogram.types.message.Message.reply_invoice")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice "aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_invoice()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_invoice "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_invoice")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_invoice()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_invoice "aiogram.types.inaccessible_message.InaccessibleMessage.answer_invoice")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_invoice()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_invoice "aiogram.types.inaccessible_message.InaccessibleMessage.reply_invoice")
