import { defineStore } from 'pinia'
import { authApi } from '@/services/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    loading: false,
    initialized: false,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
    username: (state) => state.user?.username ?? '',
    role: (state) => state.user?.role ?? null,
    isManager() { return this.role === 'management' },
    isDeveloper() { return this.role === 'developer' },
    isEmployee() { return this.role === 'employee' },
    canAccessSettings() { return this.isManager || this.isDeveloper },
    canDeleteItems() { return this.isManager },
  },

  actions: {
    async fetchUser() {
      if (this.loading) return
      this.loading = true
      try {
        const { data } = await authApi.me()
        this.user = data
        return data
      } catch {
        this.user = null
        return null
      } finally {
        this.loading = false
        this.initialized = true
      }
    },

    async login(username, password) {
      this.loading = true
      try {
        const { data } = await authApi.login(username, password)
        if (data.access) localStorage.setItem('access_token', data.access)
        if (data.refresh) localStorage.setItem('refresh_token', data.refresh)
        this.user = data.user ?? data
        return this.user
      } finally {
        this.loading = false
      }
    },

    async logout() {
      try {
        const refresh = localStorage.getItem('refresh_token')
        await authApi.logout(refresh)
      } finally {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        this.user = null
      }
    },

    ensureInitialized() {
      if (!this.initialized && !this.loading) {
        return this.fetchUser()
      }
    },
  },
})
