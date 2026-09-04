# BusinessMessagesDeleted

> Source: [https://docs.aiogram.dev/en/latest/api/types/business_messages_deleted.html](https://docs.aiogram.dev/en/latest/api/types/business_messages_deleted.html)

*class* aiogram.types.business_messages_deleted.BusinessMessagesDeleted(*\**, *business_connection_id: str*, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_ids: list[int]*, *\*\*extra_data: Any*)
:   This object is received when messages are deleted from a connected business account.

    Source: <https://core.telegram.org/bots/api#businessmessagesdeleted>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Information about a chat in the business account. The bot may not have access to the chat or the corresponding user

    message_ids*: list[int]*
    :   The list of identifiers of deleted messages in the chat of the business account
