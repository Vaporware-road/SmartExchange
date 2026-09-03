# getUserChatBoosts

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_user_chat_boosts.html](https://docs.aiogram.dev/en/latest/api/methods/get_user_chat_boosts.html)

Returns: `UserChatBoosts`

*class* aiogram.methods.get_user_chat_boosts.GetUserChatBoosts(*\**, *chat_id: int | str*, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a [`aiogram.types.user_chat_boosts.UserChatBoosts`](../types/user_chat_boosts.html#aiogram.types.user_chat_boosts.UserChatBoosts "aiogram.types.user_chat_boosts.UserChatBoosts") object.

    Source: <https://core.telegram.org/bots/api#getuserchatboosts>

    chat_id*: int | str*
    :   Unique identifier for the chat or username of the channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

## Usage

### As bot method

```
result: UserChatBoosts = await bot.get_user_chat_boosts(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_user_chat_boosts import GetUserChatBoosts`
- alias: `from aiogram.methods import GetUserChatBoosts`

#### With specific bot

```
result: UserChatBoosts = await bot(GetUserChatBoosts(...))
```
