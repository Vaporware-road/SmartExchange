# setMyDescription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_description.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_description.html)

Returns: `bool`

*class* aiogram.methods.set_my_description.SetMyDescription(*\**, *description: str | None = None*, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the bot’s description, which is shown in the chat with the bot if the chat is empty. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmydescription>

    description*: str | None*
    :   New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description

## Usage

### As bot method

```
result: bool = await bot.set_my_description(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_description import SetMyDescription`
- alias: `from aiogram.methods import SetMyDescription`

#### With specific bot

```
result: bool = await bot(SetMyDescription(...))
```

#### As reply into Webhook in handler

```
return SetMyDescription(...)
```
