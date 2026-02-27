import axios from 'axios'
import { useToast } from 'vue-toastification'
import i18n from '@/i18n'

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
}

export const dashboardApi = {
  summary: () => api.get('/dashboard/summary/'),
}

export const categoryApi = {
  list: () => api.get('/categories/'),
  create: (data) => api.post('/categories/', data),
  get: (id) => api.get(`/categories/${id}/`),
  update: (id, data) => api.put(`/categories/${id}/`, data),
  delete: (id) => api.delete(`/categories/${id}/`),
  addPriceType: (categoryId, data) =>
    api.post(`/categories/${categoryId}/price-types/`, data),
}

export const priceTypeApi = {
  update: (categoryId, id, data) => api.put(`/categories/${categoryId}/price-types/${id}/`, data),
  delete: (categoryId, id) => api.delete(`/categories/${categoryId}/price-types/${id}/`),
}

export const priceApi = {
  list: () => api.get('/prices/'),
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

export default api
