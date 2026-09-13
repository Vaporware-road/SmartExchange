import json

from django.template.loader import render_to_string

from MrExchangePanel.views import spa_with_head

from . import tutorials

_OG_IMAGE = f"{tutorials.SITE_URL}/static/landing/images/Mr%20Exchange.png"


def landing_page(request):
    """
    Public marketing page at `/`.

    The page itself is Vue (`views/landing/LandingView.vue`) and is served from
    the same SPA shell as the panel, so the marketing site and the product it
    sells share one design system and one set of translations.
    """
    # No `request=`: the fragment is static, and passing one would run every
    # context processor (a SiteSettings query included) on every page view.
    return spa_with_head(render_to_string("landing/seo_head.html"))


def tutorial_index(request):
    """`/tutorials` — the hub that replaced the shared demo."""
    page_url = f"{tutorials.SITE_URL}/tutorials"
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": tutorials.INDEX_TITLE,
            "description": tutorials.INDEX_DESCRIPTION,
            "url": page_url,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": position,
                    "url": f"{page_url}/{post['slug']}",
                    "name": post["title"],
                }
                for position, post in enumerate(tutorials.TUTORIALS, start=1)
            ],
        },
        indent=2,
    )
    seo_head = render_to_string(
        "landing/tutorial_seo_head.html",
        {
            "post": None,
            "page_title": tutorials.INDEX_TITLE,
            "page_description": tutorials.INDEX_DESCRIPTION,
            "page_url": page_url,
            "page_image": _OG_IMAGE,
            "structured_data": structured_data,
        },
    )
    return spa_with_head(seo_head)


def tutorial_detail(request, slug):
    """`/tutorials/<slug>` — one walkthrough, with its own title and card.

    An unknown slug still renders the shell: the SPA owns the "no such
    tutorial" message, and answering 404 here would blank the page instead.
    """
    post = tutorials.find(slug)
    if post is None:
        return tutorial_index(request)

    page_url = f"{tutorials.SITE_URL}/tutorials/{post['slug']}"
    image = f"{tutorials.SITE_URL}/static/landing/gifs/{post['gif']}"
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": post["title"],
            "description": post["description"],
            "url": page_url,
            "image": image,
            "publisher": {"@type": "Organization", "name": "MrExchange", "url": tutorials.SITE_URL},
        },
        indent=2,
    )
    seo_head = render_to_string(
        "landing/tutorial_seo_head.html",
        {
            "post": post,
            "page_title": f"{post['title']} — MrExchange",
            "page_description": post["description"],
            "page_url": page_url,
            "page_image": image,
            "structured_data": structured_data,
        },
    )
    return spa_with_head(seo_head)
