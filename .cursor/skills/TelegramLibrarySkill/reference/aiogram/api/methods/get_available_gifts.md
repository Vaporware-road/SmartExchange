# getAvailableGifts

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_available_gifts.html](https://docs.aiogram.dev/en/latest/api/methods/get_available_gifts.html)

Returns: `Gifts`

*class* aiogram.methods.get_available_gifts.GetAvailableGifts(*\*\*extra_data: Any*)
:   Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters. Returns a [`aiogram.types.gifts.Gifts`](../types/gifts.html#aiogram.types.gifts.Gifts "aiogram.types.gifts.Gifts") object.

    Source: <https://core.telegram.org/bots/api#getavailablegifts>

## Usage

### As bot method

```
result: Gifts = await bot.get_available_gifts(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_available_gifts import GetAvailableGifts`
- alias: `from aiogram.methods import GetAvailableGifts`

#### With specific bot

```
result: Gifts = await bot(GetAvailableGifts(...))
```
