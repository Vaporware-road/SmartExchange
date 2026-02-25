<template>
  <div>
    <nav class="mb-6">
      <router-link to="/settings" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Settings
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Logs</h1>
    <div v-if="loading" class="card-luxury overflow-x-auto p-6">
      <div class="space-y-4">
        <BaseSkeleton v-for="i in 8" :key="i" variant="table-row" />
      </div>
    </div>
    <div v-else class="card-luxury overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="border-b" style="border-color: rgba(255, 215, 0, 0.3);">
            <th class="text-left py-4 px-4 text-gold font-semibold">Level</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Source</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Message</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Date</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="log in logs"
            :key="log.id"
            class="border-b"
            style="border-color: rgba(255, 215, 0, 0.1);"
          >
            <td class="py-4 px-4">
              <span
                class="px-2 py-1 rounded text-xs font-medium"
                :class="levelClass(log.level)"
              >
                {{ log.level }}
              </span>
            </td>
            <td class="py-4 px-4 text-gray-400">{{ log.source }}</td>
            <td class="py-4 px-4">{{ log.message }}</td>
            <td class="py-4 px-4 text-gray-500 text-sm">{{ formatDate(log.created_at) }}</td>
          </tr>
        </tbody>
      </table>
      <p v-if="!loading && (!logs || !logs.length)" class="text-center text-gray-500 py-8">No logs found.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { settingsApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const logs = ref([])

function levelClass(level) {
  const map = {
    ERROR: 'bg-red-500/20 text-red-400',
    WARNING: 'bg-amber-500/20 text-amber-400',
    INFO: 'bg-blue-500/20 text-blue-400',
    DEBUG: 'bg-gray-500/20 text-gray-400',
    CRITICAL: 'bg-red-600/20 text-red-300',
  }
  return map[level] ?? 'bg-gray-500/20'
}

function formatDate(iso) {
  if (!iso) return '-'
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}

onMounted(async () => {
  try {
    const { data } = await settingsApi.logs()
    logs.value = data?.results ?? data ?? []
  } catch {
    logs.value = []
  } finally {
    loading.value = false
  }
})
</script>
