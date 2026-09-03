# InputChecklist

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_checklist.html](https://docs.aiogram.dev/en/latest/api/types/input_checklist.html)

*class* aiogram.types.input_checklist.InputChecklist(*\**, *title: str*, *tasks: list[[InputChecklistTask](input_checklist_task.html#aiogram.types.input_checklist_task.InputChecklistTask "aiogram.types.input_checklist_task.InputChecklistTask")]*, *parse_mode: str | None = None*, *title_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *others_can_add_tasks: bool | None = None*, *others_can_mark_tasks_as_done: bool | None = None*, *\*\*extra_data: Any*)
:   Describes a checklist to create.

    Source: <https://core.telegram.org/bots/api#inputchecklist>

    title*: str*
    :   Title of the checklist; 1-255 characters after entities parsing

    tasks*: list[[InputChecklistTask](input_checklist_task.html#aiogram.types.input_checklist_task.InputChecklistTask "aiogram.types.input_checklist_task.InputChecklistTask")]*
    :   List of 1-30 tasks in the checklist

    parse_mode*: str | None*
    :   *Optional*. Mode for parsing entities in the title. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    title_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the title, which can be specified instead of parse_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities are allowed

    others_can_add_tasks*: bool | None*
    :   *Optional*. Pass `True` if other users can add tasks to the checklist

    others_can_mark_tasks_as_done*: bool | None*
    :   *Optional*. Pass `True` if other users can mark tasks as done or not done in the checklist
