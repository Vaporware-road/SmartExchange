# RichTextDateTime

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_text_date_time.html](https://docs.aiogram.dev/en/latest/api/types/rich_text_date_time.html)

*class* aiogram.types.rich_text_date_time.RichTextDateTime(*\**, *type: Literal[RichTextType.DATE_TIME] = RichTextType.DATE_TIME*, *text: RichTextUnion*, *unix_time: int*, *date_time_format: str*, *\*\*extra_data: Any*)
:   Formatted date and time.

    Source: <https://core.telegram.org/bots/api#richtextdatetime>

    type*: Literal[RichTextType.DATE_TIME]*
    :   Type of the rich text, always ‘date_time’

    text*: RichTextUnion*
    :   The text

    unix_time*: int*
    :   The Unix time associated with the entity

    date_time_format*: str*
    :   The string that defines the formatting of the date and time. See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details
