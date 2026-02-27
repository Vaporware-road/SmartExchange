<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6 animate-fade-in-up">
      {{ $t('telegram.hubTitle') }}
    </h1>

    <!-- Tabs -->
    <div class="card-luxury mb-6 px-3 py-2 flex flex-wrap gap-2 items-center">
      <button
        v-for="tab in tabs"
        :key="tab.id"
        type="button"
        class="inline-flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all"
        :class="activeTab === tab.id ? 'btn-luxury' : 'btn-luxury-outline bg-transparent'"
        @click="activeTab = tab.id"
      >
        <i :class="tab.icon" />
        <span>{{ $t(tab.labelKey) }}</span>
      </button>
    </div>

    <!-- Tab content -->
    <Transition name="fade-slide" mode="out-in">
      <div :key="activeTab">
        <!-- Tab 1: Messenger -->
        <div
          v-if="activeTab === 'messenger'"
          class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start animate-fade-in-up"
        >
          <!-- Form -->
          <form @submit.prevent="handleSend" class="card-luxury space-y-4 px-4 py-3">
            <h2 class="text-lg font-semibold text-gold mb-2">
              {{ $t('telegram.tabs.messenger') }}
            </h2>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.channelLabel') }}
              </label>
              <select v-model="channelId" class="input-luxury" required>
                <option value="">{{ $t('telegram.messenger.channelPlaceholder') }}</option>
                <option
                  v-for="ch in channels"
                  :key="ch.id"
                  :value="ch.id"
                >
                  {{ ch.name }}
                </option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.bannerLabel') }}
              </label>
              <select v-model="bannerKey" class="input-luxury">
                <option
                  v-for="opt in bannerOptions"
                  :key="opt.value"
                  :value="opt.value"
                >
                  {{ $t(opt.labelKey) }}
                </option>
              </select>
            </div>

            <div v-if="useDoublePrice" class="grid grid-cols-1 gap-3">
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-2">
                  {{ $t('telegram.messenger.cashPrice') }}
                </label>
                <input
                  v-model.number="cashPrice"
                  type="number"
                  step="0.01"
                  min="0"
                  class="input-luxury"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-2">
                  {{ $t('telegram.messenger.accountPrice') }}
                </label>
                <input
                  v-model.number="accountPrice"
                  type="number"
                  step="0.01"
                  min="0"
                  class="input-luxury"
                />
              </div>
            </div>
            <div v-else>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.price') }}
              </label>
              <input
                v-model.number="singlePrice"
                type="number"
                step="0.01"
                min="0"
                class="input-luxury"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.messageLabel') }}
              </label>
              <textarea
                v-model="message"
                class="input-luxury"
                rows="4"
                :placeholder="$t('telegram.messenger.messagePlaceholder')"
              />
            </div>

            <div class="flex gap-4">
              <button type="submit" class="btn-luxury" :disabled="submitting || !channelId">
                <LoadingSpinner v-if="submitting" class="w-5 h-5" />
                <span v-else>{{ $t('telegram.messenger.send') }}</span>
              </button>
            </div>
          </form>

          <!-- Live preview -->
          <div class="card-luxury px-4 py-3 animate-fade-in-up hover-lift">
            <h2 class="text-lg font-semibold text-gold mb-4">
              {{ $t('telegram.messenger.livePreview') }}
            </h2>
            <div class="bg-[var(--glass-bg)] border border-[var(--glass-border)] rounded-2xl p-4 space-y-3">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-gradient-to-br from-gold/80 to-amber-500/80 flex items-center justify-center text-xs font-bold text-black shadow-soft">
                  {{ selectedChannelInitials }}
                </div>
                <div>
                  <p class="font-semibold text-[var(--text-primary)]">
                    {{ selectedChannel?.name || 'Channel' }}
                  </p>
                  <p class="text-xs text-[var(--text-secondary)]">
                    Telegram • {{ previewTimestamp }}
                  </p>
                </div>
              </div>

              <div class="mt-2 rounded-2xl bg-black/20 border border-white/5 px-4 py-3 space-y-2">
                <p v-if="selectedBannerLabel" class="text-xs font-semibold text-gold uppercase tracking-wide">
                  {{ selectedBannerLabel }}
                </p>
                <p v-if="previewPriceLine" class="text-sm text-[var(--text-primary)]">
                  {{ previewPriceLine }}
                </p>
                <p v-if="message" class="text-sm text-[var(--text-primary)] whitespace-pre-line">
                  {{ message }}
                </p>
              </div>

              <div class="flex justify-end">
                <div class="inline-flex rounded-full bg-white/5 border border-white/10 px-3 py-1.5 text-xs text-[var(--text-secondary)] gap-2">
                  <span class="inline-flex items-center gap-1">
                    <i class="fas fa-eye" />
                    0
                  </span>
                  <span class="inline-flex items-center gap-1">
                    <i class="fas fa-check-double" />
                    0
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 2: Bot Setup -->
        <div
          v-else-if="activeTab === 'bot'"
          class="card-luxury px-4 py-3 space-y-4 animate-fade-in-up"
        >
          <h2 class="text-lg font-semibold text-gold">
            {{ $t('telegram.tabs.botSetup') }}
          </h2>
          <p class="text-sm text-gray-400">
            Manage your Telegram bots, tokens, and connection tests.
          </p>
          <p class="text-sm text-gray-500">
            Backend APIs for full bot management will be wired to this tab.
          </p>
        </div>

        <!-- Tab 3: Channels -->
        <div
          v-else-if="activeTab === 'channels'"
          class="card-luxury px-4 py-3 space-y-4 animate-fade-in-up"
        >
          <h2 class="text-lg font-semibold text-gold">
            {{ $t('telegram.channels.title') }}
          </h2>
          <p class="text-sm text-gray-400">
            {{ $t('telegram.channels.description') }}
          </p>
          <div class="space-y-3">
            <div
              v-for="ch in channels"
              :key="ch.id"
              class="flex items-center justify-between rounded-xl border border-[var(--glass-border)] bg-[var(--glass-bg)] px-4 py-2 animate-fade-in-up"
            >
              <div>
                <p class="font-medium text-[var(--text-primary)]">
                  {{ ch.name }}
                </p>
                <p class="text-xs text-[var(--text-secondary)]">
                  {{ ch.chat_id }}
                </p>
              </div>
              <span
                class="text-xs px-2 py-1 rounded-full"
                :class="ch.is_active ? 'bg-emerald-500/10 text-emerald-400' : 'bg-gray-500/10 text-gray-400'"
              >
                {{ ch.is_active ? $t('telegram.channels.active') : $t('telegram.channels.inactive') }}
              </span>
            </div>
          </div>
        </div>

        <!-- Tab 4: Automation -->
        <div
          v-else
          class="card-luxury px-4 py-3 space-y-4 animate-fade-in-up"
        >
          <h2 class="text-lg font-semibold text-gold">
            {{ $t('telegram.tabs.automation') }}
          </h2>
          <p class="text-sm text-gray-400">
            {{ $t('telegram.automation.description') }}
          </p>
          <div class="rounded-2xl border border-dashed border-[var(--glass-border)] px-4 py-3 text-sm text-[var(--text-secondary)]">
            {{ $t('telegram.automation.hint') }}
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { telegramApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const { t } = useI18n()

const tabs = [
  { id: 'messenger', labelKey: 'telegram.tabs.messenger', icon: 'fas fa-paper-plane' },
  { id: 'bot', labelKey: 'telegram.tabs.botSetup', icon: 'fas fa-robot' },
  { id: 'channels', labelKey: 'telegram.tabs.channels', icon: 'fas fa-broadcast-tower' },
  { id: 'automation', labelKey: 'telegram.tabs.automation', icon: 'fas fa-clock' },
]

const activeTab = ref('messenger')

const channels = ref([])
const channelId = ref('')
const message = ref('')
const submitting = ref(false)

const bannerKey = ref('none')
const cashPrice = ref('')
const accountPrice = ref('')
const singlePrice = ref('')

const bannerOptions = [
  { value: 'none', labelKey: 'telegram.messenger.bannerNone' },
  { value: 'buy_gbp_double', labelKey: 'telegram.messenger.bannerBuyDouble' },
  { value: 'sell_gbp_double', labelKey: 'telegram.messenger.bannerSellDouble' },
  { value: 'generic_single', labelKey: 'telegram.messenger.bannerGenericSingle' },
]

const useDoublePrice = computed(() =>
  bannerKey.value === 'buy_gbp_double' || bannerKey.value === 'sell_gbp_double',
)

const selectedChannel = computed(() =>
  channels.value.find((c) => String(c.id) === String(channelId.value)) || null,
)

const selectedChannelInitials = computed(() => {
  const name = selectedChannel.value?.name || 'CH'
  return name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0]?.toUpperCase() ?? '')
    .join('') || 'CH'
})

const selectedBannerLabel = computed(() => {
  const found = bannerOptions.find((b) => b.value === bannerKey.value)
  return found && found.value !== 'none' ? t(found.labelKey) : ''
})

const previewPriceLine = computed(() => {
  if (useDoublePrice.value) {
    const parts = []
    if (cashPrice.value) {
      parts.push(`Cash: ${cashPrice.value}`)
    }
    if (accountPrice.value) {
      parts.push(`Account: ${accountPrice.value}`)
    }
    return parts.join(' | ')
  }
  if (singlePrice.value) {
    return `Price: ${singlePrice.value}`
  }
  return ''
})

const previewTimestamp = computed(() => {
  const now = new Date()
  return now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })
})

onMounted(async () => {
  try {
    const { data } = await telegramApi.channels()
    channels.value = data ?? []
  } catch {
    channels.value = []
  }
})

async function handleSend() {
  const ch = channels.value.find((c) => String(c.id) === String(channelId.value))
  if (!ch) return
  submitting.value = true
  try {
    await telegramApi.sendMessage({
      bot_id: ch.bot,
      channel_id: Number(channelId.value),
      message: message.value || previewPriceLine.value || selectedBannerLabel.value || '',
    })
  } finally {
    submitting.value = false
  }
}
</script>
