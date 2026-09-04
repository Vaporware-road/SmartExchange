<template>
  <div
    class="webapp-shell min-h-screen flex flex-col"
    style="background: var(--bg-base); color: var(--text-primary);"
  >
    <header
      class="sticky top-0 z-20 border-b backdrop-blur-md"
      style="border-color: var(--border-card); background: color-mix(in srgb, var(--bg-navbar) 92%, transparent);"
    >
      <div class="max-w-lg mx-auto px-4 py-3 flex items-center justify-between gap-3">
        <div class="flex items-center gap-3 min-w-0">
          <AppBrandLogo size="md" rounded="xl" />
          <div class="min-w-0">
            <p class="font-bold text-gold truncate">{{ siteName }}</p>
            <p class="text-xs text-[var(--text-secondary)] truncate">{{ tagline }}</p>
          </div>
        </div>
        <LanguageSwitcher />
      </div>
    </header>

    <main class="flex-1 max-w-lg mx-auto w-full px-4 py-5">
      <slot />
    </main>

    <footer
      class="py-4 text-center text-xs text-[var(--text-secondary)] border-t"
      style="border-color: var(--border-card);"
    >
      {{ siteName }}
    </footer>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useThemeStore } from '@/stores/theme'
import { setLocale } from '@/i18n'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'

const siteSettings = useSiteSettingsStore()
const themeStore = useThemeStore()

const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline || '')

onMounted(async () => {
  themeStore.init()
  themeStore.set('dark')

  const tgLang = window.Telegram?.WebApp?.initDataUnsafe?.user?.language_code
  if (tgLang === 'fa' || tgLang?.startsWith('fa')) {
    setLocale('fa')
  }

  try {
    await siteSettings.fetch()
  } catch {
    /* branding optional */
  }

  const script = document.createElement('script')
  script.src = 'https://telegram.org/js/telegram-web-app.js'
  script.async = true
  script.onload = () => {
    const app = window.Telegram?.WebApp
    if (app) {
      app.ready()
      app.expand()
    }
  }
  if (!document.querySelector('script[src*="telegram-web-app.js"]')) {
    document.head.appendChild(script)
  }
})
</script>
