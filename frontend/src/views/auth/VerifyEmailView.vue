<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12" style="background: var(--bg-base);">
    <div class="w-full max-w-md card-luxury text-center">
      <div class="mx-auto w-fit mb-4">
        <AppBrandLogo size="xl" rounded="xl" />
      </div>

      <template v-if="state === 'pending'">
        <LoadingSpinner class="mx-auto h-8 w-8" />
        <p class="mt-4 text-sm text-[var(--text-secondary)]">{{ $t('auth.verifying') }}</p>
      </template>

      <template v-else-if="state === 'done'">
        <i class="fas fa-circle-check text-3xl text-green-400" />
        <h1 class="text-xl font-bold text-gold mt-4 mb-2">{{ $t('auth.verifiedTitle') }}</h1>
        <p class="text-sm text-[var(--text-secondary)] mb-6">{{ $t('auth.verifiedText') }}</p>
        <router-link to="/panel" class="btn-luxury inline-flex">{{ $t('auth.goToPanel') }}</router-link>
      </template>

      <template v-else>
        <i class="fas fa-circle-exclamation text-3xl text-red-400" />
        <h1 class="text-xl font-bold text-gold mt-4 mb-2">{{ $t('auth.verifyFailedTitle') }}</h1>
        <p class="text-sm text-[var(--text-secondary)] mb-6">{{ error || $t('auth.verifyFailedText') }}</p>
        <router-link to="/panel" class="btn-luxury inline-flex">{{ $t('auth.goToPanel') }}</router-link>
      </template>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { authApi, getApiErrorDetails } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const auth = useAuthStore()

const state = ref('pending')
const error = ref('')

onMounted(async () => {
  try {
    await authApi.verifyEmail(String(route.params.token || ''))
    state.value = 'done'
    // The signed-in session is holding a stale user object with a null
    // email_verified_at; refetch so the banner disappears without a reload.
    if (auth.isAuthenticated) await auth.fetchUser()
  } catch (err) {
    error.value = getApiErrorDetails(err).message
    state.value = 'failed'
  }
})
</script>
