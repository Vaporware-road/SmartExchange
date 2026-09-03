# InputRichBlockMathematicalExpression

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_rich_block_mathematical_expression.html](https://docs.aiogram.dev/en/latest/api/types/input_rich_block_mathematical_expression.html)

*class* aiogram.types.input_rich_block_mathematical_expression.InputRichBlockMathematicalExpression(*\**, *type: Literal[InputRichBlockType.MATHEMATICAL_EXPRESSION] = InputRichBlockType.MATHEMATICAL_EXPRESSION*, *expression: str*, *\*\*extra_data: Any*)
:   A block with a mathematical expression in LaTeX format, corresponding to the custom HTML tag `<tg-math-block>`.

    Source: <https://core.telegram.org/bots/api#inputrichblockmathematicalexpression>

    type*: Literal[InputRichBlockType.MATHEMATICAL_EXPRESSION]*
    :   Type of the block, always ‘mathematical_expression’

    expression*: str*
    :   The mathematical expression in LaTeX format
