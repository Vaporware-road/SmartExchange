# EncryptedCredentials

> Source: [https://docs.aiogram.dev/en/latest/api/types/encrypted_credentials.html](https://docs.aiogram.dev/en/latest/api/types/encrypted_credentials.html)

*class* aiogram.types.encrypted_credentials.EncryptedCredentials(*\**, *data: str*, *hash: str*, *secret: str*, *\*\*extra_data: Any*)
:   Describes data required for decrypting and authenticating [`aiogram.types.encrypted_passport_element.EncryptedPassportElement`](encrypted_passport_element.html#aiogram.types.encrypted_passport_element.EncryptedPassportElement "aiogram.types.encrypted_passport_element.EncryptedPassportElement"). See the [Telegram Passport Documentation](https://core.telegram.org/passport#receiving-information) for a complete description of the data decryption and authentication processes.

    Source: <https://core.telegram.org/bots/api#encryptedcredentials>

    data*: str*
    :   Base64-encoded encrypted JSON-serialized data with unique user’s payload, data hashes and secrets required for [`aiogram.types.encrypted_passport_element.EncryptedPassportElement`](encrypted_passport_element.html#aiogram.types.encrypted_passport_element.EncryptedPassportElement "aiogram.types.encrypted_passport_element.EncryptedPassportElement") decryption and authentication

    hash*: str*
    :   Base64-encoded data hash for data authentication

    secret*: str*
    :   Base64-encoded secret, encrypted with the bot’s public RSA key, required for data decryption
