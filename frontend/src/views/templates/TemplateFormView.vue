<template>
  <div>
    <nav class="mb-6">
      <router-link to="/templates" class="text-[var(--text-secondary)] hover:text-gold transition-colors inline-flex items-center gap-2">
        <i class="fas fa-arrow-left me-2"></i>{{ $t('templateEditor.backToTemplates') }}
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('routes.templateNew') }}</h1>
    <form @submit.prevent="handleSubmit" class="card-luxury max-w-md space-y-4">
      <p v-if="presetCategory" class="text-sm text-[var(--text-secondary)] rounded-xl px-3 py-2 bg-[var(--bg-input)]">
        {{ $t('categories.templateForCategory') || 'Creating template for category' }}: <strong class="text-gold">{{ presetCategory.name }}</strong>
      </p>
      <div>
        <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('common.name') }}</label>
        <input v-model="name" type="text" class="input-luxury" required />
      </div>
      <button type="submit" class="btn-luxury" :disabled="submitting">
        <LoadingSpinner v-if="submitting" class="w-5 h-5" />
        {{ $t('common.create') }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { templateApi, templateEditorApi, categoryApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const router = useRouter()
const route = useRoute()
const name = ref('')
const submitting = ref(false)
const presetCategory = ref(null)

const categoryIdFromQuery = computed(() => {
  const id = route.query.category_id
  if (id == null || id === '') return null
  const n = Number(id)
  return Number.isFinite(n) ? n : null
})

onMounted(async () => {
  const cid = categoryIdFromQuery.value
  if (cid) {
    try {
      const { data } = await categoryApi.get(cid)
      presetCategory.value = data
    } catch {
      presetCategory.value = null
    }
  }
})

async function handleSubmit() {
  submitting.value = true
  try {
    const cid = categoryIdFromQuery.value
    if (cid != null) {
      const { data } = await templateEditorApi.create({ name: name.value, category: cid })
      router.push(`/templates/${data.id}/editor`)
      return
    }
    await templateApi.create({ name: name.value })
    router.push('/templates')
  } finally {
    submitting.value = false
  }
}
</script>
