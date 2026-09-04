# RichBlockVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_video.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_video.html)

*class* aiogram.types.rich_block_video.RichBlockVideo(*\**, *type: Literal[RichBlockType.VIDEO] = RichBlockType.VIDEO*, *video: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video")*, *has_spoiler: bool | None = None*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a video, corresponding to the HTML tag `<video>`.

    Source: <https://core.telegram.org/bots/api#richblockvideo>

    type*: Literal[RichBlockType.VIDEO]*
    :   Type of the block, always ‘video’

    video*: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video")*
    :   The video

    has_spoiler*: bool | None*
    :   *Optional*. `True`, if the media preview is covered by a spoiler animation

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
