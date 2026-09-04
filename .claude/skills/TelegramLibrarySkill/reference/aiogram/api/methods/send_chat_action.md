# sendChatAction

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_chat_action.html](https://docs.aiogram.dev/en/latest/api/methods/send_chat_action.html)

Returns: `bool`

*class* aiogram.methods.send_chat_action.SendChatAction(*\**, *chat_id: int | str*, *action: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method when you need to tell the user that something is happening on the bot’s side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns `True` on success.

    > Example: The [ImageBot](https://t.me/imagebot) needs some time to process a request and upload the image. Instead of sending a text message along the lines of ‘Retrieving image, please wait…’, the bot may use [`aiogram.methods.send_chat_action.SendChatAction`](#aiogram.methods.send_chat_action.SendChatAction "aiogram.methods.send_chat_action.SendChatAction") with *action* = *upload_photo*. The user will see a ‘sending photo’ status for the bot.

    We only recommend using this method when a response from the bot will take a **noticeable** amount of time to arrive.

    Source: <https://core.telegram.org/bots/api#sendchataction>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot or supergroup in the format `@username`. Channel chats and channel direct messages chats aren’t supported

    action*: str*
    :   Type of action to broadcast. Choose one, depending on what the user is about to receive: *typing* for [text messages](https://core.telegram.org/bots/api#sendmessage), *upload_photo* for [photos](https://core.telegram.org/bots/api#sendphoto), *record_video* or *upload_video* for [videos](https://core.telegram.org/bots/api#sendvideo), *record_voice* or *upload_voice* for [voice notes](https://core.telegram.org/bots/api#sendvoice), *upload_document* for [general files](https://core.telegram.org/bots/api#senddocument), *choose_sticker* for [stickers](https://core.telegram.org/bots/api#sendsticker), *find_location* for [location data](https://core.telegram.org/bots/api#sendlocation), *record_video_note* or *upload_video_note* for [video notes](https://core.telegram.org/bots/api#sendvideonote)

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the action will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread or topic of a forum; for supergroups and private chats of bots with forum topic mode enabled only

## Usage

### As bot method

```
result: bool = await bot.send_chat_action(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_chat_action import SendChatAction`
- alias: `from aiogram.methods import SendChatAction`

#### With specific bot

```
result: bool = await bot(SendChatAction(...))
```

#### As reply into Webhook in handler

```
return SendChatAction(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.do()`](../types/chat.html#aiogram.types.chat.Chat.do "aiogram.types.chat.Chat.do")
