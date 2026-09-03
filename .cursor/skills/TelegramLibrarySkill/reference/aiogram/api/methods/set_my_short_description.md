# setMyShortDescription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_short_description.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_short_description.html)

Returns: `bool`

*class* aiogram.methods.set_my_short_description.SetMyShortDescription(*\**, *short_description: str | None = None*, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the bot’s short description, which is shown on the bot’s profile page and is sent together with the link when users share the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmyshortdescription>

    short_description*: str | None*
    :   New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description

## Usage

### As bot method

```
result: bool = await bot.set_my_short_description(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_short_description import SetMyShortDescription`
- alias: `from aiogram.methods import SetMyShortDescription`

#### With specific bot

```
result: bool = await bot(SetMyShortDescription(...))
```

#### As reply into Webhook in handler

```
return SetMyShortDescription(...)
```
