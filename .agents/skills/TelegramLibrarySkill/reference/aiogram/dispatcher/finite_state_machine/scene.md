# Scenes Wizard

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/scene.html](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/scene.html)

Added in version 3.2.

Warning

This feature is experimental and may be changed in future versions.

**aiogram’s** basics API is easy to use and powerful,
allowing the implementation of simple interactions such as triggering a command or message
for a response.
However, certain tasks require a dialogue between the user and the bot.
This is where Scenes come into play.

## Understanding Scenes

A Scene in **aiogram** is like an abstract, isolated namespace or room that a user can be
ushered into via the code. When a user is within a Scene, most other global commands or
message handlers are bypassed, unless they are specifically designed to function outside of the Scenes.
This helps in creating an experience of focused interactions.
Scenes provide a structure for more complex interactions,
effectively isolating and managing contexts for different stages of the conversation.
They allow you to control and manage the flow of the conversation in a more organized manner.

### Scene Lifecycle

Each Scene can be “entered”, “left” or “exited”, allowing for clear transitions between different
stages of the conversation.
For instance, in a multi-step form filling interaction, each step could be a Scene -
the bot guides the user from one Scene to the next as they provide the required information.

### Scene Listeners

Scenes have their own hooks which are command or message listeners that only act while
the user is within the Scene.
These hooks react to user actions while the user is ‘inside’ the Scene,
providing the responses or actions appropriate for that context.
When the user is ushered from one Scene to another, the actions and responses change
accordingly as the user is now interacting with the set of listeners inside the new Scene.
These ‘Scene-specific’ hooks or listeners, detached from the global listening context,
allow for more streamlined and organized bot-user interactions.

### Scene Interactions

Each Scene is like a self-contained world, with interactions defined within the scope of that Scene.
As such, only the handlers defined within the specific Scene will react to user’s input during
the lifecycle of that Scene.

### Scene Benefits

Scenes can help manage more complex interaction workflows and enable more interactive and dynamic
dialogs between the user and the bot.
This offers great flexibility in handling multi-step interactions or conversations with the users.

## How to use Scenes

For example we have a quiz bot, which asks the user a series of questions and then displays the results.

Lets start with the data models, in this example simple data models are used to represent
the questions and answers, in real life you would probably use a database to store the data.

Questions list

```
@dataclass
class Answer:
    """
    Represents an answer to a question.
    """

    text: str
    """The answer text"""
    is_correct: bool = False
    """Indicates if the answer is correct"""

@dataclass
class Question:
    """
    Class representing a quiz with a question and a list of answers.
    """

    text: str
    """The question text"""
    answers: list[Answer]
    """List of answers"""

    correct_answer: str = field(init=False)

    def __post_init__(self):
        self.correct_answer = next(answer.text for answer in self.answers if answer.is_correct)

# Fake data, in real application you should use a database or something else
QUESTIONS = [
    Question(
        text="What is the capital of France?",
        answers=[
            Answer("Paris", is_correct=True),
            Answer("London"),
            Answer("Berlin"),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of Spain?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin"),
            Answer("Madrid", is_correct=True),
        ],
    ),
    Question(
        text="What is the capital of Germany?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin", is_correct=True),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of England?",
        answers=[
            Answer("Paris"),
            Answer("London", is_correct=True),
            Answer("Berlin"),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of Italy?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin"),
            Answer("Rome", is_correct=True),
        ],
    ),
]
```

Then, we need to create a Scene class that will represent the quiz game scene:

Note

Keyword argument passed into class definition describes the scene name - is the same as state of the scene.

Quiz Scene

```
class QuizScene(Scene, state="quiz"):
    """
    This class represents a scene for a quiz game.

    It inherits from Scene class and is associated with the state "quiz".
    It handles the logic and flow of the quiz game.
    """
```

Also we need to define a handler that helps to start the quiz game:

Start command handler

```
quiz_router = Router(name=__name__)
# Add handler that initializes the scene
quiz_router.message.register(QuizScene.as_handler(), Command("quiz"))
```

