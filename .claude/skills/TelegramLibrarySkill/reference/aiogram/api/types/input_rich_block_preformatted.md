# InputRichBlockPreformatted

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_preformatted.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_preformatted.html)

*class* aiogram.types.input_rich_block_preformatted.InputRichBlockPreformatted(*\**, *type: Literal[InputRichBlockType.PRE] = InputRichBlockType.PRE*, *text: RichTextUnion*, *language: str | None = None*, *\*\*extra_data: Any*)
:   A preformatted text block, corresponding to the nested HTML tags `<pre>` and `<code>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockpreformatted>

    type*: Literal[InputRichBlockType.PRE]*
    :   Type of the block, always ‘pre’

    text*: RichTextUnion*
    :   Text of the block

    language*: str | None*
    :   *Optional*. The programming language of the text
