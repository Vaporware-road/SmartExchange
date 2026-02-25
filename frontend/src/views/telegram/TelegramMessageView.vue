<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">Send Telegram Message</h1>
    <form @submit.prevent="handleSubmit" class="card-luxury max-w-lg space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Channel</label>
        <select v-model="channelId" class="input-luxury" required>
          <option value="">Select channel</option>
          <option v-for="ch in channels" :key="ch.id" :value="ch.id">{{ ch.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Message</label>
        <textarea v-model="message" class="input-luxury" rows="5" required></textarea>
      </div>
      <button type="submit" class="btn-luxury" :disabled="submitting">
        <LoadingSpinner v-if="submitting" class="w-5 h-5" />
        Send
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { telegramApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const channels = ref([])
const channelId = ref('')
const message = ref('')
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
  const ch = channels.value.find((c) => String(c.id) === String(channelId.value))
  if (!ch) return
  submitting.value = true
  try {
    await telegramApi.sendMessage({
      bot_id: ch.bot,
      channel_id: Number(channelId.value),
      message: message.value,
    })
  } finally {
    submitting.value = false
  }
}
</script>
