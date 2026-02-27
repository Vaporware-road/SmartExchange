<template>
  <div>
    <div class="flex flex-wrap justify-between items-center gap-4 mb-4 animate-fade-in-up">
      <h1 class="text-2xl font-bold text-gold">{{ $t('dashboard.title') }}</h1>
      <div class="flex items-center gap-4 text-sm">
        <span class="flex items-center gap-1.5 text-[var(--text-secondary)]">
          <span class="w-2 h-2 rounded-full" :class="isOnline ? 'bg-green-500' : 'bg-red-500'"></span>
          {{ isOnline ? $t('dashboard.online') : $t('dashboard.offline') }}
        </span>
        <span class="text-[var(--text-secondary)]" :title="$t('dashboard.connectionStatus')">{{ liveClock }}</span>
      </div>
    </div>

    <template v-if="loading">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
        <BaseSkeleton v-for="i in 8" :key="i" variant="card" />
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <BaseSkeleton variant="card" class="!h-64" />
        <BaseSkeleton variant="card" class="!h-64" />
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
        <BaseSkeleton v-for="i in 4" :key="'short-' + i" variant="card" class="!h-20" />
      </div>
      <div class="card-luxury mb-4">
        <BaseSkeleton variant="text" class="mb-4 !max-w-[180px] !h-6" />
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-28" />
        </div>
      </div>
    </template>
    <template v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
        <BaseCard
          v-for="(_, statIndex) in 8"
          :key="'stat-' + statIndex"
          variant="glass"
          padding="sm"
          class="flex items-center gap-4 hover-lift animate-fade-in-up border border-[var(--glass-border)]"
          :style="{ animationDelay: `${statIndex * 0.05}s` }"
        >
          <template v-if="statIndex === 0">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-arrow-up text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.highest_price != null ? Number(summary.highest_price).toFixed(2) : 'N/A' }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.highestPostedPrice') }}</p>
              <p v-if="summary?.highest_price_label" class="text-xs text-[var(--text-secondary)] opacity-80">{{ summary.highest_price_label }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 1">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-chart-line text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold" :class="summary?.avg_24h_change > 0 ? 'text-green-400' : summary?.avg_24h_change < 0 ? 'text-red-400' : 'text-[var(--text-secondary)]'">
                {{ (summary?.avg_24h_change ?? 0).toFixed(2) }}%
              </p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.avg24hChange') }}</p>
              <p v-if="summary?.biggest_change" class="text-xs text-[var(--text-secondary)] opacity-80">{{ summary.biggest_change.name }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 2">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-robot text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.total_bots ?? 0 }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.totalBots') }}</p>
              <p class="text-xs text-[var(--text-secondary)] opacity-80">{{ summary?.active_bots ?? 0 }} {{ $t('dashboard.active') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 3">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-broadcast-tower text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.total_channels ?? 0 }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.totalChannels') }}</p>
              <p class="text-xs text-[var(--text-secondary)] opacity-80">{{ summary?.active_channels ?? 0 }} {{ $t('dashboard.active') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 4">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-tags text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.total_price_types ?? 0 }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.priceTypes') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 5">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-sync-alt text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.recent_updates_24h ?? 0 }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.updates24h') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else-if="statIndex === 6">
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-history text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-2xl font-bold text-[var(--text-primary)]">{{ summary?.total_price_updates ?? 0 }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.totalUpdates') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
          <template v-else>
            <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
              <i class="fas fa-clock text-2xl text-gold"></i>
            </div>
            <div>
              <p class="text-xl font-bold text-[var(--text-primary)]">{{ formatLastUpdate(summary?.latest_update_time) }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ $t('dashboard.lastUpdate') }}</p>
              <svg class="w-20 h-8 mt-2 opacity-70" viewBox="0 0 80 32" preserveAspectRatio="none"><path :d="sparklinePath" fill="none" stroke="var(--primary)" stroke-width="1.5" stroke-opacity="0.7"/></svg>
            </div>
          </template>
        </BaseCard>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <BaseCard
          v-if="priceTrendLabels.length"
          variant="glass"
          padding="default"
          class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
          style="animation-delay: 0.08s"
        >
          <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
            <i class="fas fa-chart-line"></i> {{ $t('dashboard.priceTrends') }}
          </h2>
          <div class="h-56">
            <Line v-if="priceTrendData" :data="priceTrendData" :options="lineChartOptions" />
          </div>
        </BaseCard>
        <BaseCard
          v-else
          variant="glass"
          padding="default"
          class="hover-lift animate-fade-in-up border border-[var(--glass-border)] flex flex-col items-center justify-center min-h-[14rem]"
          style="animation-delay: 0.08s"
        >
          <i class="fas fa-chart-line text-4xl text-[var(--text-secondary)] mb-2"></i>
          <p class="text-[var(--text-secondary)] text-sm">{{ $t('analysis.noChartData') }}</p>
        </BaseCard>
        <BaseCard
          variant="glass"
          padding="default"
          class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
          style="animation-delay: 0.1s"
        >
          <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
            <i class="fas fa-chart-pie"></i> {{ $t('dashboard.categoryDistribution') }}
          </h2>
          <div class="h-56 flex items-center justify-center">
            <Doughnut v-if="doughnutData && doughnutData.labels.length" :data="doughnutData" :options="doughnutOptions" class="max-w-[200px]" />
            <p v-else class="text-[var(--text-secondary)] text-sm">{{ $t('dashboard.noCategoriesFound') }}</p>
          </div>
        </BaseCard>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
        <BaseCard
          v-for="(shortcut, idx) in shortcuts"
          :key="shortcut.to"
          variant="glass"
          padding="sm"
          class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
          :style="{ animationDelay: `${0.12 + idx * 0.03}s` }"
        >
          <router-link :to="shortcut.to" class="flex flex-col items-center gap-2 text-center">
            <i :class="shortcut.icon" class="text-2xl text-gold"></i>
            <span class="text-sm font-medium text-[var(--text-primary)]">{{ shortcut.label }}</span>
          </router-link>
        </BaseCard>
      </div>

      <BaseCard variant="glass" padding="default" class="mb-4 hover-lift animate-fade-in-up border border-[var(--glass-border)]" style="animation-delay: 0.1s">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-folder"></i> {{ $t('dashboard.categories') }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseCard
            v-for="(cat, index) in categories"
            :key="cat.id"
            variant="glass"
            padding="sm"
            class="text-center hover-lift animate-fade-in-up border border-[var(--glass-border)]"
            :style="{ animationDelay: `${0.15 + index * 0.05}s` }"
          >
            <h3 class="font-semibold text-gold mb-2">{{ cat.name }}</h3>
            <p class="text-sm text-[var(--text-secondary)] mb-3">{{ cat.price_type_count ?? cat.price_types?.length ?? 0 }} {{ $t('analysis.priceType') }}</p>
            <router-link
              :to="`/prices/category/${cat.id}/update`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-edit"></i> {{ $t('dashboard.updatePrices') }}
            </router-link>
          </BaseCard>
          <div v-if="!categories?.length" class="col-span-full text-center text-[var(--text-secondary)] py-8">
            {{ $t('dashboard.noCategoriesFound') }}
          </div>
        </div>
      </BaseCard>

      <BaseCard v-if="specialPriceTypes?.length" variant="glass" padding="default" class="hover-lift animate-fade-in-up border border-[var(--glass-border)]" style="animation-delay: 0.2s">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-star"></i> {{ $t('dashboard.specialPrices') }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseCard
            v-for="(sp, index) in specialPriceTypes"
            :key="sp.id"
            variant="glass"
            padding="sm"
            class="text-center hover-lift animate-fade-in-up border border-[var(--glass-border)]"
            :style="{ animationDelay: `${0.25 + index * 0.05}s` }"
          >
            <h3 class="font-semibold text-gold mb-2">{{ sp.name }}</h3>
            <p class="text-sm text-[var(--text-secondary)] mb-2">{{ sp.source_currency?.code ?? sp.source_currency }} / {{ sp.target_currency?.code ?? sp.target_currency }}</p>
            <template v-if="sp.cash_price != null || sp.account_price != null">
              <p v-if="sp.cash_price != null" class="text-[var(--text-primary)] text-sm mb-1">
                <i class="fas fa-money-bill-wave text-gold me-1"></i>{{ $t('dashboard.cashPrice') }}: <span class="font-bold text-gold">{{ Number(sp.cash_price).toLocaleString(undefined, { maximumFractionDigits: 2 }) }}</span>
              </p>
              <p v-if="sp.account_price != null" class="text-[var(--text-primary)] text-sm mb-3">
                <i class="fas fa-university text-gold me-1"></i>{{ $t('dashboard.accountPrice') }}: <span class="font-bold text-gold">{{ Number(sp.account_price).toLocaleString(undefined, { maximumFractionDigits: 2 }) }}</span>
              </p>
            </template>
            <p v-else-if="sp.latest_price?.price" class="text-gold font-bold mb-3">{{ Number(sp.latest_price.price).toLocaleString(undefined, { maximumFractionDigits: 2 }) }}</p>
            <router-link
              :to="`/special-prices/${sp.id}/update`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-edit"></i> {{ $t('dashboard.updatePrice') }}
            </router-link>
          </BaseCard>
        </div>
      </BaseCard>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useDate } from '@/composables/useDate'
import { dashboardApi, categoryApi, specialPriceApi, analysisApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseCard from '@/components/ui/BaseCard.vue'
import { Line, Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  ArcElement,
  Filler,
  Tooltip,
  Legend,
  DoughnutController,
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, ArcElement, Filler, Tooltip, Legend, DoughnutController)

const { t, locale } = useI18n()
const { formatDateTime } = useDate()
const loading = ref(true)
const summary = ref(null)
const categories = ref([])
const specialPriceTypes = ref([])
const now = ref(new Date())
const isOnline = ref(true)
const timelineData = ref(null)
let clockIntervalId = null

const liveClock = computed(() => formatDateTime(now.value))

const sparklinePath = computed(() => {
  const points = [12, 18, 14, 22, 19, 28, 24]
  const min = Math.min(...points)
  const max = Math.max(...points)
  const range = max - min || 1
  const w = 80
  const h = 32
  const step = w / (points.length - 1)
  const coords = points.map((v, i) => [i * step, h - ((v - min) / range) * (h - 4) - 2])
  return 'M ' + coords.map(([x, y]) => `${x} ${y}`).join(' L ')
})

const shortcuts = computed(() => {
  const firstCat = categories.value?.[0]
  return [
    { to: firstCat ? `/prices/category/${firstCat.id}/update` : '/prices', icon: 'fas fa-sync-alt', label: t('dashboard.shortcutUpdatePrices') },
    { to: '/special-prices', icon: 'fas fa-star', label: t('dashboard.shortcutSpecialPrices') },
    { to: '/settings/logs', icon: 'fas fa-list', label: t('dashboard.shortcutViewLogs') },
    { to: '/analysis', icon: 'fas fa-chart-line', label: t('dashboard.shortcutAnalysis') },
  ]
})

const priceTrendLabels = computed(() => {
  if (!timelineData.value?.labels?.length) return []
  return timelineData.value.labels
})

const priceTrendData = computed(() => {
  if (!priceTrendLabels.value.length || !timelineData.value?.datasets?.length) return null
  const ds = timelineData.value.datasets[0]
  const data = ds?.data ?? []
  return {
    labels: timelineData.value.labels,
    datasets: [{
      label: ds?.label ?? t('dashboard.priceTrends'),
      data,
      borderColor: '#FFD700',
      backgroundColor(context) {
        const ctx = context.chart?.ctx
        if (!ctx) return 'rgba(255, 215, 0, 0.1)'
        const gradient = ctx.createLinearGradient(0, 0, 0, 250)
        gradient.addColorStop(0, 'rgba(255, 215, 0, 0.35)')
        gradient.addColorStop(1, 'rgba(255, 215, 0, 0)')
        return gradient
      },
      fill: true,
      tension: 0.4,
      pointRadius: 0,
      pointHoverRadius: 5,
      borderWidth: 3,
      spanGaps: true,
    }],
  }
})

const lineChartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  interaction: { mode: 'index', intersect: false },
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: 'rgba(30, 30, 30, 0.92)',
      titleColor: '#FFD700',
      bodyColor: '#F5F5F5',
      borderColor: 'rgba(255, 215, 0, 0.35)',
      borderWidth: 1,
      cornerRadius: 12,
      padding: 12,
      callbacks: {
        label(ctx) {
          const v = ctx.parsed?.y
          if (v == null) return ''
          return `${ctx.dataset.label}: ${Number(v).toLocaleString(undefined, { maximumFractionDigits: 2 })}`
        },
      },
    },
  },
  scales: {
    x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9CA3AF', maxTicksLimit: 8 } },
    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9CA3AF', callback: (v) => typeof v === 'number' ? v.toLocaleString() : v } },
  },
}))

