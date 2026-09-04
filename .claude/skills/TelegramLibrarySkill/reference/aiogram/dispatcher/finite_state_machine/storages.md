# Storages

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/storages.html](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/storages.html)

## Storages out of the box

### MemoryStorage

*class* aiogram.fsm.storage.memory.MemoryStorage
:   Default FSM storage; uses a regular `dict` to store data and
    does not persist it across restarts.

    Warning

    This storage is not recommended for production use, as all data is lost
    when the bot restarts

    __init__() → None

### RedisStorage

### MongoStorage

### KeyBuilder

Keys inside Redis and Mongo storages can be customized via key builders:

*class* aiogram.fsm.storage.base.KeyBuilder
:   Base class for key builder.

    *abstract* build(*key: StorageKey*, *part: Literal['data', 'state', 'lock'] | None = None*) → str
    :   Build key to be used in storage’s db queries

        Parameters:
        :   - **key** – contextual key
            - **part** – part of the record

        Returns:
        :   key to be used in storage’s db queries

*class* aiogram.fsm.storage.base.DefaultKeyBuilder(*\**, *prefix: str = 'fsm'*, *separator: str = ':'*, *with_bot_id: bool = False*, *with_business_connection_id: bool = False*, *with_destiny: bool = False*)
:   Simple key builder with default prefix.

    Generates a colon-joined string with prefix, chat_id, user_id,
    optional bot_id, business_connection_id, destiny and field.

    Format:
    :   `<prefix>:<bot_id?>:<business_connection_id?>:<chat_id>:<user_id>:<destiny?>:<field?>`

    build(*key: StorageKey*, *part: Literal['data', 'state', 'lock'] | None = None*) → str
    :   Build key to be used in storage’s db queries

        Parameters:
        :   - **key** – contextual key
            - **part** – part of the record

        Returns:
        :   key to be used in storage’s db queries

## Writing own storages

*class* aiogram.fsm.storage.base.BaseStorage
:   Base class for all FSM storages

    *abstract async* set_state(*key: StorageKey*, *state: str | State | None = None*) → None
    :   Set state for specified key

        Parameters:
        :   - **key** – storage key
            - **state** – new state

    *abstract async* get_state(*key: StorageKey*) → str | None
    :   Get key state

        Parameters:
        :   **key** – storage key

        Returns:
        :   current state

    *abstract async* set_data(*key: StorageKey*, *data: Mapping[str, Any]*) → None
    :   Write data (replace)

        Parameters:
        :   - **key** – storage key
            - **data** – new data

    *abstract async* get_data(*key: StorageKey*) → dict[str, Any]
    :   Get current data for key

        Parameters:
        :   **key** – storage key

        Returns:
        :   current data

    *async* update_data(*key: StorageKey*, *data: Mapping[str, Any]*) → dict[str, Any]
    :   Update date in the storage for key (like dict.update)

        Parameters:
        :   - **key** – storage key
            - **data** – partial data

        Returns:
        :   new data

    *abstract async* close() → None
    :   Close storage (database connection, file or etc.)
