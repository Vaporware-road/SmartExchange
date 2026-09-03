# editStory

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_story.html](https://docs.aiogram.dev/en/latest/api/methods/edit_story.html)

Returns: `Story`

*class* aiogram.methods.edit_story.EditStory(*\**, *business_connection_id: str*, *story_id: int*, *content: [InputStoryContentPhoto](../types/input_story_content_photo.html#aiogram.types.input_story_content_photo.InputStoryContentPhoto "aiogram.types.input_story_content_photo.InputStoryContentPhoto") | [InputStoryContentVideo](../types/input_story_content_video.html#aiogram.types.input_story_content_video.InputStoryContentVideo "aiogram.types.input_story_content_video.InputStoryContentVideo")*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *areas: list[[StoryArea](../types/story_area.html#aiogram.types.story_area.StoryArea "aiogram.types.story_area.StoryArea")] | None = None*, *\*\*extra_data: Any*)
:   Edits a story previously posted by the bot on behalf of a managed business account. Requires the *can_manage_stories* business bot right. Returns [`aiogram.types.story.Story`](../types/story.html#aiogram.types.story.Story "aiogram.types.story.Story") on success.

    Source: <https://core.telegram.org/bots/api#editstory>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    story_id*: int*
    :   Unique identifier of the story to edit

    content*: InputStoryContentUnion*
    :   Content of the story

    caption*: str | None*
    :   Caption of the story, 0-2048 characters after entities parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    areas*: list[[StoryArea](../types/story_area.html#aiogram.types.story_area.StoryArea "aiogram.types.story_area.StoryArea")] | None*
    :   A JSON-serialized list of clickable areas to be shown on the story

## Usage

### As bot method

```
result: Story = await bot.edit_story(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_story import EditStory`
- alias: `from aiogram.methods import EditStory`

#### With specific bot

```
result: Story = await bot(EditStory(...))
```

#### As reply into Webhook in handler

```
return EditStory(...)
```
