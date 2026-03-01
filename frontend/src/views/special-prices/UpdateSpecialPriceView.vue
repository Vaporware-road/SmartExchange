<template>
  <div>
    <nav class="mb-6">
      <router-link to="/update" class="text-[var(--text-secondary)] hover:text-gold transition-colors">
        <i class="fas me-2" :class="$i18n.locale === 'fa' ? 'fa-arrow-right' : 'fa-arrow-left'"></i>{{ $t('priceHub.backToHub') }}
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('specialPrices.updateTitle') }}</h1>
    <div v-if="loading" class="card-luxury max-w-md p-6 space-y-4">
      <BaseSkeleton variant="text" class="!max-w-[200px] !h-4" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
    </div>
    <form v-else-if="sp" @submit.prevent="handleSubmit" class="card-luxury max-w-md space-y-4">
      <p class="text-[var(--text-secondary)]">{{ sp.name }}</p>
      <div>
        <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('specialPrices.price') }}</label>
        <input v-model.number="price" type="number" step="0.01" min="0" class="input-luxury" required />
      </div>
      <div>
        <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('specialPrices.notesOptional') }}</label>
        <input v-model="notes" type="text" class="input-luxury" />
      </div>
      <div class="flex gap-4">
        <button type="submit" class="btn-luxury" :disabled="submitting">{{ $t('common.save') }}</button>
        <router-link to="/update" class="btn-luxury-outline">{{ $t('common.cancel') }}</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { specialPriceApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const route = useRoute()
const router = useRouter()
const id = computed(() => route.params.id)
const loading = ref(true)
const sp = ref(null)
const price = ref('')
const notes = ref('')
const submitting = ref(false)

onMounted(async () => {
  try {
    const { data } = await specialPriceApi.get(id.value)
    sp.value = data
    if (data?.latest_price?.price) price.value = Number(data.latest_price.price)
  } catch {
    sp.value = null
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  submitting.value = true
  try {
    await specialPriceApi.updatePrice(id.value, { price: price.value, notes: notes.value })
    router.push('/update')
  } finally {
    submitting.value = false
  }
}
</script>
