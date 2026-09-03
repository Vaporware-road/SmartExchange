# InputProfilePhotoStatic

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_profile_photo_static.html](https://docs.aiogram.dev/en/latest/api/types/input_profile_photo_static.html)

*class* aiogram.types.input_profile_photo_static.InputProfilePhotoStatic(*\**, *type: Literal[InputProfilePhotoType.STATIC] = InputProfilePhotoType.STATIC*, *photo: str | [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *\*\*extra_data: Any*)
:   A static profile photo in the .JPG format.

    Source: <https://core.telegram.org/bots/api#inputprofilephotostatic>

    type*: Literal[InputProfilePhotoType.STATIC]*
    :   Type of the profile photo, must be *static*

    photo*: InputFileUnion*
    :   The static profile photo. Profile photos can’t be reused and can only be uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the photo was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
