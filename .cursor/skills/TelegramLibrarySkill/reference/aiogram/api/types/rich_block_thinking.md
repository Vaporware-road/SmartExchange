# RichBlockThinking

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_thinking.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_thinking.html)

*class* aiogram.types.rich_block_thinking.RichBlockThinking(*\**, *type: Literal[RichBlockType.THINKING] = RichBlockType.THINKING*, *text: RichTextUnion*, *\*\*extra_data: Any*)
:   A block with a ‘Thinking…’ placeholder, corresponding to the custom HTML tag `<tg-thinking>`. The block may be used only in [`aiogram.methods.send_rich_message_draft.SendRichMessageDraft`](../methods/send_rich_message_draft.html#aiogram.methods.send_rich_message_draft.SendRichMessageDraft "aiogram.methods.send_rich_message_draft.SendRichMessageDraft"), therefore it can’t be received in messages. See [https://t.me/addemoji/AIActions <https://t.me/addemoji/AIActions>`_`https://t.me/addemoji/AIActions](https://t.me/addemoji/AIActions) for examples of custom emoji that are recommended for usage in the block.

    Source: <https://core.telegram.org/bots/api#richblockthinking>

    type*: Literal[RichBlockType.THINKING]*
    :   Type of the block, always ‘thinking’

    text*: RichTextUnion*
    :   Text of the block. See [https://t.me/addemoji/AIActions <https://t.me/addemoji/AIActions>`_`https://t.me/addemoji/AIActions](https://t.me/addemoji/AIActions) for examples of custom emoji that are recommended for usage in the block
