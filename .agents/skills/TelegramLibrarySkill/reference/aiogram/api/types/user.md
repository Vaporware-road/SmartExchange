# User

> Source: [https://docs.aiogram.dev/en/latest/api/types/user.html](https://docs.aiogram.dev/en/latest/api/types/user.html)

*class* aiogram.types.user.User(*\**, *id: int*, *is_bot: bool*, *first_name: str*, *last_name: str | None = None*, *username: str | None = None*, *language_code: str | None = None*, *is_premium: bool | None = None*, *added_to_attachment_menu: bool | None = None*, *can_join_groups: bool | None = None*, *can_read_all_group_messages: bool | None = None*, *supports_guest_queries: bool | None = None*, *supports_inline_queries: bool | None = None*, *can_connect_to_business: bool | None = None*, *has_main_web_app: bool | None = None*, *has_topics_enabled: bool | None = None*, *allows_users_to_create_topics: bool | None = None*, *can_manage_bots: bool | None = None*, *supports_join_request_queries: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a Telegram user or bot.

    Source: <https://core.telegram.org/bots/api#user>

    id*: int*
    :   Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier

    is_bot*: bool*
    :   `True`, if this user is a bot

    first_name*: str*
    :   User’s or bot’s first name

    last_name*: str | None*
    :   *Optional*. User’s or bot’s last name

    username*: str | None*
    :   *Optional*. User’s or bot’s username

    language_code*: str | None*
    :   *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user’s language

    is_premium*: bool | None*
    :   *Optional*. `True`, if this user is a Telegram Premium user

    added_to_attachment_menu*: bool | None*
    :   *Optional*. `True`, if this user added the bot to the attachment menu

    can_join_groups*: bool | None*
    :   *Optional*. `True`, if the bot can be invited to groups. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    can_read_all_group_messages*: bool | None*
    :   *Optional*. `True`, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    supports_guest_queries*: bool | None*
    :   *Optional*. `True`, if the bot supports guest queries from chats it is not a member of. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    supports_inline_queries*: bool | None*
    :   *Optional*. `True`, if the bot supports inline queries. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    can_connect_to_business*: bool | None*
    :   *Optional*. `True`, if the bot can be connected to a user account to manage it. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    has_main_web_app*: bool | None*
    :   *Optional*. `True`, if the bot has a main Web App. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    has_topics_enabled*: bool | None*
    :   *Optional*. `True`, if the bot has forum topic mode enabled in private chats. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    allows_users_to_create_topics*: bool | None*
    :   *Optional*. `True`, if the bot allows users to create and delete topics in private chats. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    can_manage_bots*: bool | None*
    :   *Optional*. `True`, if other bots can be created to be controlled by the bot. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    supports_join_request_queries*: bool | None*
    :   *Optional*. `True`, if the bot supports join request queries and can be assigned to process them. Returned only in [`aiogram.methods.get_me.GetMe`](../methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe")

    *property* full_name*: str*

    *property* url*: str*

    mention_markdown(*name: str | None = None*) → str

    mention_html(*name: str | None = None*) → str

    get_profile_photos(*offset: int | None = None*, *limit: int | None = None*, *\*\*kwargs: Any*) → [GetUserProfilePhotos](../methods/get_user_profile_photos.html#aiogram.methods.get_user_profile_photos.GetUserProfilePhotos "aiogram.methods.get_user_profile_photos.GetUserProfilePhotos")
    :   Shortcut for method [`aiogram.methods.get_user_profile_photos.GetUserProfilePhotos`](../methods/get_user_profile_photos.html#aiogram.methods.get_user_profile_photos.GetUserProfilePhotos "aiogram.methods.get_user_profile_photos.GetUserProfilePhotos")
        will automatically fill method attributes:

        - `user_id`

        Use this method to get a list of profile pictures for a user. Returns a [`aiogram.types.user_profile_photos.UserProfilePhotos`](user_profile_photos.html#aiogram.types.user_profile_photos.UserProfilePhotos "aiogram.types.user_profile_photos.UserProfilePhotos") object.

        Source: <https://core.telegram.org/bots/api#getuserprofilephotos>

        Parameters:
        :   - **offset** – Sequential number of the first photo to be returned. By default, all photos are returned
            - **limit** – Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100

        Returns:
        :   instance of method [`aiogram.methods.get_user_profile_photos.GetUserProfilePhotos`](../methods/get_user_profile_photos.html#aiogram.methods.get_user_profile_photos.GetUserProfilePhotos "aiogram.methods.get_user_profile_photos.GetUserProfilePhotos")

    get_profile_audios(*offset: int | None = None*, *limit: int | None = None*, *\*\*kwargs: Any*) → [GetUserProfileAudios](../methods/get_user_profile_audios.html#aiogram.methods.get_user_profile_audios.GetUserProfileAudios "aiogram.methods.get_user_profile_audios.GetUserProfileAudios")
    :   Shortcut for method [`aiogram.methods.get_user_profile_audios.GetUserProfileAudios`](../methods/get_user_profile_audios.html#aiogram.methods.get_user_profile_audios.GetUserProfileAudios "aiogram.methods.get_user_profile_audios.GetUserProfileAudios")
        will automatically fill method attributes:

        - `user_id`

        Use this method to get a list of profile audios for a user. Returns a [`aiogram.types.user_profile_audios.UserProfileAudios`](user_profile_audios.html#aiogram.types.user_profile_audios.UserProfileAudios "aiogram.types.user_profile_audios.UserProfileAudios") object.

        Source: <https://core.telegram.org/bots/api#getuserprofileaudios>

        Parameters:
        :   - **offset** – Sequential number of the first audio to be returned. By default, all audios are returned
            - **limit** – Limits the number of audios to be retrieved. Values between 1-100 are accepted. Defaults to 100

        Returns:
        :   instance of method [`aiogram.methods.get_user_profile_audios.GetUserProfileAudios`](../methods/get_user_profile_audios.html#aiogram.methods.get_user_profile_audios.GetUserProfileAudios "aiogram.methods.get_user_profile_audios.GetUserProfileAudios")
