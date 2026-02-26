<template>
  <div>
    <nav class="mb-6">
      <router-link to="/categories" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
        <span class="ms-2">{{ $t('categories.backToList') }}</span>
      </router-link>
    </nav>

    <h1 class="text-2xl font-bold text-gold mb-6">
      {{ isEdit ? $t('categories.editTitle') : $t('categories.newTitle') }}
    </h1>

    <form @submit.prevent="handleSubmit" class="card-luxury max-w-md space-y-5">
      <div v-if="errors.non_field_errors" class="p-3 rounded-xl bg-danger/10 border border-danger/30 text-danger text-sm">
        {{ errors.non_field_errors }}
      </div>

      <FloatingInput
        v-model="form.name"
        :label="$t('common.name')"
        :error="errors.name"
        :rules="[v => !v?.trim() ? $t('validation.required') : true]"
        required
        @validate="e => errors.name = e"
      />

      <FloatingInput
        v-model="form.description"
        :label="$t('common.description')"
        multiline
        :rows="3"
      />

      <div class="flex gap-4 pt-2">
        <button type="submit" class="btn-luxury" :disabled="submitting || !!errors.name">
          <LoadingSpinner v-if="submitting" class="w-5 h-5" />
          {{ $t('common.save') }}
        </button>
        <router-link to="/categories" class="btn-luxury-outline">
          {{ $t('common.cancel') }}
        </router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { categoryApi } from '@/services/api'
import FloatingInput from '@/components/ui/FloatingInput.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const { t } = useI18n()
const toast = useToast()
const route = useRoute()
const router = useRouter()
const id = computed(() => route.params.id)
const isEdit = computed(() => !!id.value)
const isRtl = computed(() => document.documentElement.dir === 'rtl')

const form = ref({ name: '', description: '' })
const errors = reactive({ name: null, description: null, non_field_errors: null })
const submitting = ref(false)

function applyServerErrors(responseData) {
  if (!responseData || typeof responseData !== 'object') return
  for (const field of Object.keys(errors)) {
    const val = responseData[field]
    if (Array.isArray(val)) {
      errors[field] = val.join(' ')
    } else if (typeof val === 'string') {
      errors[field] = val
    }
  }
}

onMounted(async () => {
  if (isEdit.value) {
    try {
      const { data } = await categoryApi.get(id.value)
      form.value = { name: data.name ?? '', description: data.description ?? '' }
    } catch {
      toast.error(t('toast.serverError'))
    }
  }
})

async function handleSubmit() {
  if (!form.value.name?.trim()) {
    errors.name = t('validation.required')
    return
  }
  submitting.value = true
  try {
    if (isEdit.value) {
      await categoryApi.update(id.value, form.value)
    } else {
      await categoryApi.create(form.value)
    }
    toast.success(t('toast.saveSuccess'))
    router.push('/categories')
  } catch (err) {
    const serverData = err?.response?.data
    if (serverData && typeof serverData === 'object' && err?.response?.status < 500) {
      applyServerErrors(serverData)
    } else {
      toast.error(t('toast.serverError'))
    }
  } finally {
    submitting.value = false
  }
}
</script>
