<template>
  <div>
    <nav v-if="!embedded" class="mb-6">
      <router-link to="/settings" class="text-[var(--text-secondary)] hover:text-gold transition-colors">
        <i class="fas me-2" :class="$i18n.locale === 'fa' ? 'fa-arrow-right' : 'fa-arrow-left'"></i>{{ $t('logs.backToSettings') }}
      </router-link>
    </nav>
    <h1 v-if="!embedded" class="text-2xl font-bold text-gold mb-6">{{ $t('logs.title') }}</h1>
    <div v-if="loading" class="card-luxury overflow-x-auto p-6">
      <div class="space-y-4">
        <BaseSkeleton v-for="i in 8" :key="i" variant="table-row" />
      </div>
    </div>
    <div v-else class="card-luxury w-full min-w-0 overflow-hidden">
      <!-- Desktop/tablet: table in scrollable wrapper so only table scrolls, not the page -->
      <div class="w-full overflow-x-auto max-w-full hidden md:block">
        <table class="w-full min-w-[600px]">
          <thead>
            <tr class="border-b border-[var(--border-color)]">
              <th class="text-start py-4 px-4 text-gold font-semibold text-sm md:text-base whitespace-nowrap">{{ $t('logs.level') }}</th>
              <th class="text-start py-4 px-4 text-gold font-semibold text-sm md:text-base whitespace-nowrap">{{ $t('logs.source') }}</th>
              <th class="text-start py-4 px-4 text-gold font-semibold text-sm md:text-base">{{ $t('logs.message') }}</th>
              <th class="text-start py-4 px-4 text-gold font-semibold text-sm md:text-base whitespace-nowrap">{{ $t('logs.date') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="log in logs"
              :key="log.id"
              class="border-b border-[var(--border-card)] hover:bg-[var(--bg-hover)] transition-colors"
            >
              <td class="py-4 px-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 rounded text-xs font-medium"
                  :class="levelClass(log.level)"
                >
                  {{ log.level }}
                </span>
              </td>
              <td class="py-4 px-4 text-[var(--text-secondary)] text-xs md:text-base break-words min-w-0 max-w-[200px]">{{ log.source }}</td>
              <td class="py-4 px-4 text-xs md:text-base break-words min-w-0">{{ log.message }}</td>
              <td class="py-4 px-4 text-[var(--text-secondary)] text-xs md:text-sm whitespace-nowrap">{{ formatDate(log.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Mobile: stacked cards, text-xs for compact display -->
      <div class="block md:hidden divide-y divide-[var(--border-card)]">
        <div
          v-for="log in logs"
          :key="log.id"
          class="p-4 space-y-2"
        >
          <div class="flex items-center justify-between gap-2 flex-wrap">
            <span
              class="px-2 py-1 rounded text-xs font-medium shrink-0"
              :class="levelClass(log.level)"
            >
              {{ log.level }}
            </span>
            <span class="text-xs text-[var(--text-secondary)]">{{ formatDate(log.created_at) }}</span>
          </div>
          <p class="text-xs font-medium text-[var(--text-primary)]">{{ log.source }}</p>
          <p class="text-xs text-[var(--text-secondary)] break-words">{{ log.message }}</p>
        </div>
      </div>
      <p v-if="!loading && (!logs || !logs.length)" class="text-center text-[var(--text-secondary)] py-8">{{ $t('logs.noLogsFound') }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { settingsApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

defineProps({
  embedded: { type: Boolean, default: false },
})

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
