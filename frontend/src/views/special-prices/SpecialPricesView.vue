<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">Special Prices</h1>
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-36" />
    </div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="sp in specialPrices"
        :key="sp.id"
        class="card-luxury p-4"
      >
        <h3 class="font-semibold text-gold mb-2">{{ sp.name }}</h3>
        <p class="text-sm text-gray-400 mb-2">{{ sp.source_currency?.code ?? sp.source_currency }} / {{ sp.target_currency?.code ?? sp.target_currency }}</p>
        <p v-if="sp.latest_price?.price" class="text-gold font-bold mb-4">{{ Number(sp.latest_price.price).toFixed(2) }}</p>
        <div class="flex gap-2">
          <router-link :to="`/special-prices/${sp.id}/update`" class="btn-luxury-outline text-sm py-2">Update</router-link>
          <router-link :to="`/special-prices/${sp.id}/history`" class="btn-luxury-outline text-sm py-2">History</router-link>
        </div>
      </div>
    </div>
    <p v-if="!loading && (!specialPrices || !specialPrices.length)" class="text-center text-gray-500 py-12">No special prices.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { specialPriceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const specialPrices = ref([])

onMounted(async () => {
  try {
    const { data } = await specialPriceApi.list()
    specialPrices.value = Array.isArray(data) ? data : []
  } catch {
    specialPrices.value = []
  } finally {
    loading.value = false
  }
})
</script>
