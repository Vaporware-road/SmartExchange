# InputRichBlockAudio

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_audio.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_audio.html)

*class* aiogram.types.input_rich_block_audio.InputRichBlockAudio(*\**, *type: Literal[InputRichBlockType.AUDIO] = InputRichBlockType.AUDIO*, *audio: [InputMediaAudio](input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a music file, corresponding to the HTML tag `<audio>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockaudio>

    type*: Literal[InputRichBlockType.AUDIO]*
    :   Type of the block, always ‘audio’

    audio*: [InputMediaAudio](input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio")*
    :   The audio. Caption is ignored

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
