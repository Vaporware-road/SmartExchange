"""Crawler-facing metadata for the tutorial hub.

The posts themselves live in ``frontend/src/content/tutorials/index.js`` and
their copy in the locale files; only the title and description a bot reads
before the bundle runs are duplicated here. Keep the two in step — a crawler
that reads one and a visitor who reads the other must not be told different
things.
"""

SITE_URL = "https://mrexchange.co.uk"

TUTORIALS = (
    {
        "slug": "publish-prices",
        "title": "Update your rates and publish them everywhere",
        "description": (
            "The morning routine in an exchange office: type the new buy and sell "
            "rates, finalize them, and let the panel push the change to your website, "
            "Telegram channel, Instagram page and rate widget."
        ),
        "gif": "publish-prices.gif",
    },
    {
        "slug": "template-editor",
        "title": "Design a rate image on your own template",
        "description": (
            "Drag a widget onto the canvas, bind it to a live price and preview the "
            "rate image your customers will see — designed once, rendered on every "
            "publish."
        ),
        "gif": "template-editor.gif",
    },
    {
        "slug": "telegram-bot",
        "title": "Connect your Telegram channel and bot",
        "description": (
            "Paste your bot token, register the channel, choose what gets posted and "
            "send a test message before any rate reaches your customers."
        ),
        "gif": "telegram-bot.gif",
    },
    {
        "slug": "signup-tour",
        "title": "Sign up and find your way around the panel",
        "description": (
            "Email and password or a Google account, a one-time code to confirm it is "
            "you, then a guided tour and fourteen days of the complete product."
        ),
        "gif": "signup-tour.gif",
    },
)

INDEX_TITLE = "Tutorials — MrExchange"
INDEX_DESCRIPTION = (
    "Short, recorded walkthroughs of everything an exchange office does in the "
    "MrExchange panel: publishing rates, designing rate images, connecting "
    "Telegram and getting started."
)


def find(slug):
    for post in TUTORIALS:
        if post["slug"] == slug:
            return post
    return None
