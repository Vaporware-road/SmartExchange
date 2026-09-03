# Telegram object serialization

> Source: [https://docs.aiogram.dev/en/latest/utils/serialization.html](https://docs.aiogram.dev/en/latest/utils/serialization.html)

## Serialization

To serialize Python object to Telegram object you can use pydantic serialization methods, for example:

```
message_data = { ... }  # Some message data as dict
message = Message.model_validate(message_data)
```

If you want to bind serialized object to the Bot instance, you can use context:

```
message_data = { ... }  # Some message data as dict
message = Message.model_validate(message_data, context={"bot": bot})
```

## Deserialization

In cases when you need to deserialize Telegram object to Python object, you can use this module.

To convert Telegram object to Python object excluding files you can use
[`aiogram.utils.serialization.deserialize_telegram_object_to_python()`](#aiogram.utils.serialization.deserialize_telegram_object_to_python "aiogram.utils.serialization.deserialize_telegram_object_to_python") function.

aiogram.utils.serialization.deserialize_telegram_object_to_python(*obj: Any*, *default: [DefaultBotProperties](../api/defaults.html#aiogram.client.default.DefaultBotProperties "aiogram.client.default.DefaultBotProperties") | None = None*, *include_api_method_name: bool = True*) → Any
:   Deserialize telegram object to JSON compatible Python object excluding files.

    Parameters:
    :   - **obj** – The telegram object to be deserialized.
        - **default** – Default bot properties
          should be passed only if you want to use custom defaults.
        - **include_api_method_name** – Whether to include the API method name in the result.

    Returns:
    :   The deserialized telegram object.

To convert Telegram object to Python object including files you can use
[`aiogram.utils.serialization.deserialize_telegram_object()`](#aiogram.utils.serialization.deserialize_telegram_object "aiogram.utils.serialization.deserialize_telegram_object") function,
which returns [`aiogram.utils.serialization.DeserializedTelegramObject`](#aiogram.utils.serialization.DeserializedTelegramObject "aiogram.utils.serialization.DeserializedTelegramObject") object.

aiogram.utils.serialization.deserialize_telegram_object(*obj: Any*, *default: [DefaultBotProperties](../api/defaults.html#aiogram.client.default.DefaultBotProperties "aiogram.client.default.DefaultBotProperties") | None = None*, *include_api_method_name: bool = True*) → [DeserializedTelegramObject](#aiogram.utils.serialization.DeserializedTelegramObject "aiogram.utils.serialization.DeserializedTelegramObject")
:   Deserialize Telegram Object to JSON compatible Python object.

    Parameters:
    :   - **obj** – The object to be deserialized.
        - **default** – Default bot properties
          should be passed only if you want to use custom defaults.
        - **include_api_method_name** – Whether to include the API method name in the result.

    Returns:
    :   The deserialized Telegram object.

*class* aiogram.utils.serialization.DeserializedTelegramObject(*data: Any*, *files: dict[str, [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")]*)
:   Represents a dumped Telegram object.

    Parameters:
    :   - **data** (*Any*) – The dumped data of the Telegram object.
        - **files** (*dict**[**str**,* [*InputFile*](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*]*) – The dictionary containing the file names as keys
          and the corresponding InputFile objects as values.
