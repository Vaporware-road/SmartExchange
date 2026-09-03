# approveSuggestedPost

> Source: [https://docs.aiogram.dev/en/latest/api/methods/approve_suggested_post.html](https://docs.aiogram.dev/en/latest/api/methods/approve_suggested_post.html)

Returns: `bool`

*class* aiogram.methods.approve_suggested_post.ApproveSuggestedPost(*\**, *chat_id: int*, *message_id: int*, *send_date: datetime | timedelta | int | None = None*, *\*\*extra_data: Any*)
:   Use this method to approve a suggested post in a direct messages chat. The bot must have the ‘can_post_messages’ administrator right in the corresponding channel chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#approvesuggestedpost>

    chat_id*: int*
    :   Unique identifier for the target direct messages chat

    message_id*: int*
    :   Identifier of a suggested post message to approve

    send_date*: DateTimeUnion | None*
    :   Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future

## Usage

### As bot method

```
result: bool = await bot.approve_suggested_post(...)
```

### Method as object

Imports:

- `from aiogram.methods.approve_suggested_post import ApproveSuggestedPost`
- alias: `from aiogram.methods import ApproveSuggestedPost`

#### With specific bot

```
result: bool = await bot(ApproveSuggestedPost(...))
```

#### As reply into Webhook in handler

```
return ApproveSuggestedPost(...)
```
