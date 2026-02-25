<template>
  <Teleport to="body">
    <Transition name="drawer">
      <div
        v-show="open"
        class="fixed inset-0 z-50 flex lg:hidden"
        aria-modal="true"
        role="dialog"
      >
        <div
          class="fixed inset-0 bg-black/60 transition-opacity duration-300 ease-in-out"
          aria-hidden="true"
          @click="$emit('close')"
        />
        <Transition name="drawer-panel">
          <aside
            v-show="open"
            class="drawer-aside fixed top-0 bottom-0 w-full max-w-xs flex flex-col bg-[var(--bg-navbar)] shadow-xl"
            style="inset-inline-start: 0; border-inline-end: 1px solid var(--border-card);"
          >
            <div class="flex items-center justify-between px-6 py-5 border-b" style="border-color: var(--border-card);">
              <router-link to="/" class="flex items-center gap-3" @click="$emit('close')">
                <div
                  class="p-2.5 rounded-xl"
                  style="background: rgba(255, 215, 0, 0.15); border: 1px solid var(--border-color);"
                >
                  <i class="fas fa-coins text-xl text-[var(--primary)]" />
                </div>
                <span class="text-lg font-bold text-[var(--primary)]">{{ siteName }}</span>
              </router-link>
              <button
                class="w-10 h-10 rounded-xl flex items-center justify-center text-[var(--text-secondary)] hover:bg-[var(--bg-hover)] hover:text-[var(--primary)] transition-all duration-300"
                :aria-label="$t('header.closeMenu')"
                @click="$emit('close')"
              >
                <i class="fas fa-times text-xl" />
              </button>
            </div>
            <nav class="flex-1 overflow-y-auto py-4 px-3">
              <ul class="space-y-1">
                <li v-for="link in visibleLinks" :key="link.to">
                  <router-link
                    :to="link.to"
                    class="drawer-link flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ease-in-out text-[var(--text-secondary)] hover:text-[var(--primary)] hover:bg-[var(--bg-hover)]"
                    :class="{ 'text-[var(--primary)] bg-[var(--bg-hover)]': isActive(link) }"
                    @click="$emit('close')"
                  >
                    <i :class="link.icon" class="text-base w-5 text-center" />
                    <span class="font-medium">{{ $t(link.labelKey) }}</span>
                  </router-link>
                </li>
              </ul>
            </nav>
          </aside>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useAuthStore } from '@/stores/auth'

defineProps({
  open: Boolean,
})

defineEmits(['close'])

const route = useRoute()
const siteSettings = useSiteSettingsStore()
const auth = useAuthStore()

const siteName = computed(() => siteSettings.siteName)

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

<style scoped>
.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.3s ease;
}
.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
}
.drawer-panel-enter-active,
.drawer-panel-leave-active {
  transition: transform 0.3s ease-in-out;
}
.drawer-panel-enter-from,
.drawer-panel-leave-to {
  transform: translateX(calc(-100% * var(--drawer-dir, 1)));
}

:root[dir="rtl"] .drawer-aside {
  --drawer-dir: -1;
}
:root[dir="ltr"] .drawer-aside {
  --drawer-dir: 1;
}
</style>
