# Chat action sender

> Source: [https://docs.aiogram.dev/en/latest/utils/chat_action.html](https://docs.aiogram.dev/en/latest/utils/chat_action.html)

## Sender

*class* aiogram.utils.chat_action.ChatActionSender(*\**, *bot: Bot*, *chat_id: str | int*, *message_thread_id: int | None = None*, *action: str = 'typing'*, *interval: float = 5.0*, *initial_sleep: float = 0.0*)
:   This utility helps to automatically send chat action until long actions is done
    to take acknowledge bot users the bot is doing something and not crashed.

    Provides simply to use context manager.

    Technically sender start background task with infinity loop which works
    until action will be finished and sends the
    [chat action](https://core.telegram.org/bots/api#sendchataction)
    every 5 seconds.

    __init__(*\**, *bot: Bot*, *chat_id: str | int*, *message_thread_id: int | None = None*, *action: str = 'typing'*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → None
    :   Parameters:
        :   - **bot** – instance of the bot
            - **chat_id** – target chat id
            - **message_thread_id** – unique identifier for the target message thread; supergroups only
            - **action** – chat action type
            - **interval** – interval between iterations
            - **initial_sleep** – sleep before first sending of the action

    *classmethod* choose_sticker(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with choose_sticker action

    *classmethod* find_location(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with find_location action

    *classmethod* record_video(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with record_video action

    *classmethod* record_video_note(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with record_video_note action

    *classmethod* record_voice(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with record_voice action

    *classmethod* typing(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with typing action

    *classmethod* upload_document(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with upload_document action

    *classmethod* upload_photo(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with upload_photo action

    *classmethod* upload_video(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with upload_video action

    *classmethod* upload_video_note(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with upload_video_note action

    *classmethod* upload_voice(*chat_id: int | str*, *bot: Bot*, *message_thread_id: int | None = None*, *interval: float = 5.0*, *initial_sleep: float = 0.0*) → [ChatActionSender](#aiogram.utils.chat_action.ChatActionSender "aiogram.utils.chat_action.ChatActionSender")
    :   Create instance of the sender with upload_voice action

### Usage

```
async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
    # Do something...
    # Perform some long calculations
    await message.answer(result)
```

## Middleware

*class* aiogram.utils.chat_action.ChatActionMiddleware
:   Helps to automatically use chat action sender for all message handlers

### Usage

Before usa should be registered for the message event

```
<router or dispatcher>.message.middleware(ChatActionMiddleware())
```

After this action all handlers which works longer than initial_sleep will produce the ‘typing’ chat action.

Also sender can be customized via flags feature for particular handler.

Change only action type:

```
@router.message(...)
@flags.chat_action("sticker")
async def my_handler(message: Message): ...
```

Change sender configuration:

```
@router.message(...)
@flags.chat_action(initial_sleep=2, action="upload_document", interval=3)
async def my_handler(message: Message): ...
```
