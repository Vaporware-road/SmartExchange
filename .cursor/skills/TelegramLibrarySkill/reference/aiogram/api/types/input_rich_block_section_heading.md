# InputRichBlockSectionHeading

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_section_heading.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_section_heading.html)

*class* aiogram.types.input_rich_block_section_heading.InputRichBlockSectionHeading(*\**, *type: Literal[InputRichBlockType.HEADING] = InputRichBlockType.HEADING*, *text: RichTextUnion*, *size: int*, *\*\*extra_data: Any*)
:   A section heading, corresponding to the HTML tags `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, or `<h6>`.

    Source: <https://core.telegram.org/bots/api#inputrichblocksectionheading>

    type*: Literal[InputRichBlockType.HEADING]*
    :   Type of the block, always ‘heading’

    text*: RichTextUnion*
    :   Text of the block

    size*: int*
    :   Relative size of the text font; 1-6, 1 is the largest, 6 is the smallest
