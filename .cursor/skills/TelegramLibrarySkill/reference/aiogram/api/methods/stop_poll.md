# stopPoll

> Source: [https://docs.aiogram.dev/en/latest/api/methods/stop_poll.html](https://docs.aiogram.dev/en/latest/api/methods/stop_poll.html)

Returns: `Poll`

*class* aiogram.methods.stop_poll.StopPoll(*\**, *chat_id: int | str*, *message_id: int*, *business_connection_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Use this method to stop a poll which was sent by the bot. On success, the stopped [`aiogram.types.poll.Poll`](../types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") is returned.

    Source: <https://core.telegram.org/bots/api#stoppoll>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`

    message_id*: int*
    :   Identifier of the original message with the poll

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message to be edited was sent

    reply_markup*: [InlineKeyboardMarkup](../types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   A JSON-serialized object for a new message [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

## Usage

### As bot method

```
result: Poll = await bot.stop_poll(...)
```

### Method as object

Imports:

- `from aiogram.methods.stop_poll import StopPoll`
- alias: `from aiogram.methods import StopPoll`

#### With specific bot

```
result: Poll = await bot(StopPoll(...))
```

#### As reply into Webhook in handler

```
return StopPoll(...)
```
