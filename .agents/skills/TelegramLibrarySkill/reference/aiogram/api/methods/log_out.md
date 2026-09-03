# logOut

> Source: [https://docs.aiogram.dev/en/latest/api/methods/log_out.html](https://docs.aiogram.dev/en/latest/api/methods/log_out.html)

Returns: `bool`

*class* aiogram.methods.log_out.LogOut(*\*\*extra_data: Any*)
:   Use this method to log out from the cloud Bot API server before launching the bot locally. You **must** log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns `True` on success. Requires no parameters.

    Source: <https://core.telegram.org/bots/api#logout>

## Usage

### As bot method

```
result: bool = await bot.log_out(...)
```

### Method as object

Imports:

- `from aiogram.methods.log_out import LogOut`
- alias: `from aiogram.methods import LogOut`

#### With specific bot

```
result: bool = await bot(LogOut(...))
```

#### As reply into Webhook in handler

```
return LogOut(...)
```
