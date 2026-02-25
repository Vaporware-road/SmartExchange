<template>
  <div>
    <nav class="mb-6">
      <router-link to="/special-prices" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Special Prices
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Special Price History</h1>
    <div v-if="loading" class="card-luxury overflow-x-auto p-6">
      <div class="space-y-4">
        <BaseSkeleton v-for="i in 6" :key="i" variant="table-row" />
      </div>
    </div>
    <div v-else class="card-luxury overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="border-b" style="border-color: rgba(255, 215, 0, 0.3);">
            <th class="text-left py-4 px-4 text-gold font-semibold">Price</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="h in history" :key="h.id" class="border-b" style="border-color: rgba(255, 215, 0, 0.1);">
            <td class="py-4 px-4 text-gold font-semibold">{{ Number(h.price).toFixed(2) }}</td>
            <td class="py-4 px-4 text-gray-400">{{ formatDate(h.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { specialPriceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const route = useRoute()
const id = computed(() => route.params.id)
const loading = ref(true)
const history = ref([])

function formatDate(iso) {
  if (!iso) return '-'
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}

onMounted(async () => {
  try {
    const { data } = await specialPriceApi.history(id.value)
    history.value = data ?? []
  } catch {
    history.value = []
  } finally {
    loading.value = false
  }
})
</script>
