# RichBlockTableCell

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_block_table_cell.html](https://docs.aiogram.dev/en/latest/api/types/rich_block_table_cell.html)

*class* aiogram.types.rich_block_table_cell.RichBlockTableCell(*\**, *align: str*, *valign: str*, *text: RichTextUnion | None = None*, *is_header: bool | None = None*, *colspan: int | None = None*, *rowspan: int | None = None*, *\*\*extra_data: Any*)
:   Cell in a table.

    Source: <https://core.telegram.org/bots/api#richblocktablecell>

    align*: str*
    :   Horizontal cell content alignment. Currently, must be one of ‘left’, ‘center’, or ‘right’

    valign*: str*
    :   Vertical cell content alignment. Currently, must be one of ‘top’, ‘middle’, or ‘bottom’

    text*: RichTextUnion | None*
    :   *Optional*. Text in the cell. If omitted, then the cell is invisible

    is_header*: bool | None*
    :   *Optional*. `True`, if the cell is a header cell

    colspan*: int | None*
    :   *Optional*. The number of columns the cell spans if it is bigger than 1

    rowspan*: int | None*
    :   *Optional*. The number of rows the cell spans if it is bigger than 1
