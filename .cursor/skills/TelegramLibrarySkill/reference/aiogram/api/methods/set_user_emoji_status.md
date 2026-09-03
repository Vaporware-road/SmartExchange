# setUserEmojiStatus

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_user_emoji_status.html](https://docs.aiogram.dev/en/latest/api/methods/set_user_emoji_status.html)

Returns: `bool`

*class* aiogram.methods.set_user_emoji_status.SetUserEmojiStatus(*\**, *user_id: int*, *emoji_status_custom_emoji_id: str | None = None*, *emoji_status_expiration_date: datetime | timedelta | int | None = None*, *\*\*extra_data: Any*)
:   Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method [requestEmojiStatusAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps). Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setuseremojistatus>

    user_id*: int*
    :   Unique identifier of the target user

    emoji_status_custom_emoji_id*: str | None*
    :   Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status

    emoji_status_expiration_date*: DateTimeUnion | None*
    :   Expiration date of the emoji status, if any

## Usage

### As bot method

```
result: bool = await bot.set_user_emoji_status(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_user_emoji_status import SetUserEmojiStatus`
- alias: `from aiogram.methods import SetUserEmojiStatus`

#### With specific bot

```
result: bool = await bot(SetUserEmojiStatus(...))
```

#### As reply into Webhook in handler

```
return SetUserEmojiStatus(...)
```
