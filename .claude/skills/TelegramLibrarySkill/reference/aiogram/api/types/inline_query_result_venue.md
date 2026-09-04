# InlineQueryResultVenue

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_venue.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_venue.html)

*class* aiogram.types.inline_query_result_venue.InlineQueryResultVenue(*\**, *type: Literal[InlineQueryResultType.VENUE] = InlineQueryResultType.VENUE*, *id: str*, *latitude: float*, *longitude: float*, *title: str*, *address: str*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *input_message_content: [InputTextMessageContent](input_text_message_content.html#aiogram.types.input_text_message_content.InputTextMessageContent "aiogram.types.input_text_message_content.InputTextMessageContent") | [InputRichMessageContent](input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") | [InputLocationMessageContent](input_location_message_content.html#aiogram.types.input_location_message_content.InputLocationMessageContent "aiogram.types.input_location_message_content.InputLocationMessageContent") | [InputVenueMessageContent](input_venue_message_content.html#aiogram.types.input_venue_message_content.InputVenueMessageContent "aiogram.types.input_venue_message_content.InputVenueMessageContent") | [InputContactMessageContent](input_contact_message_content.html#aiogram.types.input_contact_message_content.InputContactMessageContent "aiogram.types.input_contact_message_content.InputContactMessageContent") | [InputInvoiceMessageContent](input_invoice_message_content.html#aiogram.types.input_invoice_message_content.InputInvoiceMessageContent "aiogram.types.input_invoice_message_content.InputInvoiceMessageContent") | None = None*, *thumbnail_url: str | None = None*, *thumbnail_width: int | None = None*, *thumbnail_height: int | None = None*, *\*\*extra_data: Any*)
:   Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the venue.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultvenue>

    type*: Literal[InlineQueryResultType.VENUE]*
    :   Type of the result, must be *venue*

    id*: str*
    :   Unique identifier for this result, 1-64 Bytes

    latitude*: float*
    :   Latitude of the venue location in degrees

    longitude*: float*
    :   Longitude of the venue location in degrees

    title*: str*
    :   Title of the venue

    address*: str*
    :   Address of the venue

    foursquare_id*: str | None*
    :   *Optional*. Foursquare identifier of the venue if known

    foursquare_type*: str | None*
    :   *Optional*. Foursquare type of the venue, if known. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)

    google_place_id*: str | None*
    :   *Optional*. Google Places identifier of the venue

    google_place_type*: str | None*
    :   *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the venue

    thumbnail_url*: str | None*
    :   *Optional*. Url of the thumbnail for the result

    thumbnail_width*: int | None*
    :   *Optional*. Thumbnail width

    thumbnail_height*: int | None*
    :   *Optional*. Thumbnail height
