<template>
  <div class="w-full min-w-0 overflow-x-hidden pb-20 md:pb-28 px-4 md:px-0">
    <h1 class="text-xl sm:text-2xl font-bold text-gold mb-4 sm:mb-6">{{ $t('sidebar.instagramHub') }}</h1>

    <div class="card-luxury p-4 sm:p-6 w-full max-w-xl" style="background: var(--glass-bg); backdrop-filter: blur(16px); border-color: var(--glass-border);">
      <p class="text-[var(--text-secondary)] mb-6">{{ $t('instagramHub.statusDescription') }}</p>

      <div class="space-y-4">
        <div
          class="flex items-center gap-3 p-4 rounded-xl border"
          :class="config.ready_for_publish ? 'border-emerald-500/30 bg-emerald-500/10' : config.has_token ? 'border-amber-500/30 bg-amber-500/10' : 'border-amber-500/30 bg-amber-500/10'"
          style="border-color: var(--border-card);"
        >
          <i v-if="config.ready_for_publish" class="fas fa-check-circle text-2xl text-emerald-400" />
          <i v-else class="fas fa-exclamation-circle text-2xl text-amber-400" />
          <div>
            <p class="font-medium text-[var(--text-primary)]">
              {{ statusLabel }}
            </p>
            <p v-if="config.has_token && config.token_expires_at" class="text-sm text-[var(--text-secondary)] mt-1">
              {{ $t('settings.instagram.tokenExpires') }}: {{ config.token_expires_at }}
            </p>
            <p v-else-if="!config.has_token" class="text-sm text-[var(--text-secondary)] mt-1">
              {{ $t('instagramHub.configureInSettings') }}
            </p>
          </div>
        </div>

        <div v-if="config.token_expired" class="p-3 rounded-xl border border-red-500/30 bg-red-500/10 text-sm">
          {{ $t('settings.instagram.tokenExpired') }}
        </div>
        <div v-else-if="config.token_expiring_soon" class="p-3 rounded-xl border border-amber-500/30 bg-amber-500/10 text-sm">
          {{ $t('settings.instagram.tokenExpiringSoon', { days: config.days_until_token_expiry }) }}
        </div>
        <div v-if="config.has_token && !config.public_base_url_configured" class="p-3 rounded-xl border border-amber-500/30 bg-amber-500/10 text-sm">
          {{ $t('settings.instagram.missingPublicBaseUrl') }}
        </div>

        <a
          v-if="connectUrl"
          :href="connectUrl"
          class="btn-luxury w-full sm:w-auto inline-flex items-center justify-center gap-2 min-h-[48px]"
        >
          <i class="fab fa-instagram" />
          {{ config.has_token ? $t('instagramHub.reconnect') : $t('settings.instagram.connectButton') }}
        </a>
        <p v-else class="text-sm text-[var(--text-secondary)]">
          {{ $t('instagramHub.setAppIdFirst') }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { instagramHubApi } from '@/services/api'
import { instagramConnectHref } from '@/utils/instagramConnect'

const { t } = useI18n()
const route = useRoute()
const router = useRouter()
const toast = useToast()

const config = ref({
  has_app_id: false,
  has_token: false,
  token_expires_at: null,
  token_expired: false,
  token_expiring_soon: false,
  days_until_token_expiry: null,
  public_base_url_configured: false,
  ready_for_publish: false,
})
const connectUrl = ref('')

const statusLabel = computed(() => {
  if (config.value.ready_for_publish) return t('instagramHub.readyForPublish')
  if (config.value.has_token) return t('instagramHub.partiallyConfigured')
  return t('instagramHub.disconnected')
})

async function loadConfig() {
  try {
    const { data } = await instagramHubApi.getConfig()
    config.value = {
      has_app_id: data?.has_app_id ?? false,
      has_token: data?.has_token ?? false,
      token_expires_at: data?.token_expires_at ?? null,
      token_expired: data?.token_expired ?? false,
      token_expiring_soon: data?.token_expiring_soon ?? false,
      days_until_token_expiry: data?.days_until_token_expiry ?? null,
      public_base_url_configured: data?.public_base_url_configured ?? false,
      ready_for_publish: data?.ready_for_publish ?? false,
    }
    connectUrl.value = instagramConnectHref(Boolean(data?.has_app_id), 'instagram')
  } catch {
    connectUrl.value = ''
  }
}

function handleOAuthCallback() {
  const instagramCallback = route.query.instagram_callback
  const msg = route.query.msg || route.query.error
  if (instagramCallback === 'success') {
    toast.success(t('settings.instagram.connectSuccess'))
  } else if (instagramCallback === 'error') {
    toast.error(msg || t('settings.instagram.connectError'))
  }
  if (instagramCallback) {
    router.replace({ name: 'instagram', query: {} })
  }
}

onMounted(() => {
  handleOAuthCallback()
  loadConfig()
})
</script>
