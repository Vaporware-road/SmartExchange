# Dice

> Source: [https://docs.aiogram.dev/en/latest/api/types/dice.html](https://docs.aiogram.dev/en/latest/api/types/dice.html)

*class* aiogram.types.dice.Dice(*\**, *emoji: str*, *value: int*, *\*\*extra_data: Any*)
:   This object represents an animated emoji that displays a random value.

    Source: <https://core.telegram.org/bots/api#dice>

    emoji*: str*
    :   Emoji on which the dice throw animation is based

    value*: int*
    :   Value of the dice, 1-6 for ‘🎲’, ‘🎯’ and ‘🎳’ base emoji, 1-5 for ‘🏀’ and ‘⚽’ base emoji, 1-64 for ‘🎰’ base emoji

*class* aiogram.types.dice.DiceEmoji
:   DICE *= '🎲'*

    DART *= '🎯'*

    BASKETBALL *= '🏀'*

    FOOTBALL *= '⚽'*

    SLOT_MACHINE *= '🎰'*

    BOWLING *= '🎳'*
