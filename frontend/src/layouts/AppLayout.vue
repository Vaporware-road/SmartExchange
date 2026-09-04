<template>
  <div class="min-h-screen flex bg-slate-50 dark:bg-[var(--bg-base)] transition-colors duration-500 max-w-[100vw] overflow-x-hidden">
    <AppSidebar />
    <AppDrawer :open="drawerOpen" @close="drawerOpen = false" />
    <div
      class="flex min-h-0 flex-1 flex-col min-w-0 overflow-x-hidden transition-[padding] duration-300 ease-in-out pb-16 md:pb-0 w-full"
      :class="['md:ps-16', sidebarStore.isCollapsed ? 'lg:ps-16' : 'lg:ps-64']"
    >
      <AppHeader @toggle-drawer="drawerOpen = !drawerOpen" />
      <main
        class="flex min-w-0 flex-1 flex-col overflow-x-hidden"
        :class="
          isTemplateEditorLayout
            ? 'min-h-0 overflow-hidden py-0 px-0'
            : 'min-h-0 overflow-x-hidden py-4 px-3 sm:px-4 lg:px-5'
        "
      >
        <div
          class="flex w-full min-w-0 flex-col"
          :class="
            isTemplateEditorLayout
              ? 'mx-0 max-w-none flex-1 min-h-0'
              : 'mx-auto max-w-7xl flex-1 min-h-0'
          "
        >
          <AppBreadcrumb v-if="!isTemplateEditorLayout" />
          <router-view v-slot="{ Component }">
            <Transition name="page" mode="out-in">
              <component :is="Component" class="min-h-0 flex-1" />
            </Transition>
          </router-view>
        </div>
      </main>
      <AppFooter v-if="!isTemplateEditorLayout" />
    </div>
    <AppBottomNav />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { AppSidebar, AppHeader, AppDrawer, AppFooter, AppBreadcrumb, AppBottomNav } from '@/components/layout'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useSidebarStore } from '@/stores/sidebar'
import { useAuthStore } from '@/stores/auth'
import { useOrdersQueueStore } from '@/stores/ordersQueue'

const route = useRoute()
const drawerOpen = ref(false)
const siteSettings = useSiteSettingsStore()
const sidebarStore = useSidebarStore()
const auth = useAuthStore()
const ordersQueue = useOrdersQueueStore()

const isTemplateEditorLayout = computed(() => Boolean(route.meta.templateEditorLayout))

function syncOrdersPolling() {
  if (auth.isAuthenticated && auth.can('orders')) {
    ordersQueue.startPolling()
  } else {
    ordersQueue.stopPolling()
  }
}

watch(() => auth.isAuthenticated, syncOrdersPolling)

onMounted(() => {
  siteSettings.fetch()
  syncOrdersPolling()
})

onUnmounted(() => {
  ordersQueue.stopPolling()
})
</script>
