# RichBlockVoiceNote

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_voice_note.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_voice_note.html)

*class* aiogram.types.rich_block_voice_note.RichBlockVoiceNote(*\**, *type: Literal[RichBlockType.VOICE_NOTE] = RichBlockType.VOICE_NOTE*, *voice_note: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a voice note, corresponding to the HTML tag `<audio>`.

    Source: <https://core.telegram.org/bots/api#richblockvoicenote>

    type*: Literal[RichBlockType.VOICE_NOTE]*
    :   Type of the block, always ‘voice_note’

    voice_note*: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice")*
    :   The voice note

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
