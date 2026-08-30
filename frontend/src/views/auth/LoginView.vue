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
        <p class="text-gray-400 text-sm">{{ $t('auth.loginTitle') }}</p>
      </div>

      <!--
        Demo autologin: the visitor clicked "Get a demo" on the marketing page and
        never asked for a login form. Show what is happening instead of a form
        they would have to ignore.
      -->
      <div v-if="openingDemo" class="card-luxury text-center">
        <LoadingSpinner class="mx-auto h-8 w-8" />
        <p class="mt-4 font-semibold">{{ $t('demo.opening.title') }}</p>
        <p class="mt-2 text-sm text-[var(--text-secondary)]">{{ $t('demo.opening.text') }}</p>
      </div>

      <div v-else class="card-luxury">
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <AlertMessage v-if="error" type="error" :show="true" @dismiss="error = ''">
            {{ error }}
          </AlertMessage>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.username') }}</label>
            <input
              v-model="username"
              type="text"
              class="input-luxury"
              :placeholder="$t('auth.username')"
              required
              autofocus
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('auth.password') }}</label>
            <input
              v-model="password"
              type="password"
              class="input-luxury"
              :placeholder="$t('auth.password')"
              required
            />
          </div>

          <button
            type="submit"
            class="btn-luxury w-full"
            :disabled="loading"
          >
            <LoadingSpinner v-if="loading" class="w-5 h-5" />
            <i v-else class="fas fa-sign-in-alt"></i>
            <span>{{ loading ? $t('auth.loggingIn') : $t('auth.loginButton') }}</span>
          </button>
        </form>
      </div>

      <div class="text-center mt-6">
        <router-link
          to="/about"
          class="text-xs tracking-widest uppercase text-[var(--text-secondary)] hover:text-[var(--primary)] transition-colors"
        >
          {{ $t('common.aboutPage') }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { getApiErrorDetails } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'
import AlertMessage from '@/components/ui/AlertMessage.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const siteSettings = useSiteSettingsStore()

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const siteName = computed(() => siteSettings.siteName)

const isDemoRequest = computed(() => route.query.demo === '1' || route.query.demo === 'true')
/* Fall back to the form if the demo login fails, so the visitor is never stuck. */
const openingDemo = computed(() => isDemoRequest.value && loading.value && !error.value)

onMounted(() => {
  siteSettings.fetch()
  if (isDemoRequest.value) {
    startDemoLogin()
  }
})

async function startDemoLogin() {
  if (auth.isAuthenticated) {
    router.push(route.query.redirect || '/panel')
    return
  }
  loading.value = true
  try {
    await auth.demoLogin()
    router.push(route.query.redirect || '/panel')
  } catch (err) {
    error.value = getApiErrorDetails(err).message
  } finally {
    loading.value = false
  }
}

async function handleSubmit() {
  error.value = ''
  loading.value = true
  try {
    await auth.login(username.value, password.value)
    const redirect = route.query.redirect
    router.push(redirect || (auth.shouldOpenProgrammerHub ? '/programmer' : '/panel'))
  } catch (err) {
    error.value = getApiErrorDetails(err).message
  } finally {
    loading.value = false
  }
}
</script>
