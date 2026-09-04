# InputRichBlockAnimation

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_animation.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_animation.html)

*class* aiogram.types.input_rich_block_animation.InputRichBlockAnimation(*\**, *type: Literal[InputRichBlockType.ANIMATION] = InputRichBlockType.ANIMATION*, *animation: [InputMediaAnimation](input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with an animation, corresponding to the HTML tag `<video>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockanimation>

    type*: Literal[InputRichBlockType.ANIMATION]*
    :   Type of the block, always ‘animation’

    animation*: [InputMediaAnimation](input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation")*
    :   The animation. Caption is ignored

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