Once the scene is defined, we need to register it in the SceneRegistry:

Registering the scene

```
def create_dispatcher() -> Dispatcher:
    # Event isolation is needed to correctly handle fast user responses
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    dispatcher.include_router(quiz_router)

    # To use scenes, you should create a SceneRegistry and register your scenes there
    scene_registry = SceneRegistry(dispatcher)
    # ... and then register a scene in the registry
    # by default, Scene will be mounted to the router that passed to the SceneRegistry,
    # but you can specify the router explicitly using the `router` argument
    scene_registry.add(QuizScene)

    return dispatcher
```

So, now we can implement the quiz game logic, each question is sent to the user one by one,
and the user’s answer is checked at the end of all questions.

Now we need to write an entry point for the question handler:

Question handler entry point

```
    @on.message.enter()
    async def on_enter(self, message: Message, state: FSMContext, step: int | None = 0) -> Any:
        """
        Method triggered when the user enters the quiz scene.

        It displays the current question and answer options to the user.

        :param message:
        :param state:
        :param step: Scene argument, can be passed to the scene using the wizard
        :return:
        """
        if not step:
            # This is the first step, so we should greet the user
            await message.answer("Welcome to the quiz!")

        try:
            quiz = QUESTIONS[step]
        except IndexError:
            # This error means that the question's list is over
            return await self.wizard.exit()

        markup = ReplyKeyboardBuilder()
        markup.add(*[KeyboardButton(text=answer.text) for answer in quiz.answers])

        if step > 0:
            markup.button(text="🔙 Back")
        markup.button(text="🚫 Exit")

        await state.update_data(step=step)
        return await message.answer(
            text=QUESTIONS[step].text,
            reply_markup=markup.adjust(2).as_markup(resize_keyboard=True),
        )
```

Once scene is entered, we should expect the user’s answer, so we need to write a handler for it,
this handler should expect the text message, save the answer and retake
the question handler for the next question:

Answer handler

```
    @on.message(F.text)
    async def answer(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user selects an answer.

        It stores the answer and proceeds to the next question.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        step = data["step"]
        answers = data.get("answers", {})
        answers[step] = message.text
        await state.update_data(answers=answers)

        await self.wizard.retake(step=step + 1)
```

When user answer with unknown message, we should expect the text message again:

Unknown message handler

```
    @on.message()
    async def unknown_message(self, message: Message) -> None:
        """
        Method triggered when the user sends a message that is not a command or an answer.

        It asks the user to select an answer.

        :param message: The message received from the user.
        :return: None
        """
        await message.answer("Please select an answer.")
```

When all questions are answered, we should show the results to the user, as you can see in the code below,
we use await self.wizard.exit() to exit from the scene when questions list is over in the QuizScene.on_enter handler.

Thats means that we need to write an exit handler to show the results to the user:

Show results handler

```
    @on.message.exit()
    async def on_exit(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user exits the quiz scene.

        It calculates the user's answers, displays the summary, and clears the stored answers.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        answers = data.get("answers", {})

        correct = 0
        incorrect = 0
        user_answers = []
        for step, quiz in enumerate(QUESTIONS):
            answer = answers.get(step)
            is_correct = answer == quiz.correct_answer
            if is_correct:
                correct += 1
                icon = "✅"
            else:
                incorrect += 1
                icon = "❌"
            if answer is None:
                answer = "no answer"
            user_answers.append(f"{quiz.text} ({icon} {html.quote(answer)})")

        content = as_list(
            as_section(
                Bold("Your answers:"),
                as_numbered_list(*user_answers),
            ),
            "",
            as_section(
                Bold("Summary:"),
                as_list(
                    as_key_value("Correct", correct),
                    as_key_value("Incorrect", incorrect),
                ),
            ),
        )

        await message.answer(**content.as_kwargs(), reply_markup=ReplyKeyboardRemove())
        await state.set_data({})
```

