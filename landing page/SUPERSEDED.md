# Superseded — do not deploy

This directory is the cPanel deployment shell for the old standalone
"mr. sarafi" static marketing site. It is **retired**.

The single MrExchange marketing site is now the Django landing app:

- app: `backend/landing/`
- page: `frontend/src/views/landing/LandingView.vue` (served through `backend/landing/views.py`)
- route: `/` (see `backend/MrExchangePanel/urls.py`)
- assets: `backend/static/landing/`

Only `robots.txt` and `sitemap.xml` are kept here, pointing at the Django-served
site, so the existing cPanel document root keeps serving valid SEO files until
DNS for `mrexchange.co.uk` is cut over to the panel host. `.cpanel.yml` is kept
for that cut-over window and still refuses to run until a real cPanel username
is set.

Delete this directory once DNS points at the panel host.
