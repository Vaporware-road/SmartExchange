import { defineStore } from 'pinia'
import { telegramApi } from '@/services/api'

export const TELEGRAM_HUB_SESSION_KEY = 'telegramHubSession'
export const TELEGRAM_HUB_VERIFY_TTL_MS = 8 * 60 * 60 * 1000

function readSession() {
  if (typeof sessionStorage === 'undefined') return null
  try {
    const raw = sessionStorage.getItem(TELEGRAM_HUB_SESSION_KEY)
    if (!raw) return null
    const parsed = JSON.parse(raw)
    return parsed && typeof parsed === 'object' ? parsed : null
  } catch {
    return null
  }
}

function writeSession(payload) {
  if (typeof sessionStorage === 'undefined') return
  try {
    sessionStorage.setItem(TELEGRAM_HUB_SESSION_KEY, JSON.stringify(payload))
  } catch {
    // Ignore quota / private-mode failures; in-memory state still works.
  }
}

function clearStorage() {
  if (typeof sessionStorage === 'undefined') return
  try {
    sessionStorage.removeItem(TELEGRAM_HUB_SESSION_KEY)
  } catch {
    // ignore
  }
}

function emptyState() {
  return {
    verifiedBot: null,
    isUnlocked: false,
    verifiedAt: null,
    lastDashboard: null,
    userId: null,
    lastAdminSection: 'customersStatus',
  }
}

function hydrateState() {
  const cached = readSession()
  if (!cached?.isUnlocked || !cached?.verifiedBot || !cached?.verifiedAt) {
    return emptyState()
  }
  const age = Date.now() - Number(cached.verifiedAt)
  if (!Number.isFinite(age) || age < 0 || age >= TELEGRAM_HUB_VERIFY_TTL_MS) {
    clearStorage()
    return emptyState()
  }
  return {
    verifiedBot: cached.verifiedBot,
    isUnlocked: true,
    verifiedAt: cached.verifiedAt,
    lastDashboard: cached.lastDashboard ?? null,
    userId: cached.userId ?? null,
    lastAdminSection: cached.lastAdminSection || 'customersStatus',
  }
}

export const useTelegramHubStore = defineStore('telegramHub', {
  state: () => hydrateState(),

  getters: {
    isSessionValid() {
      if (!this.isUnlocked || !this.verifiedBot || !this.verifiedAt) return false
      const age = Date.now() - Number(this.verifiedAt)
      return Number.isFinite(age) && age >= 0 && age < TELEGRAM_HUB_VERIFY_TTL_MS
    },
  },

  actions: {
    persist() {
      if (!this.isUnlocked || !this.verifiedBot) {
        clearStorage()
        return
      }
      writeSession({
        verifiedBot: this.verifiedBot,
        isUnlocked: this.isUnlocked,
        verifiedAt: this.verifiedAt,
        lastDashboard: this.lastDashboard,
        userId: this.userId,
        lastAdminSection: this.lastAdminSection,
      })
    },

    clearSession() {
      this.verifiedBot = null
      this.isUnlocked = false
      this.verifiedAt = null
      this.lastDashboard = null
      this.userId = null
      this.lastAdminSection = 'customersStatus'
      clearStorage()
    },

    setVerifiedBot(bot) {
      this.verifiedBot = bot || null
      this.isUnlocked = !!bot
      if (bot) {
        this.verifiedAt = Date.now()
      } else {
        this.verifiedAt = null
        this.lastDashboard = null
      }
      this.persist()
    },

    setDashboard(dashboard) {
      this.lastDashboard = dashboard ?? null
      this.persist()
    },

    setAdminSection(id) {
      this.lastAdminSection = id || 'customersStatus'
      if (this.isUnlocked) this.persist()
    },

    /**
     * Skip POST /telegram/admin/verify-bot/ when this browser tab already
     * unlocked the hub within the TTL. Pass force to re-hit Telegram getMe.
     */
    async ensureVerified({ force = false, botId = null, userId = null } = {}) {
      if (userId != null && this.userId != null && Number(this.userId) !== Number(userId)) {
        this.clearSession()
      }
      const requestedId = botId ?? this.verifiedBot?.id ?? null
      if (!force && this.isSessionValid) {
        if (requestedId == null || Number(this.verifiedBot?.id) === Number(requestedId)) {
          if (userId != null) this.userId = userId
          this.persist()
          return { ok: true, bot: this.verifiedBot, fromCache: true }
        }
      }

      const payload = requestedId != null && requestedId !== '' ? { bot_id: requestedId } : {}
      try {
        const { data } = await telegramApi.admin.verifyBot(payload)
        if (!data?.ok || !data?.bot) {
          this.clearSession()
          const err = new Error(data?.message || 'Bot verification failed')
          err.response = { data }
          throw err
        }
        this.verifiedBot = data.bot
        this.isUnlocked = true
        this.verifiedAt = Date.now()
        this.userId = userId ?? this.userId
        this.persist()
        return { ok: true, bot: data.bot, fromCache: false }
      } catch (err) {
        this.clearSession()
        throw err
      }
    },
  },
})
