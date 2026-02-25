<template>
  <header
    class="sticky top-0 z-30 flex items-center justify-between h-16 px-4 sm:px-6 border-b transition-all duration-300 ease-in-out bg-[var(--bg-navbar)] backdrop-blur-sm"
    style="border-color: var(--border-card);"
  >
    <button
      class="lg:hidden inline-flex items-center justify-center w-10 h-10 rounded-xl transition-all duration-300 ease-in-out text-[var(--primary)] hover:bg-[var(--bg-hover)]"
      :aria-label="$t('header.openMenu')"
      @click="$emit('toggle-drawer')"
    >
      <i class="fas fa-bars text-xl" />
    </button>
    <div class="hidden lg:block" />
    <div class="flex items-center gap-3">
      <LanguageSwitcher />
      <ThemeToggle />
      <template v-if="auth.isAuthenticated">
        <div class="hidden sm:flex items-center gap-3 px-4 py-2 rounded-xl border" style="background: var(--bg-card); border-color: var(--border-color);">
          <div
            class="w-9 h-9 rounded-full border-2 flex items-center justify-center"
            style="background: rgba(255, 215, 0, 0.15); border-color: var(--primary);"
          >
            <i class="fas fa-user text-sm text-[var(--primary)]" />
          </div>
          <div class="hidden md:block">
            <div class="text-sm font-bold text-[var(--text-primary)]">
              {{ auth.user?.full_name || auth.username }}
            </div>
            <div v-if="auth.role" class="text-xs text-[var(--primary)] font-medium">
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
import BaseButton from '@/components/ui/BaseButton.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'

defineEmits(['toggle-drawer'])

const router = useRouter()
const auth = useAuthStore()

function handleLogout() {
  auth.logout()
  router.push('/login')
}
</script>
