<template>
  <div>
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6 animate-fade-in-up">
      <h1 class="text-2xl font-bold text-gold">{{ $t('analysis.title') }}</h1>
      <BaseButton
        :loading="exportLoading"
        variant="outline"
        size="sm"
        class="btn-export-excel"
        @click="exportAnalyticsToExcel"
      >
        <i class="fas fa-file-excel" />
        <span>{{ exportLoading ? $t('analysis.exporting') : $t('analysis.exportData') }}</span>
      </BaseButton>
    </div>

    <template v-if="loading">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <BaseSkeleton v-for="i in 4" :key="i" variant="card" />
      </div>
      <BaseSkeleton variant="card" class="!h-72 mb-6" />
      <BaseSkeleton variant="card" class="!h-48" />
    </template>

    <template v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <BaseCard
          v-for="(stat, statIndex) in statCards"
          :key="'stat-' + statIndex"
          variant="glass"
          padding="sm"
          class="flex items-center gap-4 hover-lift animate-fade-in-up border border-[var(--glass-border)]"
          :style="{ animationDelay: `${statIndex * 0.06}s` }"
        >
          <div class="p-3 rounded-xl" :style="{ background: stat.iconBg }">
            <i :class="stat.icon" class="text-2xl" :style="{ color: stat.iconColor }" />
          </div>
          <div>
            <p class="text-2xl font-bold" :class="stat.valueClass">{{ stat.value }}</p>
            <p class="text-sm text-[var(--text-secondary)]">{{ stat.label }}</p>
          </div>
        </BaseCard>
      </div>

      <div v-if="chartData" class="card-luxury mb-6 animate-fade-in-up hover-lift border border-[var(--glass-border)]" style="animation-delay: 0.1s; background: var(--glass-bg); backdrop-filter: blur(16px);">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-chart-area" />
          {{ $t('analysis.priceHistory') }}
        </h2>
        <div class="h-72">
          <Line :data="chartData" :options="chartOptions" />
        </div>
      </div>
      <div v-else class="card-luxury mb-6 text-center py-12 animate-fade-in-up" style="animation-delay: 0.1s">
        <i class="fas fa-chart-area text-4xl text-[var(--text-secondary)] mb-3" />
        <p class="text-[var(--text-secondary)]">{{ $t('analysis.noChartData') }}</p>
      </div>

      <div v-if="topMovers.length" class="card-luxury mb-6 animate-fade-in-up hover-lift border border-[var(--glass-border)] w-full min-w-0 overflow-hidden" style="animation-delay: 0.15s; background: var(--glass-bg); backdrop-filter: blur(16px);">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-fire" />
          {{ $t('analysis.topMovers') }}
        </h2>
        <div class="w-full overflow-x-auto max-w-full">
          <table class="w-full text-start min-w-[320px]">
            <thead>
              <tr class="text-[var(--text-secondary)] text-sm border-b" style="border-color: var(--border-card);">
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.priceType') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.currentPrice') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.change24h') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.lastUpdate') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in topMovers"
                :key="item.id"
                class="border-b transition-colors hover:bg-[var(--bg-hover)]"
                style="border-color: var(--border-card);"
              >
                <td class="py-3 px-4 font-medium text-[var(--text-primary)]">{{ item.name }}</td>
                <td class="py-3 px-4 text-gold font-bold">{{ formatNumber(item.latest_price) }}</td>
                <td class="py-3 px-4">
                  <span
                    class="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg text-sm font-medium"
                    :class="(item.change_percent ?? 0) > 0 ? 'bg-success/10 text-success' : (item.change_percent ?? 0) < 0 ? 'bg-danger/10 text-danger' : 'bg-gray-500/10 text-gray-400'"
                  >
                    <i :class="(item.change_percent ?? 0) > 0 ? 'fas fa-caret-up' : (item.change_percent ?? 0) < 0 ? 'fas fa-caret-down' : 'fas fa-minus'" />
                    {{ (item.change_percent ?? 0) > 0 ? '+' : '' }}{{ (item.change_percent ?? 0).toFixed(2) }}%
                  </span>
                </td>
                <td class="py-3 px-4 text-sm text-[var(--text-secondary)]">{{ formatRelative(item.timestamp) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div
        v-if="telegramEngagement.timeline?.length || telegramEngagement.channels?.length"
        class="card-luxury mb-6 animate-fade-in-up hover-lift border border-[var(--glass-border)] w-full min-w-0 overflow-hidden"
        style="animation-delay: 0.18s; background: var(--glass-bg); backdrop-filter: blur(16px);"
      >
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fab fa-telegram-plane" />
          {{ $t('analysis.telegramEngagement') }}
        </h2>
        <div v-if="telegramEngagement.timeline?.length" class="mb-4 h-64">
          <Line :data="buildTelegramChart" :options="chartOptions" />
        </div>
        <div v-if="telegramEngagement.channels?.length" class="w-full overflow-x-auto max-w-full">
          <table class="w-full text-start text-sm min-w-[320px]">
            <thead>
              <tr class="text-[var(--text-secondary)] text-sm border-b" style="border-color: var(--border-card);">
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.channel') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.totalPosts') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.successRate') }}</th>
                <th class="py-3 px-4 text-start font-medium">{{ $t('analysis.lastPost') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="ch in telegramEngagement.channels"
                :key="ch.channel_id"
                class="border-b transition-colors hover:bg-[var(--bg-hover)]"
                style="border-color: var(--border-card);"
              >
                <td class="py-3 px-4 font-medium text-[var(--text-primary)]">
                  {{ ch.channel_name }}
                </td>
                <td class="py-3 px-4 text-gold font-semibold">
                  {{ ch.total }}
                </td>
                <td class="py-3 px-4">
                  <span
                    class="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg text-sm font-medium"
                    :class="ch.success_rate >= 0.9 ? 'bg-success/10 text-success' : ch.success_rate >= 0.7 ? 'bg-amber-500/10 text-amber-300' : 'bg-danger/10 text-danger'"
                  >
                    {{ (ch.success_rate * 100).toFixed(1) }}%
                  </span>
                </td>
                <td class="py-3 px-4 text-sm text-[var(--text-secondary)]">
                  {{ ch.last_post_at ? formatRelative(new Date(ch.last_post_at)) : '—' }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <BaseCard
        v-if="categoryBreakdown.length"
        variant="glass"
        padding="default"
        class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
        style="animation-delay: 0.2s"
      >
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-folder" />
          {{ $t('analysis.categories') }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseCard
            v-for="(cat, idx) in categoryBreakdown"
            :key="cat.category ?? idx"
            variant="glass"
            padding="sm"
            class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
            :style="{ animationDelay: `${0.25 + idx * 0.04}s` }"
          >
            <h3 class="font-semibold text-gold mb-2">{{ cat.category }}</h3>
            <div class="flex justify-between text-sm text-[var(--text-secondary)]">
              <span>{{ cat.count ?? 0 }} {{ $t('analysis.priceType') }}</span>
              <span class="text-gold">{{ $t('analysis.avgPrice') }}: {{ formatNumber(cat.average_price) }}</span>
            </div>
          </BaseCard>
        </div>
      </BaseCard>
    </template>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import * as XLSX from 'xlsx'
import { analysisApi, authApi } from '@/services/api'
import { useThemeStore } from '@/stores/theme'
import { useDate } from '@/composables/useDate'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseButton from '@/components/ui/BaseButton.vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  TimeScale,
  Title,
  Tooltip,
  Legend,
  Filler,
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, TimeScale, Title, Tooltip, Legend, Filler)

const { t } = useI18n()
const themeStore = useThemeStore()
const toast = useToast()
const { formatRelative } = useDate()

const loading = ref(true)
const exportLoading = ref(false)
const stats = reactive({ totalPriceTypes: 0, totalUpdates: 0, avgChange: 0, recentUpdates: 0 })
const topMovers = ref([])
const categoryBreakdown = ref([])
const chartData = ref(null)
const telegramEngagement = ref({ timeline: [], channels: [] })

const statCards = computed(() => [
  {
    icon: 'fas fa-tags text-gold',
    iconBg: 'var(--primary-muted)',
    iconColor: 'var(--primary)',
    value: stats.totalPriceTypes,
    valueClass: 'text-[var(--text-primary)]',
    label: t('analysis.totalPriceTypes'),
  },
  {
    icon: 'fas fa-sync-alt text-gold',
    iconBg: 'var(--primary-muted)',
    iconColor: 'var(--primary)',
    value: stats.totalUpdates,
    valueClass: 'text-[var(--text-primary)]',
    label: t('analysis.totalUpdates'),
  },
  {
    icon: 'fas fa-chart-line',
    iconBg: 'rgba(16, 185, 129, 0.15)',
    iconColor: 'var(--color-success, #10B981)',
    value: (stats.avgChange > 0 ? '+' : '') + stats.avgChange.toFixed(2) + '%',
    valueClass: stats.avgChange > 0 ? 'text-success' : stats.avgChange < 0 ? 'text-danger' : 'text-[var(--text-secondary)]',
    label: t('analysis.avgChange'),
  },
  {
    icon: 'fas fa-clock text-gold',
    iconBg: 'var(--primary-muted)',
    iconColor: 'var(--primary)',
    value: stats.recentUpdates,
    valueClass: 'text-xl text-[var(--text-primary)]',
    label: t('analysis.recentUpdates'),
  },
])

function getChartThemeColors() {
  const root = document.documentElement
  const s = getComputedStyle(root)
  return {
    primary: s.getPropertyValue('--primary').trim() || '#2563eb',
    textPrimary: s.getPropertyValue('--text-primary').trim() || '#1e293b',
    textSecondary: s.getPropertyValue('--text-secondary').trim() || '#64748b',
    bgCard: s.getPropertyValue('--bg-card').trim() || '#1e293b',
    borderColor: s.getPropertyValue('--border-card').trim() || '#334155',
  }
}

const chartOptions = computed(() => {
  themeStore.isDark /* reactive: update on theme toggle */
  const c = getChartThemeColors()
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      legend: {
        labels: { color: c.textSecondary, usePointStyle: true, padding: 16 },
      },
      tooltip: {
        backgroundColor: c.bgCard,
        titleColor: c.primary,
        bodyColor: c.textPrimary,
        borderColor: c.borderColor,
        borderWidth: 1,
        cornerRadius: 12,
        padding: 12,
      },
    },
    scales: {
      x: {
        grid: { color: c.borderColor },
        ticks: { color: c.textSecondary, maxTicksLimit: 10 },
      },
      y: {
        grid: { color: c.borderColor },
        ticks: { color: c.textSecondary },
      },
    },
  }
})

function formatNumber(val) {
  if (val == null) return '—'
  return Number(val).toLocaleString(undefined, { maximumFractionDigits: 2 })
}

function buildChartFromTimeline(datasets) {
  if (!datasets?.length) return null

  const allTimestamps = new Set()
  for (const ds of datasets) {
    for (const point of ds.data ?? []) {
      allTimestamps.add(point.x)
    }
  }

  const labels = [...allTimestamps].sort()
  if (!labels.length) return null

  const shortLabels = labels.map(iso => {
    const d = new Date(iso)
    return isNaN(d.getTime()) ? iso : d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })
  })

  const chartDatasets = datasets.map(ds => {
    const pointMap = {}
    for (const point of ds.data ?? []) {
      pointMap[point.x] = point.y
    }
    const c = getChartThemeColors()
    const primary = c.primary
    const primaryRgba = primary.startsWith('#')
      ? (() => {
          const h = primary.replace('#', '')
          if (h.length !== 6) return 'rgba(37, 99, 235, 0.08)'
          const r = parseInt(h.slice(0, 2), 16)
          const g = parseInt(h.slice(2, 4), 16)
          const b = parseInt(h.slice(4, 6), 16)
          return `rgba(${r},${g},${b},0.08)`
        })()
      : primary.replace(')', ', 0.08)').replace('rgb(', 'rgba(')
    return {
      label: ds.label ?? 'Price',
      data: labels.map(ts => pointMap[ts] ?? null),
      borderColor: ds.borderColor ?? primary,
      backgroundColor: ds.backgroundColor ?? primaryRgba,
      fill: ds.fill ?? false,
      tension: ds.tension ?? 0.35,
      pointRadius: 2,
      pointHoverRadius: 5,
      spanGaps: true,
    }
  })

  return { labels: shortLabels, datasets: chartDatasets }
}

