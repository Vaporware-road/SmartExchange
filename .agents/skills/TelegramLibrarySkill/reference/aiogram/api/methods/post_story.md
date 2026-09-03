# postStory

> Source: [https://docs.aiogram.dev/en/latest/api/methods/post_story.html](https://docs.aiogram.dev/en/latest/api/methods/post_story.html)

Returns: `Story`

*class* aiogram.methods.post_story.PostStory(*\**, *business_connection_id: str*, *content: [InputStoryContentPhoto](../types/input_story_content_photo.html#aiogram.types.input_story_content_photo.InputStoryContentPhoto "aiogram.types.input_story_content_photo.InputStoryContentPhoto") | [InputStoryContentVideo](../types/input_story_content_video.html#aiogram.types.input_story_content_video.InputStoryContentVideo "aiogram.types.input_story_content_video.InputStoryContentVideo")*, *active_period: int*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *areas: list[[StoryArea](../types/story_area.html#aiogram.types.story_area.StoryArea "aiogram.types.story_area.StoryArea")] | None = None*, *post_to_chat_page: bool | None = None*, *protect_content: bool | None = None*, *\*\*extra_data: Any*)
:   Posts a story on behalf of a managed business account. Requires the *can_manage_stories* business bot right. Returns [`aiogram.types.story.Story`](../types/story.html#aiogram.types.story.Story "aiogram.types.story.Story") on success.

    Source: <https://core.telegram.org/bots/api#poststory>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    content*: InputStoryContentUnion*
    :   Content of the story

    active_period*: int*
    :   Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400`

    caption*: str | None*
    :   Caption of the story, 0-2048 characters after entities parsing

    parse_mode*: str | None*
    :   Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*

    areas*: list[[StoryArea](../types/story_area.html#aiogram.types.story_area.StoryArea "aiogram.types.story_area.StoryArea")] | None*
    :   A JSON-serialized list of clickable areas to be shown on the story

    post_to_chat_page*: bool | None*
    :   Pass `True` to keep the story accessible after it expires

    protect_content*: bool | None*
    :   Pass `True` if the content of the story must be protected from forwarding and screenshotting

## Usage

### As bot method

```
result: Story = await bot.post_story(...)
```

### Method as object

Imports:

- `from aiogram.methods.post_story import PostStory`
- alias: `from aiogram.methods import PostStory`

#### With specific bot

```
result: Story = await bot(PostStory(...))
```

#### As reply into Webhook in handler

```
return PostStory(...)
```
