<template>
  <nav
    class="fixed bottom-0 start-0 end-0 z-30 flex items-center justify-around py-2 border-t md:hidden"
    style="background: var(--bg-navbar); border-color: var(--border-card); padding-bottom: max(0.5rem, env(safe-area-inset-bottom));"
  >
    <router-link
      v-for="item in items"
      :key="item.to"
      :to="item.to"
      class="flex flex-col items-center gap-0.5 min-h-[48px] justify-center px-4 py-2 rounded-xl transition-colors min-w-[64px]"
      :class="isActive(item) ? 'text-gold' : 'text-[var(--text-secondary)] hover:text-[var(--primary)]'"
    >
      <i :class="item.icon" class="text-lg" />
      <span class="text-xs font-medium">{{ $t(item.labelKey) }}</span>
    </router-link>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const items = [
  { to: '/', labelKey: 'sidebar.dashboard', icon: 'fas fa-tachometer-alt', exact: true },
  { to: '/update', labelKey: 'sidebar.priceHub', icon: 'fas fa-dollar-sign', exact: false },
  { to: '/finalize', labelKey: 'sidebar.finalize', icon: 'fas fa-check-circle', exact: false },
]

function isActive(item) {
  if (item.exact) return route.path === item.to
  if (item.to === '/update') {
    return route.path === '/update' ||
      (route.path.startsWith('/prices/category/') && route.path.endsWith('/update')) ||
      (route.path.startsWith('/prices/special/') && route.path.endsWith('/update'))
  }
  return route.path.startsWith(item.to)
}
</script>
