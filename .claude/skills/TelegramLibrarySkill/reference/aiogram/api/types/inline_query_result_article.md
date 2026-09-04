# InlineQueryResultArticle

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_article.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_article.html)

*class* aiogram.types.inline_query_result_article.InlineQueryResultArticle(*\**, *type: Literal[InlineQueryResultType.ARTICLE] = InlineQueryResultType.ARTICLE*, *id: str*, *title: str*, *input_message_content: [InputTextMessageContent](input_text_message_content.html#aiogram.types.input_text_message_content.InputTextMessageContent "aiogram.types.input_text_message_content.InputTextMessageContent") | [InputRichMessageContent](input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") | [InputLocationMessageContent](input_location_message_content.html#aiogram.types.input_location_message_content.InputLocationMessageContent "aiogram.types.input_location_message_content.InputLocationMessageContent") | [InputVenueMessageContent](input_venue_message_content.html#aiogram.types.input_venue_message_content.InputVenueMessageContent "aiogram.types.input_venue_message_content.InputVenueMessageContent") | [InputContactMessageContent](input_contact_message_content.html#aiogram.types.input_contact_message_content.InputContactMessageContent "aiogram.types.input_contact_message_content.InputContactMessageContent") | [InputInvoiceMessageContent](input_invoice_message_content.html#aiogram.types.input_invoice_message_content.InputInvoiceMessageContent "aiogram.types.input_invoice_message_content.InputInvoiceMessageContent")*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *url: str | None = None*, *description: str | None = None*, *thumbnail_url: str | None = None*, *thumbnail_width: int | None = None*, *thumbnail_height: int | None = None*, *hide_url: bool | None = None*, *\*\*extra_data: Any*)
:   Represents a link to an article or web page.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultarticle>

    type*: Literal[InlineQueryResultType.ARTICLE]*
    :   Type of the result, must be *article*

    id*: str*
    :   Unique identifier for this result, 1-64 Bytes

    title*: str*
    :   Title of the result

    input_message_content*: InputMessageContentUnion*
    :   Content of the message to be sent

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    url*: str | None*
    :   *Optional*. URL of the result

    description*: str | None*
    :   *Optional*. Short description of the result

    thumbnail_url*: str | None*
    :   *Optional*. Url of the thumbnail for the result

    thumbnail_width*: int | None*
    :   *Optional*. Thumbnail width

    thumbnail_height*: int | None*
    :   *Optional*. Thumbnail height

    hide_url*: bool | None*
    :   *Optional*. Pass `True` if you don’t want the URL to be shown in the message

        Deprecated since version API:8.2: <https://core.telegram.org/bots/api-changelog#january-1-2025>
