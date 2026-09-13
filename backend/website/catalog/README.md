# Website catalog

The single source of truth for what a customer website can be made of.

Four JSON files, read by **both** sides:

| File | Backend use | Frontend use |
|---|---|---|
| `sections.json` | validates section types, variants and content field names | generates the content forms, picks the variant component |
| `layouts.json` | validates `WebsiteSite.layout_slug`, seeds a new site's sections | renders the page chrome and default variants |
| `themes.json` | validates `theme_slug`, resolves tokens into a publication snapshot | applies `--ws-*` custom properties |
| `styles.json` | validates `theme_overrides` values | renders the style-modifier pickers |

The SPA imports these at build time through the `@catalog` Vite alias, so there is one
copy and no sync step. `website/tests.py::CatalogIntegrityTests` fails the build if a
catalog entry has no matching component in `frontend/src/website/registry.js`, or if a
theme is missing a token.

Adding a layout is a manifest entry plus, at most, one new section variant — never a new
page. That is the whole point of the split.
