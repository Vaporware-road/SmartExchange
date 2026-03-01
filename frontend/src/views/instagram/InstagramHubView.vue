<template>
  <div class="w-full min-w-0 overflow-x-hidden pb-20 md:pb-28 px-4 md:px-0">
    <h1 class="text-xl sm:text-2xl font-bold text-gold mb-4 sm:mb-6">{{ $t('sidebar.instagramHub') }}</h1>

    <div class="card-luxury p-4 sm:p-6 w-full max-w-xl" style="background: var(--glass-bg); backdrop-filter: blur(16px); border-color: var(--glass-border);">
      <p class="text-[var(--text-secondary)] mb-6">{{ $t('instagramHub.statusDescription') }}</p>

      <div class="space-y-4">
        <div class="flex items-center gap-3 p-4 rounded-xl border" :class="config.has_token ? 'border-emerald-500/30 bg-emerald-500/10' : 'border-amber-500/30 bg-amber-500/10'" style="border-color: var(--border-card);">
          <i v-if="config.has_token" class="fas fa-check-circle text-2xl text-emerald-400" />
          <i v-else class="fas fa-exclamation-circle text-2xl text-amber-400" />
          <div>
            <p class="font-medium text-[var(--text-primary)]">
              {{ config.has_token ? $t('instagramHub.connected') : $t('instagramHub.disconnected') }}
            </p>
            <p v-if="config.has_token && config.token_expires_at" class="text-sm text-[var(--text-secondary)] mt-1">
              {{ $t('settings.instagram.tokenExpires') }}: {{ config.token_expires_at }}
            </p>
            <p v-else-if="!config.has_token" class="text-sm text-[var(--text-secondary)] mt-1">
              {{ $t('instagramHub.configureInSettings') }}
            </p>
          </div>
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
import { ref, onMounted } from 'vue'
import { instagramHubApi } from '@/services/api'

const config = ref({
  has_token: false,
  token_expires_at: null,
})
const connectUrl = ref('')

async function loadConfig() {
  try {
    const { data } = await instagramHubApi.getConfig()
    config.value = {
      has_token: data?.has_token ?? false,
      token_expires_at: data?.token_expires_at ?? null,
    }
    connectUrl.value = data?.connect_url ?? ''
  } catch {
    connectUrl.value = ''
  }
}

onMounted(() => {
  loadConfig()
})
</script>
