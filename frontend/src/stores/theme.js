import { defineStore } from 'pinia'

const STORAGE_KEY = 'smartexchange-theme'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: true,
  }),

  getters: {
    isLight: (state) => !state.isDark,
  },

  actions: {
    init() {
      const stored = localStorage.getItem(STORAGE_KEY)
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
      localStorage.setItem(STORAGE_KEY, this.isDark ? 'dark' : 'light')
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
