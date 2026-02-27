<template>
  <div>
    <nav class="mb-6">
      <router-link to="/prices" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Prices
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-4">
      Bulk Update - {{ category?.name ?? 'Category' }}
    </h1>
    <div v-if="loading" class="card-luxury space-y-4 px-4 py-3">
      <BaseSkeleton v-for="i in 5" :key="i" variant="table-row" class="!h-14" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
    </div>
    <form
      v-else-if="priceTypes && priceTypes.length"
      @submit.prevent="handleSubmit"
      class="card-luxury space-y-4 px-4 py-3"
    >
      <div
        v-for="pt in priceTypes"
        :key="pt.id"
        class="flex items-center gap-4 flex-wrap"
      >
        <label class="flex-1 min-w-[200px]">
          {{ pt.name }} ({{ pt.source_currency }}/{{ pt.target_currency }})
        </label>
        <div
          v-if="isDoublePrice"
          class="flex flex-wrap items-center gap-3"
        >
          <div class="flex items-center gap-2">
            <span class="text-xs text-gray-400">{{ $t('dashboard.cashPrice') }}</span>
            <input
              v-model.number="cashPrices[pt.id]"
              type="number"
              step="0.01"
              min="0"
              class="input-luxury w-28"
              :placeholder="pt.cash_price != null ? String(pt.cash_price) : ''"
            />
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-gray-400">{{ $t('dashboard.accountPrice') }}</span>
            <input
              v-model.number="accountPrices[pt.id]"
              type="number"
              step="0.01"
              min="0"
              class="input-luxury w-28"
              :placeholder="pt.account_price != null ? String(pt.account_price) : ''"
            />
          </div>
        </div>
        <input
          v-else
          v-model.number="prices[pt.id]"
          type="number"
          step="0.01"
          min="0"
          class="input-luxury flex-1 max-w-[150px]"
          :placeholder="pt.latest_price != null ? String(pt.latest_price) : ''"
        />
      </div>
      <div class="pt-2">
        <label class="block text-sm font-medium text-gray-400 mb-2">Notes (optional)</label>
        <input v-model="notes" type="text" class="input-luxury" />
      </div>
      <div class="flex gap-4">
        <button type="submit" class="btn-luxury" :disabled="submitting">
          <LoadingSpinner v-if="submitting" class="w-5 h-5" />
          Save All
        </button>
        <router-link to="/prices" class="btn-luxury-outline">Cancel</router-link>
      </div>
    </form>
    <div
      v-else
      class="card-luxury px-4 py-6 text-center text-gray-500"
    >
      {{ $t('emptyState.noPrices') }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { priceApi, categoryApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const categoryId = computed(() => route.params.id)
const loading = ref(true)
const category = ref(null)
const priceTypes = ref([])
const prices = ref({})
const cashPrices = ref({})
const accountPrices = ref({})
const notes = ref('')
const submitting = ref(false)

const isDoublePrice = computed(() => !!category.value?.is_double_price)

onMounted(async () => {
  try {
    const [pRes, cRes] = await Promise.all([priceApi.list(), categoryApi.list()])
    const cats = cRes.data
    category.value = Array.isArray(cats) ? cats.find((c) => String(c.id) === String(categoryId.value)) : null
    const allPrices = pRes.data
    priceTypes.value = Array.isArray(allPrices) ? allPrices.filter((p) => String(p.category_id) === String(categoryId.value)) : []
    prices.value = {}
    cashPrices.value = {}
    accountPrices.value = {}
    priceTypes.value.forEach((pt) => {
      if (pt.latest_price != null && typeof pt.latest_price === 'number') {
        prices.value[pt.id] = Number(pt.latest_price)
      } else if (pt.latest_price && typeof pt.latest_price === 'object' && pt.latest_price.price != null) {
        prices.value[pt.id] = Number(pt.latest_price.price)
      } else {
        prices.value[pt.id] = ''
      }
      if (pt.cash_price != null) {
        cashPrices.value[pt.id] = Number(pt.cash_price)
      }
      if (pt.account_price != null) {
        accountPrices.value[pt.id] = Number(pt.account_price)
      }
    })
  } catch {
    priceTypes.value = []
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  const pricePayload = {}
  const cashPayload = {}
  const accountPayload = {}

  Object.entries(prices.value).forEach(([k, v]) => {
    if (v !== '' && v != null && !Number.isNaN(v)) pricePayload[k] = v
  })
  Object.entries(cashPrices.value).forEach(([k, v]) => {
    if (v !== '' && v != null && !Number.isNaN(v)) cashPayload[k] = v
  })
  Object.entries(accountPrices.value).forEach(([k, v]) => {
    if (v !== '' && v != null && !Number.isNaN(v)) accountPayload[k] = v
  })

  const hasAnyPayload = Object.keys(pricePayload).length || Object.keys(cashPayload).length || Object.keys(accountPayload).length
  if (!hasAnyPayload) return

  submitting.value = true
  try {
    const body = {
      prices: pricePayload,
      notes: notes.value,
    }
    if (Object.keys(cashPayload).length) {
      body.cash_prices = cashPayload
    }
    if (Object.keys(accountPayload).length) {
      body.account_prices = accountPayload
    }
    await priceApi.bulkUpdate(categoryId.value, body)
    router.push('/prices')
  } finally {
    submitting.value = false
  }
}
</script>
