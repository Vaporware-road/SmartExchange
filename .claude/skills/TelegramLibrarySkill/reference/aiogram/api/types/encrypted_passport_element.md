# EncryptedPassportElement

> Source: [https://docs.aiogram.dev/en/latest/api/types/encrypted_passport_element.html](https://docs.aiogram.dev/en/latest/api/types/encrypted_passport_element.html)

*class* aiogram.types.encrypted_passport_element.EncryptedPassportElement(*\**, *type: str*, *hash: str*, *data: str | None = None*, *phone_number: str | None = None*, *email: str | None = None*, *files: list[[PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile")] | None = None*, *front_side: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None = None*, *reverse_side: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None = None*, *selfie: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None = None*, *translation: list[[PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile")] | None = None*, *\*\*extra_data: Any*)
:   Describes documents or other Telegram Passport elements shared with the bot by the user.

    Source: <https://core.telegram.org/bots/api#encryptedpassportelement>

    type*: str*
    :   Element type. One of ‘personal_details’, ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’, ‘address’, ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’, ‘temporary_registration’, ‘phone_number’, ‘email’

    hash*: str*
    :   Base64-encoded element hash for using in [`aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified`](passport_element_error_unspecified.html#aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified "aiogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified")

    data*: str | None*
    :   *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user; available only for ‘personal_details’, ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’ and ‘address’ types. Can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")

    phone_number*: str | None*
    :   *Optional*. User’s verified phone number; available only for ‘phone_number’ type

    email*: str | None*
    :   *Optional*. User’s verified email address; available only for ‘email’ type

    files*: list[[PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile")] | None*
    :   *Optional*. Array of encrypted files with documents provided by the user; available only for ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’ and ‘temporary_registration’ types. Files can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")

    front_side*: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None*
    :   *Optional*. Encrypted file with the front side of the document, provided by the user; available only for ‘passport’, ‘driver_license’, ‘identity_card’ and ‘internal_passport’. The file can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")

    reverse_side*: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None*
    :   *Optional*. Encrypted file with the reverse side of the document, provided by the user; available only for ‘driver_license’ and ‘identity_card’. The file can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")

    selfie*: [PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile") | None*
    :   *Optional*. Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for ‘passport’, ‘driver_license’, ‘identity_card’ and ‘internal_passport’. The file can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")

    translation*: list[[PassportFile](passport_file.html#aiogram.types.passport_file.PassportFile "aiogram.types.passport_file.PassportFile")] | None*
    :   *Optional*. Array of encrypted files with translated versions of documents provided by the user; available if requested for ‘passport’, ‘driver_license’, ‘identity_card’, ‘internal_passport’, ‘utility_bill’, ‘bank_statement’, ‘rental_agreement’, ‘passport_registration’ and ‘temporary_registration’ types. Files can be decrypted and verified using the accompanying [`aiogram.types.encrypted_credentials.EncryptedCredentials`](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")
