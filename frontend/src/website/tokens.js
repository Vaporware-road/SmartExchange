/**
 * Turning a resolved theme into something the DOM can use.
 *
 * Themes are CSS custom properties rather than classes on purpose: a class name
 * assembled at runtime from JSON would never be seen by Tailwind's scanner and
 * would silently not exist. Custom properties are resolved by the browser, so a
 * theme the owner picks after build time still works.
 */

const FONT_LINK_ID = 'ws-font-link'
const loadedFamilies = new Set()

/* Shipped with the app in `website.css`; asking Google for them again would be
   a request that can only make the page slower. */
const SELF_HOSTED = new Set(['Vazirmatn', 'Inter'])

/** `{ '--ws-bg': '#fff' }` as an inline style object for the site wrapper. */
export function tokenStyle(theme) {
  if (!theme || !theme.tokens) return {}
  return { ...theme.tokens }
}

/** The `data-*` hooks `website.css` keys its button, card and background looks off. */
export function styleAttrs(theme) {
  const styles = theme?.styles || {}
  return {
    'data-ws-mode': theme?.mode || 'light',
    'data-ws-button': styles.button || 'solid',
    'data-ws-card': styles.card || 'flat',
    'data-ws-background': styles.background || 'plain',
  }
}

/**
 * Pull in the theme's web fonts once.
 *
 * Loaded on demand rather than bundled: a desk uses one pair, and shipping all
 * six would cost every visitor five downloads they never render a glyph from.
 */
export function ensureFonts(families) {
  if (typeof document === 'undefined' || !Array.isArray(families)) return
  const wanted = families.filter(
    (family) => family && !loadedFamilies.has(family) && !SELF_HOSTED.has(familyName(family)),
  )
  if (!wanted.length) return
  wanted.forEach((family) => loadedFamilies.add(family))

  const query = [...loadedFamilies].map((family) => `family=${family}`).join('&')
  let link = document.getElementById(FONT_LINK_ID)
  if (!link) {
    link = document.createElement('link')
    link.id = FONT_LINK_ID
    // Loaded out of the critical path: every theme's stack falls back to a
    // self-hosted face, so a slow or blocked CDN must never hold up first paint.
    link.rel = 'stylesheet'
    link.media = 'print'
    link.onload = () => {
      link.media = 'all'
    }
    document.head.appendChild(link)
  }
  link.href = `https://fonts.googleapis.com/css2?${query}&display=swap`
}

/** 'Space+Grotesk:wght@400;700' -> 'Space Grotesk' */
function familyName(spec) {
  return spec.split(':')[0].replaceAll('+', ' ')
}
