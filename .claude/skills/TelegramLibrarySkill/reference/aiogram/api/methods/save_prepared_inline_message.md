# savePreparedInlineMessage

> Source: [https://docs.aiogram.dev/en/latest/api/methods/save_prepared_inline_message.html](https://docs.aiogram.dev/en/latest/api/methods/save_prepared_inline_message.html)

Returns: `PreparedInlineMessage`

*class* aiogram.methods.save_prepared_inline_message.SavePreparedInlineMessage(*\**, *user_id: int*, *result: [InlineQueryResultCachedAudio](../types/inline_query_result_cached_audio.html#aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio "aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio") | [InlineQueryResultCachedDocument](../types/inline_query_result_cached_document.html#aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument "aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument") | [InlineQueryResultCachedGif](../types/inline_query_result_cached_gif.html#aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif "aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif") | [InlineQueryResultCachedMpeg4Gif](../types/inline_query_result_cached_mpeg4_gif.html#aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif "aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif") | [InlineQueryResultCachedPhoto](../types/inline_query_result_cached_photo.html#aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto "aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto") | [InlineQueryResultCachedSticker](../types/inline_query_result_cached_sticker.html#aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker "aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker") | [InlineQueryResultCachedVideo](../types/inline_query_result_cached_video.html#aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo "aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo") | [InlineQueryResultCachedVoice](../types/inline_query_result_cached_voice.html#aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice "aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice") | [InlineQueryResultArticle](../types/inline_query_result_article.html#aiogram.types.inline_query_result_article.InlineQueryResultArticle "aiogram.types.inline_query_result_article.InlineQueryResultArticle") | [InlineQueryResultAudio](../types/inline_query_result_audio.html#aiogram.types.inline_query_result_audio.InlineQueryResultAudio "aiogram.types.inline_query_result_audio.InlineQueryResultAudio") | [InlineQueryResultContact](../types/inline_query_result_contact.html#aiogram.types.inline_query_result_contact.InlineQueryResultContact "aiogram.types.inline_query_result_contact.InlineQueryResultContact") | [InlineQueryResultGame](../types/inline_query_result_game.html#aiogram.types.inline_query_result_game.InlineQueryResultGame "aiogram.types.inline_query_result_game.InlineQueryResultGame") | [InlineQueryResultDocument](../types/inline_query_result_document.html#aiogram.types.inline_query_result_document.InlineQueryResultDocument "aiogram.types.inline_query_result_document.InlineQueryResultDocument") | [InlineQueryResultGif](../types/inline_query_result_gif.html#aiogram.types.inline_query_result_gif.InlineQueryResultGif "aiogram.types.inline_query_result_gif.InlineQueryResultGif") | [InlineQueryResultLocation](../types/inline_query_result_location.html#aiogram.types.inline_query_result_location.InlineQueryResultLocation "aiogram.types.inline_query_result_location.InlineQueryResultLocation") | [InlineQueryResultMpeg4Gif](../types/inline_query_result_mpeg4_gif.html#aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif "aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif") | [InlineQueryResultPhoto](../types/inline_query_result_photo.html#aiogram.types.inline_query_result_photo.InlineQueryResultPhoto "aiogram.types.inline_query_result_photo.InlineQueryResultPhoto") | [InlineQueryResultVenue](../types/inline_query_result_venue.html#aiogram.types.inline_query_result_venue.InlineQueryResultVenue "aiogram.types.inline_query_result_venue.InlineQueryResultVenue") | [InlineQueryResultVideo](../types/inline_query_result_video.html#aiogram.types.inline_query_result_video.InlineQueryResultVideo "aiogram.types.inline_query_result_video.InlineQueryResultVideo") | [InlineQueryResultVoice](../types/inline_query_result_voice.html#aiogram.types.inline_query_result_voice.InlineQueryResultVoice "aiogram.types.inline_query_result_voice.InlineQueryResultVoice")*, *allow_user_chats: bool | None = None*, *allow_bot_chats: bool | None = None*, *allow_group_chats: bool | None = None*, *allow_channel_chats: bool | None = None*, *\*\*extra_data: Any*)
:   Stores a message that can be sent by a user of a Mini App. Returns a [`aiogram.types.prepared_inline_message.PreparedInlineMessage`](../types/prepared_inline_message.html#aiogram.types.prepared_inline_message.PreparedInlineMessage "aiogram.types.prepared_inline_message.PreparedInlineMessage") object.

    Source: <https://core.telegram.org/bots/api#savepreparedinlinemessage>

    user_id*: int*
    :   Unique identifier of the target user that can use the prepared message

    result*: InlineQueryResultUnion*
    :   A JSON-serialized object describing the message to be sent

    allow_user_chats*: bool | None*
    :   Pass `True` if the message can be sent to private chats with users

    allow_bot_chats*: bool | None*
    :   Pass `True` if the message can be sent to private chats with bots

    allow_group_chats*: bool | None*
    :   Pass `True` if the message can be sent to group and supergroup chats

    allow_channel_chats*: bool | None*
    :   Pass `True` if the message can be sent to channel chats

## Usage

### As bot method

```
result: PreparedInlineMessage = await bot.save_prepared_inline_message(...)
```

### Method as object

Imports:

- `from aiogram.methods.save_prepared_inline_message import SavePreparedInlineMessage`
- alias: `from aiogram.methods import SavePreparedInlineMessage`

#### With specific bot

```
result: PreparedInlineMessage = await bot(SavePreparedInlineMessage(...))
```

#### As reply into Webhook in handler

```
return SavePreparedInlineMessage(...)
```
