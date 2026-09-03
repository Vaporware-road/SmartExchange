# setBusinessAccountGiftSettings

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_business_account_gift_settings.html](https://docs.aiogram.dev/en/latest/api/methods/set_business_account_gift_settings.html)

Returns: `bool`

*class* aiogram.methods.set_business_account_gift_settings.SetBusinessAccountGiftSettings(*\**, *business_connection_id: str*, *show_gift_button: bool*, *accepted_gift_types: [AcceptedGiftTypes](../types/accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")*, *\*\*extra_data: Any*)
:   Changes the privacy settings pertaining to incoming gifts in a managed business account. Requires the *can_change_gift_settings* business bot right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setbusinessaccountgiftsettings>

    business_connection_id*: str*
    :   Unique identifier of the business connection

    show_gift_button*: bool*
    :   Pass `True` if a button for sending a gift to the user or by the business account must always be shown in the input field

    accepted_gift_types*: [AcceptedGiftTypes](../types/accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")*
    :   Types of gifts accepted by the business account

## Usage

### As bot method

```
result: bool = await bot.set_business_account_gift_settings(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_business_account_gift_settings import SetBusinessAccountGiftSettings`
- alias: `from aiogram.methods import SetBusinessAccountGiftSettings`

#### With specific bot

```
result: bool = await bot(SetBusinessAccountGiftSettings(...))
```

#### As reply into Webhook in handler

```
return SetBusinessAccountGiftSettings(...)
```
