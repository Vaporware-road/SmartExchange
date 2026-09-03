# Sticker

> Source: [https://docs.aiogram.dev/en/latest/api/types/sticker.html](https://docs.aiogram.dev/en/latest/api/types/sticker.html)

*class* aiogram.types.sticker.Sticker(*\**, *file_id: str*, *file_unique_id: str*, *type: str*, *width: int*, *height: int*, *is_animated: bool*, *is_video: bool*, *thumbnail: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None = None*, *emoji: str | None = None*, *set_name: str | None = None*, *premium_animation: [File](file.html#aiogram.types.file.File "aiogram.types.file.File") | None = None*, *mask_position: [MaskPosition](mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None = None*, *custom_emoji_id: str | None = None*, *needs_repainting: bool | None = None*, *file_size: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a sticker.

    Source: <https://core.telegram.org/bots/api#sticker>

    file_id*: str*
    :   Identifier for this file, which can be used to download or reuse the file

    file_unique_id*: str*
    :   Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file

    type*: str*
    :   Type of the sticker, currently one of ‘regular’, ‘mask’, ‘custom_emoji’. The type of the sticker is independent from its format, which is determined by the fields *is_animated* and *is_video*

    width*: int*
    :   Sticker width

    height*: int*
    :   Sticker height

    is_animated*: bool*
    :   `True`, if the sticker is [animated](https://telegram.org/blog/animated-stickers)

    is_video*: bool*
    :   `True`, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions)

    thumbnail*: [PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize") | None*
    :   *Optional*. Sticker thumbnail in the .WEBP or .JPG format

    emoji*: str | None*
    :   *Optional*. Emoji associated with the sticker

    set_name*: str | None*
    :   *Optional*. Name of the sticker set to which the sticker belongs

    premium_animation*: [File](file.html#aiogram.types.file.File "aiogram.types.file.File") | None*
    :   *Optional*. For premium regular stickers, premium animation for the sticker

    mask_position*: [MaskPosition](mask_position.html#aiogram.types.mask_position.MaskPosition "aiogram.types.mask_position.MaskPosition") | None*
    :   *Optional*. For mask stickers, the position where the mask should be placed

    custom_emoji_id*: str | None*
    :   *Optional*. For custom emoji stickers, unique identifier of the custom emoji

    needs_repainting*: bool | None*
    :   *Optional*. `True`, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places

    file_size*: int | None*
    :   *Optional*. File size in bytes

    set_position_in_set(*position: int*, *\*\*kwargs: Any*) → [SetStickerPositionInSet](../methods/set_sticker_position_in_set.html#aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet "aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet")
    :   Shortcut for method [`aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet`](../methods/set_sticker_position_in_set.html#aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet "aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet")
        will automatically fill method attributes:

        - `sticker`

        Use this method to move a sticker in a set created by the bot to a specific position. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setstickerpositioninset>

        Parameters:
        :   **position** – New sticker position in the set, zero-based

        Returns:
        :   instance of method [`aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet`](../methods/set_sticker_position_in_set.html#aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet "aiogram.methods.set_sticker_position_in_set.SetStickerPositionInSet")

    delete_from_set(*\*\*kwargs: Any*) → [DeleteStickerFromSet](../methods/delete_sticker_from_set.html#aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet "aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet")
    :   Shortcut for method [`aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet`](../methods/delete_sticker_from_set.html#aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet "aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet")
        will automatically fill method attributes:

        - `sticker`

        Use this method to delete a sticker from a set created by the bot. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#deletestickerfromset>

        Returns:
        :   instance of method [`aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet`](../methods/delete_sticker_from_set.html#aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet "aiogram.methods.delete_sticker_from_set.DeleteStickerFromSet")
