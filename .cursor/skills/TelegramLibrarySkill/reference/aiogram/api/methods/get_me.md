# getMe

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_me.html](https://docs.aiogram.dev/en/latest/api/methods/get_me.html)

Returns: `User`

*class* aiogram.methods.get_me.GetMe(*\*\*extra_data: Any*)
:   A simple method for testing your bot’s authentication token. Requires no parameters. Returns basic information about the bot in form of a [`aiogram.types.user.User`](../types/user.html#aiogram.types.user.User "aiogram.types.user.User") object.

    Source: <https://core.telegram.org/bots/api#getme>

## Usage

### As bot method

```
result: User = await bot.get_me(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_me import GetMe`
- alias: `from aiogram.methods import GetMe`

#### With specific bot

```
result: User = await bot(GetMe(...))
```
