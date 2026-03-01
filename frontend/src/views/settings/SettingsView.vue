<template>
  <div class="w-full min-w-0 overflow-x-hidden pb-20 md:pb-28 px-4 md:px-0">
    <h1 class="text-xl sm:text-2xl font-bold text-gold mb-4 sm:mb-6">{{ $t('settings.title') }}</h1>

    <!-- Mobile (< 768px): horizontal scrollable tabs, hidden scrollbar -->
    <div class="settings-tabs-mobile md:hidden w-full min-w-0 mb-4 border-b border-[var(--glass-border)]">
      <div class="overflow-x-auto overflow-y-hidden flex flex-nowrap gap-2 pb-4 -mx-4 px-4" style="-webkit-overflow-scrolling: touch;">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          type="button"
          class="settings-tab flex-shrink-0 flex items-center gap-2 px-3 sm:px-4 py-3 rounded-xl font-medium transition-colors duration-200 whitespace-nowrap min-h-[48px]"
          :class="activeTab === tab.id ? 'bg-[var(--bg-hover)] text-gold border border-gold/40' : 'text-[var(--text-secondary)] border border-transparent hover:bg-[var(--bg-hover)] hover:text-[var(--primary)]'"
          @click="setTab(tab.id)"
        >
          <i :class="tab.icon" class="text-base shrink-0" />
          <span class="truncate max-w-[120px] sm:max-w-none">{{ $t(tab.labelKey) }}</span>
        </button>
      </div>
    </div>

    <div class="flex flex-col md:flex-row gap-4 sm:gap-6 w-full min-w-0">
      <!-- Desktop (≥768px): vertical tab menu -->
      <nav class="hidden md:flex md:flex-col md:w-56 md:min-w-[200px] shrink-0">
        <div class="card-luxury p-2 space-y-1" style="background: var(--glass-bg); backdrop-filter: blur(16px); border-color: var(--glass-border);">
          <button
            v-for="tab in tabs"
            :key="tab.id"
            type="button"
            class="settings-tab w-full flex items-center gap-3 px-4 py-3 rounded-xl font-medium transition-colors duration-200 text-start min-h-[48px]"
            :class="activeTab === tab.id ? 'bg-[var(--bg-hover)] text-gold border border-gold/30' : 'text-[var(--text-secondary)] border border-transparent hover:bg-[var(--bg-hover)] hover:text-[var(--primary)]'"
            @click="setTab(tab.id)"
          >
            <i :class="tab.icon" class="text-base w-5 text-center shrink-0" />
            <span class="truncate">{{ $t(tab.labelKey) }}</span>
          </button>
        </div>
      </nav>

      <!-- Content area with transition -->
      <div class="flex-1 min-w-0 w-full overflow-hidden">
        <div class="card-luxury overflow-hidden w-full min-w-0" style="background: var(--glass-bg); backdrop-filter: blur(16px); border-color: var(--glass-border);">
          <Transition name="fade-slide" mode="out-in">
            <!-- General -->
            <div v-if="activeTab === 'general'" key="general" class="p-4 sm:p-6 w-full min-w-0">
              <h2 class="text-lg font-semibold text-gold mb-4 sm:mb-6">{{ $t('settings.tabs.general') }}</h2>
              <form class="space-y-4 md:space-y-6 w-full max-w-xl min-w-0" @submit.prevent="saveGeneral">
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.general.platformName') }}</label>
                  <input
                    v-model="generalForm.platformName"
                    type="text"
                    class="input-luxury w-full min-w-0 min-h-[48px]"
                    :placeholder="$t('settings.general.platformName')"
                  />
                </div>
                <!-- Vertical stack on mobile, row on desktop; touch target 48px for switch -->
                <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between sm:gap-4">
                  <label class="text-sm font-medium text-[var(--text-secondary)]">{{ $t('settings.general.maintenanceMode') }}</label>
                  <button
                    type="button"
                    role="switch"
                    :aria-checked="generalForm.maintenanceMode"
                    class="relative inline-flex items-center justify-center min-h-[48px] min-w-[48px] sm:min-w-0 h-8 w-14 sm:h-7 sm:w-12 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold focus:ring-offset-2 focus:ring-offset-[var(--bg-base)]"
                    :class="generalForm.maintenanceMode ? 'bg-gold' : 'bg-[var(--border-card)]'"
                    @click="generalForm.maintenanceMode = !generalForm.maintenanceMode"
                  >
                    <span
                      class="pointer-events-none inline-block h-6 w-6 sm:h-5 sm:w-5 transform rounded-full bg-white shadow ring-0 transition duration-200"
                      :class="generalForm.maintenanceMode ? 'translate-x-6 sm:translate-x-5' : 'translate-x-1'"
                    />
                  </button>
                </div>
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.general.defaultBaseCurrency') }}</label>
                  <select v-model="generalForm.defaultBaseCurrency" class="input-luxury w-full min-w-0 min-h-[48px]">
                    <option value="USDT">USDT</option>
                    <option value="IRR">IRR</option>
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                  </select>
                </div>
                <!-- Desktop: inline submit -->
                <button type="submit" class="btn-luxury min-h-[48px] hidden md:inline-flex">
                  <i class="fas fa-save" />
                  {{ $t('settings.general.saveChanges') }}
                </button>
              </form>
            </div>

            <!-- Uploads -->
            <div v-else-if="activeTab === 'uploads'" key="uploads" class="p-4 sm:p-6 w-full min-w-0">
              <h2 class="text-lg font-semibold text-gold mb-4 sm:mb-6">{{ $t('settings.tabs.uploads') }}</h2>
              <div class="space-y-4 md:space-y-6 w-full max-w-xl min-w-0">
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.uploads.maxFileSize') }}</label>
                  <select v-model="uploadsForm.maxFileSizeMb" class="input-luxury w-full min-w-0 min-h-[48px]">
                    <option :value="1">1 MB</option>
                    <option :value="5">5 MB</option>
                    <option :value="10">10 MB</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-3">{{ $t('settings.uploads.allowedFormats') }}</label>
                  <div class="flex flex-wrap gap-3 sm:gap-4">
                    <label class="flex items-center gap-2 cursor-pointer min-h-[48px] md:min-h-0">
                      <input v-model="uploadsForm.allowedFormats" type="checkbox" value="PNG" class="rounded border-gold/50 text-gold focus:ring-gold w-5 h-5 md:w-4 md:h-4 shrink-0" />
                      <span class="text-[var(--text-primary)]">{{ $t('settings.uploads.formatPng') }}</span>
                    </label>
                    <label class="flex items-center gap-2 cursor-pointer min-h-[48px] md:min-h-0">
                      <input v-model="uploadsForm.allowedFormats" type="checkbox" value="JPG" class="rounded border-gold/50 text-gold focus:ring-gold w-5 h-5 md:w-4 md:h-4 shrink-0" />
                      <span class="text-[var(--text-primary)]">{{ $t('settings.uploads.formatJpg') }}</span>
                    </label>
                    <label class="flex items-center gap-2 cursor-pointer min-h-[48px] md:min-h-0">
                      <input v-model="uploadsForm.allowedFormats" type="checkbox" value="SVG" class="rounded border-gold/50 text-gold focus:ring-gold w-5 h-5 md:w-4 md:h-4 shrink-0" />
                      <span class="text-[var(--text-primary)]">{{ $t('settings.uploads.formatSvg') }}</span>
                    </label>
                  </div>
                </div>
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.uploads.storageUsage') }}</label>
                  <p class="text-xs md:text-sm text-[var(--text-secondary)] mb-2">
                    {{ $t('settings.uploads.storageUsed', { percent: storageUsedPercent, total: storageTotalGb }) }}
                  </p>
                  <div class="h-2 md:h-3 w-full rounded-full bg-[var(--bg-hover)] overflow-hidden border border-[var(--glass-border)]">
                    <div
                      class="h-full rounded-full transition-all duration-300"
                      :style="{ background: 'linear-gradient(90deg, var(--primary), var(--primary-hover))', width: storageUsedPercent + '%' }"
                    />
                  </div>
                </div>
                <div class="pt-4 border-t" style="border-color: var(--glass-border);">
                  <button
                    type="button"
                    class="btn-luxury-outline border-red-500/50 text-red-400 hover:bg-red-500/10 hover:border-red-500/70 min-h-[48px]"
                    @click="showClearCacheModal = true"
                  >
                    <i class="fas fa-trash-alt" />
                    {{ $t('settings.uploads.clearTempUploads') }}
                  </button>
                </div>
              </div>
            </div>

            <!-- Instagram -->
            <div v-else-if="activeTab === 'instagram'" key="instagram" class="p-4 sm:p-6 w-full min-w-0">
              <h2 class="text-lg font-semibold text-gold mb-4 sm:mb-6">{{ $t('settings.tabs.instagram') }}</h2>
              <div class="space-y-4 md:space-y-6 w-full max-w-xl min-w-0">
                <p class="text-sm text-[var(--text-secondary)]">{{ $t('settings.instagram.description') }}</p>
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.instagram.appId') }}</label>
                  <input v-model="instagramForm.appId" type="text" class="input-luxury w-full min-w-0 min-h-[48px]" :placeholder="$t('settings.instagram.appIdPlaceholder')" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">{{ $t('settings.instagram.appSecret') }}</label>
                  <input v-model="instagramForm.appSecret" type="password" class="input-luxury w-full min-w-0 min-h-[48px]" :placeholder="$t('settings.instagram.appSecretPlaceholder')" autocomplete="off" />
                </div>
                <div class="flex flex-wrap gap-3">
                  <button type="button" class="btn-luxury min-h-[48px]" @click="saveInstagramConfig">
                    <i class="fas fa-save" />
                    {{ $t('settings.general.saveChanges') }}
                  </button>
                  <a
                    v-if="instagramConnectUrl"
                    :href="instagramConnectUrl"
                    class="btn-luxury-outline min-h-[48px] inline-flex items-center gap-2"
                  >
                    <i class="fab fa-instagram" />
                    {{ $t('settings.instagram.connectButton') }}
                  </a>
                </div>
                <div v-if="instagramConfig.has_token" class="p-3 rounded-xl border border-emerald-500/30 bg-emerald-500/10 text-sm text-[var(--text-primary)]">
                  <i class="fas fa-check-circle text-emerald-400" />
                  {{ $t('settings.instagram.connected') }}
                  <span v-if="instagramConfig.token_expires_at" class="block mt-1 text-[var(--text-secondary)]">{{ $t('settings.instagram.tokenExpires') }}: {{ instagramConfig.token_expires_at }}</span>
                </div>
              </div>
            </div>

            <!-- Logs -->
            <div v-else-if="activeTab === 'logs'" key="logs" class="p-4 sm:p-6 w-full min-w-0 overflow-x-auto overflow-y-hidden">
              <LogsView embedded />
            </div>

            <!-- Install App -->
            <div v-else-if="activeTab === 'install-app'" key="install-app" class="p-4 sm:p-6 w-full min-w-0">
              <h2 class="text-lg font-semibold text-gold mb-4 sm:mb-6">{{ $t('settings.tabs.installApp') }}</h2>
              <div class="space-y-6 w-full max-w-xl min-w-0">
                <p class="text-sm text-[var(--text-secondary)]">
                  {{ $t('settings.installAppContent.description') }}
                </p>
                <!-- Already in standalone (installed) -->
                <div
                  v-if="isStandalone"
                  class="flex items-center gap-3 p-4 rounded-xl border border-emerald-500/30 bg-emerald-500/10"
                >
                  <i class="fas fa-check-circle text-emerald-400 text-xl shrink-0" />
                  <span class="text-sm text-[var(--text-primary)]">{{ $t('settings.installAppContent.alreadyInstalled') }}</span>
                </div>
                <!-- Install button (Android/Chrome when beforeinstallprompt is available) -->
                <div v-else-if="deferredPrompt" class="flex flex-wrap gap-3">
                  <button
                    type="button"
                    class="btn-luxury flex items-center gap-2 min-h-[48px] px-6"
                    :disabled="installing"
                    @click="triggerInstall"
                  >
                    <i class="fas fa-download" />
                    {{ installing ? $t('common.loading') : $t('settings.installAppContent.installButton') }}
                  </button>
                </div>
                <!-- iOS instructions -->
                <div
                  v-if="isIos && !isStandalone"
                  class="rounded-xl border p-4 space-y-2"
                  style="border-color: var(--border-card); background: var(--bg-input);"
                >
                  <p class="text-sm font-medium text-[var(--text-primary)] flex items-center gap-2">
                    <i class="fas fa-apple-alt text-gold" />
                    {{ $t('settings.installAppContent.iosInstructions') }}
                  </p>
                </div>
                <!-- Desktop: show install hint for mobile -->
                <div
                  v-if="!deferredPrompt && !isIos && !isStandalone"
                  class="text-sm text-[var(--text-secondary)] rounded-xl border p-4"
                  style="border-color: var(--border-card);"
                >
                  {{ $t('settings.installAppContent.title') }} — {{ $t('settings.installAppContent.description') }}
                  <p class="mt-2 text-xs opacity-90">{{ $t('pwa.installDesc') }}</p>
                </div>
              </div>
            </div>
          </Transition>
        </div>
      </div>
    </div>

    <!-- Mobile: Sticky Save bar (General tab only) -->
    <div
      v-show="activeTab === 'general'"
      class="fixed bottom-0 left-0 right-0 z-30 p-4 md:hidden border-t transition-colors duration-300"
      style="background: var(--bg-base); border-color: var(--glass-border); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);"
    >
      <button
        type="button"
        class="btn-luxury w-full min-h-[48px] flex items-center justify-center gap-2"
        @click="saveGeneral"
      >
        <i class="fas fa-save" />
        {{ $t('settings.general.saveChanges') }}
      </button>
    </div>

    <!-- Clear cache confirmation modal -->
    <BaseModal
      v-model="showClearCacheModal"
      :title="$t('common.confirm')"
      aria-label="Confirm clear cache"
    >
      <p class="text-[var(--text-secondary)] mb-6">{{ $t('settings.uploads.clearCacheConfirm') }}</p>
      <div class="flex gap-3 justify-end">
        <button type="button" class="btn-luxury-outline" @click="showClearCacheModal = false">
          {{ $t('common.cancel') }}
        </button>
        <button
          type="button"
          class="btn-luxury-outline border-red-500/50 text-red-400 hover:bg-red-500/10"
          @click="clearCache"
        >
          {{ $t('common.confirm') }}
        </button>
      </div>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useI18n } from 'vue-i18n'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { settingsApi, instagramHubApi } from '@/services/api'
