# ChecklistTasksAdded

> Source: [https://docs.aiogram.dev/en/latest/api/types/checklist_tasks_added.html](https://docs.aiogram.dev/en/latest/api/types/checklist_tasks_added.html)

*class* aiogram.types.checklist_tasks_added.ChecklistTasksAdded(*\**, *tasks: list[[ChecklistTask](checklist_task.html#aiogram.types.checklist_task.ChecklistTask "aiogram.types.checklist_task.ChecklistTask")]*, *checklist_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about tasks added to a checklist.

    Source: <https://core.telegram.org/bots/api#checklisttasksadded>

    tasks*: list[[ChecklistTask](checklist_task.html#aiogram.types.checklist_task.ChecklistTask "aiogram.types.checklist_task.ChecklistTask")]*
    :   List of tasks added to the checklist

    checklist_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the checklist to which the tasks were added. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply
