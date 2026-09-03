# getBusinessConnection

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_business_connection.html](https://docs.aiogram.dev/en/latest/api/methods/get_business_connection.html)

Returns: `BusinessConnection`

*class* aiogram.methods.get_business_connection.GetBusinessConnection(*\**, *business_connection_id: str*, *\*\*extra_data: Any*)
:   Use this method to get information about the connection of the bot with a business account. Returns a [`aiogram.types.business_connection.BusinessConnection`](../types/business_connection.html#aiogram.types.business_connection.BusinessConnection "aiogram.types.business_connection.BusinessConnection") object on success.

    Source: <https://core.telegram.org/bots/api#getbusinessconnection>

    business_connection_id*: str*
    :   Unique identifier of the business connection

## Usage

### As bot method

```
result: BusinessConnection = await bot.get_business_connection(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_business_connection import GetBusinessConnection`
- alias: `from aiogram.methods import GetBusinessConnection`

#### With specific bot

```
result: BusinessConnection = await bot(GetBusinessConnection(...))
```
