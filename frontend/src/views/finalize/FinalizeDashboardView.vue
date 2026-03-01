<template>
  <div class="flex flex-col items-center">
    <h1 class="text-2xl font-bold text-gold mb-6 w-full text-center">{{ $t('finalize.title') }}</h1>
    <template v-if="loading">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 w-full max-w-5xl">
        <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-28" />
      </div>
    </template>
    <template v-else>
      <div v-if="!data?.has_pending && !data?.has_pending_special" class="card-luxury text-center py-12 w-full max-w-lg">
        <i class="fas fa-check-circle text-4xl text-gold mb-4"></i>
        <p class="text-[var(--text-secondary)]">{{ $t('finalizeDashboard.allUpToDate') }}</p>
      </div>

      <div v-if="showFinalizeAll" class="mb-6">
        <button type="button" class="btn-luxury" @click="finalizeAllModalOpen = true">
          <i class="fas fa-bolt"></i>
          {{ $t('finalize.finalizeAll') }}
        </button>
      </div>

      <div v-if="data?.pending_by_category?.length" class="mb-8 w-full max-w-5xl">
        <h2 class="text-lg font-bold text-gold mb-4 text-center">{{ $t('finalizeDashboard.categoriesWithPending') }}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 justify-items-center">
          <div
            v-for="cat in data.pending_by_category"
            :key="cat.category_id"
            class="card-luxury p-4 w-full max-w-sm"
          >
            <span class="text-xs font-medium text-[var(--text-secondary)] uppercase tracking-wide">{{ $t('finalizeDashboard.categoryLabel') }}</span>
            <h3 class="font-semibold text-gold mb-2 mt-0.5">{{ cat.category_name }}</h3>
            <p class="text-sm text-[var(--text-secondary)] mb-2">
              {{ cat.pending_prices?.length ?? 0 }} {{ $t('finalizeDashboard.pendingPricesCount') }}
            </p>
            <!-- Comparison: first pending price as representative -->
            <div v-if="cat.pending_prices?.length" class="mb-3 space-y-1">
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
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-check-circle"></i> {{ $t('finalize.startFinalize') }}
            </router-link>
          </div>
        </div>
      </div>

      <div v-if="data?.pending_special_prices?.length" class="w-full max-w-5xl">
        <h2 class="text-lg font-bold text-gold mb-4 text-center">{{ $t('finalizeDashboard.pendingSpecialPrices') }}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 justify-items-center">
          <div
            v-for="sp in data.pending_special_prices"
            :key="sp.special_price_type_id"
            class="card-luxury p-4 w-full max-w-sm"
          >
            <span class="text-xs font-medium text-[var(--text-secondary)] uppercase tracking-wide">{{ $t('finalizeDashboard.specialPriceLabel') }}</span>
            <h3 class="font-semibold text-gold mb-2 mt-0.5">{{ sp.special_price_type_name }}</h3>
            <!-- Comparison card -->
            <div class="mb-3 space-y-1">
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
              class="btn-luxury-outline text-sm py-2"
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
import { finalizeApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import FinalizeAllModal from './FinalizeAllModal.vue'

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
  try {
    const { data: res } = await finalizeApi.dashboard()
    data.value = res
  } catch {
    data.value = {}
  } finally {
    loading.value = false
  }
})
</script>
