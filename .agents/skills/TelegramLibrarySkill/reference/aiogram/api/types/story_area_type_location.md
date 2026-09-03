# StoryAreaTypeLocation

> Source: [https://docs.aiogram.dev/en/latest/api/types/story_area_type_location.html](https://docs.aiogram.dev/en/latest/api/types/story_area_type_location.html)

*class* aiogram.types.story_area_type_location.StoryAreaTypeLocation(*\**, *type: Literal[StoryAreaTypeType.LOCATION] = StoryAreaTypeType.LOCATION*, *latitude: float*, *longitude: float*, *address: [LocationAddress](location_address.html#aiogram.types.location_address.LocationAddress "aiogram.types.location_address.LocationAddress") | None = None*, *\*\*extra_data: Any*)
:   Describes a story area pointing to a location. Currently, a story can have up to 10 location areas.

    Source: <https://core.telegram.org/bots/api#storyareatypelocation>

    type*: Literal[StoryAreaTypeType.LOCATION]*
    :   Type of the area, always ‘location’

    latitude*: float*
    :   Location latitude in degrees

    longitude*: float*
    :   Location longitude in degrees

    address*: [LocationAddress](location_address.html#aiogram.types.location_address.LocationAddress "aiogram.types.location_address.LocationAddress") | None*
    :   *Optional*. Address of the location
