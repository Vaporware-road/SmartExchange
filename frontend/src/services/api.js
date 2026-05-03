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
  // Default instance sets application/json; FormData must use multipart boundary from the browser.
  if (typeof FormData !== 'undefined' && config.data instanceof FormData) {
    if (config.headers && typeof config.headers.delete === 'function') {
      config.headers.delete('Content-Type')
    } else {
      delete config.headers['Content-Type']
    }
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const toast = useToast()
    const status = error.response?.status

    const requestUrl = error.config?.url ?? ''
    const isAuthRequest = requestUrl.includes('/auth/')
    const isAuthCheck = requestUrl.includes('/auth/me')
    const isPublicBootstrapRequest =
      isAuthCheck || requestUrl.includes('/settings/site/')
    const hasAccessToken = Boolean(localStorage.getItem('access_token'))

    if (status === 401) {
      const url = error.config?.url ?? ''
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      const isSessionCheck = url.includes('/auth/me')
      const onPublicRoute = router.currentRoute?.value?.meta?.public === true
      // Never force a full reload to /login while already on a public route (login, landing, …).
      // Otherwise a stale Bearer token + e.g. GET /template-editor/fonts/ after site settings
      // triggers 401 → location.href → infinite refresh loop.
      if (!isSessionCheck && !onPublicRoute) {
        window.location.href = '/login'
      }
      return Promise.reject(error)
    }

    // Public bootstrap requests are allowed to fail silently
    // (e.g. while app is unauthenticated, during logout, or backend restart).
    if (isPublicBootstrapRequest) {
      return Promise.reject(error)
    }

    // During logout/no-session phase, 403s from protected endpoints should not spam toasts.
    if (status === 403 && !hasAccessToken) {
      return Promise.reject(error)
    } else if (status === 403) {
      toast.error(resolveApiErrorMessage({ data: error.response?.data, status }))
    } else if (status >= 500) {
      const skipServerErrorRedirect =
        error.config?.skipGlobalErrorRedirect === true ||
        requestUrl.includes('/analysis/dashboard') ||
        isAuthRequest
      const logId = error.response?.data?.log_id ?? error.response?.data?.error_id ?? error.response?.data?.request_id
      const currentName = router.currentRoute?.value?.name
      if (
        !skipServerErrorRedirect &&
        currentName !== 'login' &&
        currentName !== 'error-500' &&
        currentName !== 'not-found'
      ) {
        router.push({ name: 'error-500', query: logId != null ? { logId: String(logId) } : {} })
      }
      toast.error(resolveApiErrorMessage({ data: error.response?.data, status }))
    } else if (!error.response) {
      toast.error(i18n.global.t('errors.networkError'))
    } else if (status >= 400) {
      const msg = resolveApiErrorMessage({ data: error.response?.data, status })
      if (msg) toast.error(msg)
    }

    return Promise.reject(error)
  }
)

function normalizeErrorMessage(value) {
  if (Array.isArray(value)) return value.join(' ')
  if (value == null) return ''
  return String(value)
}

function translateApiErrorCode(code) {
  if (!code) return ''
  const key = `apiErrors.codes.${code}`
  const translated = i18n.global.t(key)
  return translated !== key ? translated : ''
}

function statusFallbackKey(status) {
  if (!status) return 'apiErrors.fallback.unknown'
  if (status === 400) return 'apiErrors.fallback.badRequest'
  if (status === 401) return 'apiErrors.fallback.unauthorized'
  if (status === 403) return 'apiErrors.fallback.forbidden'
  if (status === 404) return 'apiErrors.fallback.notFound'
  if (status === 409) return 'apiErrors.fallback.conflict'
  if (status === 422) return 'apiErrors.fallback.validation'
  if (status >= 500) return 'apiErrors.fallback.server'
  return 'apiErrors.fallback.unknown'
}

