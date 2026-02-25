<template>
  <div>
    <nav class="mb-6">
      <router-link to="/categories" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Categories
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Add Price Type</h1>
    <form @submit.prevent="handleSubmit" class="card-luxury max-w-md space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Name</label>
        <input v-model="form.name" type="text" class="input-luxury" required />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Source Currency</label>
        <select v-model="form.source_currency_id" class="input-luxury" required>
          <option v-for="c in currencies" :key="c.id" :value="c.id">{{ c.code }} - {{ c.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Target Currency</label>
        <select v-model="form.target_currency_id" class="input-luxury" required>
          <option v-for="c in currencies" :key="c.id" :value="c.id">{{ c.code }} - {{ c.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Trade Type</label>
        <select v-model="form.trade_type" class="input-luxury" required>
          <option value="buy">Buy</option>
          <option value="sell">Sell</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Description (optional)</label>
        <input v-model="form.description" type="text" class="input-luxury" />
      </div>
      <div class="flex gap-4">
        <button type="submit" class="btn-luxury" :disabled="submitting">
          <LoadingSpinner v-if="submitting" class="w-5 h-5" />
          Save
        </button>
        <router-link :to="`/categories/${categoryId}/edit`" class="btn-luxury-outline">Cancel</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { categoryApi } from '@/services/api'
import api from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const categoryId = computed(() => route.params.id)
const form = ref({
  name: '',
  source_currency_id: '',
  target_currency_id: '',
  trade_type: 'buy',
  description: '',
})
const currencies = ref([])
const submitting = ref(false)

onMounted(async () => {
  try {
    const { data } = await api.get('/categories/currencies/').catch(() => ({}))
    currencies.value = data ?? []
  } catch {
    currencies.value = []
  }
})

async function handleSubmit() {
  submitting.value = true
  try {
    await categoryApi.addPriceType(categoryId.value, form.value)
    router.push('/categories')
  } finally {
    submitting.value = false
  }
}
</script>
