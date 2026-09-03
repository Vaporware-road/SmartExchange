# repostStory

> Source: [https://docs.aiogram.dev/en/latest/api/methods/repost_story.html](https://docs.aiogram.dev/en/latest/api/methods/repost_story.html)

Returns: `Story`

*class* aiogram.methods.repost_story.RepostStory(*\**, *business_connection_id: str*, *from_chat_id: int*, *from_story_id: int*, *active_period: int*, *post_to_chat_page: bool | None = None*, *protect_content: bool | None = None*, *\*\*extra_data: Any*)
:   Reposts a story on behalf of a business account from another business account. Both business accounts must be managed by the same bot, and the story on the source account must have been posted (or reposted) by the bot. Requires the *can_manage_stories* business bot right for both business accounts. Returns [`aiogram.types.story.Story`](../types/story.html#aiogram.types.story.Story "aiogram.types.story.Story") on success.

    Source: <https://core.telegram.org/bots/api#repoststory>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    from_chat_id*: int*
    :   Unique identifier of the chat which posted the story that should be reposted

    from_story_id*: int*
    :   Unique identifier of the story that should be reposted

    active_period*: int*
    :   Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400`

    post_to_chat_page*: bool | None*
    :   Pass `True` to keep the story accessible after it expires

    protect_content*: bool | None*
    :   Pass `True` if the content of the story must be protected from forwarding and screenshotting

## Usage

### As bot method

```
result: Story = await bot.repost_story(...)
```

### Method as object

Imports:

- `from aiogram.methods.repost_story import RepostStory`
- alias: `from aiogram.methods import RepostStory`

#### With specific bot

```
result: Story = await bot(RepostStory(...))
```

#### As reply into Webhook in handler

```
return RepostStory(...)
```
