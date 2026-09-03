# setMyName

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_name.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_name.html)

Returns: `bool`

*class* aiogram.methods.set_my_name.SetMyName(*\**, *name: str | None = None*, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the bot’s name. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmyname>

    name*: str | None*
    :   New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name

## Usage

### As bot method

```
result: bool = await bot.set_my_name(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_name import SetMyName`
- alias: `from aiogram.methods import SetMyName`

#### With specific bot

```
result: bool = await bot(SetMyName(...))
```

#### As reply into Webhook in handler

```
return SetMyName(...)
```
