<template>
  <div>
    <nav class="mb-6">
      <router-link to="/templates" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Templates
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">New Template</h1>
    <form @submit.prevent="handleSubmit" class="card-luxury max-w-md space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Name</label>
        <input v-model="name" type="text" class="input-luxury" required />
      </div>
      <button type="submit" class="btn-luxury" :disabled="submitting">
        <LoadingSpinner v-if="submitting" class="w-5 h-5" />
        Create
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { templateApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const router = useRouter()
const name = ref('')
const submitting = ref(false)

async function handleSubmit() {
  submitting.value = true
  try {
    await templateApi.create({ name: name.value })
    router.push('/templates')
  } finally {
    submitting.value = false
  }
}
</script>
