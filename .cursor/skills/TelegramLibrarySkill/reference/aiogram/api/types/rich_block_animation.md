# RichBlockAnimation

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_animation.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_animation.html)

*class* aiogram.types.rich_block_animation.RichBlockAnimation(*\**, *type: Literal[RichBlockType.ANIMATION] = RichBlockType.ANIMATION*, *animation: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation")*, *has_spoiler: bool | None = None*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with an animation, corresponding to the HTML tag `<video>`.

    Source: <https://core.telegram.org/bots/api#richblockanimation>

    type*: Literal[RichBlockType.ANIMATION]*
    :   Type of the block, always ‘animation’

    animation*: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation")*
    :   The animation

    has_spoiler*: bool | None*
    :   *Optional*. `True`, if the media preview is covered by a spoiler animation

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
