# InputRichBlockVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_video.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_video.html)

*class* aiogram.types.input_rich_block_video.InputRichBlockVideo(*\**, *type: Literal[InputRichBlockType.VIDEO] = InputRichBlockType.VIDEO*, *video: [InputMediaVideo](input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a video, corresponding to the HTML tag `<video>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockvideo>

    type*: Literal[InputRichBlockType.VIDEO]*
    :   Type of the block, always ‘video’

    video*: [InputMediaVideo](input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo")*
    :   The video. Caption is ignored

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
