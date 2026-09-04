<template>
  <aside
    :class="[
      'app-sidebar hidden md:flex md:flex-col md:fixed md:inset-y-0 z-40 transition-all duration-300 ease-in-out bg-[var(--bg-navbar)]',
      'md:w-16',
      isCollapsed ? 'lg:w-16' : 'lg:w-64',
    ]"
    style="border-color: var(--border-card); inset-inline-start: 0; border-inline-end: 1px solid var(--border-card);"
  >
    <div
      class="flex items-center gap-3 px-2 py-5 border-b shrink-0 transition-all duration-300 ease-in-out md:justify-center"
      :class="isCollapsed ? 'lg:justify-center lg:px-2' : 'lg:px-6'"
      style="border-color: var(--border-card);"
    >
      <router-link to="/" class="flex items-center gap-3 group min-w-0 md:justify-center">
        <AppBrandLogo size="md" rounded="xl" class="group-hover:scale-105 transition-all duration-300 ease-in-out shrink-0" />
        <!-- Text hidden on mobile/tablet and when collapsed; only icons visible in collapsed mode -->
        <div
          class="flex flex-col min-w-0 overflow-hidden transition-all duration-300 ease-in-out hidden md:hidden"
          :class="!isCollapsed ? 'lg:flex' : ''"
        >
          <span class="text-lg font-bold leading-tight text-[var(--primary)] truncate whitespace-nowrap">
            {{ siteName }}
          </span>
          <span class="text-xs text-[var(--text-secondary)] font-medium hidden sm:block truncate whitespace-nowrap">
            {{ tagline }}
          </span>
        </div>
      </router-link>
    </div>
    <nav
      class="flex-1 overflow-y-auto overflow-x-hidden py-4 px-2 transition-all duration-300 ease-in-out"
      :class="!isCollapsed ? 'lg:px-4' : 'lg:px-2'"
    >
      <ul class="space-y-1">
        <li v-for="link in visibleLinks" :key="link.to">
          <router-link
            :to="link.to"
            class="sidebar-link flex items-center gap-3 px-3 py-3 rounded-xl transition-all duration-300 ease-in-out text-[var(--text-secondary)] hover:bg-[var(--bg-hover)] md:justify-center md:px-2 md:min-w-0"
            :class="[
              isActive(link)
                ? ['bg-[var(--bg-hover)]', link.activeColor === 'gold' ? 'text-gold' : link.activeColor === 'buy' ? 'text-buy' : link.activeColor === 'info' ? 'text-info' : 'text-template']
                : 'hover:text-[var(--primary)]',
              !isCollapsed ? 'lg:px-4' : 'lg:justify-center lg:px-2',
            ]"
          >
            <span class="relative shrink-0 flex items-center justify-center w-5">
              <i :class="link.icon" class="text-base w-5 text-center" />
              <OrderQueueBadge
                v-if="link.to === '/orders'"
                :class="!isCollapsed ? 'lg:hidden' : ''"
              />
            </span>
            <!-- Label hidden on tablet and when collapsed; only icon visible -->
            <span
              class="font-medium whitespace-nowrap overflow-hidden hidden md:hidden flex items-center gap-2"
              :class="!isCollapsed ? 'lg:inline-flex' : ''"
            >
              {{ $t(link.labelKey) }}
              <OrderQueueBadge v-if="link.to === '/orders'" inline />
            </span>
          </router-link>
        </li>
      </ul>
    </nav>
    <div class="p-2 border-t shrink-0 hidden lg:block transition-all duration-300 ease-in-out" style="border-color: var(--border-card);">
      <button
        type="button"
        class="w-full flex items-center justify-center py-2.5 rounded-xl transition-all duration-300 ease-in-out border border-[var(--border-color)] bg-[var(--bg-navbar)] hover:bg-[var(--bg-hover)] hover:border-[var(--border-card-hover)] text-[var(--text-secondary)] hover:text-[var(--primary)]"
        :aria-label="$t('a11y.toggleSidebar')"
        @click="toggleSidebar"
      >
        <i
          :class="['fas', 'text-sm', sidebarToggleIcon]"
        />
      </button>
    </div>
  </aside>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useAuthStore } from '@/stores/auth'
import { useSidebarStore } from '@/stores/sidebar'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'
import OrderQueueBadge from '@/components/layout/OrderQueueBadge.vue'
import { useAppDirection } from '@/composables/useAppDirection.js'

const route = useRoute()
const { isRtl } = useAppDirection()
const siteSettings = useSiteSettingsStore()
const auth = useAuthStore()
const sidebarStore = useSidebarStore()

const isCollapsed = ref(false)
watch(isCollapsed, (v) => { sidebarStore.isCollapsed = v }, { immediate: true })
function toggleSidebar() {
  isCollapsed.value = !isCollapsed.value
}

const sidebarToggleIcon = computed(() => {
  if (isRtl.value) {
    return isCollapsed.value ? 'fa-chevron-left' : 'fa-chevron-right'
  }
  return isCollapsed.value ? 'fa-chevron-right' : 'fa-chevron-left'
})

const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline)

/** لینک‌های سایدبار — دسترسی بر اساس config/permissions.js */
const allNavLinks = [
  { to: '/', labelKey: 'sidebar.dashboard', icon: 'fas fa-tachometer-alt', exact: true, activeColor: 'gold' },
  { to: '/update', labelKey: 'sidebar.priceHub', icon: 'fas fa-dollar-sign', exact: false, activeColor: 'buy' },
  { to: '/finalize', labelKey: 'sidebar.finalize', icon: 'fas fa-check-circle', exact: false, permission: 'finalize', activeColor: 'buy' },
  { to: '/categories', labelKey: 'sidebar.categories', icon: 'fas fa-tags', exact: false, activeColor: 'gold' },
  { to: '/analysis', labelKey: 'sidebar.analysis', icon: 'fas fa-chart-line', exact: false, permission: 'analysis', activeColor: 'info' },
  { to: '/orders', labelKey: 'sidebar.orders', icon: 'fas fa-shopping-cart', exact: false, permission: 'orders', activeColor: 'buy' },
  { to: '/telegram/send', labelKey: 'sidebar.telegram', icon: 'fab fa-telegram', exact: false, activeColor: 'info' },
  { to: '/instagram', labelKey: 'sidebar.instagramHub', icon: 'fab fa-instagram', exact: false, activeColor: 'gold' },
  { to: '/templates', labelKey: 'sidebar.templates', icon: 'fas fa-file-image', exact: false, activeColor: 'template' },
  { to: '/users', labelKey: 'sidebar.adminManagement', icon: 'fas fa-user-shield', exact: false, permission: 'adminManagement', activeColor: 'gold' },
  { to: '/settings', labelKey: 'sidebar.settings', icon: 'fas fa-cog', exact: false, permission: 'settings', activeColor: 'gold' },
]

const visibleLinks = computed(() => {
  return allNavLinks.filter(link => {
    if (!link.permission) return true
    return auth.can(link.permission)
  })
})

function isActive(link) {
  if (link.exact) return route.path === link.to
  if (link.to === '/update') {
    return route.path === '/update' ||
      (route.path.startsWith('/prices/category/') && route.path.endsWith('/update')) ||
      (route.path.startsWith('/prices/special/') && route.path.endsWith('/update'))
  }
  return route.path.startsWith(link.to)
}
</script>
