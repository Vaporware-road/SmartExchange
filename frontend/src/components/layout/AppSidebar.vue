<template>
  <aside
    class="app-sidebar hidden lg:flex lg:flex-col lg:w-64 lg:fixed lg:inset-y-0 z-40 transition-all duration-300 ease-in-out bg-[var(--bg-navbar)]"
    style="border-color: var(--border-card); inset-inline-start: 0; border-inline-end: 1px solid var(--border-card);"
  >
    <div class="flex items-center gap-3 px-6 py-5 border-b" style="border-color: var(--border-card);">
      <router-link to="/" class="flex items-center gap-3 group">
        <div
          class="p-2.5 rounded-xl transition-all duration-300 ease-in-out border group-hover:scale-105"
          style="background: rgba(255, 215, 0, 0.15); border-color: var(--border-color);"
        >
          <i class="fas fa-coins text-xl text-[var(--primary)] group-hover:rotate-12" />
        </div>
        <div class="flex flex-col min-w-0">
          <span class="text-lg font-bold leading-tight text-[var(--primary)] truncate">
            {{ siteName }}
          </span>
          <span class="text-xs text-[var(--text-secondary)] font-medium hidden sm:block truncate">
            {{ tagline }}
          </span>
        </div>
      </router-link>
    </div>
    <nav class="flex-1 overflow-y-auto py-4 px-3">
      <ul class="space-y-1">
        <li v-for="link in visibleLinks" :key="link.to">
          <router-link
            :to="link.to"
            class="sidebar-link flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ease-in-out text-[var(--text-secondary)] hover:text-[var(--primary)] hover:bg-[var(--bg-hover)]"
            :class="{
              'text-[var(--primary)] bg-[var(--bg-hover)]': isActive(link),
            }"
          >
            <i :class="link.icon" class="text-base w-5 text-center" />
            <span class="font-medium">{{ $t(link.labelKey) }}</span>
          </router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const siteSettings = useSiteSettingsStore()
const auth = useAuthStore()

const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline)

const allNavLinks = [
  { to: '/', labelKey: 'sidebar.dashboard', icon: 'fas fa-tachometer-alt', exact: true },
  { to: '/prices', labelKey: 'sidebar.prices', icon: 'fas fa-dollar-sign', exact: false },
  { to: '/special-prices', labelKey: 'sidebar.specialPrices', icon: 'fas fa-star', exact: false },
  { to: '/finalize', labelKey: 'sidebar.finalize', icon: 'fas fa-check-circle', exact: false },
  { to: '/categories', labelKey: 'sidebar.categories', icon: 'fas fa-tags', exact: false },
  { to: '/analysis', labelKey: 'sidebar.analysis', icon: 'fas fa-chart-line', exact: false, requireRole: ['management', 'developer'] },
  { to: '/telegram/send', labelKey: 'sidebar.telegram', icon: 'fab fa-telegram', exact: false },
  { to: '/templates', labelKey: 'sidebar.templates', icon: 'fas fa-file-image', exact: false },
  { to: '/settings', labelKey: 'sidebar.settings', icon: 'fas fa-cog', exact: false, requireRole: ['management', 'developer'] },
]

const visibleLinks = computed(() => {
  return allNavLinks.filter(link => {
    if (!link.requireRole) return true
    return link.requireRole.includes(auth.role)
  })
})

function isActive(link) {
  if (link.exact) return route.path === link.to
  return route.path.startsWith(link.to)
}
</script>
