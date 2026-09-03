# InputLocationMessageContent

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_location_message_content.html](https://docs.aiogram.dev/en/latest/api/types/input_location_message_content.html)

*class* aiogram.types.input_location_message_content.InputLocationMessageContent(*\**, *latitude: float*, *longitude: float*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *\*\*extra_data: Any*)
:   Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a location message to be sent as the result of an inline query.

    Source: <https://core.telegram.org/bots/api#inputlocationmessagecontent>

    latitude*: float*
    :   Latitude of the location in degrees

    longitude*: float*
    :   Longitude of the location in degrees

    horizontal_accuracy*: float | None*
    :   *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500

    live_period*: int | None*
    :   *Optional*. Period in seconds during which the location can be updated, must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely

    heading*: int | None*
    :   *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified

    proximity_alert_radius*: int | None*
    :   *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified
