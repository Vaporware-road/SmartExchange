<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('analysis.title') }}</h1>

    <template v-if="loading">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <BaseSkeleton v-for="i in 4" :key="i" variant="card" />
      </div>
      <BaseSkeleton variant="card" class="!h-72 mb-6" />
      <BaseSkeleton variant="card" class="!h-48" />
    </template>

    <template v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-tags text-2xl text-gold" />
          </div>
          <div>
            <p class="text-2xl font-bold text-[var(--text-primary)]">{{ stats.totalPriceTypes }}</p>
            <p class="text-sm text-[var(--text-secondary)]">{{ $t('analysis.totalPriceTypes') }}</p>
          </div>
        </div>

        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-sync-alt text-2xl text-gold" />
          </div>
          <div>
            <p class="text-2xl font-bold text-[var(--text-primary)]">{{ stats.totalUpdates }}</p>
            <p class="text-sm text-[var(--text-secondary)]">{{ $t('analysis.totalUpdates') }}</p>
          </div>
        </div>

        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(16, 185, 129, 0.15);">
            <i class="fas fa-chart-line text-2xl text-success" />
          </div>
          <div>
            <p class="text-2xl font-bold" :class="stats.avgChange > 0 ? 'text-success' : stats.avgChange < 0 ? 'text-danger' : 'text-[var(--text-secondary)]'">
              {{ stats.avgChange > 0 ? '+' : '' }}{{ stats.avgChange.toFixed(2) }}%
            </p>
            <p class="text-sm text-[var(--text-secondary)]">{{ $t('analysis.avgChange') }}</p>
          </div>
        </div>

        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-clock text-2xl text-gold" />
          </div>
          <div>
            <p class="text-xl font-bold text-[var(--text-primary)]">{{ stats.recentUpdates }}</p>
            <p class="text-sm text-[var(--text-secondary)]">{{ $t('analysis.recentUpdates') }}</p>
          </div>
        </div>
      </div>

      <div v-if="chartData" class="card-luxury mb-6">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-chart-area" />
          {{ $t('analysis.priceHistory') }}
        </h2>
        <div class="h-72">
          <Line :data="chartData" :options="chartOptions" />
        </div>
      </div>
      <div v-else class="card-luxury mb-6 text-center py-12">
        <i class="fas fa-chart-area text-4xl text-[var(--text-secondary)] mb-3" />
        <p class="text-[var(--text-secondary)]">{{ $t('analysis.noChartData') }}</p>
      </div>

      <div v-if="topMovers.length" class="card-luxury mb-6">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-fire" />
          {{ $t('analysis.topMovers') }}
        </h2>
        <div class="overflow-x-auto">
          <table class="w-full text-start">
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

      <div v-if="categoryBreakdown.length" class="card-luxury">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-folder" />
          {{ $t('analysis.categories') }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="(cat, idx) in categoryBreakdown"
            :key="cat.category ?? idx"
            class="p-4 rounded-xl border transition-all hover:border-gold/50"
            style="border-color: var(--border-card); background: var(--bg-elevated);"
          >
            <h3 class="font-semibold text-gold mb-2">{{ cat.category }}</h3>
            <div class="flex justify-between text-sm text-[var(--text-secondary)]">
              <span>{{ cat.count ?? 0 }} {{ $t('analysis.priceType') }}</span>
              <span class="text-gold">{{ $t('analysis.avgPrice') }}: {{ formatNumber(cat.average_price) }}</span>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { analysisApi } from '@/services/api'
import { useDate } from '@/composables/useDate'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
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

const { formatRelative } = useDate()

const loading = ref(true)
const stats = reactive({ totalPriceTypes: 0, totalUpdates: 0, avgChange: 0, recentUpdates: 0 })
const topMovers = ref([])
const categoryBreakdown = ref([])
const chartData = ref(null)

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: { mode: 'index', intersect: false },
  plugins: {
    legend: {
      labels: { color: '#9CA3AF', usePointStyle: true, padding: 16 },
    },
    tooltip: {
      backgroundColor: 'rgba(30, 30, 30, 0.9)',
      titleColor: '#FFD700',
      bodyColor: '#F5F5F5',
      borderColor: 'rgba(255, 215, 0, 0.3)',
      borderWidth: 1,
      cornerRadius: 12,
      padding: 12,
    },
  },
  scales: {
    x: {
      grid: { color: 'rgba(255, 255, 255, 0.05)' },
      ticks: { color: '#9CA3AF', maxTicksLimit: 10 },
    },
    y: {
      grid: { color: 'rgba(255, 255, 255, 0.05)' },
      ticks: { color: '#9CA3AF' },
    },
  },
}

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
    return {
      label: ds.label ?? 'Price',
      data: labels.map(ts => pointMap[ts] ?? null),
      borderColor: ds.borderColor ?? '#FFD700',
      backgroundColor: ds.backgroundColor ?? 'rgba(255, 215, 0, 0.08)',
      fill: ds.fill ?? false,
      tension: ds.tension ?? 0.35,
      pointRadius: 2,
      pointHoverRadius: 5,
      spanGaps: true,
    }
  })

  return { labels: shortLabels, datasets: chartDatasets }
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
  } catch {
    /* error toast handled by interceptor */
  } finally {
    loading.value = false
  }
})
</script>
