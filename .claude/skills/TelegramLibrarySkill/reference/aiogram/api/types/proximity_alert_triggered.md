# ProximityAlertTriggered

> Source: [https://docs.aiogram.dev/en/latest/api/types/proximity_alert_triggered.html](https://docs.aiogram.dev/en/latest/api/types/proximity_alert_triggered.html)

*class* aiogram.types.proximity_alert_triggered.ProximityAlertTriggered(*\**, *traveler: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *watcher: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *distance: int*, *\*\*extra_data: Any*)
:   This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Source: <https://core.telegram.org/bots/api#proximityalerttriggered>

    traveler*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User that triggered the alert

    watcher*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User that set the alert

    distance*: int*
    :   The distance between the users
