<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('programmerHub.register') }}</h1>
    <form class="card-luxury max-w-xl space-y-3" @submit.prevent="submitRegister">
      <input v-model="form.first_name" class="input-luxury w-full" :placeholder="$t('programmerHub.firstName')" required />
      <input v-model="form.last_name" class="input-luxury w-full" :placeholder="$t('programmerHub.lastName')" required />
      <input v-model="form.exchange_name" class="input-luxury w-full" :placeholder="$t('programmerHub.exchangeName')" required />
      <input v-model="form.country" class="input-luxury w-full" :placeholder="$t('programmerHub.country')" required />
      <input v-model="form.email" type="email" class="input-luxury w-full" :placeholder="$t('programmerHub.email')" required />
      <input v-model="form.phone" class="input-luxury w-full" :placeholder="$t('programmerHub.phone')" required />
      <input v-model="form.telegram_id" class="input-luxury w-full" :placeholder="$t('programmerHub.telegramId')" />
      <input v-model="form.telegram_bot_token" class="input-luxury w-full" :placeholder="$t('programmerHub.botToken')" required />
      <select v-model="form.plan" class="input-luxury w-full">
        <option v-for="p in plans" :key="p" :value="p">{{ $t(`programmerHub.plans.${p}`) }}</option>
      </select>
      <button type="submit" class="btn-luxury w-full" :disabled="saving">
        {{ $t('common.create') }}
      </button>
      <p v-if="generatedPassword" class="text-sm text-gold">
        {{ $t('programmerHub.generatedPassword') }}: {{ generatedPassword }}
      </p>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { authApi, getApiErrorDetails } from '@/services/api'

const plans = ['bronze', 'silver', 'gold']
const { t } = useI18n()
const router = useRouter()
const toast = useToast()
const saving = ref(false)
const generatedPassword = ref('')
const form = reactive({
  first_name: '',
  last_name: '',
  exchange_name: '',
  country: '',
  email: '',
  phone: '',
  telegram_id: '',
  telegram_bot_token: '',
  plan: 'bronze',
})

async function submitRegister() {
  saving.value = true
  generatedPassword.value = ''
  try {
    const { data } = await authApi.programmer.register({ ...form })
    generatedPassword.value = data.generated_password || ''
    toast.success(t('programmerHub.created'))
    router.push('/programmer')
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    saving.value = false
  }
}
</script>
