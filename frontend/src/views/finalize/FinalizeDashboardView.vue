<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">Finalize</h1>
    <template v-if="loading">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-28" />
      </div>
    </template>
    <template v-else>
      <div v-if="!data?.has_pending && !data?.has_pending_special" class="card-luxury text-center py-12">
        <i class="fas fa-check-circle text-4xl text-gold mb-4"></i>
        <p class="text-gray-400">All prices are up to date. Nothing to finalize.</p>
      </div>

      <div v-if="data?.pending_by_category?.length" class="mb-8">
        <h2 class="text-lg font-bold text-gold mb-4">Categories with Pending Prices</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="cat in data.pending_by_category"
            :key="cat.category_id"
            class="card-luxury p-4"
          >
            <h3 class="font-semibold text-gold mb-2">{{ cat.category_name }}</h3>
            <p class="text-sm text-gray-400 mb-3">{{ cat.pending_prices?.length ?? 0 }} pending prices</p>
            <router-link
              :to="`/finalize/category/${cat.category_id}`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-check-circle"></i> Finalize
            </router-link>
          </div>
        </div>
      </div>

      <div v-if="data?.pending_special_prices?.length">
        <h2 class="text-lg font-bold text-gold mb-4">Pending Special Prices</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="sp in data.pending_special_prices"
            :key="sp.special_price_type_id"
            class="card-luxury p-4"
          >
            <h3 class="font-semibold text-gold mb-2">{{ sp.special_price_type_name }}</h3>
            <p class="text-gold font-bold mb-3">{{ sp.price }}</p>
            <router-link
              :to="`/finalize/special-price/${sp.price_history_id}`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-check-circle"></i> Finalize
            </router-link>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { finalizeApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const data = ref(null)

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
