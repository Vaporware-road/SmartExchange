# getMyShortDescription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_short_description.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_short_description.html)

Returns: `BotShortDescription`

*class* aiogram.methods.get_my_short_description.GetMyShortDescription(*\**, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current bot short description for the given user language. Returns [`aiogram.types.bot_short_description.BotShortDescription`](../types/bot_short_description.html#aiogram.types.bot_short_description.BotShortDescription "aiogram.types.bot_short_description.BotShortDescription") on success.

    Source: <https://core.telegram.org/bots/api#getmyshortdescription>

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code or an empty string

## Usage

### As bot method

```
result: BotShortDescription = await bot.get_my_short_description(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_short_description import GetMyShortDescription`
- alias: `from aiogram.methods import GetMyShortDescription`

#### With specific bot

```
result: BotShortDescription = await bot(GetMyShortDescription(...))
```
