# InputRichBlockPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_photo.html)

*class* aiogram.types.input_rich_block_photo.InputRichBlockPhoto(*\**, *type: Literal[InputRichBlockType.PHOTO] = InputRichBlockType.PHOTO*, *photo: [InputMediaPhoto](input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a photo, corresponding to the HTML tag `<img>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockphoto>

    type*: Literal[InputRichBlockType.PHOTO]*
    :   Type of the block, always ‘photo’

    photo*: [InputMediaPhoto](input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto")*
    :   The photo. Caption is ignored

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
