/** Supported UI locales — order matches language picker. */
export const LOCALES = [
  { code: 'en', label: 'English', shortLabel: 'EN', dir: 'ltr', formatLocale: 'en' },
  { code: 'fa', label: 'فارسی', shortLabel: 'FA', dir: 'rtl', formatLocale: 'fa', jalali: true },
  { code: 'ar', label: 'العربية', shortLabel: 'AR', dir: 'rtl', formatLocale: 'ar' },
  { code: 'es', label: 'Español', shortLabel: 'ES', dir: 'ltr', formatLocale: 'es' },
]

export const SUPPORTED_LOCALE_CODES = LOCALES.map((l) => l.code)

const RTL_SET = new Set(LOCALES.filter((l) => l.dir === 'rtl').map((l) => l.code))

export function isRtlLocale(code) {
  return RTL_SET.has(code)
}

export function getLocaleMeta(code) {
  return LOCALES.find((l) => l.code === code) ?? LOCALES[0]
}

export function resolveFormatLocale(uiLocale) {
  return getLocaleMeta(uiLocale).formatLocale
}