const doughnutData = computed(() => {
  if (!categories.value?.length) return { labels: [], datasets: [{ data: [] }] }
  const labels = categories.value.map((c) => c.name || '—')
  const data = categories.value.map((c) => c.price_type_count ?? c.price_types?.length ?? 1)
  const goldShades = ['#FFD700', '#E6C200', '#B8860B', '#8A7200', '#5C4C00', '#FFE44D', '#CCAC00', '#9A7B00']
  return {
    labels,
    datasets: [{
      data,
      backgroundColor: data.map((_, i) => goldShades[i % goldShades.length]),
      borderColor: 'rgba(30, 30, 30, 0.8)',
      borderWidth: 2,
      hoverOffset: 6,
    }],
  }
})

const doughnutOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  cutout: '60%',
  plugins: {
    legend: { position: 'bottom', labels: { color: '#9CA3AF', usePointStyle: true, padding: 12 } },
    tooltip: {
      backgroundColor: 'rgba(30, 30, 30, 0.92)',
      titleColor: '#FFD700',
      bodyColor: '#F5F5F5',
      borderColor: 'rgba(255, 215, 0, 0.35)',
      borderWidth: 1,
      cornerRadius: 12,
      padding: 12,
      callbacks: {
        label(ctx) {
          const total = ctx.dataset.data.reduce((a, b) => a + b, 0)
          const pct = total ? ((ctx.raw / total) * 100).toFixed(1) : 0
          return ` ${ctx.label}: ${ctx.raw} (${pct}%)`
        },
      },
    },
  },
}))

