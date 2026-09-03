# declineSuggestedPost

> Source: [https://docs.aiogram.dev/en/latest/api/methods/decline_suggested_post.html](https://docs.aiogram.dev/en/latest/api/methods/decline_suggested_post.html)

Returns: `bool`

*class* aiogram.methods.decline_suggested_post.DeclineSuggestedPost(*\**, *chat_id: int*, *message_id: int*, *comment: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to decline a suggested post in a direct messages chat. The bot must have the ‘can_manage_direct_messages’ administrator right in the corresponding channel chat. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#declinesuggestedpost>

    chat_id*: int*
    :   Unique identifier for the target direct messages chat

    message_id*: int*
    :   Identifier of a suggested post message to decline

    comment*: str | None*
    :   Comment for the creator of the suggested post; 0-128 characters

## Usage

### As bot method

```
result: bool = await bot.decline_suggested_post(...)
```

### Method as object

Imports:

- `from aiogram.methods.decline_suggested_post import DeclineSuggestedPost`
- alias: `from aiogram.methods import DeclineSuggestedPost`

#### With specific bot

```
result: bool = await bot(DeclineSuggestedPost(...))
```

#### As reply into Webhook in handler

```
return DeclineSuggestedPost(...)
```
