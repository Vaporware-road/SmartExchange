# getUpdates

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_updates.html](https://docs.aiogram.dev/en/latest/api/methods/get_updates.html)

Returns: `list[Update]`

*class* aiogram.methods.get_updates.GetUpdates(*\**, *offset: int | None = None*, *limit: int | None = None*, *timeout: int | None = None*, *allowed_updates: list[str] | None = None*, *\*\*extra_data: Any*)
:   Use this method to receive incoming updates using long polling ([wiki](https://en.wikipedia.org/wiki/Push_technology#Long_polling)). Returns an Array of [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") objects.

    > **Notes**
    >
    > **1.** This method will not work if an outgoing webhook is set up.
    >
    > **2.** In order to avoid getting duplicate updates, recalculate *offset* after each server response.

    Source: <https://core.telegram.org/bots/api#getupdates>

    offset*: int | None*
    :   Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as [`aiogram.methods.get_updates.GetUpdates`](#aiogram.methods.get_updates.GetUpdates "aiogram.methods.get_updates.GetUpdates") is called with an *offset* higher than its *update_id*. The negative offset can be specified to retrieve updates starting from *-offset* update from the end of the updates queue. All previous updates will be forgotten

    limit*: int | None*
    :   Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100

    timeout*: int | None*
    :   Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only

    allowed_updates*: list[str] | None*
    :   A JSON-serialized list of the update types you want your bot to receive. For example, specify `["message", "edited_channel_post", "callback_query"]` to only receive updates of these types. See [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used

## Usage

### As bot method

```
result: list[Update] = await bot.get_updates(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_updates import GetUpdates`
- alias: `from aiogram.methods import GetUpdates`

#### With specific bot

```
result: list[Update] = await bot(GetUpdates(...))
```
