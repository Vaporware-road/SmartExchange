# RichBlockMap

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_map.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_map.html)

*class* aiogram.types.rich_block_map.RichBlockMap(*\**, *type: Literal[RichBlockType.MAP] = RichBlockType.MAP*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*, *zoom: int*, *width: int*, *height: int*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a map, corresponding to the custom HTML tag `<tg-map>`.

    Source: <https://core.telegram.org/bots/api#richblockmap>

    type*: Literal[RichBlockType.MAP]*
    :   Type of the block, always ‘map’

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location")*
    :   Location of the center of the map

    zoom*: int*
    :   Map zoom level; 13-20

    width*: int*
    :   Expected width of the map

    height*: int*
    :   Expected height of the map

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
