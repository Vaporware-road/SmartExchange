# InputStoryContentVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_story_content_video.html](https://docs.aiogram.dev/en/latest/api/types/input_story_content_video.html)

*class* aiogram.types.input_story_content_video.InputStoryContentVideo(*\**, *type: Literal[InputStoryContentType.VIDEO] = InputStoryContentType.VIDEO*, *video: str*, *duration: float | None = None*, *cover_frame_timestamp: float | None = None*, *is_animation: bool | None = None*, *\*\*extra_data: Any*)
:   Describes a video to post as a story.

    Source: <https://core.telegram.org/bots/api#inputstorycontentvideo>

    type*: Literal[InputStoryContentType.VIDEO]*
    :   Type of the content, must be *video*

    video*: str*
    :   The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can’t be reused and can only be uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the video was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)

    duration*: float | None*
    :   *Optional*. Precise duration of the video in seconds; 0-60

    cover_frame_timestamp*: float | None*
    :   *Optional*. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0

    is_animation*: bool | None*
    :   *Optional*. Pass `True` if the video has no sound
