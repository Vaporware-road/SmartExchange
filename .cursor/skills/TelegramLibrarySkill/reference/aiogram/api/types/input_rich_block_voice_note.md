# InputRichBlockVoiceNote

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_voice_note.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_voice_note.html)

*class* aiogram.types.input_rich_block_voice_note.InputRichBlockVoiceNote(*\**, *type: Literal[InputRichBlockType.VOICE_NOTE] = InputRichBlockType.VOICE_NOTE*, *voice_note: [InputMediaVoiceNote](input_media_voice_note.html#aiogram.types.input_media_voice_note.InputMediaVoiceNote "aiogram.types.input_media_voice_note.InputMediaVoiceNote")*, *caption: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None = None*, *\*\*extra_data: Any*)
:   A block with a voice note, corresponding to the HTML tag `<audio>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockvoicenote>

    type*: Literal[InputRichBlockType.VOICE_NOTE]*
    :   Type of the block, always ‘voice_note’

    voice_note*: [InputMediaVoiceNote](input_media_voice_note.html#aiogram.types.input_media_voice_note.InputMediaVoiceNote "aiogram.types.input_media_voice_note.InputMediaVoiceNote")*
    :   The voice note. Caption is ignored

    caption*: [RichBlockCaption](rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") | None*
    :   *Optional*. Caption of the block
