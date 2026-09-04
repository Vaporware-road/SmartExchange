# getMyDescription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_description.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_description.html)

Returns: `BotDescription`

*class* aiogram.methods.get_my_description.GetMyDescription(*\**, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current bot description for the given user language. Returns [`aiogram.types.bot_description.BotDescription`](../types/bot_description.html#aiogram.types.bot_description.BotDescription "aiogram.types.bot_description.BotDescription") on success.

    Source: <https://core.telegram.org/bots/api#getmydescription>

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code or an empty string

## Usage

### As bot method

```
result: BotDescription = await bot.get_my_description(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_description import GetMyDescription`
- alias: `from aiogram.methods import GetMyDescription`

#### With specific bot

```
result: BotDescription = await bot(GetMyDescription(...))
```