function formatDate(d) {
  return d?.toLocaleString?.() ?? '-'
}

function formatLastUpdate(iso) {
  if (!iso) return t('dashboard.never')
  try {
    const d = new Date(iso)
    return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  } catch {
    return t('dashboard.never')
  }
}

function buildTimelineFromAnalysis(dash) {
  const timelines = [...(dash?.timeline_data ?? []), ...(dash?.special_timeline_data ?? [])]
  if (!timelines?.length) return null
  const allTs = new Set()
  for (const ds of timelines) {
    for (const p of ds.data ?? []) allTs.add(p.x)
  }
  const labels = [...allTs].sort()
  if (!labels.length) return null
  const shortLabels = labels.map((iso) => {
    const d = new Date(iso)
    return isNaN(d.getTime()) ? iso : d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })
  })
  const datasets = timelines.slice(0, 3).map((ds, i) => {
    const pointMap = {}
    for (const p of ds.data ?? []) pointMap[p.x] = p.y
    return {
      label: ds.label ?? `Series ${i + 1}`,
      data: labels.map((ts) => pointMap[ts] ?? null),
    }
  })
  return { labels: shortLabels, datasets }
}

function getMockTimeline() {
  const days = 7
  const labels = []
  const data = []
  for (let i = days - 1; i >= 0; i--) {
    const d = new Date()
    d.setDate(d.getDate() - i)
    labels.push(d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }))
    data.push(1000 + Math.random() * 500 + i * 20)
  }
  return { labels, datasets: [{ label: 'Price', data }] }
}

onMounted(async () => {
  try {
    const [summaryRes, categoriesRes, specialRes, analysisRes] = await Promise.all([
      dashboardApi.summary(),
      categoryApi.list(),
      specialPriceApi.list().catch(() => ({ data: [] })),
      analysisApi.dashboard().catch(() => ({ data: {} })),
    ])
    summary.value = summaryRes.data
    const catData = categoriesRes.data
    categories.value = Array.isArray(catData) ? catData : (catData?.results ?? [])
    const spData = specialRes?.data
    specialPriceTypes.value = Array.isArray(spData) ? spData : (spData?.results ?? [])
    timelineData.value = buildTimelineFromAnalysis(analysisRes.data) || getMockTimeline()
    isOnline.value = true
  } catch {
    summary.value = {}
    categories.value = []
    specialPriceTypes.value = []
    timelineData.value = getMockTimeline()
    isOnline.value = false
  } finally {
    loading.value = false
  }
  clockIntervalId = setInterval(() => { now.value = new Date() }, 1000)
})

onUnmounted(() => {
  if (clockIntervalId) {
    clearInterval(clockIntervalId)
    clockIntervalId = null
  }
})
</script>
