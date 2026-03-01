import { defineStore } from 'pinia'
import { authApi } from '@/services/api'
import { can as canPermission, ROLES, PERMISSIONS } from '@/config/permissions'

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
    /** دسترسی به تنظیمات پنل — فقط super_admin و management */
    canAccessSettings() {
      return canPermission(this.role, 'settings')
    },
    /** دسترسی به تحلیل — همه نقش‌ها */
    canAccessAnalysis() {
      return canPermission(this.role, 'analysis')
    },
    /** دسترسی به مدیریت کاربران/ادمین — فقط super_admin و management */
    canAccessUserCenter() {
      return canPermission(this.role, 'adminManagement')
    },
    /** اجازه حذف آیتم‌ها — همه نقش‌ها */
    canDeleteItems() {
      return canPermission(this.role, 'deleteItems')
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
