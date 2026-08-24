<template>
  <div>
    <div class="mb-6 flex flex-wrap items-center justify-between gap-3">
      <div class="min-w-0">
        <router-link to="/programmer" class="text-sm text-[var(--text-secondary)] hover:text-gold">
          ← {{ $t('common.back') }}
        </router-link>
        <h1 class="mt-2 truncate text-2xl font-bold text-gold">
          {{ displayName || $t('programmerHub.userDetail') }}
        </h1>
        <p v-if="user" class="truncate text-sm text-[var(--text-secondary)]">
          {{ user.exchange_name || user.username }} · {{ $t(`programmerHub.plans.${user.plan || 'bronze'}`) }}
        </p>
      </div>
      <button
        type="button"
        class="btn-luxury"
        :disabled="!user || entering"
        @click="enterAs"
      >
        <i class="fas fa-sign-in-alt me-2" />
        {{ $t('programmerHub.enterAs') }}
      </button>
    </div>

    <div v-if="loading" class="space-y-4">
      <BaseSkeleton variant="card" class="!h-12" />
      <BaseSkeleton variant="card" class="!h-64" />
    </div>

    <template v-else-if="user">
      <div class="mb-6 flex flex-wrap gap-2 border-b" style="border-color: var(--border-card)">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          type="button"
          class="rounded-t-xl px-4 py-3 font-medium transition-colors -mb-px"
          :class="activeTab === tab.id
            ? 'border-b-2 border-gold bg-[var(--bg-hover)] text-gold'
            : 'text-[var(--text-secondary)] hover:text-[var(--primary)]'"
          @click="activeTab = tab.id"
        >
          <i :class="tab.icon" class="me-2" />
          {{ $t(tab.labelKey) }}
        </button>
      </div>

      <!-- Registered information (editable) -->
      <form
        v-show="activeTab === 'registered'"
        class="card-luxury max-w-xl space-y-3"
        @submit.prevent="saveRegistration"
      >
        <input v-model="form.first_name" class="input-luxury w-full" :placeholder="$t('programmerHub.firstName')" required />
        <input v-model="form.last_name" class="input-luxury w-full" :placeholder="$t('programmerHub.lastName')" required />
        <input v-model="form.exchange_name" class="input-luxury w-full" :placeholder="$t('programmerHub.exchangeName')" required />
        <input v-model="form.country" class="input-luxury w-full" :placeholder="$t('programmerHub.country')" required />
        <input v-model="form.email" type="email" class="input-luxury w-full" :placeholder="$t('programmerHub.email')" required />
        <input v-model="form.phone" class="input-luxury w-full" :placeholder="$t('programmerHub.phone')" required />
        <input v-model="form.telegram_id" class="input-luxury w-full" :placeholder="$t('programmerHub.telegramId')" />
        <input
          v-model="form.telegram_username"
          class="input-luxury w-full"
          :placeholder="$t('programmerHub.telegramUsername')"
        />
        <input
          v-if="!isDelegated"
          v-model="form.telegram_bot_token"
          class="input-luxury w-full"
          :placeholder="$t('programmerHub.botTokenOptional')"
          autocomplete="off"
        />
        <p
          v-if="!isDelegated && user.telegram_bot_token_masked"
          class="text-xs text-[var(--text-secondary)]"
        >
          {{ $t('programmerHub.currentBotToken') }}: {{ user.telegram_bot_token_masked }}
        </p>
        <select v-model="form.plan" class="input-luxury w-full">
          <option v-for="p in plans" :key="p" :value="p">{{ $t(`programmerHub.plans.${p}`) }}</option>
        </select>
        <select v-model="form.sub_role" class="input-luxury w-full">
          <option v-for="r in subRoles" :key="r" :value="r">{{ $t(`programmerHub.${r}`) }}</option>
        </select>
        <input
          v-if="isDelegated"
          v-model="form.owner_username"
          class="input-luxury w-full"
          :placeholder="$t('programmerHub.ownerUsername')"
        />
        <p v-if="isDelegated" class="text-xs text-[var(--text-secondary)]">
          {{ $t('programmerHub.ownerUsernameHint') }}
        </p>
        <label class="flex items-center gap-2 text-sm text-[var(--text-secondary)]">
          <input v-model="form.is_active" type="checkbox" class="rounded border-[var(--border-card)]" />
          {{ $t('programmerHub.active') }}
        </label>
        <button type="submit" class="btn-luxury w-full" :disabled="saving">
          {{ $t('common.save') }}
        </button>
      </form>

      <!-- Bot access (read-only) -->
      <div v-show="activeTab === 'botAccess'" class="space-y-4">
        <p v-if="!bots.length" class="card-luxury p-6 text-center text-[var(--text-secondary)]">
          {{ $t('programmerHub.noBots') }}
        </p>
        <BaseCard
          v-for="bot in bots"
          :key="bot.id"
          variant="glass"
          padding="sm"
          class="border border-[var(--glass-border)]"
        >
          <div class="flex flex-wrap items-start justify-between gap-3">
            <div class="min-w-0">
              <p class="font-semibold text-[var(--text-primary)]">{{ bot.display_name || bot.name }}</p>
              <p class="text-sm text-[var(--text-secondary)]">{{ bot.name }}</p>
            </div>
            <span
              class="rounded px-2 py-0.5 text-xs font-medium"
              :class="bot.is_active ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'"
            >
              {{ bot.is_active ? $t('programmerHub.active') : $t('programmerHub.inactive') }}
            </span>
          </div>
          <dl class="mt-3 grid gap-2 text-sm sm:grid-cols-2">
            <div>
              <dt class="text-[var(--text-secondary)]">{{ $t('programmerHub.botToken') }}</dt>
              <dd class="font-mono text-[var(--text-primary)]">{{ bot.token_masked || '—' }}</dd>
            </div>
            <div>
              <dt class="text-[var(--text-secondary)]">{{ $t('programmerHub.ttlMinutes') }}</dt>
              <dd class="text-[var(--text-primary)]">{{ bot.default_exchange_ttl_minutes }}</dd>
            </div>
            <div>
              <dt class="text-[var(--text-secondary)]">{{ $t('programmerHub.restrictChannels') }}</dt>
              <dd class="text-[var(--text-primary)]">{{ bot.restrict_to_known_channels ? $t('common.yes') : $t('common.no') }}</dd>
            </div>
            <div>
              <dt class="text-[var(--text-secondary)]">{{ $t('programmerHub.logMessages') }}</dt>
              <dd class="text-[var(--text-primary)]">{{ bot.log_all_messages ? $t('common.yes') : $t('common.no') }}</dd>
            </div>
          </dl>
          <div class="mt-4">
            <p class="mb-2 text-sm font-medium text-gold">{{ $t('programmerHub.channels') }}</p>
            <p v-if="!bot.channels?.length" class="text-sm text-[var(--text-secondary)]">
              {{ $t('programmerHub.noChannels') }}
            </p>
            <ul v-else class="divide-y divide-[var(--border-card)] rounded-xl border border-[var(--border-card)]">
              <li
                v-for="ch in bot.channels"
                :key="ch.id"
                class="flex items-center justify-between gap-2 px-3 py-2 text-sm"
              >
                <span class="truncate text-[var(--text-primary)]">{{ ch.name }} · {{ ch.chat_id }}</span>
                <span
                  class="shrink-0 rounded px-2 py-0.5 text-xs"
                  :class="ch.is_active ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'"
                >
                  {{ ch.is_active ? $t('programmerHub.active') : $t('programmerHub.inactive') }}
                </span>
              </li>
            </ul>
          </div>
        </BaseCard>
      </div>

      <!-- Bot analytics (read-only) -->
      <div v-show="activeTab === 'botAnalytics'" class="space-y-4">
        <p class="text-sm text-[var(--text-secondary)]">{{ $t('programmerHub.botAnalyticsHint') }}</p>
        <p v-if="!telegramAnalytics.length" class="card-luxury p-6 text-center text-[var(--text-secondary)]">
          {{ $t('programmerHub.noBots') }}
        </p>
        <BaseCard
          v-for="block in telegramAnalytics"
          :key="block.bot_id"
          variant="glass"
          padding="sm"
          class="border border-[var(--glass-border)] space-y-3"
        >
          <p class="font-semibold text-gold">{{ block.bot_name }}</p>
          <template v-if="block.analytics">
            <div class="grid grid-cols-2 gap-3 text-sm sm:grid-cols-4">
              <div>
                <p class="text-[var(--text-secondary)]">{{ $t('programmerHub.returnedUsers') }}</p>
                <p class="text-lg font-semibold">{{ block.analytics.customer_analysis?.returned ?? 0 }}</p>
              </div>
              <div>
                <p class="text-[var(--text-secondary)]">{{ $t('programmerHub.inactiveUsers') }}</p>
                <p class="text-lg font-semibold">{{ block.analytics.customer_analysis?.inactive ?? 0 }}</p>
              </div>
              <div>
                <p class="text-[var(--text-secondary)]">{{ $t('programmerHub.vipRatio') }}</p>
                <p class="text-lg font-semibold">{{ block.analytics.customer_analysis?.vip_vs_ordinary_request_ratio ?? '—' }}</p>
              </div>
              <div>
                <p class="text-[var(--text-secondary)]">{{ $t('telegram.admin.reports.pending') }}</p>
                <p class="text-lg font-semibold">{{ block.analytics.exchange_status?.pending ?? 0 }}</p>
              </div>
            </div>
            <div>
              <p class="mb-1 text-sm font-medium text-gold">{{ $t('telegram.admin.exchangeRequests.mostRequested') }}</p>
              <ul class="text-sm space-y-0.5">
                <li v-for="row in (block.analytics.most_requested_currencies || [])" :key="row.currency">
                  {{ row.currency }} — {{ row.count }}
                </li>
              </ul>
            </div>
            <div v-if="(block.analytics.channel_members || []).length">
              <p class="mb-1 text-sm font-medium text-gold">{{ $t('telegram.admin.analytics.channelMembers') }}</p>
              <ul class="text-sm space-y-0.5">
                <li v-for="ch in block.analytics.channel_members" :key="ch.channel_id">
                  {{ ch.name }}: {{ ch.member_count ?? '—' }}
                </li>
              </ul>
            </div>
          </template>
        </BaseCard>
      </div>

      <!-- Audit logs (read-only) -->
      <div v-show="activeTab === 'audit'" class="card-luxury overflow-hidden border border-[var(--glass-border)]">
        <p v-if="!auditLogs.length" class="p-8 text-center text-[var(--text-secondary)]">
          {{ $t('programmerHub.noAuditLogs') }}
        </p>
        <div v-else class="hidden overflow-x-auto md:block">
          <table class="w-full min-w-[560px]">
            <thead>
              <tr class="border-b border-[var(--border-color)]">
                <th class="px-4 py-3 text-start text-gold">{{ $t('programmerHub.actionType') }}</th>
                <th class="px-4 py-3 text-start text-gold">{{ $t('programmerHub.details') }}</th>
                <th class="px-4 py-3 text-start text-gold">{{ $t('programmerHub.ip') }}</th>
                <th class="px-4 py-3 text-start text-gold">{{ $t('logs.date') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="log in auditLogs"
                :key="log.id"
                class="border-b border-[var(--border-card)]"
              >
                <td class="px-4 py-3 text-sm text-[var(--text-primary)]">{{ actionLabel(log.action_type) }}</td>
                <td class="max-w-xs truncate px-4 py-3 text-sm text-[var(--text-secondary)]" :title="log.details">
                  {{ log.details || '—' }}
                </td>
                <td class="px-4 py-3 text-sm text-[var(--text-secondary)]">{{ log.ip_address || '—' }}</td>
                <td class="px-4 py-3 text-sm text-[var(--text-secondary)]">{{ formatDate(log.created_at) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="divide-y divide-[var(--border-card)] md:hidden">
          <div v-for="log in auditLogs" :key="log.id" class="space-y-1 p-4">
            <div class="flex justify-between gap-2 text-sm">
              <span class="font-medium text-[var(--text-primary)]">{{ actionLabel(log.action_type) }}</span>
              <span class="text-xs text-[var(--text-secondary)]">{{ formatDate(log.created_at) }}</span>
            </div>
            <p class="text-sm text-[var(--text-secondary)]">{{ log.details || '—' }}</p>
            <p class="text-xs text-[var(--text-secondary)]">{{ log.ip_address || '—' }}</p>
          </div>
        </div>
      </div>

      <!-- Templates (read-only) -->
      <div v-show="activeTab === 'templates'">
        <p class="mb-4 text-sm text-[var(--text-secondary)]">{{ $t('programmerHub.userTemplatesHint') }}</p>
        <p v-if="!templateItems.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
          {{ $t('programmerHub.noTemplates') }}
        </p>
        <div v-else class="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
          <BaseCard
            v-for="item in templateItems"
            :key="item.kind + item.id"
            variant="glass"
            padding="none"
            class="overflow-hidden border border-[var(--glass-border)]"
          >
            <div class="h-28 bg-[var(--bg-hover)]">
              <img v-if="item.image" :src="item.image" alt="" class="h-full w-full object-cover" />
            </div>
            <div class="space-y-1 p-3">
              <p class="truncate text-sm font-semibold text-[var(--text-primary)]">{{ item.name }}</p>
              <span
                class="inline-block rounded px-2 py-0.5 text-xs font-medium border"
                :class="planBadgeClass(item.plan)"
              >
                {{ $t(`programmerHub.plans.${item.plan}`) }}
              </span>
            </div>
          </BaseCard>
        </div>
      </div>
    </template>

    <p v-else class="card-luxury p-8 text-center text-[var(--text-secondary)]">
      {{ $t('programmerHub.userNotFound') }}
    </p>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { authApi, getApiErrorDetails } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const plans = ['bronze', 'silver', 'gold']
const tabs = [
  { id: 'registered', labelKey: 'programmerHub.tabs.registered', icon: 'fas fa-id-card' },
  { id: 'botAccess', labelKey: 'programmerHub.tabs.botAccess', icon: 'fas fa-robot' },
  { id: 'botAnalytics', labelKey: 'programmerHub.tabs.botAnalytics', icon: 'fas fa-chart-bar' },
  { id: 'audit', labelKey: 'programmerHub.tabs.audit', icon: 'fas fa-history' },
  { id: 'templates', labelKey: 'programmerHub.tabs.templates', icon: 'fas fa-images' },
]

const route = useRoute()
const router = useRouter()
const toast = useToast()
const auth = useAuthStore()
const { t, te } = useI18n()

const loading = ref(true)
const saving = ref(false)
const entering = ref(false)
const activeTab = ref('registered')
const user = ref(null)
const bots = ref([])
const telegramAnalytics = ref([])
const auditLogs = ref([])
const priceTemplates = ref([])
const editorTemplates = ref([])

const subRoles = ['admin', 'operator', 'head_operator']

const form = reactive({
  first_name: '',
  last_name: '',
  exchange_name: '',
  country: '',
  email: '',
  phone: '',
  telegram_id: '',
  telegram_username: '',
  telegram_bot_token: '',
  plan: 'bronze',
  sub_role: 'admin',
  owner_username: '',
  is_active: true,
})

const isDelegated = computed(
  () => form.sub_role === 'operator' || form.sub_role === 'head_operator'
)

const displayName = computed(() => {
  const u = user.value
  if (!u) return ''
  return `${u.first_name || ''} ${u.last_name || ''}`.trim() || u.full_name || u.username
})

const templateItems = computed(() => {
  const price = priceTemplates.value.map((row) => ({
    kind: 'price',
    id: row.id,
    name: row.name,
    plan: row.plan || 'bronze',
    image: row.background_image,
  }))
  const editor = editorTemplates.value.map((row) => ({
    kind: 'editor',
    id: row.id,
    name: row.name,
    plan: row.plan || 'bronze',
    image: row.image,
  }))
  return [...price, ...editor]
})

function planBadgeClass(plan) {
  if (plan === 'gold') return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  if (plan === 'silver') return 'bg-slate-400/20 text-slate-200 border-slate-400/40'
  return 'bg-orange-800/30 text-orange-300 border-orange-700/40'
}

function fillForm(u) {
  form.first_name = u.first_name || ''
  form.last_name = u.last_name || ''
  form.exchange_name = u.exchange_name || ''
  form.country = u.country || ''
  form.email = u.email || ''
  form.phone = u.phone || ''
  form.telegram_id = u.telegram_id || ''
  form.telegram_username = u.telegram_username || ''
  form.telegram_bot_token = ''
  form.plan = u.plan || 'bronze'
  form.sub_role = u.sub_role || 'admin'
  form.owner_username = u.owner_username || ''
  form.is_active = u.is_active !== false
}

function actionLabel(actionType) {
  const key = `programmerHub.actionTypes.${actionType}`
  if (te(key)) return t(key)
  return actionType
}

function formatDate(iso) {
  if (!iso) return '—'
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}

async function loadDetail() {
  loading.value = true
  user.value = null
  try {
    const { data } = await authApi.programmer.get(route.params.id)
    user.value = data.user
    bots.value = data.bots || []
    telegramAnalytics.value = data.telegram_analytics || []
    auditLogs.value = data.audit_logs || []
    priceTemplates.value = data.templates?.price_templates || []
    editorTemplates.value = data.templates?.editor_templates || []
    fillForm(data.user)
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    loading.value = false
  }
}

async function saveRegistration() {
  saving.value = true
  try {
    const payload = {
      first_name: form.first_name,
      last_name: form.last_name,
      exchange_name: form.exchange_name,
      country: form.country,
      email: form.email,
      phone: form.phone,
      telegram_id: form.telegram_id,
      telegram_username: form.telegram_username,
      sub_role: form.sub_role,
      owner_username: form.owner_username,
      plan: form.plan,
      is_active: form.is_active,
    }
    if (!isDelegated.value && form.telegram_bot_token.trim()) {
      payload.telegram_bot_token = form.telegram_bot_token.trim()
    }
    const { data } = await authApi.programmer.update(route.params.id, payload)
    user.value = data
    fillForm(data)
    toast.success(t('programmerHub.userUpdated'))
    const detail = await authApi.programmer.get(route.params.id)
    user.value = detail.data.user
    bots.value = detail.data.bots || []
    telegramAnalytics.value = detail.data.telegram_analytics || []
    auditLogs.value = detail.data.audit_logs || []
    priceTemplates.value = detail.data.templates?.price_templates || []
    editorTemplates.value = detail.data.templates?.editor_templates || []
    fillForm(detail.data.user)
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    saving.value = false
  }
}

async function enterAs() {
  if (!user.value) return
  entering.value = true
  try {
    await auth.impersonate(user.value.id)
    router.push('/panel')
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    entering.value = false
  }
}

watch(() => route.params.id, () => {
  if (route.name === 'programmer-user') loadDetail()
})

onMounted(loadDetail)
</script>
