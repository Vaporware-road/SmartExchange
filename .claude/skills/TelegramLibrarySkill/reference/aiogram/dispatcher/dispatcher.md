# Dispatcher

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/dispatcher.html](https://docs.aiogram.dev/en/latest/dispatcher/dispatcher.html)

Dispatcher is root [`Router`](router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router") and in code Dispatcher can be used directly for routing updates or attach another routers into dispatcher.

Here is only listed base information about Dispatcher. All about writing handlers, filters and etc. you can find in next pages:

- [Router](router.html#router)
- [Filtering events](filters/index.html#filtering-events)

*class* aiogram.dispatcher.dispatcher.Dispatcher(*\**, *storage: [BaseStorage](finite_state_machine/storages.html#aiogram.fsm.storage.base.BaseStorage "aiogram.fsm.storage.base.BaseStorage") | None = None*, *fsm_strategy: [FSMStrategy](finite_state_machine/strategy.html#aiogram.fsm.strategy.FSMStrategy "aiogram.fsm.strategy.FSMStrategy") = FSMStrategy.USER_IN_CHAT*, *events_isolation: BaseEventIsolation | None = None*, *disable_fsm: bool = False*, *name: str | None = None*, *\*\*kwargs: Any*)
:   Root router

    __init__(*\**, *storage: [BaseStorage](finite_state_machine/storages.html#aiogram.fsm.storage.base.BaseStorage "aiogram.fsm.storage.base.BaseStorage") | None = None*, *fsm_strategy: [FSMStrategy](finite_state_machine/strategy.html#aiogram.fsm.strategy.FSMStrategy "aiogram.fsm.strategy.FSMStrategy") = FSMStrategy.USER_IN_CHAT*, *events_isolation: BaseEventIsolation | None = None*, *disable_fsm: bool = False*, *name: str | None = None*, *\*\*kwargs: Any*) → None
    :   Root router

        Parameters:
        :   - **storage** – Storage for FSM
            - **fsm_strategy** – FSM strategy
            - **events_isolation** – Events isolation
            - **disable_fsm** – Disable FSM, note that if you disable FSM
              then you should not use storage and events isolation
            - **kwargs** – Other arguments, will be passed as keyword arguments to handlers

    *async* feed_raw_update(*bot: Bot*, *update: dict[str, Any]*, *\*\*kwargs: Any*) → Any
    :   Main entry point for incoming updates with automatic Dict->Update serializer

        Parameters:
        :   - **bot**
            - **update**
            - **kwargs**

    *async* feed_update(*bot: Bot*, *update: [Update](../api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update")*, *\*\*kwargs: Any*) → Any
    :   Main entry point for incoming updates
        Response of this method can be used as Webhook response

        Parameters:
        :   - **bot**
            - **update**

    run_polling(*\*bots: Bot*, *polling_timeout: int = 10*, *handle_as_tasks: bool = True*, *backoff_config: BackoffConfig = BackoffConfig(min_delay=1.0, max_delay=5.0, factor=1.3, jitter=0.1)*, *allowed_updates: list[str] | UNSET_TYPE | None = sentinel.UNSET*, *handle_signals: bool = True*, *close_bot_session: bool = True*, *tasks_concurrency_limit: int | None = None*, *\*\*kwargs: Any*) → None
    :   Run many bots with polling

        Parameters:
        :   - **bots** – Bot instances (one or more)
            - **polling_timeout** – Long-polling wait time
            - **handle_as_tasks** – Run task for each event and no wait result
            - **backoff_config** – backoff-retry config
            - **allowed_updates** – List of the update types you want your bot to receive
            - **handle_signals** – handle signals (SIGINT/SIGTERM)
            - **close_bot_session** – close bot sessions on shutdown
            - **tasks_concurrency_limit** – Maximum number of concurrent updates to process
              (None = no limit), used only if handle_as_tasks is True
            - **kwargs** – contextual data

        Returns:

    *async* start_polling(*\*bots: Bot*, *polling_timeout: int = 10*, *handle_as_tasks: bool = True*, *backoff_config: BackoffConfig = BackoffConfig(min_delay=1.0, max_delay=5.0, factor=1.3, jitter=0.1)*, *allowed_updates: list[str] | UNSET_TYPE | None = sentinel.UNSET*, *handle_signals: bool = True*, *close_bot_session: bool = True*, *tasks_concurrency_limit: int | None = None*, *\*\*kwargs: Any*) → None
    :   Polling runner

        Parameters:
        :   - **bots** – Bot instances (one or more)
            - **polling_timeout** – Long-polling wait time
            - **handle_as_tasks** – Run task for each event and no wait result
            - **backoff_config** – backoff-retry config
            - **allowed_updates** – List of the update types you want your bot to receive
              By default, all used update types are enabled (resolved from handlers)
            - **handle_signals** – handle signals (SIGINT/SIGTERM)
            - **close_bot_session** – close bot sessions on shutdown
            - **tasks_concurrency_limit** – Maximum number of concurrent updates to process
              (None = no limit), used only if handle_as_tasks is True
            - **kwargs** – contextual data

        Returns:

    *async* stop_polling() → None
    :   Execute this method if you want to stop polling programmatically

        Returns:

## Simple usage

Example:

```
dp = Dispatcher()

@dp.message()
async def message_handler(message: types.Message) -> None:
    await SendMessage(chat_id=message.from_user.id, text=message.text)
```

Including routers

Example:

```
dp = Dispatcher()
router1 = Router()
dp.include_router(router1)
```

## Handling updates

All updates can be propagated to the dispatcher by [`feed_update()`](#aiogram.dispatcher.dispatcher.Dispatcher.feed_update "aiogram.dispatcher.dispatcher.Dispatcher.feed_update") method:

```
from aiogram import Bot, Dispatcher

async def update_handler(update: Update, bot: Bot, dispatcher: Dispatcher):
  result = await dp.feed_update(bot, update)
```

Also you can feed raw update (dictionary) object to the dispatcher by [`feed_raw_update()`](#aiogram.dispatcher.dispatcher.Dispatcher.feed_raw_update "aiogram.dispatcher.dispatcher.Dispatcher.feed_raw_update") method:

```
from aiogram import Bot, Dispatcher

async def update_handler(raw_update: dict[str, Any], bot: Bot, dispatcher: Dispatcher):
  result = await dp.feed_raw_update(bot, raw_update)
```
