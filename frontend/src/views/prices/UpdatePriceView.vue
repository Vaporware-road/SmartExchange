<template>
  <div>
    <nav class="mb-6">
      <router-link to="/prices" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Prices
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Update Price</h1>
    <div v-if="loading" class="card-luxury max-w-md p-6 space-y-4">
      <BaseSkeleton variant="text" class="!max-w-[200px] !h-4" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
    </div>
    <div v-else-if="priceType" class="card-luxury max-w-md">
      <p class="text-gray-400 mb-2">{{ priceType.name }}</p>
      <p class="text-sm text-gray-500 mb-4">{{ priceType.source_currency }} / {{ priceType.target_currency }} - {{ priceType.category_name }}</p>
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">New Price</label>
          <input v-model.number="price" type="number" step="0.01" min="0" class="input-luxury" required />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Notes (optional)</label>
          <input v-model="notes" type="text" class="input-luxury" placeholder="Optional notes" />
        </div>
        <div class="flex gap-4">
          <button type="submit" class="btn-luxury" :disabled="submitting">
            <LoadingSpinner v-if="submitting" class="w-5 h-5" />
            <i v-else class="fas fa-save"></i>
            Save
          </button>
          <router-link to="/prices" class="btn-luxury-outline">Cancel</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { priceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const id = computed(() => route.params.id)
const loading = ref(true)
const priceType = ref(null)
const price = ref('')
const notes = ref('')
const submitting = ref(false)

onMounted(async () => {
  try {
    const { data } = await priceApi.list()
    priceType.value = data.find((p) => String(p.id) === String(id.value))
    if (priceType.value?.latest_price != null) {
      price.value = Number(priceType.value.latest_price)
    }
  } catch {
    priceType.value = null
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  submitting.value = true
  try {
    await priceApi.update(id.value, { price: price.value, notes: notes.value })
    router.push('/prices')
  } finally {
    submitting.value = false
  }
}
</script>
