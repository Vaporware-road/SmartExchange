/**
 * Content leaves are `{ locale: text }` maps so one publication serves every
 * language the desk enabled. Everything that renders text goes through here.
 */

/** One string out of a localized map, preferring `locale` then the site default. */
export function localize(value, locale, primaryLocale) {
  if (typeof value === 'string') return value
  if (!value || typeof value !== 'object') return ''
  for (const candidate of [locale, primaryLocale, '']) {
    const text = value[candidate]
    if (text) return text
  }
  // A field filled in for one language only still beats a blank page.
  return Object.values(value).find((text) => typeof text === 'string' && text) || ''
}

/** True when a localized field has nothing in it for any language. */
export function isBlank(value) {
  if (typeof value === 'string') return !value.trim()
  if (!value || typeof value !== 'object') return true
  return !Object.values(value).some((text) => typeof text === 'string' && text.trim())
}

const RTL_LOCALES = new Set(['fa', 'ar', 'he', 'ur'])

export function directionFor(locale) {
  return RTL_LOCALES.has(locale) ? 'rtl' : 'ltr'
}

/* Sections whose worth does not come from typed text: the header and footer
   always draw branding, and the rate board draws prices. */
const ALWAYS_RENDER = new Set(['header', 'footer', 'rates'])

/**
 * True when a section has nothing to say.
 *
 * A published page must not reserve a screenful of padding for a block the
 * owner never filled in — a new site would read as broken. Booleans and numbers
 * do not count: they are settings that ship with defaults, not content.
 */
export function isSectionBlank(section, branding = {}) {
  if (ALWAYS_RENDER.has(section.type)) return false
  const content = section.content || {}
  if (Object.values(content).some(hasValue)) return false
  // Contact is the one block that can be full without a word typed into it:
  // by default it shows the phone and address already in panel Settings.
  if (section.type === 'contact' && content.inherit_panel_contact !== false) {
    return !hasValue(branding.contact)
  }
  return true
}

function hasValue(value) {
  if (typeof value === 'string') return Boolean(value.trim())
  if (Array.isArray(value)) return value.length > 0
  if (value && typeof value === 'object') return Object.values(value).some(hasValue)
  return false
}
