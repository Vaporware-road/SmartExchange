import { createI18n } from 'vue-i18n'
import fa from '@/locales/fa.json'
import en from '@/locales/en.json'

const savedLocale = localStorage.getItem('smartexchange-locale') || 'en'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'fa',
  messages: { en, fa },
})

export function setLocale(locale) {
  i18n.global.locale.value = locale
  localStorage.setItem('smartexchange-locale', locale)
  document.documentElement.lang = locale
  document.documentElement.dir = locale === 'fa' ? 'rtl' : 'ltr'
}

export default i18n
