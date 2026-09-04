/**
 * Number and date formatting tied to the app's UI language,
 * not the browser default locale (which caused wrong digit shapes).
 */

import { resolveFormatLocale } from '@/constants/locales.js'

const PRESETS = {
  en: { tag: 'en-US', numberingSystem: 'latn' },
  fa: { tag: 'fa-IR', numberingSystem: 'arabext' },
  ar: { tag: 'ar-SA', numberingSystem: 'latn' },
  es: { tag: 'es-ES', numberingSystem: 'latn' },
}

function pack(appLocale) {
  return PRESETS[appLocale] ?? PRESETS.en
}

export { resolveFormatLocale }

export function formatAppNumber(appLocale, value, options = {}) {
  const { tag, numberingSystem } = pack(resolveFormatLocale(appLocale))
  const n = Number(value)
  if (value == null || value === '' || !Number.isFinite(n)) {
    if (value == null || value === '') return ''
    return String(value)
  }
  try {
    return new Intl.NumberFormat(tag, { numberingSystem, ...options }).format(n)
  } catch {
    return new Intl.NumberFormat(tag, options).format(n)
  }
}

export function formatAppDecimal(appLocale, value, fractionDigits = 2) {
  return formatAppNumber(appLocale, value, {
    minimumFractionDigits: fractionDigits,
    maximumFractionDigits: fractionDigits,
  })
}

export function createAppDateTimeFormat(appLocale, options = {}) {
  const { tag, numberingSystem } = pack(resolveFormatLocale(appLocale))
  try {
    return new Intl.DateTimeFormat(tag, { numberingSystem, ...options })
  } catch {
    return new Intl.DateTimeFormat(tag, options)
  }
}