import LogsView from './LogsView.vue'
import BaseModal from '@/components/ui/BaseModal.vue'

const route = useRoute()
const toast = useToast()
const { t } = useI18n()
const siteSettings = useSiteSettingsStore()

const tabs = [
  { id: 'general', labelKey: 'settings.tabs.general', icon: 'fas fa-sliders-h' },
  { id: 'uploads', labelKey: 'settings.tabs.uploads', icon: 'fas fa-cloud-upload-alt' },
  { id: 'instagram', labelKey: 'settings.tabs.instagram', icon: 'fab fa-instagram' },
  { id: 'logs', labelKey: 'settings.tabs.logs', icon: 'fas fa-list' },
  { id: 'install-app', labelKey: 'settings.tabs.installApp', icon: 'fas fa-mobile-alt' },
]

const activeTab = ref('general')
const showClearCacheModal = ref(false)
let deferredInstallPrompt = null
const installing = ref(false)

const isStandalone = computed(() => {
  if (typeof window === 'undefined') return false
  return window.matchMedia('(display-mode: standalone)').matches ||
    window.navigator.standalone === true ||
    document.referrer.includes('android-app://')
})

const isIos = computed(() => {
  if (typeof navigator === 'undefined') return false
  return /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)
})

const deferredPrompt = ref(null)

