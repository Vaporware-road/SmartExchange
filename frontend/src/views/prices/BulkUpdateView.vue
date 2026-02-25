<template>
  <div>
    <nav class="mb-6">
      <router-link to="/prices" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Prices
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Bulk Update - {{ category?.name ?? 'Category' }}</h1>
    <div v-if="loading" class="card-luxury space-y-4 p-6">
      <BaseSkeleton v-for="i in 5" :key="i" variant="table-row" class="!h-14" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
    </div>
    <form v-else @submit.prevent="handleSubmit" class="card-luxury space-y-4">
      <div v-for="pt in priceTypes" :key="pt.id" class="flex items-center gap-4 flex-wrap">
        <label class="flex-1 min-w-[200px]">{{ pt.name }} ({{ pt.source_currency }}/{{ pt.target_currency }})</label>
        <input
          v-model.number="prices[pt.id]"
          type="number"
          step="0.01"
          min="0"
          class="input-luxury flex-1 max-w-[150px]"
          :placeholder="pt.latest_price != null ? String(pt.latest_price) : ''"
        />
      </div>
      <div>
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
const notes = ref('')
const submitting = ref(false)

onMounted(async () => {
  try {
    const [pRes, cRes] = await Promise.all([priceApi.list(), categoryApi.list()])
    const cats = cRes.data
    category.value = Array.isArray(cats) ? cats.find((c) => String(c.id) === String(categoryId.value)) : null
    const allPrices = pRes.data
    priceTypes.value = Array.isArray(allPrices) ? allPrices.filter((p) => String(p.category_id) === String(categoryId.value)) : []
    prices.value = {}
    priceTypes.value.forEach((pt) => {
      prices.value[pt.id] = pt.latest_price != null ? Number(pt.latest_price) : ''
    })
  } catch {
    priceTypes.value = []
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  const payload = {}
  Object.entries(prices.value).forEach(([k, v]) => {
    if (v !== '' && v != null && !Number.isNaN(v)) payload[k] = v
  })
  if (Object.keys(payload).length === 0) return
  submitting.value = true
  try {
    await priceApi.bulkUpdate(categoryId.value, { prices: payload, notes: notes.value })
    router.push('/prices')
  } finally {
    submitting.value = false
  }
}
</script>
