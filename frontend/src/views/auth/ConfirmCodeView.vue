<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12" style="background: var(--bg-base)">
    <div class="w-full max-w-md">
      <div class="card-luxury text-center mb-6">
        <div class="mx-auto w-fit mb-4">
          <AppBrandLogo size="xl" rounded="xl" />
        </div>
        <h1 class="text-2xl font-bold text-gold mb-1">{{ $t('auth.confirmTitle') }}</h1>
        <p class="text-sm text-[var(--text-secondary)]">
          {{ $t(channel === 'sms' ? 'auth.confirmSentSms' : 'auth.confirmSentEmail', { to: destination }) }}
        </p>
      </div>

      <div class="card-luxury">
        <form class="space-y-4" @submit.prevent="submit">
          <AlertMessage v-if="error" type="error" :show="true" @dismiss="error = ''">{{ error }}</AlertMessage>
          <AlertMessage v-if="notice" type="success" :show="true" @dismiss="notice = ''">{{ notice }}</AlertMessage>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.confirmCode') }}</label>
            <input
              v-model="code"
              type="text"
              inputmode="numeric"
              autocomplete="one-time-code"
              maxlength="6"
              class="input-luxury text-center tracking-[0.5em] text-xl"
              dir="ltr"
              required
              autofocus
            >
          </div>

          <button type="submit" class="btn-luxury w-full" :disabled="loading || code.length < 6">
            <LoadingSpinner v-if="loading" class="w-5 h-5" />
            <i v-else class="fas fa-check" />
            <span>{{ $t('auth.confirmButton') }}</span>
          </button>
        </form>

        <div class="mt-4 flex items-center justify-between text-xs">
          <button type="button" class="text-gold hover:underline" :disabled="resending" @click="resend">
            {{ $t('auth.confirmResend') }}
          </button>
          <router-link to="/panel" class="text-[var(--text-secondary)] hover:underline">
            {{ $t('auth.confirmSkip') }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { getApiErrorDetails } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import AlertMessage from '@/components/ui/AlertMessage.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

const { t } = useI18n()
const router = useRouter()
const auth = useAuthStore()

const code = ref('')
const channel = ref('email')
const error = ref('')
const notice = ref('')
const loading = ref(false)
const resending = ref(false)

const destination = computed(() =>
  channel.value === 'sms' ? auth.user?.phone || '' : auth.user?.email || '',
)

/* Already-verified accounts (Google signups) have nothing to confirm. */
onMounted(async () => {
  if (!auth.needsEmailVerification) {
    router.replace('/panel')
    return
  }
  await request()
})

async function request() {
  try {
    const data = await auth.requestOtp()
    if (data.channel) channel.value = data.channel
    if (!data.sent) error.value = t('auth.confirmSendFailed')
  } catch (err) {
    error.value = getApiErrorDetails(err).message
  }
}

async function resend() {
  error.value = ''
  notice.value = ''
  resending.value = true
  try {
    await request()
    if (!error.value) notice.value = t('auth.confirmResent')
  } finally {
    resending.value = false
  }
}

async function submit() {
  error.value = ''
  notice.value = ''
  loading.value = true
  try {
    await auth.verifyOtp(code.value.trim())
    router.push('/panel')
  } catch (err) {
    error.value = getApiErrorDetails(err).message
  } finally {
    loading.value = false
  }
}
</script>
