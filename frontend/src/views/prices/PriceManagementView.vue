<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('routes.priceHub') }}</h1>

    <div v-if="loading" class="grid grid-cols-1 gap-3">
      <BaseSkeleton v-for="i in 8" :key="i" variant="card" class="!h-36" />
    </div>

    <template v-else>
      <section class="mb-10">
        <h2 class="text-lg font-bold text-[var(--text-secondary)] uppercase tracking-wider mb-4 flex items-center gap-2">
          <i class="fas fa-coins text-gold"></i>
          {{ $t('priceHub.standardCategories') }}
        </h2>
        <div class="space-y-3">
          <CategoryGroup
            v-for="cat in categories"
            :key="cat.id"
            :category="cat"
            :editing-price-type-id="editing.priceTypeId"
            :saving-price-type-id="savingPriceTypeId"
            @edit-start="onEditStart"
            @edit-cancel="onEditCancel"
            @edit-save="onEditSave"
          />
        </div>
        <p v-if="!categories.length" class="text-center text-[var(--text-secondary)] py-8">
          {{ $t('dashboard.noCategoriesFound') }}
        </p>
      </section>

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
              <p class="text-xs text-[var(--text-secondary)] truncate mb-0.5" :title="renderPairSummary(sp)">
                {{ renderPairSummary(sp) }}
              </p>
              <p v-if="extractLatestPrice(sp) != null" class="text-xl sm:text-2xl font-bold text-gold tabular-nums truncate" :title="formatPrice(extractLatestPrice(sp))">
                {{ formatPrice(extractLatestPrice(sp)) }}
              </p>
              <p v-else class="text-sm text-[var(--text-secondary)]">—</p>
            </div>
            <!-- Update: compact icon button at bottom -->
            <router-link
              :to="`/prices/special/${sp.id}/update`"
              class="mt-auto flex items-center justify-center gap-2 py-2.5 px-3.5 rounded-lg text-sm font-semibold bg-gold/15 hover:bg-gold/25 text-gold border border-gold/60 shadow-sm transition-colors shrink-0"
              :title="$t('common.update')"
            >
              <i class="fas fa-sync-alt text-sm"></i>
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
import { useToast } from 'vue-toastification'
import { useI18n } from 'vue-i18n'
import { formatAppNumber } from '@/utils/localeFormat.js'
import { categoryApi, specialPriceApi, priceApi, formatDrfError } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import CategoryGroup from '@/components/prices/CategoryGroup.vue'

const { locale } = useI18n()
const loading = ref(true)
const categories = ref([])
const specialPrices = ref([])
const editing = ref({ categoryId: null, priceTypeId: null })
const savingPriceTypeId = ref(null)
const toast = useToast()

function formatPrice(value) {
  if (value == null || Number.isNaN(value)) return '—'
  const n = Number(value)
  const appLoc = locale.value === 'fa' ? 'fa' : 'en'
  if (n >= 1e9) return formatAppNumber(appLoc, n / 1e9, { maximumFractionDigits: 1, minimumFractionDigits: 1 }) + 'B'
  if (n >= 1e6) return formatAppNumber(appLoc, n / 1e6, { maximumFractionDigits: 1, minimumFractionDigits: 1 }) + 'M'
  if (n >= 1e3) return formatAppNumber(appLoc, n / 1e3, { maximumFractionDigits: 1, minimumFractionDigits: 1 }) + 'K'
  return formatAppNumber(appLoc, n, { maximumFractionDigits: 0 })
}

function normalizeCategoryList(catData) {
  return Array.isArray(catData)
    ? catData
    : (catData?.results ?? []).filter((c) => c && c.id != null)
}

function normalizeSpecialList(spData) {
  return Array.isArray(spData) ? spData : (spData?.results ?? [])
}

function renderPairSummary(sp) {
  const pairs = Array.isArray(sp?.pairs) ? sp.pairs : []
  if (!pairs.length) {
    const src = sp?.source_currency?.code ?? sp?.source_currency ?? '—'
    const tgt = sp?.target_currency?.code ?? sp?.target_currency ?? '—'
    return `${src} / ${tgt}`
  }
  if (pairs.length === 1) {
    const type = pairs[0].trade_type === 'sell' ? 'Sell' : 'Buy'
    return `${pairs[0].name ?? ''} - ${pairs[0].source_currency?.code ?? '—'} / ${pairs[0].target_currency?.code ?? '—'} (${type})`
  }
  const type = pairs[0].trade_type === 'sell' ? 'Sell' : 'Buy'
  return `${pairs[0].name ?? ''} - ${pairs[0].source_currency?.code ?? '—'} / ${pairs[0].target_currency?.code ?? '—'} (${type}) +${pairs.length - 1}`
}

function extractLatestPrice(sp) {
  const candidates = Array.isArray(sp?.pairs) ? sp.pairs : []
  const values = candidates
    .map((pair) => pair?.latest_price?.price)
    .filter((value) => value != null)
    .map((value) => Number(value))
    .filter((value) => Number.isFinite(value))
  if (values.length) return values[0]
  if (sp?.latest_price?.price != null) return Number(sp.latest_price.price)
  if (sp?.latest_price != null) return Number(sp.latest_price)
  return null
}

function onEditStart(payload) {
  editing.value = payload
}

function onEditCancel() {
  editing.value = { categoryId: null, priceTypeId: null }
}

function updatePriceTypeInCategory(categoryId, priceTypeId, nextPrice) {
  const category = categories.value.find((item) => item.id === categoryId)
  if (!category || !Array.isArray(category.price_types)) return
  category.price_types = category.price_types.map((pt) => {
    if (pt.id !== priceTypeId) return pt
    return {
      ...pt,
      latest_price: nextPrice,
      latest_price_at: new Date().toISOString(),
    }
  })
}

async function onEditSave({ categoryId, priceTypeId, value }) {
  const nextPrice = Number(String(value).replaceAll(',', ''))
  if (!Number.isFinite(nextPrice)) {
    toast.error(i18n.global.t('validation.required'))
    return
  }
  savingPriceTypeId.value = priceTypeId
  try {
    await priceApi.update(priceTypeId, { price: nextPrice, notes: '' })
    updatePriceTypeInCategory(categoryId, priceTypeId, nextPrice)
    onEditCancel()
    toast.success(i18n.global.t('toast.saveSuccess'))
  } catch (error) {
    toast.error(formatDrfError(error?.response?.data))
  } finally {
    savingPriceTypeId.value = null
  }
}

onMounted(async () => {
  try {
    const [catRes, spRes] = await Promise.all([
      categoryApi.list(),
      specialPriceApi.list(),
    ])
    categories.value = normalizeCategoryList(catRes.data)
    specialPrices.value = normalizeSpecialList(spRes.data)
  } catch {
    categories.value = []
    specialPrices.value = []
  } finally {
    loading.value = false
  }
})
</script>