Also we can implement a actions to exit from the quiz game or go back to the previous question:

Exit handler

```
    @on.message(F.text == "🚫 Exit")
    async def exit(self, message: Message) -> None:
        """
        Method triggered when the user selects the "Exit" button.

        It exits the quiz.

        :param message:
        :return:
        """
        await self.wizard.exit()
```

Back handler

```
    @on.message(F.text == "🔙 Back")
    async def back(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user selects the "Back" button.

        It allows the user to go back to the previous question.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        step = data["step"]

        previous_step = step - 1
        if previous_step < 0:
            # In case when the user tries to go back from the first question,
            # we just exit the quiz
            return await self.wizard.exit()
        return await self.wizard.back(step=previous_step)
```

Now we can run the bot and test the quiz game:

Run the bot

```
async def main() -> None:
    dp = create_dispatcher()
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Alternatively, you can use aiogram-cli:
    # `aiogram run polling quiz_scene:create_dispatcher --log-level info --token BOT_TOKEN`
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

Complete them all

Quiz Example

```
import asyncio
import logging
from dataclasses import dataclass, field
from os import getenv
from typing import Any

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.types import KeyboardButton, Message, ReplyKeyboardRemove
from aiogram.utils.formatting import (
    Bold,
    as_key_value,
    as_list,
    as_numbered_list,
    as_section,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = getenv("BOT_TOKEN")

@dataclass
class Answer:
    """
    Represents an answer to a question.
    """

    text: str
    """The answer text"""
    is_correct: bool = False
    """Indicates if the answer is correct"""

@dataclass
class Question:
    """
    Class representing a quiz with a question and a list of answers.
    """

    text: str
    """The question text"""
    answers: list[Answer]
    """List of answers"""

    correct_answer: str = field(init=False)

    def __post_init__(self):
        self.correct_answer = next(answer.text for answer in self.answers if answer.is_correct)

# Fake data, in real application you should use a database or something else
QUESTIONS = [
    Question(
        text="What is the capital of France?",
        answers=[
            Answer("Paris", is_correct=True),
            Answer("London"),
            Answer("Berlin"),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of Spain?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin"),
            Answer("Madrid", is_correct=True),
        ],
    ),
    Question(
        text="What is the capital of Germany?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin", is_correct=True),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of England?",
        answers=[
            Answer("Paris"),
            Answer("London", is_correct=True),
            Answer("Berlin"),
            Answer("Madrid"),
        ],
    ),
    Question(
        text="What is the capital of Italy?",
        answers=[
            Answer("Paris"),
            Answer("London"),
            Answer("Berlin"),
            Answer("Rome", is_correct=True),
        ],
    ),
]

