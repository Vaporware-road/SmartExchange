# StoryAreaTypeLink

> Source: [https://docs.aiogram.dev/en/latest/api/types/story_area_type_link.html](https://docs.aiogram.dev/en/latest/api/types/story_area_type_link.html)

*class* aiogram.types.story_area_type_link.StoryAreaTypeLink(*\**, *type: Literal[StoryAreaTypeType.LINK] = StoryAreaTypeType.LINK*, *url: str*, *\*\*extra_data: Any*)
:   Describes a story area pointing to an HTTP or tg:// link. Currently, a story can have up to 3 link areas.

    Source: <https://core.telegram.org/bots/api#storyareatypelink>

    type*: Literal[StoryAreaTypeType.LINK]*
    :   Type of the area, always ‘link’

    url*: str*
    :   HTTP or tg:// URL to be opened when the area is clicked
