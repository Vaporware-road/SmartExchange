import { defineStore } from 'pinia'
import { STORAGE_THEME, STORAGE_THEME_LEGACY, storageGet, storageSet } from '@/constants/branding.js'

const THEMES = ['light', 'dark', 'black-gold']
const DEFAULT_THEME = 'dark'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    /** 'light' | 'dark' | 'black-gold' */
    theme: DEFAULT_THEME,
  }),

  getters: {
    isDark: (state) => state.theme !== 'light',
    isLight: (state) => state.theme === 'light',
    isBlackGold: (state) => state.theme === 'black-gold',
  },

  actions: {
    init() {
      const stored = storageGet(STORAGE_THEME, STORAGE_THEME_LEGACY)
      if (THEMES.includes(stored)) {
        this.theme = stored
      } else if (stored === 'dark' || stored === 'light') {
        // Legacy binary values
        this.theme = stored
      } else if (window.matchMedia?.('(prefers-color-scheme: light)').matches) {
        this.theme = 'light'
      } else {
        this.theme = DEFAULT_THEME
      }
      this.apply()
    },

    apply() {
      const root = document.documentElement
      // Clear all theme classes
      root.classList.remove('dark', 'black-gold')
      if (this.theme === 'dark') {
        root.classList.add('dark')
      } else if (this.theme === 'black-gold') {
        root.classList.add('black-gold')
      }
      storageSet(STORAGE_THEME, STORAGE_THEME_LEGACY, this.theme)
    },

    toggle() {
      // Cycle: light → dark → black-gold → light
      const idx = THEMES.indexOf(this.theme)
      this.theme = THEMES[(idx + 1) % THEMES.length]
      this.apply()
    },

    set(mode) {
      if (THEMES.includes(mode)) {
        this.theme = mode
      }
      this.apply()
    },
  },
})