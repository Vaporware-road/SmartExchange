# InputRichBlockTable

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_table.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_table.html)

*class* aiogram.types.input_rich_block_table.InputRichBlockTable(*\**, *type: Literal[InputRichBlockType.TABLE] = InputRichBlockType.TABLE*, *cells: list[list[[RichBlockTableCell](rich_block_table_cell.html#aiogram.types.rich_block_table_cell.RichBlockTableCell "aiogram.types.rich_block_table_cell.RichBlockTableCell")]]*, *is_bordered: bool | None = None*, *is_striped: bool | None = None*, *caption: RichTextUnion | None = None*, *\*\*extra_data: Any*)
:   A table, corresponding to the HTML tag `<table>`.

    Source: <https://core.telegram.org/bots/api#inputrichblocktable>

    type*: Literal[InputRichBlockType.TABLE]*
    :   Type of the block, always ‘table’

    cells*: list[list[[RichBlockTableCell](rich_block_table_cell.html#aiogram.types.rich_block_table_cell.RichBlockTableCell "aiogram.types.rich_block_table_cell.RichBlockTableCell")]]*
    :   Cells of the table

    is_bordered*: bool | None*
    :   *Optional*. Pass `True` if the table has borders

    is_striped*: bool | None*
    :   *Optional*. Pass `True` if the table is striped

    caption*: RichTextUnion | None*
    :   *Optional*. Caption of the table
