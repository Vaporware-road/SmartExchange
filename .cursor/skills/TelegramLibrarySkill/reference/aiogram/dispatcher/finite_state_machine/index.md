# Finite State Machine

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/index.html](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/index.html)

> A finite-state machine (FSM) or finite-state automaton (FSA, plural: automata), finite automaton,
> or simply a state machine, is a mathematical model of computation.
>
> It is an abstract machine that can be in exactly one of a finite number of states at any given time.
> The FSM can change from one state to another in response to some inputs;
> the change from one state to another is called a transition.
>
> An FSM is defined by a list of its states, its initial state,
> and the inputs that trigger each transition.
>
> ---
>
> Source: [WikiPedia](wiki)

## Usage example

Not all functionality of the bot can be implemented as single handler,
for example you will need to collect some data from user in separated steps you will need to use FSM.

Let’s see how to do that step-by-step

### Step by step

Before handle any states you will need to specify what kind of states you want to handle

```
class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()
```

And then write handler for each state separately from the start of dialog

Here is dialog can be started only via command `/start`, so lets handle it and make transition user to state `Form.name`

```
@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Hi there! What's your name?",
        reply_markup=ReplyKeyboardRemove(),
    )
```

After that you will need to save some data to the storage and make transition to next step.

```
@form_router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.like_bots)
    await message.answer(
        f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Yes"),
                    KeyboardButton(text="No"),
                ],
            ],
            resize_keyboard=True,
        ),
    )
```

At the next steps user can make different answers, it can be yes, no or any other

Handle `yes` and soon we need to handle `Form.language` state

```
@form_router.message(Form.like_bots, F.text.casefold() == "yes")
async def process_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.language)

    await message.reply(
        "Cool! I'm too!\nWhat programming language did you use for it?",
        reply_markup=ReplyKeyboardRemove(),
    )
```

Handle `no`

```
@form_router.message(Form.like_bots, F.text.casefold() == "no")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.clear()
    await message.answer(
        "Not bad not terrible.\nSee you soon.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await show_summary(message=message, data=data, positive=False)
```

And handle any other answers

```
@form_router.message(Form.like_bots)
async def process_unknown_write_bots(message: Message) -> None:
    await message.reply("I don't understand you :(")
```

All possible cases of like_bots step was covered, let’s implement finally step

```
@form_router.message(Form.language)
async def process_language(message: Message, state: FSMContext) -> None:
    data = await state.update_data(language=message.text)
    await state.clear()

    if message.text.casefold() == "python":
        await message.reply(
            "Python, you say? That's the language that makes my circuits light up! 😉",
        )

    await show_summary(message=message, data=data)
```

```
async def show_summary(message: Message, data: dict[str, Any], positive: bool = True) -> None:
    name = data["name"]
    language = data.get("language", "<something unexpected>")
    text = f"I'll keep in mind that, {html.quote(name)}, "
    text += (
        f"you like to write bots with {html.quote(language)}."
        if positive
        else "you don't like to write bots, so sad..."
    )
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
```

And now you have covered all steps from the image, but you can make possibility to cancel conversation, lets do that via command or text

```
@form_router.message(Command("cancel"))
@form_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )
```

### Complete example

