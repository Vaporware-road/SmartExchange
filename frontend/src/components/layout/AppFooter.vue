<template>
  <footer
    class="mt-auto py-6 px-4 sm:px-6 text-center text-sm text-[var(--text-secondary)] transition-colors duration-300"
    style="background: var(--bg-footer);"
  >
    <div
      class="h-px mb-6 mx-auto max-w-xs"
      style="background: linear-gradient(90deg, transparent 0%, rgba(255, 215, 0, 0.3) 50%, transparent 100%);"
    />
    <p>{{ $t('footer.copyright', { year: currentYear, name: siteName }) }}</p>
    <a
      v-if="supportPhone"
      :href="`tel:${supportPhone}`"
      class="inline-block mt-2 text-[var(--primary)] hover:underline transition-colors"
    >
      {{ $t('footer.support') }}: {{ supportPhone }}
    </a>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useSiteSettingsStore } from '@/stores/siteSettings'

const siteSettings = useSiteSettingsStore()

const currentYear = new Date().getFullYear()
const siteName = computed(() => siteSettings.siteName)
const supportPhone = computed(() => siteSettings.settings.support_phone)
</script>
