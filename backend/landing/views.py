from django.http import HttpResponse
from django.template.loader import render_to_string

from MrExchangePanel.views import spa_index_path, spa_not_built_response


def landing_page(request):
    """
    Public marketing page at `/`.

    The page itself is Vue (`views/landing/LandingView.vue`) and is served from
    the same SPA shell as the panel, so the marketing site and the product it
    sells share one design system and one set of translations. Only the
    crawler-facing metadata is rendered here: the SPA fills `<head>` after
    hydration, which is too late for a bot that never runs the bundle.
    """
    index_path = spa_index_path()
    if index_path is None:
        return spa_not_built_response()

    shell = index_path.read_text()
    # No `request=`: the fragment is static, and passing one would run every
    # context processor (a SiteSettings query included) on every page view.
    seo_head = render_to_string("landing/seo_head.html")
    # Drop the shell's generic <title> first: browsers and crawlers honour the
    # first <title> in the document, so leaving it would shadow the marketing one.
    html = shell.replace("<title>MrExchange</title>", "", 1)
    # The shell always carries a </head>; str.replace is a no-op if it ever does not.
    html = html.replace("</head>", f"{seo_head}\n</head>", 1)

    response = HttpResponse(html, content_type="text/html")
    response["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response
