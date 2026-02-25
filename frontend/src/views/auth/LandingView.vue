<template>
  <div class="min-h-screen relative" style="background: var(--bg-base);">
    <div class="absolute top-4 right-4">
        <ThemeToggle />
      </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <div class="text-center">
        <div class="p-6 rounded-2xl mx-auto w-fit mb-8" style="background: rgba(255, 215, 0, 0.15); border: 1px solid rgba(255, 215, 0, 0.3);">
          <i class="fas fa-coins text-6xl text-gold"></i>
        </div>
        <h1 class="text-4xl sm:text-5xl font-bold text-gold mb-4">{{ siteName }}</h1>
        <p class="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">{{ tagline }}</p>
        <router-link to="/login" class="btn-luxury inline-flex">
          <i class="fas fa-sign-in-alt"></i>
          <span>Access Panel</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'

const siteSettings = useSiteSettingsStore()
const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline)

onMounted(() => siteSettings.fetch())
</script>
