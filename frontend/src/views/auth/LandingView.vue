<template>
  <div class="min-h-screen relative" style="background: var(--bg-base);">
    <div class="absolute top-4 right-4">
        <ThemeToggle />
      </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <div class="text-center">
        <div class="mx-auto w-fit mb-8">
          <AppBrandLogo size="xl" rounded="xl" />
        </div>
        <h1 class="text-4xl sm:text-5xl font-bold text-gold mb-4">{{ siteName }}</h1>
        <p class="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">{{ tagline }}</p>
        <div class="flex flex-wrap items-center justify-center gap-4">
          <router-link to="/login" class="btn-luxury inline-flex">
            <i class="fas fa-sign-in-alt"></i>
            <span>Access Panel</span>
          </router-link>
          <button type="button" class="btn-luxury inline-flex" :disabled="demoLoading" @click="startDemo">
            <LoadingSpinner v-if="demoLoading" class="w-5 h-5" />
            <i v-else class="fas fa-play-circle"></i>
            <span>{{ demoLoading ? 'Signing in…' : 'Explore Demo' }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useAuthStore } from '@/stores/auth'
import { getApiErrorDetails } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

const router = useRouter()
const siteSettings = useSiteSettingsStore()
const auth = useAuthStore()
const demoLoading = ref(false)

const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline)

onMounted(() => siteSettings.fetch())

async function startDemo() {
  if (auth.isAuthenticated) {
    router.push('/')
    return
  }
  demoLoading.value = true
  try {
    await auth.demoLogin()
    router.push('/')
  } catch (err) {
    const { message } = getApiErrorDetails(err)
    alert(message)
  } finally {
    demoLoading.value = false
  }
}
</script>
