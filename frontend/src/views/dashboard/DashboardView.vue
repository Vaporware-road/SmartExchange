<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex flex-wrap justify-between items-center gap-4 animate-fade-in-up">
      <div>
        <h1 class="text-3xl font-bold text-gold">{{ $t('dashboard.title') }}</h1>
        <p class="text-sm text-[var(--text-secondary)] mt-1">{{ liveClock }}</p>
      </div>
      <div class="flex items-center gap-3">
        <span class="flex items-center gap-2 px-3 py-1.5 rounded-full text-sm font-medium"
          :class="isOnline
            ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30'
            : 'bg-rose-500/15 text-rose-400 border border-rose-500/30'"
        >
          <span class="w-2 h-2 rounded-full animate-pulse"
            :class="isOnline ? 'bg-emerald-400' : 'bg-rose-400'"
          ></span>
          {{ isOnline ? $t('dashboard.online') : $t('dashboard.offline') }}
        </span>
      </div>
    </div>

    <!-- ─── LOADING SKELETONS ─── -->
    <template v-if="loading">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <BaseSkeleton v-for="i in 3" :key="i" variant="card" class="!h-40" />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <BaseSkeleton v-for="i in 3" :key="'s'+i" variant="card" class="!h-44" />
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <BaseSkeleton variant="card" class="!h-64" />
        <BaseSkeleton variant="card" class="!h-64" />
      </div>
    </template>

    <template v-else>
      <!-- ═══════════════════════════════════════════════
           SECTION 1 — PENDING EXCHANGE REQUESTS
      ═══════════════════════════════════════════════ -->
      <BaseCard
        variant="glass"
        padding="default"
        class="animate-fade-in-up border border-[var(--glass-border)]"
        style="animation-delay: 0.04s"
      >
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center gap-3">
            <div class="p-2.5 rounded-xl bg-amber-500/15">
              <i class="fas fa-exchange-alt text-xl text-amber-400"></i>
            </div>
            <div>
              <h2 class="text-lg font-bold text-[var(--text-primary)]">
                {{ $t('dashboard.exchangeRequests') }}
              </h2>
              <p class="text-xs text-[var(--text-secondary)]">{{ $t('dashboard.last30Days') }}</p>
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span
              v-if="pendingRequests.length"
              class="px-3 py-1 rounded-full text-sm font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30"
            >
              {{ pendingRequests.length }}
            </span>
            <router-link :to="{ path: '/telegram/send', query: { section: 'exchangeRequests' } }" class="btn-luxury-outline text-sm py-1.5 px-4">
              <i class="fas fa-arrow-right me-1"></i>{{ $t('dashboard.viewAll') }}
            </router-link>
          </div>
        </div>

        <!-- Table -->
        <div v-if="pendingRequests.length" class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr class="border-b border-[var(--glass-border)] text-[var(--text-secondary)]">
                <th class="pb-2 text-start font-medium">{{ $t('dashboard.customer') }}</th>
                <th class="pb-2 text-start font-medium">{{ $t('dashboard.exchange') }}</th>
                <th class="pb-2 text-start font-medium">{{ $t('dashboard.amount') }}</th>
                <th class="pb-2 text-start font-medium">{{ $t('common.status') }}</th>
                <th class="pb-2 text-start font-medium hidden sm:table-cell">{{ $t('dashboard.ttl') }}</th>
                <th class="pb-2 text-start font-medium hidden md:table-cell">{{ $t('common.date') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="req in pendingRequests.slice(0, 8)"
                :key="req.id"
                class="border-b border-[var(--glass-border)]/40 hover:bg-white/5 transition-colors cursor-pointer"
                @click="$router.push({ path: '/telegram/send', query: { section: 'exchangeRequests', requestId: String(req.id) } })"
              >
                <td class="py-2.5 pe-4">
                  <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold"
                      :class="tagBadgeClass(req.customer_tag)"
                    >
                      {{ (req.customer_name || '?')[0].toUpperCase() }}
                    </span>
                    <span class="font-medium text-[var(--text-primary)] truncate max-w-[100px]">
                      {{ req.customer_name || `#${req.customer_telegram_user_id}` }}
                    </span>
                  </div>
                </td>
                <td class="py-2.5 pe-4">
                  <span class="font-mono text-[var(--text-primary)]">
                    {{ req.source_currency }}
                    <i class="fas fa-arrow-right text-[var(--text-secondary)] text-xs mx-1"></i>
                    {{ req.target_currency }}
                  </span>
                </td>
                <td class="py-2.5 pe-4 font-semibold text-gold">
                  {{ fmtAmount(req.amount) }}
                </td>
                <td class="py-2.5 pe-4">
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold"
                    :class="statusBadgeClass(req.status)"
                  >
                    {{ statusLabel(req.status) }}
                  </span>
                </td>
                <td class="py-2.5 pe-4 hidden sm:table-cell text-[var(--text-secondary)]">
                  {{ req.ttl_minutes }}m
                </td>
                <td class="py-2.5 hidden md:table-cell text-[var(--text-secondary)] text-xs">
                  {{ formatRelative(req.created_at) }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Empty state -->
        <div v-else class="flex flex-col items-center justify-center py-10 text-[var(--text-secondary)]">
          <i class="fas fa-check-circle text-4xl text-emerald-400/60 mb-3"></i>
          <p class="text-sm">{{ $t('dashboard.noPendingRequests') }}</p>
        </div>
      </BaseCard>

      <!-- ═══════════════════════════════════════════════
           SECTION 2 — BOT STATUS
      ═══════════════════════════════════════════════ -->
      <div class="animate-fade-in-up" style="animation-delay: 0.08s">
        <div class="flex items-center gap-2 mb-3">
          <i class="fas fa-robot text-gold"></i>
          <h2 class="text-lg font-bold text-[var(--text-primary)]">{{ $t('dashboard.botStatus') }}</h2>
        </div>
        <div
          v-if="telegramStats?.bots?.length"
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3"
        >
          <BaseCard
            v-for="(bot, idx) in telegramStats.bots"
            :key="bot.id"
            variant="glass"
            padding="sm"
            class="hover-lift border border-[var(--glass-border)] animate-fade-in-up"
            :style="{ animationDelay: `${0.1 + idx * 0.04}s` }"
          >
            <div class="flex items-start justify-between mb-3">
              <div class="p-2 rounded-lg"
                :class="bot.is_active ? 'bg-emerald-500/15' : 'bg-rose-500/15'"
              >
                <i class="fas fa-robot text-lg"
                  :class="bot.is_active ? 'text-emerald-400' : 'text-rose-400'"
                ></i>
              </div>
              <span class="flex items-center gap-1.5 text-xs font-semibold px-2 py-1 rounded-full border"
                :class="bot.is_active
                  ? 'bg-emerald-500/15 text-emerald-400 border-emerald-500/30'
                  : 'bg-rose-500/15 text-rose-400 border-rose-500/30'"
              >
                <span class="w-1.5 h-1.5 rounded-full"
                  :class="bot.is_active ? 'bg-emerald-400' : 'bg-rose-400'"
                ></span>
                {{ bot.is_active ? $t('dashboard.activeBot') : $t('dashboard.inactiveBot') }}
              </span>
            </div>
            <p class="font-semibold text-[var(--text-primary)] truncate">{{ bot.display_name }}</p>
            <p class="text-xs text-[var(--text-secondary)] mt-0.5">
              {{ bot.channel_count }} {{ $t('dashboard.channels') }}
            </p>
          </BaseCard>
        </div>
        <BaseCard v-else variant="glass" padding="default" class="border border-[var(--glass-border)]">
          <p class="text-center text-[var(--text-secondary)] text-sm py-4">
            <i class="fas fa-robot me-2 opacity-50"></i>{{ $t('common.noData') }}
          </p>
        </BaseCard>
      </div>

      <!-- ═══════════════════════════════════════════════
           SECTION 3 — TELEGRAM ANALYTICS (3 columns)
      ═══════════════════════════════════════════════ -->
      <div class="animate-fade-in-up" style="animation-delay: 0.12s">
        <div class="flex items-center gap-2 mb-3">
          <i class="fab fa-telegram text-gold"></i>
          <h2 class="text-lg font-bold text-[var(--text-primary)]">{{ $t('dashboard.telegramAnalytics') }}</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

          <!-- Col 1: Daily Active Users -->
          <BaseCard
            variant="glass"
            padding="default"
            class="border border-[var(--glass-border)] hover-lift"
          >
            <div class="flex items-center gap-3 mb-4">
              <div class="p-2.5 rounded-xl bg-blue-500/15">
                <i class="fas fa-users text-xl text-blue-400"></i>
              </div>
              <div>
                <p class="text-xs text-[var(--text-secondary)] uppercase tracking-wide font-medium">
                  {{ $t('dashboard.dailyActiveUsers') }}
                </p>
                <p class="text-2xl font-bold text-[var(--text-primary)]">
                  {{ fmtInt(telegramStats?.total_active_users_yesterday ?? 0) }}
                </p>
                <p class="text-xs text-[var(--text-secondary)]">{{ $t('dashboard.usersYesterday') }}</p>
              </div>
            </div>
            <!-- Sparkline -->
            <svg v-if="dailySparklinePath" class="w-full h-16" viewBox="0 0 200 50" preserveAspectRatio="none">
              <defs>
                <linearGradient id="sparkGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#60a5fa" stop-opacity="0"/>
                </linearGradient>
              </defs>
              <path :d="dailySparklineFill" fill="url(#sparkGrad)" />
              <path :d="dailySparklinePath" fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <p class="text-xs text-[var(--text-secondary)] mt-2 text-center">{{ $t('dashboard.last30Days') }}</p>
          </BaseCard>

          <!-- Col 2: Channel Members -->
          <BaseCard
            variant="glass"
            padding="default"
            class="border border-[var(--glass-border)] hover-lift"
          >
            <div class="flex items-center gap-3 mb-4">
              <div class="p-2.5 rounded-xl bg-purple-500/15">
                <i class="fas fa-broadcast-tower text-xl text-purple-400"></i>
              </div>
              <div>
                <p class="text-xs text-[var(--text-secondary)] uppercase tracking-wide font-medium">
                  {{ $t('dashboard.channelMembers') }}
                </p>
                <p class="text-2xl font-bold text-[var(--text-primary)]">
                  {{ fmtInt(telegramStats?.total_members ?? 0) }}
                </p>
                <p class="text-xs text-[var(--text-secondary)]">{{ $t('dashboard.totalMembers') }}</p>
              </div>
            </div>
            <!-- Per-channel breakdown -->
            <ul v-if="telegramStats?.channel_snapshots?.length" class="space-y-2">
              <li
                v-for="ch in telegramStats.channel_snapshots.slice(0, 4)"
                :key="ch.channel_id"
                class="flex items-center justify-between text-sm"
              >
                <span class="text-[var(--text-secondary)] truncate me-2 max-w-[130px]">
                  <i class="fas fa-hashtag text-xs me-1 opacity-60"></i>{{ ch.name }}
                </span>
                <span class="font-semibold text-[var(--text-primary)] tabular-nums">
                  {{ fmtInt(ch.member_count) }}
                </span>
              </li>
            </ul>
            <p v-else class="text-xs text-[var(--text-secondary)] text-center py-4">
              {{ $t('common.noData') }}
            </p>
          </BaseCard>

          <!-- Col 3: Channel Views (N/A) -->
          <BaseCard
            variant="glass"
            padding="default"
            class="border border-[var(--glass-border)] hover-lift"
          >
            <div class="flex items-center gap-3 mb-4">
              <div class="p-2.5 rounded-xl bg-slate-500/15">
                <i class="fas fa-eye text-xl text-slate-400"></i>
              </div>
              <div>
                <p class="text-xs text-[var(--text-secondary)] uppercase tracking-wide font-medium">
                  {{ $t('dashboard.channelViews') }}
                </p>
                <p class="text-2xl font-bold text-[var(--text-secondary)]">—</p>
                <p class="text-xs text-[var(--text-secondary)]">&nbsp;</p>
              </div>
            </div>
            <div class="flex flex-col items-center justify-center py-6 text-center">
              <i class="fas fa-satellite-dish text-3xl text-[var(--text-secondary)] opacity-30 mb-3"></i>
              <p class="text-xs text-[var(--text-secondary)]">{{ $t('dashboard.viewsNotAvailable') }}</p>
            </div>
          </BaseCard>

        </div>
      </div>

      <!-- ═══════════════════════════════════════════════
           ROW: RECENT PRICE UPDATES + QUICK ACTIONS
      ═══════════════════════════════════════════════ -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 animate-fade-in-up" style="animation-delay: 0.16s">

        <!-- Recent Price Updates -->
        <BaseCard variant="glass" padding="default" class="border border-[var(--glass-border)]">
          <div class="flex items-center gap-2 mb-4">
            <i class="fas fa-history text-gold"></i>
            <h2 class="text-base font-bold text-[var(--text-primary)]">{{ $t('dashboard.recentPriceUpdates') }}</h2>
          </div>
          <ul v-if="summary?.recent_price_updates?.length" class="space-y-2.5">
            <li
              v-for="(u, i) in summary.recent_price_updates"
              :key="i"
              class="flex items-center justify-between p-2.5 rounded-lg bg-white/5 border border-[var(--glass-border)]/40"
            >
              <div class="min-w-0">
                <p class="font-medium text-sm text-[var(--text-primary)] truncate">{{ u.price_type }}</p>
                <p class="text-xs text-[var(--text-secondary)]">{{ u.category }}</p>
              </div>
              <div class="text-end ms-3 shrink-0">
                <p class="font-bold text-gold text-sm tabular-nums">{{ fmtPrice(u.price) }}</p>
                <p class="text-xs text-[var(--text-secondary)]">{{ formatRelative(u.updated_at) }}</p>
              </div>
            </li>
          </ul>
          <p v-else class="text-center text-[var(--text-secondary)] text-sm py-8">
            <i class="fas fa-history me-2 opacity-40"></i>{{ $t('dashboard.noRecentUpdates') }}
          </p>
        </BaseCard>

        <!-- Quick Actions -->
        <BaseCard variant="glass" padding="default" class="border border-[var(--glass-border)]">
          <div class="flex items-center gap-2 mb-4">
            <i class="fas fa-bolt text-gold"></i>
            <h2 class="text-base font-bold text-[var(--text-primary)]">{{ $t('dashboard.quickActions') }}</h2>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <router-link
              v-for="(action, idx) in quickActions"
              :key="action.to"
              :to="action.to"
              class="flex flex-col items-center gap-2 p-4 rounded-xl border border-[var(--glass-border)] hover:border-[var(--primary)] hover:bg-white/5 transition-all text-center group animate-fade-in-up"
              :style="{ animationDelay: `${0.18 + idx * 0.04}s` }"
            >
              <div class="p-2.5 rounded-xl group-hover:scale-110 transition-transform"
                :class="action.iconBg"
              >
                <i :class="action.icon + ' text-xl ' + action.iconColor"></i>
              </div>
              <span class="text-sm font-medium text-[var(--text-primary)]">{{ action.label }}</span>
            </router-link>
          </div>
        </BaseCard>

      </div>

      <!-- ═══════════════════════════════════════════════
           PRICE TREND CHART + TOP CATEGORIES
      ═══════════════════════════════════════════════ -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 animate-fade-in-up" style="animation-delay: 0.24s">
        <BaseCard
          v-if="priceTrendLabels.length"
          variant="glass"
          padding="default"
          class="hover-lift border border-[var(--glass-border)]"
        >
          <h2 class="text-base font-bold text-gold mb-1 flex items-center gap-2">
            <i class="fas fa-chart-line"></i> {{ $t('dashboard.priceTrends') }}
          </h2>
          <p v-if="lastTrendLabel" class="text-sm text-[var(--text-secondary)] mb-3 truncate">
            {{ lastTrendLabel }}
          </p>
          <div class="h-64">
            <Line v-if="priceTrendData" :data="priceTrendData" :options="lineChartOptions" />
          </div>
        </BaseCard>
        <BaseCard
          v-else
          variant="glass"
          padding="default"
          class="border border-[var(--glass-border)] flex items-center justify-center min-h-[12rem]"
        >
          <div class="text-center text-[var(--text-secondary)]">
            <i class="fas fa-chart-line text-4xl mb-2 opacity-40"></i>
            <p class="text-sm">{{ $t('analysis.noChartData') }}</p>
          </div>
        </BaseCard>

        <BaseCard variant="glass" padding="default" class="hover-lift border border-[var(--glass-border)]">
          <h2 class="text-base font-bold text-gold mb-4 flex items-center gap-2">
            <i class="fas fa-chart-bar"></i> {{ topCategoriesTitle }}
          </h2>
          <div class="h-56">
            <Bar
              v-if="topCategoriesData && topCategoriesData.labels.length"
              :data="topCategoriesData"
              :options="topCategoriesOptions"
            />
            <p v-else class="h-full flex items-center justify-center text-[var(--text-secondary)] text-sm">
              {{ $t('dashboard.noCategoriesFound') }}
            </p>
          </div>
        </BaseCard>
      </div>

      <!-- ═══════════════════════════════════════════════
           CATEGORIES GRID
      ═══════════════════════════════════════════════ -->
      <BaseCard
        variant="glass"
        padding="default"
        class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
        style="animation-delay: 0.28s"
      >
        <h2 class="text-base font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-folder"></i> {{ $t('dashboard.categories') }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseCard
            v-for="(cat, index) in categories"
            :key="cat.id"
            variant="glass"
            padding="sm"
            class="text-center hover-lift border border-[var(--glass-border)]"
            :style="{ animationDelay: `${0.3 + index * 0.04}s` }"
          >
            <h3 class="font-semibold text-gold mb-2 inline-flex items-center justify-center gap-2 w-full">
              <CategoryIcon :category-name="cat.name" size-class="h-4 w-4" />
              <span class="truncate">{{ cat.name }}</span>
            </h3>
            <p class="text-sm text-[var(--text-secondary)] mb-3">
              {{ fmtInt(cat.price_type_count ?? cat.price_types?.length ?? 0) }} {{ $t('analysis.priceType') }}
            </p>
            <router-link :to="`/prices/category/${cat.id}/update`" class="btn-luxury-outline text-sm py-2">
              <i class="fas fa-edit"></i> {{ $t('dashboard.updatePrices') }}
            </router-link>
          </BaseCard>
          <div v-if="!categories?.length" class="col-span-full text-center text-[var(--text-secondary)] py-8">
            {{ $t('dashboard.noCategoriesFound') }}
          </div>
        </div>
      </BaseCard>

    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { useDate } from '@/composables/useDate'
import { dashboardApi, categoryApi, specialPriceApi, analysisApi, telegramApi } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import { useThemeStore } from '@/stores/theme'
import { formatAppNumber, formatAppDecimal, createAppDateTimeFormat } from '@/utils/localeFormat.js'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseCard from '@/components/ui/BaseCard.vue'
import CategoryIcon from '@/components/ui/CategoryIcon.vue'
import { Line, Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js'
import type {
  DashboardSummary,
  TelegramStats,
  ExchangeRequest,
} from '@/types/dashboard'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Filler, Tooltip, Legend)

const { t, locale } = useI18n()
const auth = useAuthStore()
const themeStore = useThemeStore()
const { formatDateTime } = useDate()
const router = useRouter()

const loading = ref(true)
const summary = ref<DashboardSummary | null>(null)
const telegramStats = ref<TelegramStats | null>(null)
const pendingRequests = ref<ExchangeRequest[]>([])
const categories = ref<any[]>([])
const specialPriceTypes = ref<any[]>([])
const now = ref(new Date())
const isOnline = ref(true)
const timelineData = ref<any>(null)
const priceTrendTimestamps = ref<string[]>([])
const lastTrendLabel = ref('')

let clockIntervalId: ReturnType<typeof setInterval> | null = null

const liveClock = computed(() => formatDateTime(now.value))
const appLoc = computed(() => (locale.value === 'fa' ? 'fa' : 'en'))

function fmtInt(v: number) {
  return formatAppNumber(appLoc.value, v, { maximumFractionDigits: 0 })
}

function fmtPrice(v: number | string | null | undefined) {
  if (v == null || v === '') return '—'
  return formatAppNumber(appLoc.value, Number(v), { maximumFractionDigits: 2 })
}

function fmtAmount(v: string | number) {
  const n = Number(v)
  return isNaN(n) ? String(v) : formatAppNumber(appLoc.value, n, { maximumFractionDigits: 4 })
}

function formatRelative(iso: string | null | undefined): string {
  if (!iso) return '—'
  try {
    const d = new Date(iso)
    const diff = Date.now() - d.getTime()
    const mins = Math.floor(diff / 60000)
    if (mins < 1) return locale.value === 'fa' ? 'همین الان' : 'just now'
    if (mins < 60) return locale.value === 'fa' ? `${mins} دقیقه پیش` : `${mins}m ago`
    const hrs = Math.floor(mins / 60)
    if (hrs < 24) return locale.value === 'fa' ? `${hrs} ساعت پیش` : `${hrs}h ago`
    const days = Math.floor(hrs / 24)
    return locale.value === 'fa' ? `${days} روز پیش` : `${days}d ago`
  } catch {
    return '—'
  }
}

function tagBadgeClass(tag: string) {
  if (tag === 'vip') return 'bg-amber-500/20 text-amber-400'
  if (tag === 'special') return 'bg-purple-500/20 text-purple-400'
  return 'bg-blue-500/20 text-blue-400'
}

function statusBadgeClass(status: string) {
  if (status === 'new') return 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
  if (status === 'successful') return 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
  if (status === 'cancelled') return 'bg-rose-500/20 text-rose-400 border border-rose-500/30'
  return 'bg-slate-500/20 text-slate-400 border border-slate-500/30'
}

function statusLabel(status: string) {
  if (status === 'new') return t('dashboard.statusNew')
  if (status === 'successful') return t('dashboard.statusSuccessful')
  if (status === 'cancelled') return t('dashboard.statusCancelled')
  return status
}

// ── Sparkline for daily usage ──
const dailySparklinePath = computed(() => {
  const data = telegramStats.value?.daily_usage ?? []
  if (data.length < 2) return ''
  const values = data.map((d) => d.active_users)
  const min = Math.min(...values)
  const max = Math.max(...values)
  const range = max - min || 1
  const W = 200
  const H = 50
  const step = W / (values.length - 1)
  const coords = values.map((v, i) => [i * step, H - ((v - min) / range) * (H - 8) - 4])
  return 'M ' + coords.map(([x, y]) => `${x.toFixed(1)} ${y.toFixed(1)}`).join(' L ')
})

const dailySparklineFill = computed(() => {
  const path = dailySparklinePath.value
  if (!path) return ''
  return `${path} L 200 50 L 0 50 Z`
})

// ── Quick actions ──
const quickActions = computed(() => [
  { to: '/categories', label: t('dashboard.shortcutUpdatePrices'), icon: 'fas fa-edit', iconBg: 'bg-blue-500/15', iconColor: 'text-blue-400' },
  { to: '/telegram', label: t('dashboard.goToTelegram'), icon: 'fab fa-telegram', iconBg: 'bg-sky-500/15', iconColor: 'text-sky-400' },
  { to: '/analysis', label: t('dashboard.goToAnalysis'), icon: 'fas fa-chart-line', iconBg: 'bg-emerald-500/15', iconColor: 'text-emerald-400' },
  { to: '/finalize', label: t('dashboard.goToFinalize'), icon: 'fas fa-paper-plane', iconBg: 'bg-amber-500/15', iconColor: 'text-amber-400' },
])

// ── Chart helpers (unchanged from old view) ──
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

function hexToRgba(hex: string, alpha: number) {
  const h = hex.replace('#', '')
  if (h.length !== 6) return hex
  const r = parseInt(h.slice(0, 2), 16)
  const g = parseInt(h.slice(2, 4), 16)
  const b = parseInt(h.slice(4, 6), 16)
  return `rgba(${r},${g},${b},${alpha})`
}

const priceTrendLabels = computed(() => timelineData.value?.labels?.length ? timelineData.value.labels : [])

const priceTrendDirection = computed(() => {
  const data: (number | null)[] = timelineData.value?.datasets?.[0]?.data ?? []
  const values = data.filter((v) => v != null && !Number.isNaN(Number(v))).map(Number)
  if (values.length < 2) return 'neutral'
  return values[values.length - 1] > values[0] ? 'up' : values[values.length - 1] < values[0] ? 'down' : 'neutral'
})

const priceTrendData = computed(() => {
  themeStore.isDark
  if (!priceTrendLabels.value.length || !timelineData.value?.datasets?.length) return null
  const ds = timelineData.value.datasets[0]
  const data = ds?.data ?? []
  const dir = priceTrendDirection.value
  const colors = getChartThemeColors()
  const borderColor = dir === 'up' ? '#10B981' : dir === 'down' ? '#F43F5E' : colors.primary
  const gradStart = dir === 'up' ? 'rgba(16,185,129,0.35)' : dir === 'down' ? 'rgba(244,63,94,0.35)' : hexToRgba(colors.primary, 0.35)
  const bgFall = dir === 'up' ? 'rgba(16,185,129,0.1)' : dir === 'down' ? 'rgba(244,63,94,0.1)' : hexToRgba(colors.primary, 0.1)
  return {
    labels: timelineData.value.labels,
    datasets: [{
      label: ds?.label ?? t('dashboard.priceTrends'),
      data,
      borderColor,
      backgroundColor(context: any) {
        const ctx = context.chart?.ctx
        if (!ctx) return bgFall
        const gradient = ctx.createLinearGradient(0, 0, 0, 220)
        gradient.addColorStop(0, gradStart)
        gradient.addColorStop(1, 'transparent')
        return gradient
      },
      fill: true,
      tension: 0.4,
      pointRadius: data.filter((v: any) => v != null).length <= 24 ? 3 : 0,
      pointHoverRadius: 6,
      borderWidth: 3,
      spanGaps: true,
    }],
  }
})

const lineChartOptions = computed(() => {
  themeStore.isDark
  const c = getChartThemeColors()
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: c.bgCard,
        titleColor: c.primary,
        bodyColor: c.textPrimary,
        borderColor: c.borderColor,
        borderWidth: 1,
        cornerRadius: 12,
        padding: 12,
        callbacks: {
          title(items: any[]) {
            const i = items[0]?.dataIndex
            const iso = priceTrendTimestamps.value[i]
            if (iso) {
              try { return formatDateTime(new Date(iso)) } catch { return iso }
            }
            return items[0]?.label ?? ''
          },
          label(ctx: any) {
            const v = ctx.parsed?.y
            if (v == null) return ''
            return `${ctx.dataset.label}: ${formatAppNumber(appLoc.value, v, { maximumFractionDigits: 2 })}`
          },
        },
      },
    },
    scales: {
      x: { grid: { color: c.borderColor }, ticks: { color: c.textSecondary, maxTicksLimit: 10, maxRotation: 45 } },
      y: {
        grid: { color: c.borderColor },
        ticks: {
          color: c.textSecondary,
          callback: (v: any) => (typeof v === 'number' ? formatAppNumber(appLoc.value, v, { maximumFractionDigits: 2 }) : v),
        },
      },
    },
  }
})

const topCategoriesTitle = computed(() =>
  locale.value === 'fa' ? 'پُرکارترین دسته‌بندی‌ها' : 'Top Categories by Price Types'
)

const topCategoriesData = computed(() => {
  if (!categories.value?.length) return { labels: [], datasets: [{ data: [] }] }
  const rows = [...categories.value]
    .map((c: any) => ({ name: c.name || '—', count: Number(c.price_type_count ?? c.price_types?.length ?? 0) }))
    .sort((a, b) => b.count - a.count)
    .slice(0, 8)
  const c = getChartThemeColors()
  return {
    labels: rows.map((r) => r.name),
    datasets: [{
      label: t('dashboard.priceTypes'),
      data: rows.map((r) => r.count),
      backgroundColor: c.primary.startsWith('#') ? hexToRgba(c.primary, 0.6) : c.primary,
      borderColor: c.primary,
      borderWidth: 1,
      borderRadius: 8,
      maxBarThickness: 28,
    }],
  }
})

const topCategoriesOptions = computed(() => {
  themeStore.isDark
  const c = getChartThemeColors()
  return {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    plugins: {
      legend: { display: false },
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
      x: { beginAtZero: true, grid: { color: c.borderColor }, ticks: { color: c.textSecondary, precision: 0 } },
      y: { grid: { display: false }, ticks: { color: c.textSecondary } },
    },
  }
})

function buildTimelineFromLastUpdated(trend: any) {
  if (!trend?.data?.length) return null
  lastTrendLabel.value = trend.label ?? ''
  const timestamps: string[] = []
  const labels: string[] = []
  const values: number[] = []
  for (const p of trend.data) {
    timestamps.push(p.x)
    const d = new Date(p.x)
    labels.push(
      isNaN(d.getTime())
        ? String(p.x)
        : createAppDateTimeFormat(appLoc.value, { month: 'short', day: 'numeric' }).format(d)
    )
    values.push(p.y)
  }
  priceTrendTimestamps.value = timestamps
  return { labels, datasets: [{ label: trend.label ?? '', data: values }] }
}

function buildTimelineFromAnalysis(dash: any) {
  lastTrendLabel.value = ''
  priceTrendTimestamps.value = []
  const timelines = [...(dash?.timeline_data ?? []), ...(dash?.special_timeline_data ?? [])]
  if (!timelines?.length) return null
  const allTs = new Set<string>()
  for (const ds of timelines) for (const p of ds.data ?? []) allTs.add(p.x)
  const sortedLabels = [...allTs].sort()
  if (!sortedLabels.length) return null
  const shortLabels = sortedLabels.map((iso) => {
    const d = new Date(iso)
    return isNaN(d.getTime()) ? iso : createAppDateTimeFormat(appLoc.value, { month: 'short', day: 'numeric' }).format(d)
  })
  priceTrendTimestamps.value = sortedLabels
  const datasets = timelines.slice(0, 3).map((ds: any, i: number) => {
    const pointMap: Record<string, number> = {}
    for (const p of ds.data ?? []) pointMap[p.x] = p.y
    return { label: ds.label ?? `Series ${i + 1}`, data: sortedLabels.map((ts) => pointMap[ts] ?? null) }
  })
  return { labels: shortLabels, datasets }
}

const silent = { silent: true }

onMounted(async () => {
  try {
    const [summaryRes, telegramStatsRes, categoriesRes, specialRes, analysisRes, exchangeRes] = await Promise.all([
      dashboardApi.summary(silent).catch(() => ({ data: {} })),
      dashboardApi.telegramStats(silent).catch(() => ({ data: {} })),
      categoryApi.list(silent).catch(() => ({ data: [] })),
      specialPriceApi.list(silent).catch(() => ({ data: [] })),
      analysisApi.dashboard({}, silent).catch(() => ({ data: {} })),
      telegramApi.exchangeRequests.list({ status: 'new' }).catch(() => ({ data: { results: [] } })),
    ])

    summary.value = summaryRes.data ?? {}
    telegramStats.value = telegramStatsRes.data ?? {}

    const catData = categoriesRes.data
    categories.value = Array.isArray(catData) ? catData : (catData?.results ?? [])

    const spData = specialRes?.data
    specialPriceTypes.value = Array.isArray(spData) ? spData : (spData?.results ?? [])

    const exData = exchangeRes.data
    pendingRequests.value = Array.isArray(exData) ? exData : (exData?.results ?? [])

    const dash = analysisRes.data ?? {}
    timelineData.value =
      buildTimelineFromLastUpdated(dash.last_updated_price_trend)
      || buildTimelineFromAnalysis(dash)
      || null

    isOnline.value = true
  } catch {
    summary.value = null
    telegramStats.value = null
    categories.value = []
    specialPriceTypes.value = []
    pendingRequests.value = []
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
