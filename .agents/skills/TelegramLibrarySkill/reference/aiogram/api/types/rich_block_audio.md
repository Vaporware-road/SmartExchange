# RichBlockAudio

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_audio.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_audio.html)

*class* aiogram.types.rich_block_audio.RichBlockAudio(*\**, *type: Literal[RichBlockType.AUDIO] = RichBlockType.AUDIO*, *audio: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a music file, corresponding to the HTML tag `<audio>`.

    Source: <https://core.telegram.org/bots/api#richblockaudio>

    type*: Literal[RichBlockType.AUDIO]*
    :   Type of the block, always ‘audio’

    audio*: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio")*
    :   The audio

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
