# WriteAccessAllowed

> Source: [https://docs.aiogram.dev/en/latest/api/types/write_access_allowed.html](https://docs.aiogram.dev/en/latest/api/types/write_access_allowed.html)

*class* aiogram.types.write_access_allowed.WriteAccessAllowed(*\**, *from_request: bool | None = None*, *web_app_name: str | None = None*, *from_attachment_menu: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps).

    Source: <https://core.telegram.org/bots/api#writeaccessallowed>

    from_request*: bool | None*
    :   *Optional*. `True`, if the access was granted after the user accepted an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps)

    web_app_name*: str | None*
    :   *Optional*. Name of the Web App, if the access was granted when the Web App was launched from a link

    from_attachment_menu*: bool | None*
    :   *Optional*. `True`, if the access was granted when the bot was added to the attachment or side menu
