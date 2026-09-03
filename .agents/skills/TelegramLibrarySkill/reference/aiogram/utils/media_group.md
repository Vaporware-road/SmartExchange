# Media group builder

> Source: [https://docs.aiogram.dev/en/latest/utils/media_group.html](https://docs.aiogram.dev/en/latest/utils/media_group.html)

This module provides a builder for media groups, it can be used to build media groups
for [`aiogram.types.input_media_photo.InputMediaPhoto`](../api/types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto"), [`aiogram.types.input_media_video.InputMediaVideo`](../api/types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo"),
[`aiogram.types.input_media_document.InputMediaDocument`](../api/types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument") and [`aiogram.types.input_media_audio.InputMediaAudio`](../api/types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio").

Warning

[`aiogram.types.input_media_animation.InputMediaAnimation`](../api/types/input_media_animation.html#aiogram.types.input_media_animation.InputMediaAnimation "aiogram.types.input_media_animation.InputMediaAnimation")
is not supported yet in the Bot API to send as media group.

## Usage

```
media_group = MediaGroupBuilder(caption="Media group caption")

# Add photo
media_group.add_photo(media="https://picsum.photos/200/300")
# Dynamically add photo with known type without using separate method
media_group.add(type="photo", media="https://picsum.photos/200/300")
# ... or video
media_group.add(type="video", media=FSInputFile("media/video.mp4"))
```

To send media group use [`aiogram.methods.send_media_group.SendMediaGroup()`](../api/methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup") method,
but when you use [`aiogram.utils.media_group.MediaGroupBuilder`](#aiogram.utils.media_group.MediaGroupBuilder "aiogram.utils.media_group.MediaGroupBuilder")
you should pass `media` argument as `media_group.build()`.

If you specify `caption` in [`aiogram.utils.media_group.MediaGroupBuilder`](#aiogram.utils.media_group.MediaGroupBuilder "aiogram.utils.media_group.MediaGroupBuilder")
it will be used as `caption` for first media in group.

```
await bot.send_media_group(chat_id=chat_id, media=media_group.build())
```

## References

*class* aiogram.utils.media_group.MediaGroupBuilder(*media: list[[InputMediaAudio](../api/types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaPhoto](../api/types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](../api/types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo") | [InputMediaDocument](../api/types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument")] | None = None*, *caption: str | None = None*, *caption_entities: list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*)
:   add(*\**, *type: Literal[InputMediaType.AUDIO]*, *media: str | [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *caption: str | None = None*, *parse_mode: str | None = UNSET_PARSE_MODE*, *caption_entities: list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *\*\*kwargs: Any*) → None

    add(*\**, *type: Literal[InputMediaType.PHOTO]*, *media: str | [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *caption: str | None = None*, *parse_mode: str | None = UNSET_PARSE_MODE*, *caption_entities: list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *has_spoiler: bool | None = None*, *\*\*kwargs: Any*) → None

    add(*\**, *type: Literal[InputMediaType.VIDEO]*, *media: str | [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *thumbnail: [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | str | None = None*, *caption: str | None = None*, *parse_mode: str | None = UNSET_PARSE_MODE*, *caption_entities: list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *width: int | None = None*, *height: int | None = None*, *duration: int | None = None*, *supports_streaming: bool | None = None*, *has_spoiler: bool | None = None*, *\*\*kwargs: Any*) → None

    add(*\**, *type: Literal[InputMediaType.DOCUMENT]*, *media: str | [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *thumbnail: [InputFile](../api/types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | str | None = None*, *caption: str | None = None*, *parse_mode: str | None = UNSET_PARSE_MODE*, *caption_entities: list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *disable_content_type_detection: bool | None = None*, *\*\*kwargs: Any*) → None
    :   Add a media object to the media group.

        Parameters:
        :   **kwargs** – Keyword arguments for the media object.
            The available keyword arguments depend on the media type.

        Returns:
        :   None

    add_audio(*media: str | ~aiogram.types.input_file.InputFile*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *\*\*kwargs: ~typing.Any*) → None
    :   Add an audio file to the media group.

        Parameters:
        :   - **media** –

              File to send. Pass a file_id to send a file that exists on the
              Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from
              the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using
              multipart/form-data under <file_attach_name> name.

              > [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **thumbnail** – *Optional*. Thumbnail of the file sent; can be ignored if
              thumbnail generation for the file is supported server-side. The thumbnail should
              be in JPEG format and less than 200 kB in size. A thumbnail’s width and height
              should not exceed 320.
            - **caption** – *Optional*. Caption of the audio to be sent, 0-1024 characters
              after entities parsing
            - **parse_mode** – *Optional*. Mode for parsing entities in the audio caption.
              See [formatting options](https://core.telegram.org/bots/api#formatting-options)
              for more details.
            - **caption_entities** – *Optional*. List of special entities that appear in the caption,
              which can be specified instead of *parse_mode*
            - **duration** – *Optional*. Duration of the audio in seconds
            - **performer** – *Optional*. Performer of the audio
            - **title** – *Optional*. Title of the audio

        Returns:
        :   None

    add_document(*media: str | ~aiogram.types.input_file.InputFile*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *\*\*kwargs: ~typing.Any*) → None
    :   Add a document to the media group.

        Parameters:
        :   - **media** – File to send. Pass a file_id to send a file that exists on the
              Telegram servers (recommended), pass an HTTP URL for Telegram to get a file
              from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using
              multipart/form-data under <file_attach_name> name.
              [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **thumbnail** – *Optional*. Thumbnail of the file sent; can be ignored
              if thumbnail generation for the file is supported server-side.
              The thumbnail should be in JPEG format and less than 200 kB in size.
              A thumbnail’s width and height should not exceed 320.
              Ignored if the file is not uploaded using multipart/form-data.
              Thumbnails can’t be reused and can be only uploaded as a new file,
              so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded
              using multipart/form-data under <file_attach_name>.
              [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **caption** – *Optional*. Caption of the document to be sent,
              0-1024 characters after entities parsing
            - **parse_mode** –

              *Optional*. Mode for parsing entities in the document caption.
              See [formatting options](https://core.telegram.org/bots/api#formatting-options)
              for more details.
            - **caption_entities** – *Optional*. List of special entities that appear
              in the caption, which can be specified instead of *parse_mode*
            - **disable_content_type_detection** – *Optional*. Disables automatic server-side
              content type detection for files uploaded using multipart/form-data.
              Always `True`, if the document is sent as part of an album.

        Returns:
        :   None

    add_photo(*media: str | ~aiogram.types.input_file.InputFile*, *caption: str | None = None*, *parse_mode: str | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *has_spoiler: bool | None = None*, *\*\*kwargs: ~typing.Any*) → None
    :   Add a photo to the media group.

        Parameters:
        :   - **media** –

              File to send. Pass a file_id to send a file that exists on the
              Telegram servers (recommended), pass an HTTP URL for Telegram to get a file
              from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new
              one using multipart/form-data under <file_attach_name> name.

              > [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **caption** – *Optional*. Caption of the photo to be sent, 0-1024 characters
              after entities parsing
            - **parse_mode** –

              *Optional*. Mode for parsing entities in the photo caption.
              See [formatting options](https://core.telegram.org/bots/api#formatting-options)
              for more details.
            - **caption_entities** – *Optional*. List of special entities that appear in the caption,
              which can be specified instead of *parse_mode*
            - **has_spoiler** – *Optional*. Pass `True` if the photo needs to be covered
              with a spoiler animation

        Returns:
        :   None

    add_video(*media: str | ~aiogram.types.input_file.InputFile*, *thumbnail: ~aiogram.types.input_file.InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *width: int | None = None*, *height: int | None = None*, *duration: int | None = None*, *supports_streaming: bool | None = None*, *has_spoiler: bool | None = None*, *\*\*kwargs: ~typing.Any*) → None
    :   Add a video to the media group.

        Parameters:
        :   - **media** – File to send. Pass a file_id to send a file that exists on the
              Telegram servers (recommended), pass an HTTP URL for Telegram to get a file
              from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one
              using multipart/form-data under <file_attach_name> name.
              [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **thumbnail** – *Optional*. Thumbnail of the file sent; can be ignored if thumbnail
              generation for the file is supported server-side. The thumbnail should be in JPEG
              format and less than 200 kB in size. A thumbnail’s width and height should
              not exceed 320. Ignored if the file is not uploaded using multipart/form-data.
              Thumbnails can’t be reused and can be only uploaded as a new file, so you
              can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using
              multipart/form-data under <file_attach_name>.
              [More information on Sending Files »](../api/upload_file.html#sending-files)
            - **caption** – *Optional*. Caption of the video to be sent,
              0-1024 characters after entities parsing
            - **parse_mode** –

              *Optional*. Mode for parsing entities in the video caption.
              See [formatting options](https://core.telegram.org/bots/api#formatting-options)
              for more details.
            - **caption_entities** – *Optional*. List of special entities that appear in the caption,
              which can be specified instead of *parse_mode*
            - **width** – *Optional*. Video width
            - **height** – *Optional*. Video height
            - **duration** – *Optional*. Video duration in seconds
            - **supports_streaming** – *Optional*. Pass `True` if the uploaded video is
              suitable for streaming
            - **has_spoiler** – *Optional*. Pass `True` if the video needs to be covered
              with a spoiler animation

        Returns:
        :   None

    build() → list[[InputMediaAudio](../api/types/input_media_audio.html#aiogram.types.input_media_audio.InputMediaAudio "aiogram.types.input_media_audio.InputMediaAudio") | [InputMediaPhoto](../api/types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") | [InputMediaVideo](../api/types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo") | [InputMediaDocument](../api/types/input_media_document.html#aiogram.types.input_media_document.InputMediaDocument "aiogram.types.input_media_document.InputMediaDocument")]
    :   Builds a list of media objects for a media group.

        Adds the caption to the first media object if it is present.

        Returns:
        :   List of media objects.
