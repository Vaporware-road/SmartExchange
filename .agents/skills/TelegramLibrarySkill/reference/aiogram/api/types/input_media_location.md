# InputMediaLocation

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_media_location.html](https://docs.aiogram.dev/en/latest/api/types/input_media_location.html)

*class* aiogram.types.input_media_location.InputMediaLocation(*\**, *type: Literal[InputMediaType.LOCATION] = InputMediaType.LOCATION*, *latitude: float*, *longitude: float*, *horizontal_accuracy: float | None = None*, *\*\*extra_data: Any*)
:   Represents a location to be sent.

    Source: <https://core.telegram.org/bots/api#inputmedialocation>

    type*: Literal[InputMediaType.LOCATION]*
    :   Type of the media, must be *location*

    latitude*: float*
    :   Latitude of the location

    longitude*: float*
    :   Longitude of the location

    horizontal_accuracy*: float | None*
    :   *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500
