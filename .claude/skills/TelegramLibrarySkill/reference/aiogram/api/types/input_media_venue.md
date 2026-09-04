# InputMediaVenue

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_venue.html](https://docs.aiogram.dev/en/latest/api/types/input_media_venue.html)

*class* aiogram.types.input_media_venue.InputMediaVenue(*\**, *type: Literal[InputMediaType.VENUE] = InputMediaType.VENUE*, *latitude: float*, *longitude: float*, *title: str*, *address: str*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *\*\*extra_data: Any*)
:   Represents a venue to be sent.

    Source: <https://core.telegram.org/bots/api#inputmediavenue>

    type*: Literal[InputMediaType.VENUE]*
    :   Type of the media, must be *venue*

    latitude*: float*
    :   Latitude of the location

    longitude*: float*
    :   Longitude of the location

    title*: str*
    :   Name of the venue

    address*: str*
    :   Address of the venue

    foursquare_id*: str | None*
    :   *Optional*. Foursquare identifier of the venue

    foursquare_type*: str | None*
    :   *Optional*. Foursquare type of the venue, if known. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)

    google_place_id*: str | None*
    :   *Optional*. Google Places identifier of the venue

    google_place_type*: str | None*
    :   *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
