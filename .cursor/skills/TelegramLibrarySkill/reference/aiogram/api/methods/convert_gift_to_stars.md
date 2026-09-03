# convertGiftToStars

> Source: [https://docs.aiogram.dev/en/latest/api/methods/convert_gift_to_stars.html](https://docs.aiogram.dev/en/latest/api/methods/convert_gift_to_stars.html)

Returns: `bool`

*class* aiogram.methods.convert_gift_to_stars.ConvertGiftToStars(*\**, *business_connection_id: str*, *owned_gift_id: str*, *\*\*extra_data: Any*)
:   Converts a given regular gift to Telegram Stars. Requires the *can_convert_gifts_to_stars* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#convertgifttostars>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    owned_gift_id*: str*
    :   Unique identifier of the regular gift that should be converted to Telegram Stars

## Usage

### As bot method

```
result: bool = await bot.convert_gift_to_stars(...)
```

### Method as object

Imports:

- `from aiogram.methods.convert_gift_to_stars import ConvertGiftToStars`
- alias: `from aiogram.methods import ConvertGiftToStars`

#### With specific bot

```
result: bool = await bot(ConvertGiftToStars(...))
```

#### As reply into Webhook in handler

```
return ConvertGiftToStars(...)
```
