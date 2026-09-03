# InputRichBlockMap

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_map.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_map.html)

*class* aiogram.types.input_rich_block_map.InputRichBlockMap(*\**, *type: Literal[InputRichBlockType.MAP] = InputRichBlockType.MAP*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*, *zoom: int*, *width: int*, *height: int*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a map, corresponding to the custom HTML tag `<tg-map>`. The map’s width and height must not exceed 10000 in total. The width and height ratio must be at most 20.

    Source: <https://core.telegram.org/bots/api#inputrichblockmap>

    type*: Literal[InputRichBlockType.MAP]*
    :   Type of the block, always ‘map’

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*
    :   Location of the center of the map

    zoom*: int*
    :   Map zoom level; 0-24

    width*: int*
    :   Map width; 0-10000

    height*: int*
    :   Map height; 0-10000

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
