# Game

> Source: [https://docs.aiogram.dev/en/latest/api/types/game.html](https://docs.aiogram.dev/en/latest/api/types/game.html)

*class* aiogram.types.game.Game(*\**, *title: str*, *description: str*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]*, *text: str | None = None*, *text_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *animation: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None = None*, *\*\*extra_data: Any*)
:   This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Source: <https://core.telegram.org/bots/api#game>

    title*: str*
    :   Title of the game

    description*: str*
    :   Description of the game

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")]*
    :   Photo that will be displayed in the game message in chats

    text*: str | None*
    :   *Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [`aiogram.methods.set_game_score.SetGameScore`](../methods/set_game_score.html#aiogram.methods.set_game_score.SetGameScore "aiogram.methods.set_game_score.SetGameScore"), or manually edited using [`aiogram.methods.edit_message_text.EditMessageText`](../methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText"). 0-4096 characters

    text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc

    animation*: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None*
    :   *Optional*. Animation that will be displayed in the game message in chats. Upload via [BotFather](https://t.me/botfather)
