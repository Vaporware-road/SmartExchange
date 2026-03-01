<template>
  <div>
    <nav class="mb-6">
      <router-link
        to="/categories"
        class="text-[var(--text-secondary)] hover:text-gold transition-colors inline-flex items-center gap-2"
      >
        <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
        {{ $t('categories.backToList') }}
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('specialPrices.newTitle') }}</h1>
    <BaseCard
      variant="glass"
      padding="default"
      class="w-full max-w-md animate-fade-in-up border border-[var(--glass-border)]"
    >
      <form @submit.prevent="handleSubmit" class="space-y-5">
        <div
          v-if="errors.non_field_errors"
          class="p-3 rounded-xl bg-danger/10 border border-danger/30 text-danger text-sm"
        >
          {{ errors.non_field_errors }}
        </div>

        <FloatingInput
          v-model="form.name"
          :label="$t('common.name')"
          :error="errors.name"
          :rules="[v => !v?.trim() ? $t('validation.required') : true]"
          required
          @validate="e => (errors.name = e)"
        />

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('specialPrices.sourceCurrency') }}
          </label>
          <select v-model="form.source_currency_id" class="input-luxury" required>
            <option value="" disabled>—</option>
            <option v-for="c in currencies" :key="c.id" :value="c.id">{{ c.code }} - {{ c.name }}</option>
          </select>
          <p v-if="errors.source_currency_id" class="text-sm text-red-400 mt-1">{{ errors.source_currency_id }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('specialPrices.targetCurrency') }}
          </label>
          <select v-model="form.target_currency_id" class="input-luxury" required>
            <option value="" disabled>—</option>
            <option v-for="c in currencies" :key="c.id" :value="c.id">{{ c.code }} - {{ c.name }}</option>
          </select>
          <p v-if="errors.target_currency_id" class="text-sm text-red-400 mt-1">{{ errors.target_currency_id }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('specialPrices.tradeType') }}
          </label>
          <select v-model="form.trade_type" class="input-luxury" required>
            <option value="buy">{{ $t('specialPrices.buy') }}</option>
            <option value="sell">{{ $t('specialPrices.sell') }}</option>
          </select>
        </div>

        <FloatingInput
          v-model="form.description"
          :label="$t('common.description')"
          multiline
          :rows="2"
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
    </BaseCard>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import api from '@/services/api'
import { specialPriceApi } from '@/services/api'
import FloatingInput from '@/components/ui/FloatingInput.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import BaseCard from '@/components/ui/BaseCard.vue'

const { t } = useI18n()
const toast = useToast()
const router = useRouter()
const isRtl = computed(() => document.documentElement.dir === 'rtl')

const form = ref({
  name: '',
  source_currency_id: '',
  target_currency_id: '',
  trade_type: 'buy',
  description: '',
})
const errors = reactive({
  name: null,
  source_currency_id: null,
  target_currency_id: null,
  non_field_errors: null,
})
const currencies = ref([])
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
  try {
    const { data } = await api.get('/categories/currencies/').catch(() => ({}))
    currencies.value = data ?? []
  } catch {
    currencies.value = []
  }
})

async function handleSubmit() {
  if (!form.value.name?.trim()) {
    errors.name = t('validation.required')
    return
  }
  if (!form.value.source_currency_id || !form.value.target_currency_id) {
    return
  }
  submitting.value = true
  try {
    await specialPriceApi.create({
      name: form.value.name.trim(),
      source_currency_id: Number(form.value.source_currency_id),
      target_currency_id: Number(form.value.target_currency_id),
      trade_type: form.value.trade_type,
      description: form.value.description?.trim() || '',
    })
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
