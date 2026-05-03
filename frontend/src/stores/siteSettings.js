import { defineStore } from 'pinia'
import { settingsApi, templateEditorApi } from '@/services/api'
import i18n from '@/i18n'
import { editorFontFamilyToken, injectTemplateEditorFontFaces } from '@/pages/templates/templateEditorFonts'

function normalizeAssetUrl(value) {
  if (!value || typeof value !== 'string') return value
  const trimmed = value.trim()
  if (!trimmed) return trimmed
  if (typeof window === 'undefined') return trimmed

  // Already relative to current origin.
  if (trimmed.startsWith('/media/') || trimmed.startsWith('/static/')) return trimmed

  try {
    const parsed = new URL(trimmed, window.location.origin)
    const isAssetPath = parsed.pathname.startsWith('/media/') || parsed.pathname.startsWith('/static/')
    if (!isAssetPath) return trimmed

    // If backend returns a non-browser-reachable host (e.g. 127.0.0.1:8000 or docker internal host),
    // keep only path so browser uses current origin/proxy.
    if (parsed.origin !== window.location.origin) {
      return `${parsed.pathname}${parsed.search}${parsed.hash}`
    }
  } catch {
    return trimmed
  }
  return trimmed
}

export const useSiteSettingsStore = defineStore('siteSettings', {
  state: () => ({
    settings: {
      site_name: 'SmartExchange',
      tagline: 'Premium Exchange Panel',
      logo: null,
      favicon: null,
      support_phone: '',
      support_phone_2: '',
      support_phone_3: '',
      base_currency_code: 'USD',
      support_email: '',
      address: '',
      office_map_url: '',
      business_hours: '',
      telegram_link: '',
      instagram_link: '',
      twitter_link: '',
      linkedin_link: '',
      ui_font_filename_rtl: '',
      ui_font_filename_ltr: '',
    },
    loading: false,
  }),

  getters: {
    siteName: (state) => state.settings.site_name ?? 'SmartExchange',
    tagline: (state) => state.settings.tagline ?? 'Premium Exchange Panel',
  },

  actions: {
    applySettings(data = {}) {
      const normalized = { ...data }
      if (Object.hasOwn(normalized, 'logo')) {
        normalized.logo = normalizeAssetUrl(normalized.logo)
      }
      if (Object.hasOwn(normalized, 'favicon')) {
        normalized.favicon = normalizeAssetUrl(normalized.favicon)
      }
      this.settings = { ...this.settings, ...normalized }
      this._applyDynamicAssets(this.settings)
      if (typeof window !== 'undefined') {
        queueMicrotask(() => {
          this.refreshUiTypography(this.settings).catch(() => {})
        })
      }
    },

    async fetch() {
      this.loading = true
      try {
        const { data } = await settingsApi.site()
        this.applySettings(data)
        return data
      } catch {
        return this.settings
      } finally {
        this.loading = false
      }
    },

    _applyDynamicAssets(data) {
      const t = i18n.global.t
      const name = data.site_name || 'SmartExchange'
      document.title = `${name} | ${t('common.panel')}`

      if (data.favicon) {
        let link = document.querySelector("link[rel~='icon']")
        if (!link) {
          link = document.createElement('link')
          link.rel = 'icon'
          document.head.appendChild(link)
        }
        link.href = data.favicon
      }
    },

    /**
     * Set --font-ui-rtl / --font-ui-ltr and inject @font-face rules for /static/fonts (full list when API allows).
     */
    async refreshUiTypography(settings) {
      if (typeof document === 'undefined') return
      const s = settings || this.settings
      const rtl = String(s?.ui_font_filename_rtl || '').trim()
      const ltr = String(s?.ui_font_filename_ltr || '').trim()
      const tokenRtl = rtl ? editorFontFamilyToken(rtl) : ''
      const tokenLtr = ltr ? editorFontFamilyToken(ltr) : ''
      const stackRtl = tokenRtl
        ? `'${tokenRtl}', Vazirmatn, system-ui, -apple-system, sans-serif`
        : `'Vazirmatn', system-ui, -apple-system, sans-serif`
      const stackLtr = tokenLtr
        ? `'${tokenLtr}', Inter, system-ui, sans-serif`
        : `'Inter', system-ui, -apple-system, sans-serif`
      document.documentElement.style.setProperty('--font-ui-rtl', stackRtl)
      document.documentElement.style.setProperty('--font-ui-ltr', stackLtr)

      const minimal = [...new Set([rtl, ltr].filter(Boolean))].map((fn) => ({
        filename: fn,
        display_name: fn,
      }))
      try {
        const { data } = await templateEditorApi.fonts()
        injectTemplateEditorFontFaces(Array.isArray(data) ? data : [])
      } catch {
        injectTemplateEditorFontFaces(minimal)
      }
    },
  },
})
