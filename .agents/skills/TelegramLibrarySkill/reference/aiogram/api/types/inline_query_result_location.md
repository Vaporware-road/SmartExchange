# InlineQueryResultLocation

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_location.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_location.html)

*class* aiogram.types.inline_query_result_location.InlineQueryResultLocation(*\**, *type: Literal[InlineQueryResultType.LOCATION] = InlineQueryResultType.LOCATION*, *id: str*, *latitude: float*, *longitude: float*, *title: str*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *input_message_content: [InputTextMessageContent](input_text_message_content.html#aiogram.types.input_text_message_content.InputTextMessageContent "aiogram.types.input_text_message_content.InputTextMessageContent") | [InputRichMessageContent](input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") | [InputLocationMessageContent](input_location_message_content.html#aiogram.types.input_location_message_content.InputLocationMessageContent "aiogram.types.input_location_message_content.InputLocationMessageContent") | [InputVenueMessageContent](input_venue_message_content.html#aiogram.types.input_venue_message_content.InputVenueMessageContent "aiogram.types.input_venue_message_content.InputVenueMessageContent") | [InputContactMessageContent](input_contact_message_content.html#aiogram.types.input_contact_message_content.InputContactMessageContent "aiogram.types.input_contact_message_content.InputContactMessageContent") | [InputInvoiceMessageContent](input_invoice_message_content.html#aiogram.types.input_invoice_message_content.InputInvoiceMessageContent "aiogram.types.input_invoice_message_content.InputInvoiceMessageContent") | None = None*, *thumbnail_url: str | None = None*, *thumbnail_width: int | None = None*, *thumbnail_height: int | None = None*, *\*\*extra_data: Any*)
:   Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the location.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultlocation>

    type*: Literal[InlineQueryResultType.LOCATION]*
    :   Type of the result, must be *location*

    id*: str*
    :   Unique identifier for this result, 1-64 Bytes

    latitude*: float*
    :   Location latitude in degrees

    longitude*: float*
    :   Location longitude in degrees

    title*: str*
    :   Location title

    horizontal_accuracy*: float | None*
    :   *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500

    live_period*: int | None*
    :   *Optional*. Period in seconds during which the location can be updated, must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely

    heading*: int | None*
    :   *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified

    proximity_alert_radius*: int | None*
    :   *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the location

    thumbnail_url*: str | None*
    :   *Optional*. Url of the thumbnail for the result

    thumbnail_width*: int | None*
    :   *Optional*. Thumbnail width

    thumbnail_height*: int | None*
    :   *Optional*. Thumbnail height
