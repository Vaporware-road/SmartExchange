# InputStoryContentPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_story_content_photo.html](https://docs.aiogram.dev/en/latest/api/types/input_story_content_photo.html)

*class* aiogram.types.input_story_content_photo.InputStoryContentPhoto(*\**, *type: Literal[InputStoryContentType.PHOTO] = InputStoryContentType.PHOTO*, *photo: str*, *\*\*extra_data: Any*)
:   Describes a photo to post as a story.

    Source: <https://core.telegram.org/bots/api#inputstorycontentphoto>

    type*: Literal[InputStoryContentType.PHOTO]*
    :   Type of the content, must be *photo*

    photo*: str*
    :   The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can’t be reused and can only be uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the photo was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
