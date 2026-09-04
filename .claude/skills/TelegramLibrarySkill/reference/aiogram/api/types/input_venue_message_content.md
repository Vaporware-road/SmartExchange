# InputVenueMessageContent

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_venue_message_content.html](https://docs.aiogram.dev/en/latest/api/types/input_venue_message_content.html)

*class* aiogram.types.input_venue_message_content.InputVenueMessageContent(*\**, *latitude: float*, *longitude: float*, *title: str*, *address: str*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *\*\*extra_data: Any*)
:   Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a venue message to be sent as the result of an inline query.

    Source: <https://core.telegram.org/bots/api#inputvenuemessagecontent>

    latitude*: float*
    :   Latitude of the venue in degrees

    longitude*: float*
    :   Longitude of the venue in degrees

    title*: str*
    :   Name of the venue

    address*: str*
    :   Address of the venue

    foursquare_id*: str | None*
    :   *Optional*. Foursquare identifier of the venue, if known

    foursquare_type*: str | None*
    :   *Optional*. Foursquare type of the venue, if known. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)

    google_place_id*: str | None*
    :   *Optional*. Google Places identifier of the venue

    google_place_type*: str | None*
    :   *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
