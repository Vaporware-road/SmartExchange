# Location

> Source: [https://docs.aiogram.dev/en/latest/api/types/location.html](https://docs.aiogram.dev/en/latest/api/types/location.html)

*class* aiogram.types.location.Location(*\**, *latitude: float*, *longitude: float*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a point on the map.

    Source: <https://core.telegram.org/bots/api#location>

    latitude*: float*
    :   Latitude as defined by the sender

    longitude*: float*
    :   Longitude as defined by the sender

    horizontal_accuracy*: float | None*
    :   *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500

    live_period*: int | None*
    :   *Optional*. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only

    heading*: int | None*
    :   *Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only

    proximity_alert_radius*: int | None*
    :   *Optional*. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only
