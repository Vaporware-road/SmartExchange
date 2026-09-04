# InputPollOption

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_poll_option.html](https://docs.aiogram.dev/en/latest/api/types/input_poll_option.html)

*class* aiogram.types.input_poll_option.InputPollOption(*\**, *text: str*, *text_parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *text_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *media: ~typing.Annotated[~aiogram.types.input_media_animation.InputMediaAnimation | ~aiogram.types.input_media_link.InputMediaLink | ~aiogram.types.input_media_live_photo.InputMediaLivePhoto | ~aiogram.types.input_media_location.InputMediaLocation | ~aiogram.types.input_media_photo.InputMediaPhoto | ~aiogram.types.input_media_sticker.InputMediaSticker | ~aiogram.types.input_media_venue.InputMediaVenue | ~aiogram.types.input_media_video.InputMediaVideo*, *FieldInfo(annotation=NoneType*, *required=True*, *discriminator='type')] | None = None*, *\*\*extra_data: ~typing.Any*)
:   This object contains information about one answer option in a poll to be sent.

    Source: <https://core.telegram.org/bots/api#inputpolloption>

    text*: str*
    :   Option text, 1-100 characters

    text_parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed

    text_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text_parse_mode*

    media*: InputPollOptionMediaUnion | None*
    :   *Optional*. Media added to the poll option
