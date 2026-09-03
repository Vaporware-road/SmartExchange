# Global defaults

> Source: [https://docs.aiogram.dev/en/latest/api/defaults.html](https://docs.aiogram.dev/en/latest/api/defaults.html)

aiogram provides mechanism to set some global defaults for all requests to Telegram Bot API
in your application using [`aiogram.client.default.DefaultBotProperties`](#aiogram.client.default.DefaultBotProperties "aiogram.client.default.DefaultBotProperties") class.

There are some properties that can be set:

*class* aiogram.client.default.DefaultBotProperties(*\**, *parse_mode: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_sending_without_reply: bool | None = None*, *link_preview: [LinkPreviewOptions](types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*, *link_preview_is_disabled: bool | None = None*, *link_preview_prefer_small_media: bool | None = None*, *link_preview_prefer_large_media: bool | None = None*, *link_preview_show_above_text: bool | None = None*, *show_caption_above_media: bool | None = None*)
:   Default bot properties.

    parse_mode*: str | None*
    :   Default parse mode for messages.

    disable_notification*: bool | None*
    :   Sends the message silently. Users will receive a notification with no sound.

    protect_content*: bool | None*
    :   Protects content from copying.

    allow_sending_without_reply*: bool | None*
    :   Allows to send messages without reply.

    link_preview*: [LinkPreviewOptions](types/link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None*
    :   Link preview settings.

    link_preview_is_disabled*: bool | None*
    :   Disables link preview.

    link_preview_prefer_small_media*: bool | None*
    :   Prefer small media in link preview.

    link_preview_prefer_large_media*: bool | None*
    :   Prefer large media in link preview.

    link_preview_show_above_text*: bool | None*
    :   Show link preview above text.

    show_caption_above_media*: bool | None*
    :   Show caption above media.

Note

If you need to override default properties for some requests, you should use aiogram.client.default.DefaultBotProperties
only for properties that you want to set as defaults and pass explicit values for other properties.

Danger

If you upgrading from aiogram 3.0-3.6 to 3.7,
you should update your code to use aiogram.client.default.DefaultBotProperties.

## Example

Here is an example of setting default parse mode for all requests to Telegram Bot API:

```
bot = Bot(
    token=...,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
)
```

In this case all messages sent by this bot will be parsed as HTML, so you don’t need to specify parse_mode
in every message you send.

Instead of

```
await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)
```

you can use

```
await bot.send_message(chat_id, text)
```

and the message will be sent with HTML parse mode.

In some cases you may want to override default properties for some requests. You can do it by passing
explicit values to the method:

```
await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN_V2)
```

In this case the message will be sent with Markdown parse mode instead of default HTML.

Another example of overriding default properties:

```
await bot.send_message(chat_id, text, parse_mode=None)
```

In this case the message will be send withoout parse mode, even if default parse mode is set it may be useful
if you want to send message with plain text or aiogram.types.message_entity.MessageEntity.

```
await bot.send_message(
    chat_id=chat_id,
    text=text,
    entities=[MessageEntity(type='bold', offset=0, length=4)],
    parse_mode=None
)
```
