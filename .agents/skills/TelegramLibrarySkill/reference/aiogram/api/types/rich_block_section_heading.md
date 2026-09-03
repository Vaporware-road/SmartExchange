# RichBlockSectionHeading

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_section_heading.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_section_heading.html)

*class* aiogram.types.rich_block_section_heading.RichBlockSectionHeading(*\**, *type: Literal[RichBlockType.HEADING] = RichBlockType.HEADING*, *text: RichTextUnion*, *size: int*, *\*\*extra_data: Any*)
:   A section heading, corresponding to the HTML tags `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, or `<h6>`.

    Source: <https://core.telegram.org/bots/api#richblocksectionheading>

    type*: Literal[RichBlockType.HEADING]*
    :   Type of the block, always ‘heading’

    text*: RichTextUnion*
    :   Text of the block

    size*: int*
    :   Relative size of the text font; 1-6, 1 is the largest, 6 is the smallest
