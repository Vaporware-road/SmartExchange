import { defineStore } from 'pinia'
import { settingsApi } from '@/services/api'
import i18n from '@/i18n'

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
      support_email: '',
      address: '',
      office_map_url: '',
      business_hours: '',
      telegram_link: '',
      instagram_link: '',
      twitter_link: '',
      linkedin_link: '',
    },
    loading: false,
  }),

  getters: {
    siteName: (state) => state.settings.site_name ?? 'SmartExchange',
    tagline: (state) => state.settings.tagline ?? 'Premium Exchange Panel',
  },

  actions: {
    async fetch() {
      this.loading = true
      try {
        const { data } = await settingsApi.site()
        this.settings = data
        this._applyDynamicAssets(data)
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
  },
})
