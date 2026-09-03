# ChecklistTasksDone

> Source: [https://docs.aiogram.dev/en/latest/api/types/checklist_tasks_done.html](https://docs.aiogram.dev/en/latest/api/types/checklist_tasks_done.html)

*class* aiogram.types.checklist_tasks_done.ChecklistTasksDone(*\**, *checklist_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *marked_as_done_task_ids: list[int] | None = None*, *marked_as_not_done_task_ids: list[int] | None = None*, *\*\*extra_data: Any*)
:   Describes a service message about checklist tasks marked as done or not done.

    Source: <https://core.telegram.org/bots/api#checklisttasksdone>

    checklist_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. Message containing the checklist whose tasks were marked as done or not done. Note that the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain the *reply_to_message* field even if it itself is a reply

    marked_as_done_task_ids*: list[int] | None*
    :   *Optional*. Identifiers of the tasks that were marked as done

    marked_as_not_done_task_ids*: list[int] | None*
    :   *Optional*. Identifiers of the tasks that were marked as not done