const buildTelegramChart = computed(() => {
  if (!telegramEngagement.value.timeline?.length) return null
  return buildChartFromTimeline(telegramEngagement.value.timeline)
})

function formatTimestamp(iso) {
  if (!iso) return ''
  try {
    const d = new Date(iso)
    if (isNaN(d.getTime())) return String(iso)
    const y = d.getFullYear()
    const m = String(d.getMonth() + 1).padStart(2, '0')
    const day = String(d.getDate()).padStart(2, '0')
    const h = String(d.getHours()).padStart(2, '0')
    const min = String(d.getMinutes()).padStart(2, '0')
    return `${y}-${m}-${day} ${h}:${min}`
  } catch {
    return String(iso)
  }
}

const PRICE_ACTIONS = ['price_update', 'bulk_price_update', 'special_price_update']

async function exportAnalyticsToExcel() {
  exportLoading.value = true
  try {
    const [dashRes, activityRes] = await Promise.all([
      analysisApi.dashboard(),
      authApi.activity({}).catch(() => ({ data: [] })),
    ])
    const dash = dashRes.data ?? {}
    const timelineData = dash.timeline_data ?? []
    const specialTimelineData = dash.special_timeline_data ?? []
    const overallStats = dash.overall_stats ?? {}
    const categorySummary = dash.category_summary ?? []
    const topMovers = dash.top_movers ?? []
    const priceStatistics = dash.price_statistics ?? {}
    const activityList = Array.isArray(activityRes.data) ? activityRes.data : (activityRes.data?.results ?? [])

    const historicalRows = [['Date', 'Currency Pair', 'Category', 'Price']]
    for (const ds of [...timelineData, ...specialTimelineData]) {
      const label = ds.label ?? ''
      const category = ds.category ?? ''
      for (const point of ds.data ?? []) {
        historicalRows.push([
          formatTimestamp(point.x),
          label,
          category,
          point.y != null ? Number(point.y) : '',
        ])
      }
    }

    const summaryRows = [[t('analysis.sheetSummary')], []]
    summaryRows.push(['Metric', 'Value'])
    if (overallStats.active_price_types != null) summaryRows.push([t('analysis.totalPriceTypes'), overallStats.active_price_types])
    if (overallStats.total_price_updates != null) summaryRows.push([t('analysis.totalUpdates'), overallStats.total_price_updates])
    if (overallStats.week_price_updates != null) summaryRows.push([t('analysis.recentUpdates'), overallStats.week_price_updates])
    summaryRows.push([])
    summaryRows.push([t('analysis.topMovers'), ''])
    for (const m of topMovers.slice(0, 10)) {
      summaryRows.push([m.name ?? '', `${formatNumber(m.latest_price)} (${(m.change_percent ?? 0).toFixed(2)}%)`])
    }
    summaryRows.push([])
    summaryRows.push([t('analysis.categories'), ''])
    for (const cat of categorySummary) {
      summaryRows.push([cat.category ?? '', `Count: ${cat.count ?? 0}, Avg: ${formatNumber(cat.average_price)}, Max: ${formatNumber(cat.max_price)}, Min: ${formatNumber(cat.min_price)}`])
    }
    const statsList = Object.values(priceStatistics)
    if (statsList.length) {
      summaryRows.push([])
      summaryRows.push(['Max price in period (sample)', ''])
      for (const s of statsList.slice(0, 10)) {
        summaryRows.push([s.price_type_name ?? s.category ?? '', formatNumber(s.max)])
      }
    }

    const activityRows = [['Date', 'User', 'Action Type', 'Details']]
    const filteredActivity = activityList.filter((a) => PRICE_ACTIONS.includes(a.action_type))
    for (const a of filteredActivity) {
      const at = a.created_at ? formatTimestamp(a.created_at) : ''
      activityRows.push([
        at,
        a.user_display ?? a.user ?? '—',
        a.action_type ?? '—',
        a.details ?? '—',
      ])
    }

    const hasHistorical = historicalRows.length > 1
    const hasSummary = summaryRows.length > 2
    const hasActivity = activityRows.length > 1
    if (!hasHistorical && !hasSummary && !hasActivity) {
      toast.warning(t('analysis.exportEmpty'))
      return
    }

    const wb = XLSX.utils.book_new()
    if (hasHistorical) {
      const ws = XLSX.utils.aoa_to_sheet(historicalRows)
      XLSX.utils.book_append_sheet(wb, ws, t('analysis.sheetHistoricalPrices').slice(0, 31))
    }
    if (hasSummary) {
      const wsSummary = XLSX.utils.aoa_to_sheet(summaryRows)
      XLSX.utils.book_append_sheet(wb, wsSummary, t('analysis.sheetSummary').slice(0, 31))
    }
    if (hasActivity) {
      const wsActivity = XLSX.utils.aoa_to_sheet(activityRows)
      XLSX.utils.book_append_sheet(wb, wsActivity, t('analysis.sheetActivityLogs').slice(0, 31))
    }

    const dateStr = new Date().toISOString().slice(0, 10)
    const fileName = `SmartExchange_Analysis_${dateStr}.xlsx`
    XLSX.writeFile(wb, fileName)
    toast.success(t('analysis.exportSuccess'))
  } catch (e) {
    console.error(e)
    toast.error(t('analysis.exportError'))
  } finally {
    exportLoading.value = false
  }
}

