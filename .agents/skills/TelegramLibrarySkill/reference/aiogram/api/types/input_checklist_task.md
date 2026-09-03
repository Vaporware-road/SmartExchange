# InputChecklistTask

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_checklist_task.html](https://docs.aiogram.dev/en/latest/api/types/input_checklist_task.html)

*class* aiogram.types.input_checklist_task.InputChecklistTask(*\**, *id: int*, *text: str*, *parse_mode: str | None = None*, *text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Describes a task to add to a checklist.

    Source: <https://core.telegram.org/bots/api#inputchecklisttask>

    id*: int*
    :   Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist

    text*: str*
    :   Text of the task; 1-100 characters after entities parsing

    parse_mode*: str | None*
    :   *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the text, which can be specified instead of parse_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities are allowed
