import { createI18n } from 'vue-i18n'
import fa from '@/locales/fa.json'
import en from '@/locales/en.json'
import ar from '@/locales/ar.json'
import es from '@/locales/es.json'
import {
  STORAGE_LOCALE,
  STORAGE_LOCALE_LEGACY,
  storageGet,
  storageSet,
} from '@/constants/branding.js'
import { isRtlLocale, SUPPORTED_LOCALE_CODES } from '@/constants/locales.js'

const safeStorage = {
  get() {
    return storageGet(STORAGE_LOCALE, STORAGE_LOCALE_LEGACY)
  },
  set(value) {
    storageSet(STORAGE_LOCALE, STORAGE_LOCALE_LEGACY, value)
  },
}

const savedLocale = safeStorage.get() || 'en'
const initialLocale = SUPPORTED_LOCALE_CODES.includes(savedLocale) ? savedLocale : 'en'

const enMessages = en?.default ?? en
const faMessages = fa?.default ?? fa
const arMessages = ar?.default ?? ar
const esMessages = es?.default ?? es

/** Resolve nested key (e.g. "dashboard.title") from a messages object */
function getMessageByPath(obj, path) {
  if (!obj || typeof path !== 'string') return undefined
  const keys = path.split('.')
  let current = obj
  for (const k of keys) {
    if (current == null || typeof current !== 'object') return undefined
    current = current[k]
  }
  return typeof current === 'string' ? current : undefined
}

function applyDocumentLocale(locale) {
  document.documentElement.lang = locale
  document.documentElement.dir = isRtlLocale(locale) ? 'rtl' : 'ltr'
}

const i18n = createI18n({
  legacy: true,
  locale: initialLocale,
  fallbackLocale: 'en',
  globalInjection: true,
  missingWarn: false,
  fallbackWarn: false,
  messages: {
    en: enMessages,
    fa: faMessages,
    ar: arMessages,
    es: esMessages,
  },
  missing: (locale, key) => {
    const fallback = getMessageByPath(enMessages, key)
    return fallback ?? key
  },
})

applyDocumentLocale(initialLocale)

export function setLocale(locale) {
  const next = SUPPORTED_LOCALE_CODES.includes(locale) ? locale : 'en'
  const g = i18n.global
  if (typeof g.locale === 'string') {
    g.locale = next
  } else if (g.locale && typeof g.locale === 'object' && 'value' in g.locale) {
    g.locale.value = next
  }
  safeStorage.set(next)
  applyDocumentLocale(next)
}

export default i18n
