# setPassportDataErrors

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_passport_data_errors.html](https://docs.aiogram.dev/en/latest/api/methods/set_passport_data_errors.html)

Returns: `bool`

*class* aiogram.methods.set_passport_data_errors.SetPassportDataErrors(*\**, *user_id: int*, *errors: list[Annotated[[PassportElementErrorDataField](../types/passport_element_error_data_field.html#aiogram.types.passport_element_error_data_field.PassportElementErrorDataField "aiogram.types.passport_element_error_data_field.PassportElementErrorDataField") | [PassportElementErrorFrontSide](../types/passport_element_error_front_side.html#aiogram.types.passport_element_error_front_side.PassportElementErrorFrontSide "aiogram.types.passport_element_error_front_side.PassportElementErrorFrontSide") | [PassportElementErrorReverseSide](../types/passport_element_error_reverse_side.html#aiogram.types.passport_element_error_reverse_side.PassportElementErrorReverseSide "aiogram.types.passport_element_error_reverse_side.PassportElementErrorReverseSide") | [PassportElementErrorSelfie](../types/passport_element_error_selfie.html#aiogram.types.passport_element_error_selfie.PassportElementErrorSelfie "aiogram.types.passport_element_error_selfie.PassportElementErrorSelfie") | [PassportElementErrorFile](../types/passport_element_error_file.html#aiogram.types.passport_element_error_file.PassportElementErrorFile "aiogram.types.passport_element_error_file.PassportElementErrorFile") | [PassportElementErrorFiles](../types/passport_element_error_files.html#aiogram.types.passport_element_error_files.PassportElementErrorFiles "aiogram.types.passport_element_error_files.PassportElementErrorFiles") | [PassportElementErrorTranslationFile](../types/passport_element_error_translation_file.html#aiogram.types.passport_element_error_translation_file.PassportElementErrorTranslationFile "aiogram.types.passport_element_error_translation_file.PassportElementErrorTranslationFile") | [PassportElementErrorTranslationFiles](../types/passport_element_error_translation_files.html#aiogram.types.passport_element_error_translation_files.PassportElementErrorTranslationFiles "aiogram.types.passport_element_error_translation_files.PassportElementErrorTranslationFiles") | [PassportElementErrorUnspecified](../types/passport_element_error_unspecified.html#aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified "aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified"), FieldInfo(annotation=NoneType, required=True, discriminator='source')]]*, *\*\*extra_data: Any*)
:   Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns `True` on success.
    Use this if the data submitted by the user doesn’t satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

    Source: <https://core.telegram.org/bots/api#setpassportdataerrors>

    user_id*: int*
    :   User identifier

    errors*: list[PassportElementErrorUnion]*
    :   A JSON-serialized Array describing the errors

## Usage

### As bot method

```
result: bool = await bot.set_passport_data_errors(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_passport_data_errors import SetPassportDataErrors`
- alias: `from aiogram.methods import SetPassportDataErrors`

#### With specific bot

```
result: bool = await bot(SetPassportDataErrors(...))
```

#### As reply into Webhook in handler

```
return SetPassportDataErrors(...)
```
