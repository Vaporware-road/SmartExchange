import { defineStore } from 'pinia'
import { ordersApi } from '@/services/api'

const POLL_MS = 30000

export const useOrdersQueueStore = defineStore('ordersQueue', {
  state: () => ({
    pendingCount: 0,
    loading: false,
    pollTimer: null,
  }),

  actions: {
    async fetchPendingCount() {
      this.loading = true
      try {
        const { data } = await ordersApi.pendingCount()
        this.pendingCount = Number(data?.pending) || 0
      } catch {
        /* keep last known count */
      } finally {
        this.loading = false
      }
    },

    startPolling() {
      this.stopPolling()
      this.fetchPendingCount()
      this.pollTimer = setInterval(() => {
        this.fetchPendingCount()
      }, POLL_MS)
    },

    stopPolling() {
      if (this.pollTimer) {
        clearInterval(this.pollTimer)
        this.pollTimer = null
      }
    },
  },
})
