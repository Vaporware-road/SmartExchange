<template>
  <div class="finalize-dashboard mx-auto flex w-full max-w-6xl flex-col items-center px-1 pb-2">
    <h1 class="mb-4 w-full text-center text-2xl font-bold text-gold">{{ $t('finalize.title') }}</h1>
    <template v-if="loading">
      <div class="grid w-full grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-3">
        <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-28" />
      </div>
    </template>
    <template v-else>
      <div v-if="!data?.has_pending && !data?.has_pending_special" class="finalize-empty w-full max-w-xl text-center">
        <i class="fas fa-check-circle mb-3 text-4xl text-gold"></i>
        <p class="text-[var(--text-secondary)]">{{ $t('finalizeDashboard.allUpToDate') }}</p>
      </div>

      <div v-if="showFinalizeAll" class="mb-5">
        <button type="button" class="btn-luxury finalize-all-btn" @click="finalizeAllModalOpen = true">
          <i class="fas fa-bolt"></i>
          {{ $t('finalize.finalizeAll') }}
        </button>
      </div>

      <div v-if="data?.pending_by_category?.length" class="mb-6 w-full">
        <h2 class="mb-3 text-center text-lg font-semibold text-gold">{{ $t('finalizeDashboard.categoriesWithPending') }}</h2>
        <div class="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-3">
          <div
            v-for="cat in data.pending_by_category"
            :key="cat.category_id"
            class="finalize-card w-full"
          >
            <span class="text-xs font-medium uppercase tracking-wide text-[var(--text-secondary)]">{{ $t('finalizeDashboard.categoryLabel') }}</span>
            <h3 class="mb-2 mt-0.5 inline-flex items-center gap-2 text-base font-semibold text-gold">
              <span class="inline-flex h-6 w-6 items-center justify-center rounded-md bg-primary-muted">
                <CategoryIcon :category-name="cat.category_name" size-class="h-3.5 w-3.5" />
              </span>
              <span>{{ cat.category_name }}</span>
            </h3>
            <p class="mb-2 text-sm text-[var(--text-secondary)]">
              {{ cat.pending_prices?.length ?? 0 }} {{ $t('finalizeDashboard.pendingPricesCount') }}
            </p>
            <!-- Comparison: first pending price as representative -->
            <div v-if="cat.pending_prices?.length" class="mb-3 space-y-1.5">
              <div v-if="getFirstPending(cat.pending_prices)" class="text-sm">
                <div v-if="getFirstPending(cat.pending_prices).previous_price != null" class="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
                  <span class="text-[var(--text-secondary)]">
                    {{ $t('finalize.oldPrice') }}: {{ formatPrice(getFirstPending(cat.pending_prices).previous_price) }}
                  </span>
                  <span class="text-gold font-bold">{{ $t('finalize.newPrice') }}: {{ formatPrice(getFirstPending(cat.pending_prices).price) }}</span>
                  <span
                    :class="priceChangeClass(getFirstPending(cat.pending_prices))"
                    class="font-medium"
                  >
                    {{ $t('finalize.change') }}: {{ formatPriceChange(getFirstPending(cat.pending_prices)) }}
                  </span>
                </div>
                <div v-else>
                  <span class="text-gold font-bold">{{ $t('finalize.newPrice') }}: {{ formatPrice(getFirstPending(cat.pending_prices).price) }}</span>
                  <span class="text-[var(--text-secondary)] text-xs ms-1">({{ $t('finalize.firstPublication') }})</span>
                </div>
                <p v-if="getFirstPending(cat.pending_prices).created_at" class="text-xs text-[var(--text-secondary)] mt-1">
                  {{ $t('finalize.lastDraftUpdate') }}: {{ formatDate(getFirstPending(cat.pending_prices).created_at) }}
                </p>
              </div>
              <p v-if="(cat.pending_prices?.length ?? 0) > 1" class="text-xs text-[var(--text-secondary)]">
                {{ $t('finalizeDashboard.andMore', { count: cat.pending_prices.length - 1 }) }}
              </p>
            </div>
            <router-link
              :to="`/finalize/category/${cat.category_id}`"
              class="btn-luxury-outline finalize-link-btn text-sm py-2"
            >
              <i class="fas fa-check-circle"></i> {{ $t('finalize.startFinalize') }}
            </router-link>
          </div>
        </div>
      </div>

      <div v-if="data?.pending_special_prices?.length" class="w-full">
        <h2 class="mb-3 text-center text-lg font-semibold text-gold">{{ $t('finalizeDashboard.pendingSpecialPrices') }}</h2>
        <div class="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-3">
          <div
            v-for="sp in data.pending_special_prices"
            :key="sp.special_price_type_id"
            class="finalize-card w-full"
          >
            <span class="text-xs font-medium uppercase tracking-wide text-[var(--text-secondary)]">{{ $t('finalizeDashboard.specialPriceLabel') }}</span>
            <h3 class="mb-2 mt-0.5 text-base font-semibold text-gold">{{ sp.special_price_type_name }}</h3>
            <!-- Comparison card -->
            <div class="mb-3 space-y-1.5">
              <div v-if="sp.previous_price != null" class="text-sm flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
                <span class="text-[var(--text-secondary)]">{{ $t('finalize.oldPrice') }}: {{ formatPrice(sp.previous_price) }}</span>
                <span class="text-gold font-bold">{{ $t('finalize.newPrice') }}: {{ formatPrice(sp.price) }}</span>
                <span :class="priceChangeClass(sp)" class="font-medium">{{ $t('finalize.change') }}: {{ formatPriceChange(sp) }}</span>
              </div>
              <div v-else>
                <span class="text-gold font-bold">{{ $t('finalize.newPrice') }}: {{ formatPrice(sp.price) }}</span>
                <span class="text-[var(--text-secondary)] text-xs ms-1">({{ $t('finalize.firstPublication') }})</span>
              </div>
              <p v-if="sp.created_at" class="text-xs text-[var(--text-secondary)] mt-1">
                {{ $t('finalize.lastDraftUpdate') }}: {{ formatDate(sp.created_at) }}
              </p>
            </div>
            <router-link
              :to="`/finalize/special-price/${sp.price_history_id}`"
              class="btn-luxury-outline finalize-link-btn text-sm py-2"
            >
              <i class="fas fa-check-circle"></i> {{ $t('finalize.startFinalize') }}
            </router-link>
          </div>
        </div>
      </div>
    </template>

    <FinalizeAllModal
      v-if="finalizeAllModalOpen"
      :data="data"
      @close="finalizeAllModalOpen = false"
      @success="onFinalizeAllSuccess"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { useI18n } from 'vue-i18n'
import { finalizeApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import FinalizeAllModal from './FinalizeAllModal.vue'
import CategoryIcon from '@/components/ui/CategoryIcon.vue'

const toast = useToast()
const { t } = useI18n()
const loading = ref(true)
const data = ref(null)
const finalizeAllModalOpen = ref(false)

const showFinalizeAll = computed(() => {
  if (!data.value) return false
  const cats = data.value.pending_by_category?.length ?? 0
  const special = data.value.pending_special_prices?.length ?? 0
  return (cats + special) > 1
})

function onFinalizeAllSuccess() {
  finalizeAllModalOpen.value = false
  fetchData()
}

async function fetchData() {
  try {
    const { data: res } = await finalizeApi.dashboard()
    if (res?.degraded) {
      toast.warning(res.detail || t('apiErrors.fallback.server'))
    }
    data.value = res
  } catch {
    data.value = {}
  } finally {
    loading.value = false
  }
}

function getFirstPending(pendingPrices) {
  return pendingPrices?.[0] ?? null
}

function formatPrice(value) {
  if (value == null || value === '') return '—'
  const num = typeof value === 'string' ? parseFloat(value) : value
  if (Number.isNaN(num)) return String(value)
  return num.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
}

function formatPriceChange(item) {
  const prev = item.previous_price != null ? parseFloat(item.previous_price) : null
  const next = item.price != null ? parseFloat(item.price) : null
  if (prev == null || next == null || Number.isNaN(prev) || Number.isNaN(next)) return '—'
  const diff = next - prev
  const sign = diff >= 0 ? '+' : ''
  return sign + formatPrice(String(diff))
}

function priceChangeClass(item) {
  const prev = item.previous_price != null ? parseFloat(item.previous_price) : null
  const next = item.price != null ? parseFloat(item.price) : null
  if (prev == null || next == null || Number.isNaN(prev) || Number.isNaN(next)) return 'text-[var(--text-secondary)]'
  const diff = next - prev
  if (diff > 0) return 'text-success'
  if (diff < 0) return 'text-danger'
  return 'text-[var(--text-secondary)]'
}

function formatDate(isoString) {
  if (!isoString) return '—'
  try {
    const d = new Date(isoString)
    return d.toLocaleString(undefined, { dateStyle: 'short', timeStyle: 'short' })
  } catch {
    return isoString
  }
}

onMounted(async () => {
  await fetchData()
})
</script>

<style scoped>
.finalize-card,
.finalize-empty {
  border: 1px solid var(--border-card);
  border-radius: 1rem;
  background: color-mix(in srgb, var(--bg-card) 92%, transparent);
  padding: 0.9rem;
  box-shadow: 0 8px 20px -18px rgba(15, 23, 42, 0.8);
}

.finalize-all-btn {
  padding-inline: 1rem;
  padding-block: 0.55rem;
}

.finalize-link-btn {
  width: 100%;
  justify-content: center;
}
</style>