```
  1import asyncio
  2import logging
  3import sys
  4from os import getenv
  5from typing import Any
  6
  7from aiogram import Bot, Dispatcher, F, Router, html
  8from aiogram.client.default import DefaultBotProperties
  9from aiogram.enums import ParseMode
 10from aiogram.filters import Command, CommandStart
 11from aiogram.fsm.context import FSMContext
 12from aiogram.fsm.state import State, StatesGroup
 13from aiogram.types import (
 14    KeyboardButton,
 15    Message,
 16    ReplyKeyboardMarkup,
 17    ReplyKeyboardRemove,
 18)
 19
 20TOKEN = getenv("BOT_TOKEN")
 21
 22form_router = Router()
 23
 24
 25class Form(StatesGroup):
 26    name = State()
 27    like_bots = State()
 28    language = State()
 29
 30
 31@form_router.message(CommandStart())
 32async def command_start(message: Message, state: FSMContext) -> None:
 33    await state.set_state(Form.name)
 34    await message.answer(
 35        "Hi there! What's your name?",
 36        reply_markup=ReplyKeyboardRemove(),
 37    )
 38
 39
 40@form_router.message(Command("cancel"))
 41@form_router.message(F.text.casefold() == "cancel")
 42async def cancel_handler(message: Message, state: FSMContext) -> None:
 43    """
 44    Allow user to cancel any action
 45    """
 46    current_state = await state.get_state()
 47    if current_state is None:
 48        return
 49
 50    logging.info("Cancelling state %r", current_state)
 51    await state.clear()
 52    await message.answer(
 53        "Cancelled.",
 54        reply_markup=ReplyKeyboardRemove(),
 55    )
 56
 57
 58@form_router.message(Form.name)
 59async def process_name(message: Message, state: FSMContext) -> None:
 60    await state.update_data(name=message.text)
 61    await state.set_state(Form.like_bots)
 62    await message.answer(
 63        f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
 64        reply_markup=ReplyKeyboardMarkup(
 65            keyboard=[
 66                [
 67                    KeyboardButton(text="Yes"),
 68                    KeyboardButton(text="No"),
 69                ],
 70            ],
 71            resize_keyboard=True,
 72        ),
 73    )
 74
 75
 76@form_router.message(Form.like_bots, F.text.casefold() == "no")
 77async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
 78    data = await state.get_data()
 79    await state.clear()
 80    await message.answer(
 81        "Not bad not terrible.\nSee you soon.",
 82        reply_markup=ReplyKeyboardRemove(),
 83    )
 84    await show_summary(message=message, data=data, positive=False)
 85
 86
 87@form_router.message(Form.like_bots, F.text.casefold() == "yes")
 88async def process_like_write_bots(message: Message, state: FSMContext) -> None:
 89    await state.set_state(Form.language)
 90
 91    await message.reply(
 92        "Cool! I'm too!\nWhat programming language did you use for it?",
 93        reply_markup=ReplyKeyboardRemove(),
 94    )
 95
 96
 97@form_router.message(Form.like_bots)
 98async def process_unknown_write_bots(message: Message) -> None:
 99    await message.reply("I don't understand you :(")
100
101
102@form_router.message(Form.language)
103async def process_language(message: Message, state: FSMContext) -> None:
104    data = await state.update_data(language=message.text)
105    await state.clear()
106
107    if message.text.casefold() == "python":
108        await message.reply(
109            "Python, you say? That's the language that makes my circuits light up! 😉",
110        )
111
112    await show_summary(message=message, data=data)
113
114
115async def show_summary(message: Message, data: dict[str, Any], positive: bool = True) -> None:
116    name = data["name"]
117    language = data.get("language", "<something unexpected>")
118    text = f"I'll keep in mind that, {html.quote(name)}, "
119    text += (
120        f"you like to write bots with {html.quote(language)}."
121        if positive
122        else "you don't like to write bots, so sad..."
123    )
124    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
125
126
127async def main() -> None:
128    # Initialize Bot instance with default bot properties which will be passed to all API calls
129    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
130
131    dp = Dispatcher()
132
133    dp.include_router(form_router)
134
135    # Start event dispatching
136    await dp.start_polling(bot)
137
138
139if __name__ == "__main__":
140    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
141    asyncio.run(main())
```

### Changing state for another user

In some cases, you might need to change the state for a user other than the one who triggered the current handler.
For example, you might want to change the state of a user based on an admin’s command.

To do this, you can use the `get_context` method of the FSM middleware through the dispatcher:

```
@example_router.message(Command("example"))
async def command_example(message: Message, dispatcher: Dispatcher, bot: Bot):
    user_id = ...  # Get the user ID in the way that you need
    state = dispatcher.fsm.get_context(
        bot=bot,
        chat_id=user_id,
        user_id=user_id,
    )

    # Now you can use the state context to change the state for the specified user
    await state.set_state(YourState.some_state)

    # Or store data in the state
    await state.update_data(some_key="some_value")

    # Or clear the state
    await state.clear()
```

This allows you to manage the state of any user in your bot, not just the one who triggered the current handler.

## Read more