// General form: platform name from store, rest local
const generalForm = reactive({
  platformName: '',
  maintenanceMode: false,
  defaultBaseCurrency: 'USDT',
})

// Uploads: all local / mock
const uploadsForm = reactive({
  maxFileSizeMb: 5,
  allowedFormats: ['PNG', 'JPG'],
})
const storageUsedPercent = 45
const storageTotalGb = '10 GB'

const instagramForm = reactive({ appId: '', appSecret: '' })
const instagramConfig = ref({ has_app_id: false, has_token: false, token_expires_at: null })
const instagramConnectUrl = ref('')

function setTab(id) {
  activeTab.value = id
  const hash = '#' + id
  if (typeof window !== 'undefined' && window.history.replaceState) {
    window.history.replaceState(null, '', route.path + hash)
  }
}

function initFromHash() {
  const hash = window.location.hash?.slice(1)
  if (hash && tabs.some(t => t.id === hash)) {
    activeTab.value = hash
  }
}

async function saveGeneral() {
  try {
    await settingsApi.updateSite({ site_name: generalForm.platformName })
    siteSettings.settings = { ...siteSettings.settings, site_name: generalForm.platformName }
    toast.success(t('toast.saveSuccess'))
  } catch {
    toast.error(t('toast.serverError'))
  }
}

