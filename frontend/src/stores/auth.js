import { defineStore } from 'pinia'
import { authApi } from '@/services/api'
import { can as canPermission, ROLES, PERMISSIONS } from '@/config/permissions'
import { useTelegramHubStore } from '@/stores/telegramHub'

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

    isSuperAdmin() {
      return this.role === ROLES.SUPER_ADMIN
    },
    isManager() {
      return this.role === ROLES.MANAGEMENT
    },
    isDeveloper() {
      return this.role === ROLES.DEVELOPER
    },
    isEmployee() {
      return this.role === ROLES.EMPLOYEE
    },

    /** دسترسی به نهایی‌سازی (فاینالایز) — فقط super_admin و management */
    canAccessFinalize() {
      return canPermission(this.role, 'finalize')
    },
    /** دسترسی به تنظیمات پنل — فقط super_admin (backend: IsSuperAdmin) */
    canAccessSettings() {
      return canPermission(this.role, 'settings')
    },
    /** دسترسی به تحلیل — همه نقش‌ها */
    canAccessAnalysis() {
      return canPermission(this.role, 'analysis')
    },
    /** دسترسی به ربات و کانال تلگرام — super_admin، management و employee */
    canAccessTelegram() {
      return canPermission(this.role, 'telegram')
    },
    /** دسترسی به مدیریت کاربران/ادمین — فقط super_admin (backend: IsSuperAdmin) */
    canAccessUserCenter() {
      return canPermission(this.role, 'adminManagement')
    },
    /** اجازه حذف آیتم‌ها — فقط super_admin و management */
    canDeleteItems() {
      return canPermission(this.role, 'deleteItems')
    },
    canAccessProgrammerHub() {
      return canPermission(this.role, 'programmerHub')
    },
    isImpersonating() {
      return Boolean(this.user?.impersonated_by)
    },
    /** Shared public demo account — the panel labels the session and offers the tour. */
    isDemo() {
      return Boolean(this.user?.is_demo)
    },
    shouldOpenProgrammerHub() {
      return this.canAccessProgrammerHub && !this.isImpersonating
    },
  },

  actions: {
    /**
     * Check access for a permission key (e.g. 'settings', 'analysis', 'adminManagement').
     * Must be an action so it can accept arguments (Pinia getters don't take params).
     */
    can(permission) {
      return canPermission(this.role, permission)
    },

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
        sessionStorage.removeItem('programmer_access_token')
        sessionStorage.removeItem('programmer_refresh_token')
        this.user = data.user ?? data
        useTelegramHubStore().clearSession()
        return this.user
      } finally {
        this.loading = false
      }
    },

    async demoLogin() {
      this.loading = true
      try {
        const { data } = await authApi.demoLogin()
        if (data.access) localStorage.setItem('access_token', data.access)
        if (data.refresh) localStorage.setItem('refresh_token', data.refresh)
        sessionStorage.removeItem('programmer_access_token')
        sessionStorage.removeItem('programmer_refresh_token')
        this.user = data.user ?? data
        useTelegramHubStore().clearSession()
        return this.user
      } finally {
        this.loading = false
      }
    },

    async logout() {
      const refresh = localStorage.getItem('refresh_token')
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      sessionStorage.removeItem('programmer_access_token')
      sessionStorage.removeItem('programmer_refresh_token')
      this.user = null
      useTelegramHubStore().clearSession()
      try {
        await authApi.logout(refresh)
      } catch {
        // Ignore network/logout endpoint failures; client session is already cleared.
      }
    },

    async impersonate(userId) {
      const programmerUsername = this.username
      const { data } = await authApi.impersonate(userId)
      sessionStorage.setItem('programmer_access_token', localStorage.getItem('access_token') || '')
      sessionStorage.setItem('programmer_refresh_token', localStorage.getItem('refresh_token') || '')
      if (data.access) localStorage.setItem('access_token', data.access)
      if (data.refresh) localStorage.setItem('refresh_token', data.refresh)
      const nextUser = data.user ?? data
      this.user = nextUser?.impersonated_by
        ? nextUser
        : { ...nextUser, impersonated_by: { username: programmerUsername } }
      useTelegramHubStore().clearSession()
      return this.user
    },

    async stopImpersonating() {
      const access = sessionStorage.getItem('programmer_access_token')
      const refresh = sessionStorage.getItem('programmer_refresh_token')
      sessionStorage.removeItem('programmer_access_token')
      sessionStorage.removeItem('programmer_refresh_token')
      if (access) localStorage.setItem('access_token', access)
      if (refresh) localStorage.setItem('refresh_token', refresh)
      if (!access) {
        this.user = null
        useTelegramHubStore().clearSession()
        return null
      }
      useTelegramHubStore().clearSession()
      return this.fetchUser()
    },

    ensureInitialized() {
      if (!this.initialized && !this.loading) {
        return this.fetchUser()
      }
    },
  },
})
