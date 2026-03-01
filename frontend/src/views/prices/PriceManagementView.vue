<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('routes.priceHub') }}</h1>

    <div v-if="loading" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-4 gap-3">
      <BaseSkeleton v-for="i in 8" :key="i" variant="card" class="!h-36" />
    </div>

    <template v-else>
      <!-- Section 1: Standard Categories -->
      <section class="mb-10">
        <h2 class="text-lg font-bold text-[var(--text-secondary)] uppercase tracking-wider mb-4 flex items-center gap-2">
          <i class="fas fa-coins text-gold"></i>
          {{ $t('priceHub.standardCategories') }}
        </h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-4 gap-3">
          <div
            v-for="cat in categories"
            :key="cat.id"
            class="group rounded-xl border-2 p-3 sm:p-4 flex flex-col min-h-[140px] max-h-[160px] transition-all duration-300 ease-in-out hover:scale-[1.02] hover:shadow-lg border-[var(--border-color)] bg-[var(--bg-card)]"
          >
            <!-- Header: name top-left (small, truncate), icon top-right -->
            <div class="flex items-start justify-between gap-2 mb-2 shrink-0">
              <h3 class="text-sm font-semibold text-[var(--text-primary)] group-hover:text-gold transition-colors truncate min-w-0 flex-1" :title="cat.name">
                {{ cat.name }}
              </h3>
              <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-primary-muted">
                <i class="fas fa-coins text-gold text-sm"></i>
              </div>
            </div>
            <!-- Price display: prominent center/right -->
            <div class="flex-1 flex flex-col justify-center min-h-0">
              <p v-if="displayPrice(cat) != null" class="text-xl sm:text-2xl font-bold text-gold tabular-nums truncate" :title="formatPrice(displayPrice(cat))">
                {{ formatPrice(displayPrice(cat)) }}
              </p>
              <p v-else class="text-sm text-[var(--text-secondary)]">
                {{ cat.price_type_count ?? cat.price_types?.length ?? 0 }} {{ $t('analysis.priceType') }}
              </p>
            </div>
            <!-- Update: compact icon button at bottom -->
            <router-link
              :to="`/prices/category/${cat.id}/update`"
              class="mt-auto flex items-center justify-center gap-1.5 py-2 px-3 rounded-lg text-sm font-medium bg-[var(--bg-hover)] hover:bg-gold/20 hover:text-gold text-[var(--text-secondary)] border border-[var(--border-color)] transition-colors shrink-0"
              :title="$t('common.update')"
            >
              <i class="fas fa-sync-alt text-xs"></i>
              <span class="hidden sm:inline">{{ $t('common.update') }}</span>
            </router-link>
          </div>
        </div>
        <p v-if="!categories.length" class="text-center text-[var(--text-secondary)] py-8">
          {{ $t('dashboard.noCategoriesFound') }}
        </p>
      </section>

      <!-- Section 2: Special Offers (VIP) -->
      <section v-if="specialPrices.length">
        <h2 class="text-lg font-bold text-[var(--text-secondary)] uppercase tracking-wider mb-4 flex items-center gap-2">
          <i class="fas fa-star text-gold"></i>
          {{ $t('priceHub.specialOffersVip') }}
        </h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-4 gap-3">
          <div
            v-for="sp in specialPrices"
            :key="sp.id"
            class="group rounded-xl border-2 p-3 sm:p-4 flex flex-col min-h-[140px] max-h-[160px] transition-all duration-300 ease-in-out hover:scale-[1.02] hover:shadow-lg overflow-hidden border-[var(--glass-border)]"
            style="border-color: var(--border-card-hover); background: linear-gradient(135deg, var(--bg-card) 0%, var(--primary-muted) 100%);"
          >
            <!-- Header: name top-left (small, truncate), active badge top-right -->
            <div class="flex items-start justify-between gap-2 mb-2 shrink-0">
              <div class="min-w-0 flex-1 flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg flex items-center justify-center text-sm shrink-0 bg-primary-muted border border-[var(--border-card-hover)]">
                  <i :class="sp.icon || 'fas fa-star'" class="text-gold"></i>
                </div>
                <h3 class="text-sm font-semibold text-[var(--primary)] truncate" :title="sp.name">{{ sp.name }}</h3>
              </div>
              <span class="inline-flex items-center gap-1 rounded-full px-1.5 py-0.5 text-[10px] font-medium shrink-0 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                <span class="w-1 h-1 rounded-full bg-emerald-400" />
                {{ $t('dashboard.active') }}
              </span>
            </div>
            <!-- Currency pair (truncate) + Price prominent -->
            <div class="flex-1 flex flex-col justify-center min-h-0">
              <p class="text-xs text-[var(--text-secondary)] truncate mb-0.5">
                {{ (sp.source_currency?.code ?? sp.source_currency) || '—' }} / {{ (sp.target_currency?.code ?? sp.target_currency) || '—' }}
              </p>
              <p v-if="sp.latest_price != null" class="text-xl sm:text-2xl font-bold text-gold tabular-nums truncate" :title="formatPrice(sp.latest_price)">
                {{ formatPrice(sp.latest_price) }}
              </p>
              <p v-else class="text-sm text-[var(--text-secondary)]">—</p>
            </div>
            <!-- Update: compact icon button at bottom -->
            <router-link
              :to="`/prices/special/${sp.id}/update`"
              class="mt-auto flex items-center justify-center gap-1.5 py-2 px-3 rounded-lg text-sm font-medium bg-[var(--bg-hover)] hover:bg-gold/20 hover:text-gold text-[var(--text-secondary)] border border-[var(--border-color)] transition-colors shrink-0"
              :title="$t('common.update')"
            >
              <i class="fas fa-sync-alt text-xs"></i>
              <span class="hidden sm:inline">{{ $t('common.update') }}</span>
            </router-link>
          </div>
        </div>
      </section>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { categoryApi, specialPriceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const categories = ref([])
const specialPrices = ref([])

/** First price type's latest_price for display, or null if none. */
function displayPrice(cat) {
  const pts = cat?.price_types
  if (!pts?.length) return null
  const first = pts[0]
  const price = first?.latest_price
  if (price != null) return Number(price)
  return null
}

function formatPrice(value) {
  if (value == null || Number.isNaN(value)) return '—'
  const n = Number(value)
  if (n >= 1e9) return (n / 1e9).toFixed(1) + 'B'
  if (n >= 1e6) return (n / 1e6).toFixed(1) + 'M'
  if (n >= 1e3) return (n / 1e3).toFixed(1) + 'K'
  return new Intl.NumberFormat(undefined, { maximumFractionDigits: 0 }).format(n)
}

onMounted(async () => {
  try {
    const [catRes, spRes] = await Promise.all([
      categoryApi.list(),
      specialPriceApi.list(),
    ])
    const catData = catRes.data
    categories.value = Array.isArray(catData) ? catData : (catData?.results ?? []).filter((c) => c && c.id != null)
    const spData = spRes.data
    specialPrices.value = Array.isArray(spData) ? spData : (spData?.results ?? [])
  } catch {
    categories.value = []
    specialPrices.value = []
  } finally {
    loading.value = false
  }
})
</script>
