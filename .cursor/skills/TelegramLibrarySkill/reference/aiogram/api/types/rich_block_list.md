# RichBlockList

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_list.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_list.html)

*class* aiogram.types.rich_block_list.RichBlockList(*\**, *type: Literal[RichBlockType.LIST] = RichBlockType.LIST*, *items: list[[RichBlockListItem](rich_block_list_item.html#aiogram.types.rich_block_list_item.RichBlockListItem "aiogram.types.rich_block_list_item.RichBlockListItem")]*, *\*\*extra_data: Any*)
:   A list of blocks, corresponding to the HTML tag `<ul>` or `<ol>` with multiple nested tags `<li>`.

    Source: <https://core.telegram.org/bots/api#richblocklist>

    type*: Literal[RichBlockType.LIST]*
    :   Type of the block, always ‘list’

    items*: list[[RichBlockListItem](rich_block_list_item.html#aiogram.types.rich_block_list_item.RichBlockListItem "aiogram.types.rich_block_list_item.RichBlockListItem")]*
    :   Items of the list