onMounted(async () => {
  try {
    const dashRes = await analysisApi.dashboard().catch(() => ({ data: {} }))
    const dash = dashRes.data ?? {}

    const overallStats = dash.overall_stats ?? {}
    stats.totalPriceTypes = overallStats.active_price_types ?? 0
    stats.totalUpdates = overallStats.total_price_updates ?? 0
    stats.recentUpdates = overallStats.week_price_updates ?? 0

    const movers = dash.top_movers ?? []
    topMovers.value = movers

    if (movers.length) {
      const validChanges = movers
        .map(m => m.change_percent)
        .filter(c => c != null)
      stats.avgChange = validChanges.length
        ? validChanges.reduce((s, v) => s + v, 0) / validChanges.length
        : 0
    }

    categoryBreakdown.value = dash.category_summary ?? []

    const timelines = [...(dash.timeline_data ?? []), ...(dash.special_timeline_data ?? [])]
    chartData.value = buildChartFromTimeline(timelines)

    telegramEngagement.value = dash.telegram_engagement ?? { timeline: [], channels: [] }
  } catch {
    /* error toast handled by interceptor */
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.btn-export-excel {
  --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  box-shadow: var(--tw-shadow);
}
html:not(.dark) .btn-export-excel {
  border-color: rgb(37 99 235);
  color: rgb(37 99 235);
}
html:not(.dark) .btn-export-excel:hover {
  background-color: rgba(37 99 235 / 0.08);
}
.dark .btn-export-excel {
  border-color: var(--primary);
  color: var(--primary);
}
.dark .btn-export-excel:hover {
  background-color: var(--primary-muted);
}
</style>