class QuizScene(Scene, state="quiz"):
    """
    This class represents a scene for a quiz game.

    It inherits from Scene class and is associated with the state "quiz".
    It handles the logic and flow of the quiz game.
    """

    @on.message.enter()
    async def on_enter(self, message: Message, state: FSMContext, step: int | None = 0) -> Any:
        """
        Method triggered when the user enters the quiz scene.

        It displays the current question and answer options to the user.

        :param message:
        :param state:
        :param step: Scene argument, can be passed to the scene using the wizard
        :return:
        """
        if not step:
            # This is the first step, so we should greet the user
            await message.answer("Welcome to the quiz!")

        try:
            quiz = QUESTIONS[step]
        except IndexError:
            # This error means that the question's list is over
            return await self.wizard.exit()

        markup = ReplyKeyboardBuilder()
        markup.add(*[KeyboardButton(text=answer.text) for answer in quiz.answers])

        if step > 0:
            markup.button(text="🔙 Back")
        markup.button(text="🚫 Exit")

        await state.update_data(step=step)
        return await message.answer(
            text=QUESTIONS[step].text,
            reply_markup=markup.adjust(2).as_markup(resize_keyboard=True),
        )

    @on.message.exit()
    async def on_exit(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user exits the quiz scene.

        It calculates the user's answers, displays the summary, and clears the stored answers.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        answers = data.get("answers", {})

        correct = 0
        incorrect = 0
        user_answers = []
        for step, quiz in enumerate(QUESTIONS):
            answer = answers.get(step)
            is_correct = answer == quiz.correct_answer
            if is_correct:
                correct += 1
                icon = "✅"
            else:
                incorrect += 1
                icon = "❌"
            if answer is None:
                answer = "no answer"
            user_answers.append(f"{quiz.text} ({icon} {html.quote(answer)})")

        content = as_list(
            as_section(
                Bold("Your answers:"),
                as_numbered_list(*user_answers),
            ),
            "",
            as_section(
                Bold("Summary:"),
                as_list(
                    as_key_value("Correct", correct),
                    as_key_value("Incorrect", incorrect),
                ),
            ),
        )

        await message.answer(**content.as_kwargs(), reply_markup=ReplyKeyboardRemove())
        await state.set_data({})

    @on.message(F.text == "🔙 Back")
    async def back(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user selects the "Back" button.

        It allows the user to go back to the previous question.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        step = data["step"]

        previous_step = step - 1
        if previous_step < 0:
            # In case when the user tries to go back from the first question,
            # we just exit the quiz
            return await self.wizard.exit()
        return await self.wizard.back(step=previous_step)

    @on.message(F.text == "🚫 Exit")
    async def exit(self, message: Message) -> None:
        """
        Method triggered when the user selects the "Exit" button.

        It exits the quiz.

        :param message:
        :return:
        """
        await self.wizard.exit()

    @on.message(F.text)
    async def answer(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user selects an answer.

        It stores the answer and proceeds to the next question.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        step = data["step"]
        answers = data.get("answers", {})
        answers[step] = message.text
        await state.update_data(answers=answers)

        await self.wizard.retake(step=step + 1)

    @on.message()
    async def unknown_message(self, message: Message) -> None:
        """
        Method triggered when the user sends a message that is not a command or an answer.

        It asks the user to select an answer.

        :param message: The message received from the user.
        :return: None
        """
        await message.answer("Please select an answer.")

quiz_router = Router(name=__name__)
# Add handler that initializes the scene
quiz_router.message.register(QuizScene.as_handler(), Command("quiz"))

@quiz_router.message(Command("start"))
async def command_start(message: Message, scenes: ScenesManager) -> None:
    await scenes.close()
    await message.answer(
        "Hi! This is a quiz bot. To start the quiz, use the /quiz command.",
        reply_markup=ReplyKeyboardRemove(),
    )

def create_dispatcher() -> Dispatcher:
    # Event isolation is needed to correctly handle fast user responses
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    dispatcher.include_router(quiz_router)

    # To use scenes, you should create a SceneRegistry and register your scenes there
    scene_registry = SceneRegistry(dispatcher)
    # ... and then register a scene in the registry
    # by default, Scene will be mounted to the router that passed to the SceneRegistry,
    # but you can specify the router explicitly using the `router` argument
    scene_registry.add(QuizScene)

    return dispatcher

async def main() -> None:
    dp = create_dispatcher()
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Alternatively, you can use aiogram-cli:
    # `aiogram run polling quiz_scene:create_dispatcher --log-level info --token BOT_TOKEN`
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

## Components

- [`aiogram.fsm.scene.Scene`](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene") - represents a scene, contains handlers
- [`aiogram.fsm.scene.SceneRegistry`](#aiogram.fsm.scene.SceneRegistry "aiogram.fsm.scene.SceneRegistry") - container for all scenes in the bot, used to register scenes and resolve them by name
- [`aiogram.fsm.scene.ScenesManager`](#aiogram.fsm.scene.ScenesManager "aiogram.fsm.scene.ScenesManager") - manages scenes for each user, used to enter, leave and resolve current scene for user
- [`aiogram.fsm.scene.SceneConfig`](#aiogram.fsm.scene.SceneConfig "aiogram.fsm.scene.SceneConfig") - scene configuration, used to configure scene
- [`aiogram.fsm.scene.SceneWizard`](#aiogram.fsm.scene.SceneWizard "aiogram.fsm.scene.SceneWizard") - scene wizard, used to interact with user in scene from active scene handler
- Markers - marker for scene handlers, used to mark scene handlers

*class* aiogram.fsm.scene.Scene(*wizard: [SceneWizard](#aiogram.fsm.scene.SceneWizard "aiogram.fsm.scene.SceneWizard")*)
:   Represents a scene in a conversation flow.

    A scene is a specific state in a conversation where certain actions can take place.

    Each scene has a set of filters that determine when it should be triggered,
    and a set of handlers that define the actions to be executed when the scene is active.

    Note

    This class is not meant to be used directly. Instead, it should be subclassed
    to define custom scenes.

    *classmethod* add_to_router(*router: [Router](../router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")*) → None
    :   Adds the scene to the given router.

        Parameters:
        :   **router**

        Returns:

    *classmethod* as_handler(*\*\*handler_kwargs: Any*) → Callable[[...], Any]
    :   Create an entry point handler for the scene, can be used to simplify the handler
        that starts the scene.

        ```
        >>> router.message.register(MyScene.as_handler(), Command("start"))
        ```

    *classmethod* as_router(*name: str | None = None*) → [Router](../router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")
    :   Returns the scene as a router.

        Returns:
        :   new router

*class* aiogram.fsm.scene.SceneRegistry(*router: [Router](../router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")*, *register_on_add: bool = True*)
:   A class that represents a registry for scenes in a Telegram bot.

    add(*\*scenes: type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")]*, *router: [Router](../router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router") | None = None*) → None
    :   This method adds the specified scenes to the registry
        and optionally registers it to the router.

        If a scene with the same state already exists in the registry, a SceneException is raised.

        Warning

        If the router is not specified, the scenes will not be registered to the router.
        You will need to include the scenes manually to the router or use the register method.

        Parameters:
        :   - **scenes** – A variable length parameter that accepts one or more types of scenes.
              These scenes are instances of the Scene class.
            - **router** – An optional parameter that specifies the router
              to which the scenes should be added.

        Returns:
        :   None

    get(*scene: type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")] | State | str | None*) → type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")]
    :   This method returns the registered Scene object for the specified scene.
        The scene parameter can be either a Scene object, State object or a string representing
        the name of the scene. If a Scene object is provided, the state attribute
        of the SceneConfig object associated with the Scene object will be used as the scene name.
        If a State object is provided, the state attribute of the State object will be used as the
        scene name. If None or an invalid type is provided, a SceneException will be raised.

        If the specified scene is not registered in the SceneRegistry object,
        a SceneException will be raised.

        Parameters:
        :   **scene** – A Scene object, State object or a string representing the name of the scene.

        Returns:
        :   The registered Scene object corresponding to the given scene parameter.

    register(*\*scenes: type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")]*) → None
    :   Registers one or more scenes to the SceneRegistry.

        Parameters:
        :   **scenes** – One or more scene classes to register.

        Returns:
        :   None

*class* aiogram.fsm.scene.ScenesManager(*registry: [SceneRegistry](#aiogram.fsm.scene.SceneRegistry "aiogram.fsm.scene.SceneRegistry")*, *update_type: str*, *event: TelegramObject*, *state: FSMContext*, *data: dict[str, Any]*)
:   The ScenesManager class is responsible for managing scenes in an application.
    It provides methods for entering and exiting scenes, as well as retrieving the active scene.

    *async* close(*\*\*kwargs: Any*) → None
    :   Close method is used to exit the currently active scene in the ScenesManager.

        Parameters:
        :   **kwargs** – Additional keyword arguments passed to the scene’s exit method.

        Returns:
        :   None

    *async* enter(*scene_type: type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")] | State | str | None*, *_check_active: bool = True*, *\*\*kwargs: Any*) → None
    :   Enters the specified scene.

        Parameters:
        :   - **scene_type** – Optional Type[Scene], State or str representing the scene type to enter.
            - **_check_active** – Optional bool indicating whether to check if
              there is an active scene to exit before entering the new scene. Defaults to True.
            - **kwargs** – Additional keyword arguments to pass to the scene’s wizard.enter() method.

        Returns:
        :   None

*class* aiogram.fsm.scene.SceneConfig(*state: 'str | None'*, *handlers: 'list[HandlerContainer]'*, *actions: 'dict[SceneAction*, *dict[str*, *CallableObject]]'*, *reset_data_on_enter: 'bool | None' = None*, *reset_history_on_enter: 'bool | None' = None*, *callback_query_without_state: 'bool | None' = None*, *attrs_resolver: 'ClassAttrsResolver' = <function get_sorted_mro_attrs_resolver at 0x11f10fce0>*)
:   actions*: dict[SceneAction, dict[str, CallableObject]]*
    :   Scene actions

    attrs_resolver() → Generator[tuple[str, Any], None, None]
    :   Attributes resolver.

        Danger

        This attribute should only be changed when you know what you are doing.

        Added in version 3.19.0.

    callback_query_without_state*: bool | None* *= None*
    :   Allow callback query without state

    handlers*: list[HandlerContainer]*
    :   Scene handlers

    reset_data_on_enter*: bool | None* *= None*
    :   Reset scene data on enter

    reset_history_on_enter*: bool | None* *= None*
    :   Reset scene history on enter

    state*: str | None*
    :   Scene state

*class* aiogram.fsm.scene.SceneWizard(*scene_config: [SceneConfig](#aiogram.fsm.scene.SceneConfig "aiogram.fsm.scene.SceneConfig")*, *manager: [ScenesManager](#aiogram.fsm.scene.ScenesManager "aiogram.fsm.scene.ScenesManager")*, *state: FSMContext*, *update_type: str*, *event: TelegramObject*, *data: dict[str, Any]*)
:   A class that represents a wizard for managing scenes in a Telegram bot.

    Instance of this class is passed to each scene as a parameter.
    So, you can use it to transition between scenes, get and set data, etc.

    Note

    This class is not meant to be used directly. Instead, it should be used
    as a parameter in the scene constructor.

    *async* back(*\*\*kwargs: Any*) → None
    :   This method is used to go back to the previous scene.

        Parameters:
        :   **kwargs** – Keyword arguments that can be passed to the method.

        Returns:
        :   None

    *async* clear_data() → None
    :   Clears the data.

        Returns:
        :   None

    *async* enter(*\*\*kwargs: Any*) → None
    :   Enter method is used to transition into a scene in the SceneWizard class.
        It sets the state, clears data and history if specified,
        and triggers entering event of the scene.

        Parameters:
        :   **kwargs** – Additional keyword arguments.

        Returns:
        :   None

    *async* exit(*\*\*kwargs: Any*) → None
    :   Exit the current scene and enter the default scene/state.

        Parameters:
        :   **kwargs** – Additional keyword arguments.

        Returns:
        :   None

    *async* get_data() → dict[str, Any]
    :   This method returns the data stored in the current state.

        Returns:
        :   A dictionary containing the data stored in the scene state.

    *async* goto(*scene: type[[Scene](#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")] | State | str*, *\*\*kwargs: Any*) → None
    :   The goto method transitions to a new scene.
        It first calls the leave method to perform any necessary cleanup
        in the current scene, then calls the enter event to enter the specified scene.

        Parameters:
        :   - **scene** – The scene to transition to. Can be either a Scene instance
              State instance or a string representing the scene.
            - **kwargs** – Additional keyword arguments to pass to the enter
              method of the scene manager.

        Returns:
        :   None

    *async* leave(*_with_history: bool = True*, *\*\*kwargs: Any*) → None
    :   Leaves the current scene.
        This method is used to exit a scene and transition to the next scene.

        Parameters:
        :   - **_with_history** – Whether to include history in the snapshot. Defaults to True.
            - **kwargs** – Additional keyword arguments.

        Returns:
        :   None

    *async* retake(*\*\*kwargs: Any*) → None
    :   This method allows to re-enter the current scene.

        Parameters:
        :   **kwargs** – Additional keyword arguments to pass to the scene.

        Returns:
        :   None

    *async* set_data(*data: Mapping[str, Any]*) → None
    :   Sets custom data in the current state.

        Parameters:
        :   **data** – A mapping containing the custom data to be set in the current state.

        Returns:
        :   None

    *async* update_data(*data: Mapping[str, Any] | None = None*, *\*\*kwargs: Any*) → dict[str, Any]
    :   This method updates the data stored in the current state

        Parameters:
        :   - **data** – Optional mapping of data to update.
            - **kwargs** – Additional key-value pairs of data to update.

        Returns:
        :   Dictionary of updated data

### Markers

Markers are similar to the Router event registering mechanism,
but they are used to mark scene handlers in the Scene class.

It can be imported from `from aiogram.fsm.scene import on` and should be used as decorator.

Allowed event types:

- message
- edited_message
- channel_post
- edited_channel_post
- inline_query
- chosen_inline_result
- callback_query
- shipping_query
- pre_checkout_query
- poll
- poll_answer
- my_chat_member
- chat_member
- chat_join_request

Each event type can be filtered in the same way as in the Router.

Also each event type can be marked as scene entry point, exit point or leave point.

If you want to mark the scene can be entered from message or inline query,
you should use `on.message` or `on.inline_query` marker:

```
class MyScene(Scene, name="my_scene"):
    @on.message.enter()
    async def on_enter(self, message: types.Message):
        pass

    @on.callback_query.enter()
    async def on_enter(self, callback_query: types.CallbackQuery):
        pass
```

Scene has only three points for transitions:

- enter point - when user enters to the scene
- leave point - when user leaves the scene and the enter another scene
- exit point - when user exits from the scene

### How to enter the scene

There are several ways to enter a scene in aiogram. Each approach has specific use cases and advantages

1. **Directly using the scene’s entry point as a handler:**

   You can convert a scene’s entry point to a handler and register it like any other handler:

   ```
   router.message.register(SettingsScene.as_handler(), Command("settings"))
   ```
2. **From a regular handler using ScenesManager:**

   Enter a scene from any regular handler by using the ScenesManager:

   Note

   When using ScenesManager, you need to explicitly pass all dependencies required by the scene’s
   entry point handler as arguments to the enter method.

   ```
   @router.message(Command("settings"))
   async def settings_handler(message: Message, scenes: ScenesManager):
       await scenes.enter(SettingsScene, some_data="data")  # pass additional arguments to the scene
   ```
3. **From another scene using After.goto marker:**

   Transition to another scene after a handler is executed using the After marker:

   ```
   class MyScene(Scene, state="my_scene"):

       ...

       @on.message(F.text.startswith("🚀"), after=After.goto(AnotherScene))
       async def on_message(self, message: Message, some_repo: SomeRepository, db: AsyncSession):
           # Persist some data before going to another scene
           await some_repo.save(user_id=message.from_user.id, value=message.text)
           await db.commit()

       ...
   ```
4. **Using explicit transition with wizard.goto:**

   For more control over the transition, use the wizard.goto method from within a scene handler:

   Note

   Dependencies will be injected into the handler normally and then extended with
   the arguments specified in the goto method.

   ```
   class MyScene(Scene, state="my_scene"):
       ...

       @on.message(F.text.startswith("🚀"))
       async def on_message(self, message: Message):
           # Direct control over when and how to transition
           await self.wizard.goto(AnotherScene, value=message.text)

       ...
   ```

Each method offers different levels of control and integration with your application’s architecture.
Choose the approach that best fits your specific use case and coding style.