async function saveInstagramConfig() {
  try {
    await instagramHubApi.patchConfig({
      app_id: instagramForm.appId || undefined,
      app_secret: instagramForm.appSecret || undefined,
    })
    toast.success(t('toast.saveSuccess'))
    if (instagramForm.appSecret) instagramForm.appSecret = ''
    loadInstagramConfig()
  } catch {
    toast.error(t('toast.serverError'))
  }
}

async function loadInstagramConfig() {
  try {
    const { data } = await instagramHubApi.getConfig()
    instagramConfig.value = {
      has_app_id: data?.has_app_id ?? false,
      has_token: data?.has_token ?? false,
      token_expires_at: data?.token_expires_at ?? null,
    }
    instagramConnectUrl.value = data?.connect_url ?? ''
    if (data?.has_app_id && !instagramForm.appId) instagramForm.appId = '••••••••'
  } catch {
    instagramConnectUrl.value = ''
  }
}

function clearCache() {
  showClearCacheModal.value = false
  toast.success(t('toast.cacheCleared'))
}

function handleBeforeInstall(e) {
  e.preventDefault()
  deferredInstallPrompt = e
  deferredPrompt.value = e
}

async function triggerInstall() {
  if (!deferredInstallPrompt) return
  installing.value = true
  try {
    deferredInstallPrompt.prompt()
    const { outcome } = await deferredInstallPrompt.userChoice
    deferredInstallPrompt = null
    deferredPrompt.value = null
    if (outcome === 'accepted') {
      toast.success(t('pwa.installTitle'))
    }
  } finally {
    installing.value = false
  }
}

