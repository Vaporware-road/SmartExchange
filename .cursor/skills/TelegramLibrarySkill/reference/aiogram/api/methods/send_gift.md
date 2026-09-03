# sendGift

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_gift.html](https://docs.aiogram.dev/en/latest/api/methods/send_gift.html)

Returns: `bool`

*class* aiogram.methods.send_gift.SendGift(*\**, *gift_id: str*, *user_id: int | None = None*, *chat_id: int | str | None = None*, *pay_for_upgrade: bool | None = None*, *text: str | None = None*, *text_parse_mode: str | None = None*, *text_entities: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *\*\*extra_data: Any*)
:   Sends a gift to the given user or channel chat. The gift can’t be converted to Telegram Stars by the receiver. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#sendgift>

    gift_id*: str*
    :   Identifier of the gift; limited gifts can’t be sent to channel chats

    user_id*: int | None*
    :   Required if *chat_id* is not specified. Unique identifier of the target user who will receive the gift

    chat_id*: ChatIdUnion | None*
    :   Required if *user_id* is not specified. Unique identifier for the chat or username of the channel (in the format `@username`) that will receive the gift

    pay_for_upgrade*: bool | None*
    :   Pass `True` to pay for the gift upgrade from the bot’s balance, thereby making the upgrade free for the receiver

    text*: str | None*
    :   Text that will be shown along with the gift; 0-128 characters

    text_parse_mode*: str | None*
    :   Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Entities other than ‘bold’, ‘italic’, ‘underline’, ‘strikethrough’, ‘spoiler’, ‘custom_emoji’, and ‘date_time’ are ignored

    text_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than ‘bold’, ‘italic’, ‘underline’, ‘strikethrough’, ‘spoiler’, ‘custom_emoji’, and ‘date_time’ are ignored

## Usage

### As bot method

```
result: bool = await bot.send_gift(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_gift import SendGift`
- alias: `from aiogram.methods import SendGift`

#### With specific bot

```
result: bool = await bot(SendGift(...))
```

#### As reply into Webhook in handler

```
return SendGift(...)
```
