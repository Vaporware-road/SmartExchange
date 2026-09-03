# Checklist

> Source: [https://docs.aiogram.dev/en/latest/api/types/checklist.html](https://docs.aiogram.dev/en/latest/api/types/checklist.html)

*class* aiogram.types.checklist.Checklist(*\**, *title: str*, *tasks: list[[ChecklistTask](checklist_task.html#aiogram.types.checklist_task.ChecklistTask "aiogram.types.checklist_task.ChecklistTask")]*, *title_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *others_can_add_tasks: bool | None = None*, *others_can_mark_tasks_as_done: bool | None = None*, *\*\*extra_data: Any*)
:   Describes a checklist.

    Source: <https://core.telegram.org/bots/api#checklist>

    title*: str*
    :   Title of the checklist

    tasks*: list[[ChecklistTask](checklist_task.html#aiogram.types.checklist_task.ChecklistTask "aiogram.types.checklist_task.ChecklistTask")]*
    :   List of tasks in the checklist

    title_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the checklist title

    others_can_add_tasks*: bool | None*
    :   *Optional*. `True`, if users other than the creator of the list can add tasks to the list

    others_can_mark_tasks_as_done*: bool | None*
    :   *Optional*. `True`, if users other than the creator of the list can mark tasks as done or not done
