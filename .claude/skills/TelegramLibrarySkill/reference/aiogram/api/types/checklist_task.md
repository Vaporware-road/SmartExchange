# ChecklistTask

> Source: [https://docs.aiogram.dev/en/latest/api/types/checklist_task.html](https://docs.aiogram.dev/en/latest/api/types/checklist_task.html)

*class* aiogram.types.checklist_task.ChecklistTask(*\**, *id: int*, *text: str*, *text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *completed_by_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *completed_by_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *completion_date: int | None = None*, *\*\*extra_data: Any*)
:   Describes a task in a checklist.

    Source: <https://core.telegram.org/bots/api#checklisttask>

    id*: int*
    :   Unique identifier of the task

    text*: str*
    :   Text of the task

    text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the task text

    completed_by_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. User that completed the task; omitted if the task wasn’t completed by a user

    completed_by_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Chat that completed the task; omitted if the task wasn’t completed by a chat

    completion_date*: int | None*
    :   *Optional*. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn’t completed
