# close

> Source: [https://docs.aiogram.dev/en/latest/api/methods/close.html](https://docs.aiogram.dev/en/latest/api/methods/close.html)

Returns: `bool`

*class* aiogram.methods.close.Close(*\*\*extra_data: Any*)
:   Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn’t launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns `True` on success. Requires no parameters.

    Source: <https://core.telegram.org/bots/api#close>

## Usage

### As bot method

```
result: bool = await bot.close(...)
```

### Method as object

Imports:

- `from aiogram.methods.close import Close`
- alias: `from aiogram.methods import Close`

#### With specific bot

```
result: bool = await bot(Close(...))
```

#### As reply into Webhook in handler

```
return Close(...)
```
