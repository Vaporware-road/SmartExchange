# Landing app

The public marketing site served at `/`. It is a Vue page inside the panel's own
SPA, not a separate stack: the marketing site and the product it sells share one
design system, one component set and one set of translations.

| Piece | Path |
|---|---|
| Page | `frontend/src/views/landing/LandingView.vue` |
| Sections | `frontend/src/views/landing/components/` |
| Animation | `frontend/src/views/landing/composables/` |
| Styles | `frontend/src/views/landing/landing.css` + Tailwind + the app's design tokens |
| Prices, phone, links | `frontend/src/config/landing.js` |
| Copy (7 languages) | `landing.*` in `frontend/src/locales/*.json` |
| Crawler metadata | `landing/templates/landing/seo_head.html` |
| Video / logo | `static/landing/Demo.mp4`, `static/landing/images/` |

## How `/` is served

`landing.views.landing_page` reads the built SPA shell — the same file `SPAView`
serves — strips its generic `<title>`, injects `seo_head.html` into `<head>`, and
returns it. The Vue router then renders `LandingView` for `/`.

Only the crawler-facing metadata is server-rendered: title, description, OG and
Twitter cards, and the `SoftwareApplication` / `Organization` / `FAQPage`
JSON-LD. Everything a human reads comes from the SPA. **Keep the JSON-LD FAQ in
step with `landing.faq` in the locale files** — a crawler that reads one and a
visitor who reads the other must not be told different things.

## Editing copy

Every string is a `landing.*` key in `frontend/src/locales/<lang>.json`, across
`en` (default), `fa`, `ar`, `de`, `fr`, `es` and `tr`. Adding a string means
adding the key to all seven; a key missing from one falls back to `en`, which
reads as a bug to that visitor.

Numbers are not copy. Prices, the sales phone number, the WhatsApp deep link and
the Telegram channel handle all live in `frontend/src/config/landing.js` — change
them once there, not in seven dictionaries.

The Telegram channel handle is a placeholder (`TELEGRAM_CHANNEL`); point it at
the real channel when it is live and the nav, the channel section and the footer
all follow.

## Pricing

One package at a one-off price, plus add-ons. `ADDONS` carries both our price and
`market`, the researched 2026 going rate for the same service; the cards render
the market figure struck through beside ours. If you change a price, keep ours
below the market figure or the comparison stops being honest.

Monthly support is an add-on and is marked optional — the panel runs without it.

## Animation

No animation library. `composables/` holds the hero particle canvas, the
scroll-reveal observer, the stat count-up and the live-price jitter; the marquees
and everything else are CSS. Every one of them is disabled under
`prefers-reduced-motion`.

Marquees (`LandingMarquee.vue`) render their item list **twice** and translate the
track by exactly `-50%`. The end frame is then identical to the start, so the
loop is seamless — no visible seam, no snap back to the beginning. Anything that
scrolls forever on this page must be built that way.
