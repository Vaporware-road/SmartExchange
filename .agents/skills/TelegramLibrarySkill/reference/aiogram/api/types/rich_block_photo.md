# RichBlockPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_photo.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_photo.html)

*class* aiogram.types.rich_block_photo.RichBlockPhoto(*\**, *type: Literal[RichBlockType.PHOTO] = RichBlockType.PHOTO*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]*, *has_spoiler: bool | None = None*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a photo, corresponding to the HTML tag `<img>`.

    Source: <https://core.telegram.org/bots/api#richblockphoto>

    type*: Literal[RichBlockType.PHOTO]*
    :   Type of the block, always ‘photo’

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]*
    :   Available sizes of the photo

    has_spoiler*: bool | None*
    :   *Optional*. `True`, if the media preview is covered by a spoiler animation

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
