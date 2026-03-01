<template>
  <div class="min-h-screen flex bg-[var(--bg-base)] transition-colors duration-500 max-w-[100vw] overflow-x-hidden">
    <AppSidebar />
    <AppDrawer :open="drawerOpen" @close="drawerOpen = false" />
    <div
      class="flex-1 flex flex-col min-w-0 overflow-x-hidden transition-[padding] duration-300 ease-in-out pb-16 md:pb-0 w-full"
      :class="['md:ps-16', sidebarStore.isCollapsed ? 'lg:ps-16' : 'lg:ps-64']"
    >
      <AppHeader @toggle-drawer="drawerOpen = !drawerOpen" />
      <main class="flex-1 py-4 px-3 sm:px-4 lg:px-5 min-w-0 overflow-x-hidden">
        <div class="max-w-7xl mx-auto w-full min-w-0">
          <AppBreadcrumb />
          <router-view v-slot="{ Component }">
            <Transition name="page" mode="out-in">
              <component :is="Component" />
            </Transition>
          </router-view>
        </div>
      </main>
      <AppFooter />
    </div>
    <AppBottomNav />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { AppSidebar, AppHeader, AppDrawer, AppFooter, AppBreadcrumb, AppBottomNav } from '@/components/layout'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useSidebarStore } from '@/stores/sidebar'

const drawerOpen = ref(false)
const siteSettings = useSiteSettingsStore()
const sidebarStore = useSidebarStore()

onMounted(() => {
  siteSettings.fetch()
})
</script>
