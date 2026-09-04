# PassportData

> Source: [https://docs.aiogram.dev/en/latest/api/types/passport_data.html](https://docs.aiogram.dev/en/latest/api/types/passport_data.html)

*class* aiogram.types.passport_data.PassportData(*\**, *data: list[[EncryptedPassportElement](encrypted_passport_element.html#aiogram.types.encrypted_passport_element.EncryptedPassportElement "aiogram.types.encrypted_passport_element.EncryptedPassportElement")]*, *credentials: [EncryptedCredentials](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")*, *\*\*extra_data: Any*)
:   Describes Telegram Passport data shared with the bot by the user.

    Source: <https://core.telegram.org/bots/api#passportdata>

    data*: list[[EncryptedPassportElement](../enums/encrypted_passport_element.html#aiogram.enums.encrypted_passport_element.EncryptedPassportElement "aiogram.enums.encrypted_passport_element.EncryptedPassportElement")]*
    :   Array with information about documents and other Telegram Passport elements that was shared with the bot

    credentials*: [EncryptedCredentials](encrypted_credentials.html#aiogram.types.encrypted_credentials.EncryptedCredentials "aiogram.types.encrypted_credentials.EncryptedCredentials")*
    :   Encrypted credentials required to decrypt the data
