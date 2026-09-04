# Venue

> Source: [https://docs.aiogram.dev/en/latest/api/types/venue.html](https://docs.aiogram.dev/en/latest/api/types/venue.html)

*class* aiogram.types.venue.Venue(*\**, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*, *title: str*, *address: str*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *\*\*extra_data: Any*)
:   This object represents a venue.

    Source: <https://core.telegram.org/bots/api#venue>

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*
    :   Venue location. Can’t be a live location

    title*: str*
    :   Name of the venue

    address*: str*
    :   Address of the venue

    foursquare_id*: str | None*
    :   *Optional*. Foursquare identifier of the venue

    foursquare_type*: str | None*
    :   *Optional*. Foursquare type of the venue. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)

    google_place_id*: str | None*
    :   *Optional*. Google Places identifier of the venue

    google_place_type*: str | None*
    :   *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