/** Parse API errors while supporting both DRF and project-standard payloads. */
export function extractApiErrorDetails(data) {
  if (!data || typeof data !== 'object') {
    return { message: 'Request failed', code: null, fieldErrors: {} }
  }

  const code = typeof data.code === 'string' ? data.code : null
  const fieldErrors = {}

  if (data.errors && typeof data.errors === 'object') {
    for (const [key, val] of Object.entries(data.errors)) {
      fieldErrors[key] = normalizeErrorMessage(val)
    }
  }

  for (const [key, val] of Object.entries(data)) {
    if (['detail', 'message', 'code', 'error', 'errors', 'sync_error'].includes(key)) continue
    if (typeof val === 'string' || Array.isArray(val)) {
      fieldErrors[key] = normalizeErrorMessage(val)
    }
  }

  let message = ''
  if (typeof data.message === 'string' && data.message.trim()) {
    message = data.message.trim()
  } else if (typeof data.detail === 'string' && data.detail.trim()) {
    message = data.detail.trim()
  } else if (Array.isArray(data.detail)) {
    message = data.detail.join(' ').trim()
  } else if (data.sync_error) {
    const syncPart = normalizeErrorMessage(data.sync_error)
    message = syncPart ? `Save failed: ${syncPart}` : 'Save failed'
  }

  if (!message) {
    const parts = Object.entries(fieldErrors).map(([key, val]) => `${key}: ${val}`)
    message = parts.length ? parts.join(' ') : 'Request failed'
  }

  return { message, code, fieldErrors }
}

export function resolveApiErrorMessage({ data, status } = {}) {
  const { message, code } = extractApiErrorDetails(data)
  const byCode = translateApiErrorCode(code)
  if (byCode) return byCode
  if (message) return message
  return i18n.global.t(statusFallbackKey(status))
}

export function resolveApiFieldErrors(data) {
  const { fieldErrors } = extractApiErrorDetails(data)
  const resolved = {}
  for (const [field, rawMessage] of Object.entries(fieldErrors || {})) {
    let picked = ''
    const codeLike = String(rawMessage || '')
    const byFieldCode = i18n.global.t(`apiErrors.fields.${field}.${codeLike}`)
    if (byFieldCode !== `apiErrors.fields.${field}.${codeLike}`) {
      picked = byFieldCode
    } else {
      picked = rawMessage
    }
    resolved[field] = picked
  }
  return resolved
}

export function getApiErrorDetails(error) {
  const status = error?.response?.status
  const data = error?.response?.data
  return {
    status,
    message: resolveApiErrorMessage({ data, status }),
    code: extractApiErrorDetails(data).code,
    fieldErrors: resolveApiFieldErrors(data),
  }
}

/** Format API errors for general user-visible messages. */
export function formatDrfError(data) {
  return resolveApiErrorMessage({ data })
}

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
  currencies: () => api.get('/categories/currencies/'),
  create: (data) => api.post('/categories/', data),
  get: (id) => api.get(`/categories/${id}/`),
  update: (id, data) => api.put(`/categories/${id}/`, data),
  patch: (id, data) => api.patch(`/categories/${id}/`, data),
  delete: (id) => api.delete(`/categories/${id}/`),
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
  history: (id, params = {}) => api.get(`/special-prices/${id}/history/`, { params }),
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
  uploads: () => api.get('/settings/uploads/'),
  updateUploads: (data) => api.put('/settings/uploads/', data),
  clearTempUploads: () => api.post('/settings/uploads/clear-temp/'),
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
  patch: (id, data) => api.patch(`/template-editor/templates/${id}/`, data),
  delete: (id) => api.delete(`/template-editor/templates/${id}/`),
  updateConfig: (id, config) =>
    api.put(`/template-editor/templates/${id}/config/`, { config }),
  updateConfigJson: (id, body) =>
    api.put(`/template-editor/templates/${id}/config/`, body),
  uploadMedia: (formData) => api.post('/template-editor/media/', formData),
  listMedia: () => api.get('/template-editor/media/'),
  variables: (params = {}) => api.get('/template-editor/variables/', { params }),
  preview: (id, config = null, themeName = null) => {
    const payload = config != null ? { config, theme_name: themeName } : {}
    return api.post(`/template-editor/templates/${id}/preview/`, payload, {
      responseType: 'blob',
    })
  },
  fonts: () => api.get('/template-editor/fonts/'),
  uploadFont: (formData) => api.post('/template-editor/fonts/', formData),
  deleteFont: (filename) =>
    api.delete(`/template-editor/fonts/${encodeURIComponent(filename)}/`),
  priceBindingsPreview: (params = {}) => api.get('/template-editor/price-bindings-preview/', { params }),
  categoryPriceTypes: (params = {}) => api.get('/template-editor/category-price-types/', { params }),
}

export default api
