<template>
  <header
    class="sticky top-0 z-30 flex h-16 items-center justify-between border-b border-slate-200 bg-white/95 px-4 backdrop-blur-sm transition-all duration-300 ease-in-out sm:px-6 dark:border-[var(--border-card)] dark:bg-[var(--bg-navbar)]"
  >
    <button
      class="md:hidden inline-flex items-center justify-center w-10 h-10 rounded-xl transition-all duration-300 ease-in-out text-[var(--primary)] hover:bg-[var(--bg-hover)]"
      :aria-label="$t('header.openMenu')"
      @click="$emit('toggle-drawer')"
    >
      <i class="fas fa-bars text-xl" />
    </button>
    <router-link to="/panel" class="hidden md:flex items-center gap-2 min-w-0">
      <AppBrandLogo size="sm" rounded="lg" />
      <span class="text-sm font-semibold text-[var(--primary)] truncate max-w-[180px]">{{ siteName }}</span>
    </router-link>
    <div class="flex items-center gap-3">
      <LanguageSwitcher />
      <ThemeToggle />
      <template v-if="auth.isAuthenticated">
        <div
          class="flex shrink-0 items-center gap-3 rounded-xl border border-slate-200 bg-white px-3 py-2 sm:px-4 dark:border-[var(--border-color)] dark:bg-[var(--bg-card)]"
        >
          <div
            class="w-9 h-9 rounded-full border-2 flex items-center justify-center shrink-0 bg-primary-muted border-[var(--primary)]"
          >
            <i class="fas fa-user text-sm text-[var(--primary)]" />
          </div>
          <div class="min-w-0 hidden sm:block">
            <div class="text-sm font-bold text-[var(--text-primary)] truncate">
              {{ auth.user?.full_name || auth.username }}
            </div>
            <div v-if="auth.role" class="text-xs text-[var(--primary)] font-medium hidden md:block truncate">
              {{ auth.role }}
            </div>
          </div>
        </div>
        <BaseButton
          variant="outline"
          size="sm"
          class="!border-red-500/50 !text-red-400 hover:!bg-red-500/10"
          @click="handleLogout"
        >
          <i class="fas fa-sign-out-alt" />
          <span class="hidden xl:inline">{{ $t('common.logout') }}</span>
        </BaseButton>
      </template>
      <template v-else>
        <router-link to="/login">
          <BaseButton variant="outline" size="sm">
            <i class="fas fa-sign-in-alt" />
            <span class="hidden sm:inline">{{ $t('common.login') }}</span>
          </BaseButton>
        </router-link>
      </template>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { computed } from 'vue'
import BaseButton from '@/components/ui/BaseButton.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

defineEmits(['toggle-drawer'])

const router = useRouter()
const auth = useAuthStore()
const siteSettings = useSiteSettingsStore()
const siteName = computed(() => siteSettings.siteName)

function handleLogout() {
  auth.logout()
  router.push('/login')
}
</script>
