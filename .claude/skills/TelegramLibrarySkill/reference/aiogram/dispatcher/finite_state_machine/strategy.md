# Strategy

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/strategy.html](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/strategy.html)

This module provides the FSMStrategy enumeration which is used to define the strategy of the finite state machine.

*class* aiogram.fsm.strategy.FSMStrategy(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)
:   FSM strategy for storage key generation.

    CHAT *= 2*
    :   State will be stored for each chat globally without separating by users.

    CHAT_TOPIC *= 5*
    :   State will be stored for each chat and topic, but not separated by users.

    GLOBAL_USER *= 3*
    :   State will be stored globally for each user globally.

    USER_IN_CHAT *= 1*
    :   State will be stored for each user in chat.

    USER_IN_TOPIC *= 4*
    :   State will be stored for each user in chat and topic.
