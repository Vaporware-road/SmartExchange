import json

from django.http import HttpResponse
from django.template.loader import render_to_string

from MrExchangePanel.views import spa_index_path, spa_not_built_response

from . import tutorials

_OG_IMAGE = f"{tutorials.SITE_URL}/static/landing/images/Mr%20Exchange.png"


def _spa_with_head(seo_head):
    """The built SPA shell with its generic ``<title>`` swapped for ``seo_head``.

    Only the crawler-facing metadata is rendered here: the SPA fills ``<head>``
    after hydration, which is too late for a bot that never runs the bundle.
    """
    index_path = spa_index_path()
    if index_path is None:
        return spa_not_built_response()

    shell = index_path.read_text()
    # Drop the shell's generic <title> first: browsers and crawlers honour the
    # first <title> in the document, so leaving it would shadow ours.
    html = shell.replace("<title>MrExchange</title>", "", 1)
    # The shell always carries a </head>; str.replace is a no-op if it ever does not.
    html = html.replace("</head>", f"{seo_head}\n</head>", 1)

    response = HttpResponse(html, content_type="text/html")
    response["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


def landing_page(request):
    """
    Public marketing page at `/`.

    The page itself is Vue (`views/landing/LandingView.vue`) and is served from
    the same SPA shell as the panel, so the marketing site and the product it
    sells share one design system and one set of translations.
    """
    # No `request=`: the fragment is static, and passing one would run every
    # context processor (a SiteSettings query included) on every page view.
    return _spa_with_head(render_to_string("landing/seo_head.html"))


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
    return _spa_with_head(seo_head)


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
    return _spa_with_head(seo_head)
