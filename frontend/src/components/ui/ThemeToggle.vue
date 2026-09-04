<template>
  <button
    type="button"
    class="theme-toggle inline-flex items-center justify-center w-10 h-10 rounded-xl transition-all duration-300 ease-in-out bg-[var(--bg-hover)] hover:bg-[var(--border-color)] text-[var(--primary)]"
    :aria-label="$t('a11y.toggleTheme')"
    @click="theme.toggle()"
  >
    <Transition name="icon-fade" mode="out-in">
      <i
        :key="theme.isDark ? 'moon' : 'sun'"
        :class="theme.isDark ? 'fas fa-moon' : 'fas fa-sun'"
        class="text-lg"
      />
    </Transition>
  </button>
</template>

<script setup>
import { useThemeStore } from '@/stores/theme'

const theme = useThemeStore()
</script>

<style scoped>
.icon-fade-enter-active,
.icon-fade-leave-active {
  transition: opacity 0.2s ease;
}
.icon-fade-enter-from,
.icon-fade-leave-to {
  opacity: 0;
}
</style>
