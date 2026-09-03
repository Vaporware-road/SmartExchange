# InputRichBlockList

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_list.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_list.html)

*class* aiogram.types.input_rich_block_list.InputRichBlockList(*\**, *type: Literal[InputRichBlockType.LIST] = InputRichBlockType.LIST*, *items: list[[InputRichBlockListItem](input_rich_block_list_item.html#aiogram.types.input_rich_block_list_item.InputRichBlockListItem "aiogram.types.input_rich_block_list_item.InputRichBlockListItem")]*, *\*\*extra_data: Any*)
:   A list of blocks, corresponding to the HTML tag `<ul>` or `<ol>` with multiple nested tags `<li>`.

    Source: <https://core.telegram.org/bots/api#inputrichblocklist>

    type*: Literal[InputRichBlockType.LIST]*
    :   Type of the block, always ‘list’

    items*: list[[InputRichBlockListItem](input_rich_block_list_item.html#aiogram.types.input_rich_block_list_item.InputRichBlockListItem "aiogram.types.input_rich_block_list_item.InputRichBlockListItem")]*
    :   Items of the list
