# RichBlockPullQuotation

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_pull_quotation.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_pull_quotation.html)

*class* aiogram.types.rich_block_pull_quotation.RichBlockPullQuotation(*\**, *type: Literal[RichBlockType.PULLQUOTE] = RichBlockType.PULLQUOTE*, *text: RichTextUnion*, *credit: RichTextUnion | None = None*, *\*\*extra_data: Any*)
:   A quotation with centered text, loosely corresponding to the HTML tag `<aside>`.

    Source: <https://core.telegram.org/bots/api#richblockpullquotation>

    type*: Literal[RichBlockType.PULLQUOTE]*
    :   Type of the block, always ‘pullquote’

    text*: RichTextUnion*
    :   Text of the block

    credit*: RichTextUnion | None*
    :   *Optional*. Credit of the block
