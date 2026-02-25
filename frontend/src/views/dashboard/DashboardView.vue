<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gold">Dashboard</h1>
      <div class="text-gray-400 text-sm">
        <span>{{ formatDate(now) }}</span>
      </div>
    </div>

    <template v-if="loading">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <BaseSkeleton v-for="i in 8" :key="i" variant="card" />
      </div>
      <div class="card-luxury mb-6">
        <BaseSkeleton variant="text" class="mb-4 !max-w-[180px] !h-6" />
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-28" />
        </div>
      </div>
    </template>
    <template v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-arrow-up text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.highest_price?.toFixed(2) ?? 'N/A' }}</p>
            <p class="text-sm text-gray-400">Highest Posted Price</p>
            <p v-if="summary?.highest_price_label" class="text-xs text-gray-500">{{ summary.highest_price_label }}</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-chart-line text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold" :class="summary?.avg_24h_change > 0 ? 'text-green-400' : summary?.avg_24h_change < 0 ? 'text-red-400' : 'text-gray-400'">
              {{ (summary?.avg_24h_change ?? 0).toFixed(2) }}%
            </p>
            <p class="text-sm text-gray-400">Avg 24h Change</p>
            <p v-if="summary?.biggest_change" class="text-xs text-gray-500">{{ summary.biggest_change.name }}</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-robot text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.total_bots ?? 0 }}</p>
            <p class="text-sm text-gray-400">Total Bots</p>
            <p class="text-xs text-gray-500">{{ summary?.active_bots ?? 0 }} active</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-broadcast-tower text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.total_channels ?? 0 }}</p>
            <p class="text-sm text-gray-400">Total Channels</p>
            <p class="text-xs text-gray-500">{{ summary?.active_channels ?? 0 }} active</p>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-tags text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.total_price_types ?? 0 }}</p>
            <p class="text-sm text-gray-400">Price Types</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-sync-alt text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.recent_updates_24h ?? 0 }}</p>
            <p class="text-sm text-gray-400">Updates (24h)</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-history text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-2xl font-bold text-white">{{ summary?.total_price_updates ?? 0 }}</p>
            <p class="text-sm text-gray-400">Total Updates</p>
          </div>
        </div>
        <div class="card-luxury flex items-center gap-4">
          <div class="p-3 rounded-xl" style="background: rgba(255, 215, 0, 0.15);">
            <i class="fas fa-clock text-2xl text-gold"></i>
          </div>
          <div>
            <p class="text-xl font-bold text-white">{{ formatLastUpdate(summary?.latest_update_time) }}</p>
            <p class="text-sm text-gray-400">Last Update</p>
          </div>
        </div>
      </div>

      <div class="card-luxury mb-6">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-folder"></i> Categories
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="cat in categories"
            :key="cat.id"
            class="p-4 rounded-xl border text-center transition-all hover:border-gold/50"
            style="background: rgba(31, 31, 31, 0.5); border-color: rgba(255, 215, 0, 0.2);"
          >
            <h3 class="font-semibold text-gold mb-2">{{ cat.name }}</h3>
            <p class="text-sm text-gray-400 mb-3">{{ cat.price_type_count ?? cat.price_types?.length ?? 0 }} price types</p>
            <router-link
              :to="`/prices/category/${cat.id}/update`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-edit"></i> Update Prices
            </router-link>
          </div>
          <div v-if="!categories?.length" class="col-span-full text-center text-gray-500 py-8">
            No categories found.
          </div>
        </div>
      </div>

      <div v-if="specialPriceTypes?.length" class="card-luxury">
        <h2 class="text-lg font-bold text-gold mb-4 flex items-center gap-2">
          <i class="fas fa-star"></i> Special Prices
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="sp in specialPriceTypes"
            :key="sp.id"
            class="p-4 rounded-xl border text-center"
            style="background: rgba(31, 31, 31, 0.5); border-color: rgba(255, 215, 0, 0.2);"
          >
            <h3 class="font-semibold text-gold mb-2">{{ sp.name }}</h3>
            <p class="text-sm text-gray-400 mb-2">{{ sp.source_currency?.code ?? sp.source_currency }} / {{ sp.target_currency?.code ?? sp.target_currency }}</p>
            <p v-if="sp.latest_price?.price" class="text-gold font-bold mb-3">{{ Number(sp.latest_price.price).toFixed(2) }}</p>
            <router-link
              :to="`/special-prices/${sp.id}/update`"
              class="btn-luxury-outline text-sm py-2"
            >
              <i class="fas fa-edit"></i> Update Price
            </router-link>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { dashboardApi, categoryApi, specialPriceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const summary = ref(null)
const categories = ref([])
const specialPriceTypes = ref([])
const now = ref(new Date())

function formatDate(d) {
  return d?.toLocaleString?.() ?? '-'
}

function formatLastUpdate(iso) {
  if (!iso) return 'Never'
  try {
    const d = new Date(iso)
    return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  } catch {
    return 'Never'
  }
}

onMounted(async () => {
  try {
    const [summaryRes, categoriesRes, specialRes] = await Promise.all([
      dashboardApi.summary(),
      categoryApi.list(),
      specialPriceApi.list().catch(() => ({ data: [] })),
    ])
    summary.value = summaryRes.data
    categories.value = categoriesRes.data
    specialPriceTypes.value = Array.isArray(specialRes?.data) ? specialRes.data : []
  } catch {
    summary.value = {}
    categories.value = []
    specialPriceTypes.value = []
  } finally {
    loading.value = false
  }
  setInterval(() => { now.value = new Date() }, 1000)
})
</script>
