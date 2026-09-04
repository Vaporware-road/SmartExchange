<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12 relative" style="background: var(--bg-base);">
    <div class="absolute top-4 right-4 flex items-center gap-2">
      <LanguageSwitcher />
      <ThemeToggle />
    </div>
    <div class="w-full max-w-md">
      <div class="card-luxury text-center mb-6">
        <div class="mx-auto w-fit mb-4">
          <AppBrandLogo size="xl" rounded="xl" />
        </div>
        <h1 class="text-2xl font-bold text-gold mb-1">{{ siteName }}</h1>
        <p class="text-gray-400 text-sm">{{ $t('auth.signupTitle', { days: trialDays }) }}</p>
      </div>

      <div class="card-luxury">
        <form class="space-y-4" @submit.prevent="handleSubmit">
          <AlertMessage v-if="error" type="error" :show="true" @dismiss="error = ''">
            {{ error }}
          </AlertMessage>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.email') }}</label>
            <input
              v-model="form.email"
              type="email"
              autocomplete="email"
              class="input-luxury"
              :placeholder="$t('auth.emailPlaceholder')"
              required
              autofocus
            >
            <p v-if="fieldError('email')" class="text-xs mt-2 text-red-400">{{ fieldError('email') }}</p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.firstName') }}</label>
              <input v-model="form.first_name" type="text" autocomplete="given-name" class="input-luxury" required>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.lastName') }}</label>
              <input v-model="form.last_name" type="text" autocomplete="family-name" class="input-luxury">
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.exchangeName') }}</label>
            <input
              v-model="form.exchange_name"
              type="text"
              class="input-luxury"
              :placeholder="$t('auth.exchangeNamePlaceholder')"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.password') }}</label>
            <input
              v-model="form.password"
              type="password"
              autocomplete="new-password"
              class="input-luxury"
              minlength="8"
              required
            >
            <p v-if="fieldError('password')" class="text-xs mt-2 text-red-400">{{ fieldError('password') }}</p>
            <p v-else class="text-xs mt-2 text-[var(--text-secondary)]">{{ $t('auth.passwordHint') }}</p>
          </div>

          <button type="submit" class="btn-luxury w-full" :disabled="loading">
            <LoadingSpinner v-if="loading" class="w-5 h-5" />
            <i v-else class="fas fa-rocket" />
            <span>{{ loading ? $t('auth.signingUp') : $t('auth.signupButton', { days: trialDays }) }}</span>
          </button>

          <p class="text-xs text-center text-[var(--text-secondary)]">{{ $t('auth.signupNoCard') }}</p>
        </form>
      </div>

      <div class="text-center mt-6 space-y-2">
        <p class="text-sm text-[var(--text-secondary)]">
          {{ $t('auth.haveAccount') }}
          <router-link to="/login" class="text-gold hover:underline">{{ $t('auth.loginButton') }}</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { getApiErrorDetails } from '@/services/api'
import { TRIAL_DAYS } from '@/config/landing'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'
import AlertMessage from '@/components/ui/AlertMessage.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const siteSettings = useSiteSettingsStore()

const trialDays = TRIAL_DAYS
const siteName = computed(() => siteSettings.siteName)

const form = reactive({
  email: String(route.query.email || ''),
  password: '',
  first_name: '',
  last_name: '',
  exchange_name: '',
})
const error = ref('')
const fieldErrors = ref({})
const loading = ref(false)

onMounted(() => {
  siteSettings.fetch()
})

function fieldError(name) {
  const value = fieldErrors.value?.[name]
  return Array.isArray(value) ? value[0] : value || ''
}

async function handleSubmit() {
  error.value = ''
  fieldErrors.value = {}
  loading.value = true
  try {
    await auth.signup({ ...form })
    router.push('/panel')
  } catch (err) {
    const details = getApiErrorDetails(err)
    error.value = details.message
    fieldErrors.value = details.fieldErrors || {}
  } finally {
    loading.value = false
  }
}
</script>
