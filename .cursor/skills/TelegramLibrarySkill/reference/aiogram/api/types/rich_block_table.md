# RichBlockTable

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_table.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_table.html)

*class* aiogram.types.rich_block_table.RichBlockTable(*\**, *type: Literal[RichBlockType.TABLE] = RichBlockType.TABLE*, *cells: list[list[[RichBlockTableCell](rich_block_table_cell.html#aiogram.types.rich_block_table_cell.RichBlockTableCell "aiogram.types.rich_block_table_cell.RichBlockTableCell")]]*, *is_bordered: bool | None = None*, *is_striped: bool | None = None*, *caption: RichTextUnion | None = None*, *\*\*extra_data: Any*)
:   A table, corresponding to the HTML tag `<table>`.

    Source: <https://core.telegram.org/bots/api#richblocktable>

    type*: Literal[RichBlockType.TABLE]*
    :   Type of the block, always ‘table’

    cells*: list[list[[RichBlockTableCell](rich_block_table_cell.html#aiogram.types.rich_block_table_cell.RichBlockTableCell "aiogram.types.rich_block_table_cell.RichBlockTableCell")]]*
    :   Cells of the table

    is_bordered*: bool | None*
    :   *Optional*. `True`, if the table has borders

    is_striped*: bool | None*
    :   *Optional*. `True`, if the table is striped

    caption*: RichTextUnion | None*
    :   *Optional*. Caption of the table