onMounted(() => {
  window.addEventListener('beforeinstallprompt', handleBeforeInstall)
  initFromHash()
  const q = new URLSearchParams(window.location.search)
  const instagramCallback = q.get('instagram_callback')
  if (instagramCallback === 'success') {
    toast.success(t('settings.instagram.connectSuccess'))
    window.history.replaceState(null, '', route.path)
    activeTab.value = 'instagram'
  } else if (instagramCallback === 'error') {
    const msg = q.get('msg') || q.get('error') || t('settings.instagram.connectError')
    toast.error(msg)
    window.history.replaceState(null, '', route.path)
    activeTab.value = 'instagram'
  }
  loadInstagramConfig()
  if (siteSettings.settings?.site_name != null) {
    generalForm.platformName = siteSettings.settings.site_name
  } else {
    siteSettings.fetch().then(() => {
      generalForm.platformName = siteSettings.settings?.site_name ?? ''
    })
  }
})

onUnmounted(() => {
  window.removeEventListener('beforeinstallprompt', handleBeforeInstall)
})

watch(() => route.path, () => initFromHash())
</script>

<style scoped>
/* Hide scrollbar on horizontal tab strip (mobile) */
.settings-tabs-mobile .overflow-x-auto {
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.settings-tabs-mobile .overflow-x-auto::-webkit-scrollbar {
  display: none;
}
</style>
