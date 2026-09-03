# deleteStory

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_story.html](https://docs.aiogram.dev/en/latest/api/methods/delete_story.html)

Returns: `bool`

*class* aiogram.methods.delete_story.DeleteStory(*\**, *business_connection_id: str*, *story_id: int*, *\*\*extra_data: Any*)
:   Deletes a story previously posted by the bot on behalf of a managed business account. Requires the *can_manage_stories* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletestory>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    story_id*: int*
    :   Unique identifier of the story to delete

## Usage

### As bot method

```
result: bool = await bot.delete_story(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_story import DeleteStory`
- alias: `from aiogram.methods import DeleteStory`

#### With specific bot

```
result: bool = await bot(DeleteStory(...))
```

#### As reply into Webhook in handler

```
return DeleteStory(...)
```
