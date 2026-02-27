<template>
  <div class="min-h-screen flex bg-[var(--bg-base)]">
    <AppSidebar />
    <AppDrawer :open="drawerOpen" @close="drawerOpen = false" />
    <div class="flex-1 flex flex-col lg:ps-64">
      <AppHeader @toggle-drawer="drawerOpen = !drawerOpen" />
      <main class="flex-1 py-4 px-3 sm:px-4 lg:px-5">
        <div class="max-w-7xl mx-auto">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { AppSidebar, AppHeader, AppDrawer, AppFooter, AppBreadcrumb } from '@/components/layout'
import { useSiteSettingsStore } from '@/stores/siteSettings'

const drawerOpen = ref(false)
const siteSettings = useSiteSettingsStore()

onMounted(() => {
  siteSettings.fetch()
})
</script>
