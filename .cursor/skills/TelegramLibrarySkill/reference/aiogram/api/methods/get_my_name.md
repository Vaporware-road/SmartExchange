# getMyName

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_name.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_name.html)

Returns: `BotName`

*class* aiogram.methods.get_my_name.GetMyName(*\**, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current bot name for the given user language. Returns [`aiogram.types.bot_name.BotName`](../types/bot_name.html#aiogram.types.bot_name.BotName "aiogram.types.bot_name.BotName") on success.

    Source: <https://core.telegram.org/bots/api#getmyname>

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code or an empty string

## Usage

### As bot method

```
result: BotName = await bot.get_my_name(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_name import GetMyName`
- alias: `from aiogram.methods import GetMyName`

#### With specific bot

```
result: BotName = await bot(GetMyName(...))
```
