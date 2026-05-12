import { defineStore } from 'pinia'
import { STORAGE_THEME, STORAGE_THEME_LEGACY, storageGet, storageSet } from '@/constants/branding.js'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: true,
  }),

  getters: {
    isLight: (state) => !state.isDark,
  },

  actions: {
    init() {
      const stored = storageGet(STORAGE_THEME, STORAGE_THEME_LEGACY)
      if (stored === 'light' || stored === 'dark') {
        this.isDark = stored === 'dark'
      } else if (window.matchMedia?.('(prefers-color-scheme: light)').matches) {
        this.isDark = false
      }
      this.apply()
    },

    apply() {
      const root = document.documentElement
      if (this.isDark) {
        root.classList.add('dark')
      } else {
        root.classList.remove('dark')
      }
      storageSet(STORAGE_THEME, STORAGE_THEME_LEGACY, this.isDark ? 'dark' : 'light')
    },

    toggle() {
      this.isDark = !this.isDark
      this.apply()
    },

    set(mode) {
      this.isDark = mode === 'dark'
      this.apply()
    },
  },
})