- [Storages](storages.html)
  - [Storages out of the box](storages.html#storages-out-of-the-box)
    - [MemoryStorage](storages.html#memorystorage)
      - [`MemoryStorage`](storages.html#aiogram.fsm.storage.memory.MemoryStorage)
        - [`MemoryStorage.__init__()`](storages.html#aiogram.fsm.storage.memory.MemoryStorage.__init__)
    - [RedisStorage](storages.html#redisstorage)
    - [MongoStorage](storages.html#mongostorage)
    - [KeyBuilder](storages.html#keybuilder)
      - [`KeyBuilder`](storages.html#aiogram.fsm.storage.base.KeyBuilder)
        - [`KeyBuilder.build()`](storages.html#aiogram.fsm.storage.base.KeyBuilder.build)
      - [`DefaultKeyBuilder`](storages.html#aiogram.fsm.storage.base.DefaultKeyBuilder)
        - [`DefaultKeyBuilder.build()`](storages.html#aiogram.fsm.storage.base.DefaultKeyBuilder.build)
  - [Writing own storages](storages.html#writing-own-storages)
    - [`BaseStorage`](storages.html#aiogram.fsm.storage.base.BaseStorage)
      - [`BaseStorage.set_state()`](storages.html#aiogram.fsm.storage.base.BaseStorage.set_state)
      - [`BaseStorage.get_state()`](storages.html#aiogram.fsm.storage.base.BaseStorage.get_state)
      - [`BaseStorage.set_data()`](storages.html#aiogram.fsm.storage.base.BaseStorage.set_data)
      - [`BaseStorage.get_data()`](storages.html#aiogram.fsm.storage.base.BaseStorage.get_data)
      - [`BaseStorage.update_data()`](storages.html#aiogram.fsm.storage.base.BaseStorage.update_data)
      - [`BaseStorage.close()`](storages.html#aiogram.fsm.storage.base.BaseStorage.close)
- [Strategy](strategy.html)
  - [`FSMStrategy`](strategy.html#aiogram.fsm.strategy.FSMStrategy)
    - [`FSMStrategy.CHAT`](strategy.html#aiogram.fsm.strategy.FSMStrategy.CHAT)
    - [`FSMStrategy.CHAT_TOPIC`](strategy.html#aiogram.fsm.strategy.FSMStrategy.CHAT_TOPIC)
    - [`FSMStrategy.GLOBAL_USER`](strategy.html#aiogram.fsm.strategy.FSMStrategy.GLOBAL_USER)
    - [`FSMStrategy.USER_IN_CHAT`](strategy.html#aiogram.fsm.strategy.FSMStrategy.USER_IN_CHAT)
    - [`FSMStrategy.USER_IN_TOPIC`](strategy.html#aiogram.fsm.strategy.FSMStrategy.USER_IN_TOPIC)
- [Scenes Wizard](scene.html)
  - [Understanding Scenes](scene.html#understanding-scenes)
    - [Scene Lifecycle](scene.html#scene-lifecycle)
    - [Scene Listeners](scene.html#scene-listeners)
    - [Scene Interactions](scene.html#scene-interactions)
    - [Scene Benefits](scene.html#scene-benefits)
  - [How to use Scenes](scene.html#how-to-use-scenes)
  - [Components](scene.html#components)
    - [`Scene`](scene.html#aiogram.fsm.scene.Scene)
      - [`Scene.add_to_router()`](scene.html#aiogram.fsm.scene.Scene.add_to_router)
      - [`Scene.as_handler()`](scene.html#aiogram.fsm.scene.Scene.as_handler)
      - [`Scene.as_router()`](scene.html#aiogram.fsm.scene.Scene.as_router)
    - [`SceneRegistry`](scene.html#aiogram.fsm.scene.SceneRegistry)
      - [`SceneRegistry.add()`](scene.html#aiogram.fsm.scene.SceneRegistry.add)
      - [`SceneRegistry.get()`](scene.html#aiogram.fsm.scene.SceneRegistry.get)
      - [`SceneRegistry.register()`](scene.html#aiogram.fsm.scene.SceneRegistry.register)
    - [`ScenesManager`](scene.html#aiogram.fsm.scene.ScenesManager)
      - [`ScenesManager.close()`](scene.html#aiogram.fsm.scene.ScenesManager.close)
      - [`ScenesManager.enter()`](scene.html#aiogram.fsm.scene.ScenesManager.enter)
    - [`SceneConfig`](scene.html#aiogram.fsm.scene.SceneConfig)
      - [`SceneConfig.actions`](scene.html#aiogram.fsm.scene.SceneConfig.actions)
      - [`SceneConfig.attrs_resolver()`](scene.html#aiogram.fsm.scene.SceneConfig.attrs_resolver)
      - [`SceneConfig.callback_query_without_state`](scene.html#aiogram.fsm.scene.SceneConfig.callback_query_without_state)
      - [`SceneConfig.handlers`](scene.html#aiogram.fsm.scene.SceneConfig.handlers)
      - [`SceneConfig.reset_data_on_enter`](scene.html#aiogram.fsm.scene.SceneConfig.reset_data_on_enter)
      - [`SceneConfig.reset_history_on_enter`](scene.html#aiogram.fsm.scene.SceneConfig.reset_history_on_enter)
      - [`SceneConfig.state`](scene.html#aiogram.fsm.scene.SceneConfig.state)
    - [`SceneWizard`](scene.html#aiogram.fsm.scene.SceneWizard)
      - [`SceneWizard.back()`](scene.html#aiogram.fsm.scene.SceneWizard.back)
      - [`SceneWizard.clear_data()`](scene.html#aiogram.fsm.scene.SceneWizard.clear_data)
      - [`SceneWizard.enter()`](scene.html#aiogram.fsm.scene.SceneWizard.enter)
      - [`SceneWizard.exit()`](scene.html#aiogram.fsm.scene.SceneWizard.exit)
      - [`SceneWizard.get_data()`](scene.html#aiogram.fsm.scene.SceneWizard.get_data)
      - [`SceneWizard.goto()`](scene.html#aiogram.fsm.scene.SceneWizard.goto)
      - [`SceneWizard.leave()`](scene.html#aiogram.fsm.scene.SceneWizard.leave)
      - [`SceneWizard.retake()`](scene.html#aiogram.fsm.scene.SceneWizard.retake)
      - [`SceneWizard.set_data()`](scene.html#aiogram.fsm.scene.SceneWizard.set_data)
      - [`SceneWizard.update_data()`](scene.html#aiogram.fsm.scene.SceneWizard.update_data)
    - [Markers](scene.html#markers)
    - [How to enter the scene](scene.html#how-to-enter-the-scene)
