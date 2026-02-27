<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-4">{{ $t('routes.prices') }}</h1>
    <div v-if="loading" class="space-y-4">
      <div class="card-luxury overflow-x-auto px-4 py-3">
        <div class="space-y-4">
          <BaseSkeleton v-for="i in 8" :key="i" variant="table-row" />
        </div>
      </div>
      <div class="card-luxury px-4 py-3">
        <BaseSkeleton variant="text" class="mb-3 !max-w-[200px] !h-5" />
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-20" />
        </div>
      </div>
    </div>
    <div v-else class="card-luxury overflow-x-auto px-4 py-3">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" style="border-color: rgba(255, 215, 0, 0.3);">
            <th class="text-left py-4 px-4 text-gold font-semibold">Price Type</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Category</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Pair</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Latest Price</th>
            <th class="text-left py-4 px-4 text-gold font-semibold">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="pt in prices"
            :key="pt.id"
            class="border-b hover:bg-white/5 transition-colors"
            style="border-color: rgba(255, 215, 0, 0.1);"
          >
            <td class="py-4 px-4">{{ pt.name }}</td>
            <td class="py-4 px-4 text-gray-400">{{ pt.category_name }}</td>
            <td class="py-4 px-4">{{ pt.source_currency }} / {{ pt.target_currency }}</td>
            <td class="py-4 px-4 text-gold font-semibold">{{ pt.latest_price != null ? Number(pt.latest_price).toFixed(2) : '-' }}</td>
            <td class="py-4 px-4">
              <router-link :to="`/prices/${pt.id}/update`" class="btn-luxury-outline text-sm py-1.5 px-3">
                <i class="fas fa-edit"></i> Update
              </router-link>
              <router-link :to="`/prices/${pt.id}/history`" class="btn-luxury-outline text-sm py-1.5 px-3 ml-2">
                <i class="fas fa-history"></i> History
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
      <p
        v-if="!loading && (!prices || !prices.length)"
        class="text-center text-gray-500 py-6"
      >
        {{ $t('emptyState.noPrices') }}
      </p>
    </div>
    <div class="mt-4">
      <h2 class="text-lg font-bold text-gold mb-3">Update by Category</h2>
      <div
        v-if="categories && categories.length"
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3"
      >
        <div
          v-for="cat in categories"
          :key="cat.id"
          class="card-luxury p-4 flex items-center justify-between"
        >
          <span class="truncate">{{ cat.name }}</span>
          <router-link :to="`/prices/category/${cat.id}/update`" class="btn-luxury-outline text-sm py-2">
            Bulk Update
          </router-link>
        </div>
      </div>
      <p
        v-else
        class="text-center text-gray-500 py-6"
      >
        {{ $t('dashboard.noCategoriesFound') }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { priceApi, categoryApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const prices = ref([])
const categories = ref([])

onMounted(async () => {
  try {
    const [pRes, cRes] = await Promise.all([priceApi.list(), categoryApi.list()])

    const priceData = pRes.data
    prices.value = Array.isArray(priceData) ? priceData : (priceData?.results ?? [])

    const catData = cRes.data
    const rawCategories = Array.isArray(catData) ? catData : (catData?.results ?? [])
    categories.value = rawCategories.filter((c) => c && c.id != null)
  } catch {
    prices.value = []
    categories.value = []
  } finally {
    loading.value = false
  }
})
</script>
