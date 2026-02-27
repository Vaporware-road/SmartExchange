<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6 animate-fade-in-up">{{ $t('analysis.title') }}</h1>

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

      <div v-if="topMovers.length" class="card-luxury mb-6 animate-fade-in-up hover-lift border border-[var(--glass-border)]" style="animation-delay: 0.15s; background: var(--glass-bg); backdrop-filter: blur(16px);">
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

      <div
        v-if="telegramEngagement.timeline?.length || telegramEngagement.channels?.length"
        class="card-luxury mb-6 animate-fade-in-up hover-lift border border-[var(--glass-border)]"
        style="animation-delay: 0.18s; background: var(--glass-bg); backdrop-filter: blur(16px);"
      >
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fab fa-telegram-plane" />
          {{ $t('analysis.telegramEngagement') }}
        </h2>
        <div v-if="telegramEngagement.timeline?.length" class="mb-4 h-64">
          <Line :data="buildTelegramChart" :options="chartOptions" />
        </div>
        <div v-if="telegramEngagement.channels?.length" class="overflow-x-auto">
          <table class="w-full text-start text-sm">
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
import { analysisApi } from '@/services/api'
import { useDate } from '@/composables/useDate'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseCard from '@/components/ui/BaseCard.vue'
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
const { formatRelative } = useDate()

const loading = ref(true)
const stats = reactive({ totalPriceTypes: 0, totalUpdates: 0, avgChange: 0, recentUpdates: 0 })
const topMovers = ref([])
const categoryBreakdown = ref([])
const chartData = ref(null)
const telegramEngagement = ref({ timeline: [], channels: [] })

const statCards = computed(() => [
  {
    icon: 'fas fa-tags text-gold',
    iconBg: 'rgba(255, 215, 0, 0.15)',
    iconColor: 'var(--primary)',
    value: stats.totalPriceTypes,
    valueClass: 'text-[var(--text-primary)]',
    label: t('analysis.totalPriceTypes'),
  },
  {
    icon: 'fas fa-sync-alt text-gold',
    iconBg: 'rgba(255, 215, 0, 0.15)',
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
    iconBg: 'rgba(255, 215, 0, 0.15)',
    iconColor: 'var(--primary)',
    value: stats.recentUpdates,
    valueClass: 'text-xl text-[var(--text-primary)]',
    label: t('analysis.recentUpdates'),
  },
])

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

const buildTelegramChart = computed(() => {
  if (!telegramEngagement.value.timeline?.length) return null
  return buildChartFromTimeline(telegramEngagement.value.timeline)
})

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
