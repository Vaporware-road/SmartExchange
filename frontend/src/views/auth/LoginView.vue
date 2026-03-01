<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12 relative" style="background: var(--bg-base);">
    <div class="absolute top-4 right-4">
        <ThemeToggle />
      </div>
    <div class="w-full max-w-md">
      <div class="card-luxury text-center mb-6">
        <div class="p-4 rounded-xl mx-auto w-fit mb-4 bg-primary-muted">
          <i class="fas fa-coins text-4xl text-gold"></i>
        </div>
        <h1 class="text-2xl font-bold text-gold mb-1">{{ siteName }}</h1>
        <p class="text-gray-400 text-sm">Sign in to the panel</p>
      </div>

      <div class="card-luxury">
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <AlertMessage v-if="error" type="error" :show="true" @dismiss="error = ''">
            {{ error }}
          </AlertMessage>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">Username</label>
            <input
              v-model="username"
              type="text"
              class="input-luxury"
              placeholder="Enter username"
              required
              autofocus
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-400 mb-2">Password</label>
            <input
              v-model="password"
              type="password"
              class="input-luxury"
              placeholder="Enter password"
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
            <span>{{ loading ? 'Signing in...' : 'Sign In' }}</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import AlertMessage from '@/components/ui/AlertMessage.vue'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const siteSettings = useSiteSettingsStore()

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const siteName = computed(() => siteSettings.siteName)

onMounted(() => siteSettings.fetch())

async function handleSubmit() {
  error.value = ''
  loading.value = true
  try {
    await auth.login(username.value, password.value)
    const redirect = route.query.redirect || '/'
    router.push(redirect)
  } catch (err) {
    error.value = err.response?.data?.detail || err.response?.data?.non_field_errors?.[0] || 'Invalid credentials'
  } finally {
    loading.value = false
  }
}
</script>
