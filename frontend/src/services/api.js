import axios from 'axios'
import { useToast } from 'vue-toastification'
import i18n from '@/i18n'
import router from '@/router'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  },
  withCredentials: true,
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const toast = useToast()
    const status = error.response?.status

    const isAuthCheck = error.config?.url?.includes('/auth/me')

    if (status === 401) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      window.location.href = '/login'
    } else if (status === 403 && !isAuthCheck) {
      toast.error(i18n.global.t('errors.forbidden'))
    } else if (status >= 500) {
      const logId = error.response?.data?.log_id ?? error.response?.data?.error_id ?? error.response?.data?.request_id
      const currentName = router.currentRoute?.value?.name
      if (currentName !== 'error-500' && currentName !== 'not-found') {
        router.push({ name: 'error-500', query: logId != null ? { logId: String(logId) } : {} })
      }
      toast.error(i18n.global.t('errors.serverError'))
    } else if (!error.response) {
      toast.error(i18n.global.t('errors.networkError'))
    }

    return Promise.reject(error)
  }
)

export const authApi = {
  login: (username, password) =>
    api.post('/auth/login/', { username, password }),
  logout: (refresh) => api.post('/auth/logout/', { refresh }),
  me: () => api.get('/auth/me/'),
  users: {
    list: (params) => api.get('/auth/users/', { params }),
    create: (data) => api.post('/auth/users/', data),
    get: (id) => api.get(`/auth/users/${id}/`),
    update: (id, data) => api.patch(`/auth/users/${id}/`, data),
    forceLogout: (id) => api.post(`/auth/users/${id}/force-logout/`),
  },
  activity: (params) => api.get('/auth/activity/', { params }),
}

export const dashboardApi = {
  summary: () => api.get('/dashboard/summary/'),
}

export const categoryApi = {
  list: () => api.get('/categories/'),
  create: (data) => api.post('/categories/', data),
  get: (id) => api.get(`/categories/${id}/`),
  update: (id, data) => api.put(`/categories/${id}/`, data),
  patch: (id, data) => api.patch(`/categories/${id}/`, data),
  delete: (id) => api.delete(`/categories/${id}/`),
  uploadTelegramMedia: (id, formData) =>
    api.post(`/categories/${id}/telegram-media/`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  addPriceType: (categoryId, data) =>
    api.post(`/categories/${categoryId}/price-types/`, data),
  reorderPriceTypes: (categoryId, orderIds) =>
    api.post(`/categories/${categoryId}/price-types/reorder/`, { order: orderIds }),
}

export const priceTypeApi = {
  get: (categoryId, id) => api.get(`/categories/${categoryId}/price-types/${id}/`),
  update: (categoryId, id, data) => api.put(`/categories/${categoryId}/price-types/${id}/`, data),
  patch: (categoryId, id, data) => api.patch(`/categories/${categoryId}/price-types/${id}/`, data),
  delete: (categoryId, id) => api.delete(`/categories/${categoryId}/price-types/${id}/`),
}

export const priceApi = {
  list: () => api.get('/prices/'),
  get: (id) => api.get(`/prices/${id}/`),
  update: (priceTypeId, data) =>
    api.post(`/prices/${priceTypeId}/update/`, data),
  bulkUpdate: (categoryId, data) =>
    api.post(`/prices/category/${categoryId}/bulk-update/`, data),
  history: (priceTypeId) =>
    api.get(`/prices/${priceTypeId}/history/`),
}

export const specialPriceApi = {
  list: () => api.get('/special-prices/'),
  create: (data) => api.post('/special-prices/', data),
  get: (id) => api.get(`/special-prices/${id}/`),
  update: (id, data) => api.put(`/special-prices/${id}/`, data),
  delete: (id) => api.delete(`/special-prices/${id}/`),
  updatePrice: (id, data) =>
    api.post(`/special-prices/${id}/update-price/`, data),
  history: (id) => api.get(`/special-prices/${id}/history/`),
}

export const finalizeApi = {
  dashboard: () => api.get('/finalize/dashboard/'),
  finalizeCategory: (categoryId, data) =>
    api.post(`/finalize/category/${categoryId}/`, data),
  finalizeSpecialPrice: (specialPriceId, data) =>
    api.post(`/finalize/special-price/${specialPriceId}/`, data),
  finalizeAll: (data) => api.post('/finalize/all/', data),
}

export const instagramHubApi = {
  preview: (data) => api.post('/instagram-hub/preview/', data),
  status: () => api.get('/instagram-hub/status/'),
  getConfig: () => api.get('/instagram-hub/config/'),
  patchConfig: (data) => api.patch('/instagram-hub/config/', data),
}

export const settingsApi = {
  site: () => api.get('/settings/site/'),
  updateSite: (data) => api.put('/settings/site/', data),
  logs: (params) => api.get('/settings/logs/', { params }),
}

export const analysisApi = {
  pricing: () => api.get('/analysis/pricing/'),
  dashboard: () => api.get('/analysis/dashboard/'),
}

export const telegramApi = {
  channels: () => api.get('/telegram/channels/'),
  sendMessage: (data) => api.post('/telegram/send-message/', data),
  bots: {
    list: () => api.get('/telegram/bots/'),
    create: (data) => api.post('/telegram/bots/', data),
    update: (id, data) => api.put(`/telegram/bots/${id}/`, data),
    delete: (id) => api.delete(`/telegram/bots/${id}/`),
    testConnection: (id, data) =>
      api.post(`/telegram/bots/${id}/test-connection/`, data),
  },
  channelsManage: {
    list: () => api.get('/telegram/channels/manage/'),
    create: (data) => api.post('/telegram/channels/manage/', data),
    update: (id, data) => api.put(`/telegram/channels/manage/${id}/`, data),
    delete: (id) => api.delete(`/telegram/channels/manage/${id}/`),
  },
  autoPostConfig: {
    list: () => api.get('/telegram/auto-post-config/'),
    create: (data) => api.post('/telegram/auto-post-config/', data),
    update: (id, data) => api.put(`/telegram/auto-post-config/${id}/`, data),
    delete: (id) => api.delete(`/telegram/auto-post-config/${id}/`),
  },
  automationSettings: {
    get: () => api.get('/telegram/automation-settings/'),
    update: (data) => api.put('/telegram/automation-settings/', data),
  },
}

export const templateApi = {
  list: () => api.get('/templates/'),
  create: (data) => api.post('/templates/', data),
  get: (id) => api.get(`/templates/${id}/`),
  update: (id, data) => api.put(`/templates/${id}/`, data),
  delete: (id) => api.delete(`/templates/${id}/`),
}

export const templateEditorApi = {
  list: () => api.get('/template-editor/templates/'),
  get: (id) => api.get(`/template-editor/templates/${id}/`),
  create: (data) => api.post('/template-editor/templates/', data),
  update: (id, data) => api.put(`/template-editor/templates/${id}/`, data),
  updateConfig: (id, config) =>
    api.put(`/template-editor/templates/${id}/config/`, { config }),
  preview: (id, config = null, themeName = null) => {
    const payload = config != null ? { config, theme_name: themeName } : {}
    return api.post(`/template-editor/templates/${id}/preview/`, payload, {
      responseType: 'blob',
    })
  },
  variables: () => api.get('/template-editor/variables/'),
  fonts: () => api.get('/template-editor/fonts/'),
}

export default api
