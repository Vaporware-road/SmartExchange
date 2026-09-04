# StoryAreaTypeWeather

> Source: [https://docs.aiogram.dev/en/latest/api/types/story_area_type_weather.html](https://docs.aiogram.dev/en/latest/api/types/story_area_type_weather.html)

*class* aiogram.types.story_area_type_weather.StoryAreaTypeWeather(*\**, *type: Literal[StoryAreaTypeType.WEATHER] = StoryAreaTypeType.WEATHER*, *temperature: float*, *emoji: str*, *background_color: int*, *\*\*extra_data: Any*)
:   Describes a story area containing weather information. Currently, a story can have up to 3 weather areas.

    Source: <https://core.telegram.org/bots/api#storyareatypeweather>

    type*: Literal[StoryAreaTypeType.WEATHER]*
    :   Type of the area, always ‘weather’

    temperature*: float*
    :   Temperature, in degree Celsius

    emoji*: str*
    :   Emoji representing the weather

    background_color*: int*
    :   A color of the area background in the ARGB format
