<template>
  <div>
    <nav class="mb-6">
      <router-link to="/finalize" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Finalize
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Finalize Special Price</h1>
    <form @submit.prevent="handleSubmit" class="card-luxury max-w-lg space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Channel</label>
        <select v-model="channelId" class="input-luxury" required>
          <option value="">Select a channel</option>
          <option v-for="ch in channels" :key="ch.id" :value="ch.id">{{ ch.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Notes (optional)</label>
        <input v-model="notes" type="text" class="input-luxury" />
      </div>
      <div class="flex gap-4">
        <button type="submit" class="btn-luxury" :disabled="submitting">
          <LoadingSpinner v-if="submitting" class="w-5 h-5" />
          Finalize
        </button>
        <router-link to="/finalize" class="btn-luxury-outline">Cancel</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { finalizeApi, telegramApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const specialPriceHistoryId = computed(() => route.params.id)
const channels = ref([])
const channelId = ref('')
const notes = ref('')
const submitting = ref(false)

onMounted(async () => {
  try {
    const { data } = await telegramApi.channels()
    channels.value = data ?? []
  } catch {
    channels.value = []
  }
})

async function handleSubmit() {
  submitting.value = true
  try {
    await finalizeApi.finalizeSpecialPrice(specialPriceHistoryId.value, {
      channel_id: Number(channelId.value),
      notes: notes.value,
    })
    router.push('/finalize')
  } finally {
    submitting.value = false
  }
}
</script>
