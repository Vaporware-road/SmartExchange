<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('ownerConsole.title') }}</h1>

    <div class="flex flex-wrap gap-2 mb-6">
      <button
        v-for="t in tabs"
        :key="t.key"
        type="button"
        class="px-4 py-2 rounded-lg text-sm font-medium border transition-colors"
        :class="tab === t.key
          ? 'bg-amber-500/20 text-amber-400 border-amber-500/40'
          : 'border-[var(--border-card)] text-[var(--text-secondary)]'"
        @click="tab = t.key"
      >
        <i :class="t.icon" class="me-1" />
        {{ $t(`ownerConsole.tabs.${t.key}`) }}
      </button>
    </div>

    <!-- Logins & IPs -->
    <template v-if="tab === 'activity'">
      <div class="flex flex-wrap items-end gap-2 mb-4">
        <div class="grow min-w-[12rem]">
          <label class="block text-xs text-[var(--text-secondary)] mb-1" for="console-q">
            {{ $t('ownerConsole.search') }}
          </label>
          <input
            id="console-q"
            v-model="filters.q"
            type="search"
            class="input-luxury w-full"
            :placeholder="$t('ownerConsole.searchHint')"
            @keyup.enter="load"
          />
        </div>
        <div class="w-40">
          <label class="block text-xs text-[var(--text-secondary)] mb-1" for="console-ip">
            {{ $t('ownerConsole.ip') }}
          </label>
          <input id="console-ip" v-model="filters.ip" type="text" class="input-luxury w-full" @keyup.enter="load" />
        </div>
        <div class="w-44">
          <label class="block text-xs text-[var(--text-secondary)] mb-1" for="console-action">
            {{ $t('ownerConsole.action') }}
          </label>
          <select id="console-action" v-model="filters.action_type" class="input-luxury w-full" @change="load">
            <option value="">{{ $t('ownerConsole.allActions') }}</option>
            <option v-for="a in actionTypes" :key="a" :value="a">
              {{ $t(`ownerConsole.actions.${a}`) }}
            </option>
          </select>
        </div>
        <div class="w-40">
          <label class="block text-xs text-[var(--text-secondary)] mb-1" for="console-from">
            {{ $t('ownerConsole.from') }}
          </label>
          <input id="console-from" v-model="filters.date_from" type="date" class="input-luxury w-full" @change="load" />
        </div>
        <div class="w-40">
          <label class="block text-xs text-[var(--text-secondary)] mb-1" for="console-to">
            {{ $t('ownerConsole.to') }}
          </label>
          <input id="console-to" v-model="filters.date_to" type="date" class="input-luxury w-full" @change="load" />
        </div>
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
          @click="load"
        >
          <i class="fas fa-filter me-1" />{{ $t('ownerConsole.apply') }}
        </button>
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-[var(--border-card)] text-[var(--text-secondary)]"
          :disabled="!activity.length"
          @click="exportCsv"
        >
          <i class="fas fa-file-csv me-1" />{{ $t('ownerConsole.exportCsv') }}
        </button>
      </div>

      <div v-if="loading" class="grid grid-cols-1 gap-4">
        <BaseSkeleton v-for="i in 4" :key="i" variant="card" class="!h-24" />
      </div>
      <div v-else-if="!activity.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
        {{ $t('ownerConsole.noActivity') }}
      </div>
      <div v-else class="card-luxury p-0 overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="text-start text-xs uppercase text-[var(--text-secondary)]">
              <th class="p-3 text-start">{{ $t('ownerConsole.user') }}</th>
              <th class="p-3 text-start">{{ $t('ownerConsole.account') }}</th>
              <th class="p-3 text-start">{{ $t('ownerConsole.action') }}</th>
              <th class="p-3 text-start">{{ $t('ownerConsole.ip') }}</th>
              <th class="p-3 text-start">{{ $t('ownerConsole.device') }}</th>
              <th class="p-3 text-start">{{ $t('ownerConsole.when') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in activity" :key="row.id" class="border-t border-[var(--border-card)]">
              <td class="p-3">
                <p class="text-[var(--text-primary)]">{{ row.user_display || $t('ownerConsole.unknownUser') }}</p>
                <p class="text-xs text-[var(--text-secondary)]">{{ row.email || '—' }}</p>
              </td>
              <td class="p-3 text-[var(--text-secondary)]">{{ row.account || '—' }}</td>
              <td class="p-3">
                <span
                  class="rounded-lg px-2 py-1 text-xs font-semibold border"
                  :class="actionClass(row.action_type)"
                >
                  {{ $t(`ownerConsole.actions.${row.action_type}`) }}
                </span>
              </td>
              <td class="p-3">
                <code class="text-xs text-[var(--text-secondary)]">{{ row.ip_address || '—' }}</code>
              </td>
              <td class="p-3 text-xs text-[var(--text-secondary)] max-w-xs truncate" :title="row.user_agent">
                {{ deviceLabel(row.user_agent) }}
              </td>
              <td class="p-3 text-[var(--text-secondary)] whitespace-nowrap">{{ formatDateTime(row.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <!-- Accounts & trials -->
    <template v-else-if="tab === 'accounts'">
      <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <BaseSkeleton v-for="i in 4" :key="i" variant="card" class="!h-44" />
      </div>
      <div v-else-if="!accounts.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
        {{ $t('ownerConsole.noAccounts') }}
      </div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <BaseCard
          v-for="row in accounts"
          :key="row.id"
          variant="glass"
          padding="sm"
          class="border border-[var(--glass-border)]"
        >
          <div class="flex items-start justify-between gap-3">
            <div class="min-w-0">
              <p class="font-semibold text-[var(--text-primary)] truncate">{{ row.name }}</p>
              <p class="text-sm text-[var(--text-secondary)] truncate">
                {{ row.owner?.full_name || row.owner?.username || '—' }}
              </p>
              <p class="text-xs text-[var(--text-secondary)] mt-1 truncate">
                <i class="fas fa-envelope me-1" />{{ row.owner?.email || '—' }}
                <i
                  v-if="row.owner?.email_verified_at"
                  class="fas fa-circle-check ms-1 text-emerald-400"
                  :title="$t('ownerConsole.verified')"
                />
              </p>
            </div>
            <span
              class="shrink-0 rounded-lg px-2 py-1 text-xs font-semibold border"
              :class="accountBadgeClass(row)"
            >
              {{ accountBadgeLabel(row) }}
            </span>
          </div>

          <dl class="mt-3 grid grid-cols-2 gap-x-4 gap-y-1 text-xs text-[var(--text-secondary)]">
            <div>
              <dt class="inline">{{ $t('ownerConsole.signedUp') }}:</dt>
              <dd class="inline ms-1">{{ formatDate(row.created_at) }}</dd>
            </div>
            <div>
              <dt class="inline">{{ $t('ownerConsole.lastLogin') }}:</dt>
              <dd class="inline ms-1">{{ formatDate(row.owner?.last_login) }}</dd>
            </div>
            <div>
              <dt class="inline">{{ $t('ownerConsole.seats') }}:</dt>
              <dd class="inline ms-1">{{ row.user_count }}</dd>
            </div>
            <div>
              <dt class="inline">{{ $t('ownerConsole.revenue') }}:</dt>
              <dd class="inline ms-1">{{ row.sales_total }}</dd>
            </div>
          </dl>

          <div v-if="row.owner" class="mt-3 flex flex-wrap gap-2">
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-[var(--border-card)] text-[var(--text-secondary)]"
              :disabled="busyId === row.id"
              @click="extendTrial(row)"
            >
              <i class="fas fa-clock me-1" />{{ $t('fleet.extend', { days: EXTEND_DAYS }) }}
            </button>
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-amber-500/40 bg-amber-500/20 text-amber-400"
              :disabled="busyId === row.id"
              @click="openSale(row)"
            >
              <i class="fas fa-receipt me-1" />{{ $t('ownerConsole.recordSale') }}
            </button>
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-[var(--border-card)] text-[var(--text-secondary)]"
              :disabled="busyId === row.id"
              @click="forceLogout(row)"
            >
              <i class="fas fa-right-from-bracket me-1" />{{ $t('ownerConsole.forceLogout') }}
            </button>
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border"
              :class="row.owner.is_active
                ? 'border-red-500/40 bg-red-500/10 text-red-400'
                : 'border-emerald-500/40 bg-emerald-500/10 text-emerald-400'"
              :disabled="busyId === row.id"
              @click="toggleSuspend(row)"
            >
              <i :class="row.owner.is_active ? 'fas fa-ban' : 'fas fa-play'" class="me-1" />
              {{ row.owner.is_active ? $t('ownerConsole.suspend') : $t('ownerConsole.reinstate') }}
            </button>
          </div>
        </BaseCard>
      </div>
    </template>

    <!-- Sales -->
    <template v-else-if="tab === 'sales'">
      <div class="flex justify-end mb-4">
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
          @click="openSale(null)"
        >
          <i class="fas fa-plus me-1" />{{ $t('ownerConsole.recordSale') }}
        </button>
      </div>

      <div v-if="loading" class="grid grid-cols-1 gap-4">
        <BaseSkeleton v-for="i in 3" :key="i" variant="card" class="!h-24" />
      </div>
      <div v-else-if="!sales.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
        {{ $t('ownerConsole.noSales') }}
      </div>
      <template v-else>
        <div class="card-luxury p-0 overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr class="text-start text-xs uppercase text-[var(--text-secondary)]">
                <th class="p-3 text-start">{{ $t('ownerConsole.customer') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.account') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.amount') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.salePlan') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.soldAt') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.reference') }}</th>
                <th class="p-3 text-start">{{ $t('fleet.license') }}</th>
                <th class="p-3 text-start">{{ $t('ownerConsole.recordedBy') }}</th>
                <th class="p-3 text-end">{{ $t('common.actions') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="row in sales" :key="row.id" class="border-t border-[var(--border-card)]">
                <td class="p-3">
                  <p class="text-[var(--text-primary)]">{{ row.customer_display }}</p>
                  <p class="text-xs text-[var(--text-secondary)]">{{ row.customer_email || '—' }}</p>
                </td>
                <td class="p-3 text-[var(--text-secondary)]">{{ row.account_name || '—' }}</td>
                <td class="p-3 text-[var(--text-primary)] whitespace-nowrap">
                  {{ row.amount }} {{ row.currency }}
                </td>
                <td class="p-3 text-[var(--text-secondary)]">{{ $t(`ownerConsole.salePlans.${row.sale_plan}`) }}</td>
                <td class="p-3 text-[var(--text-secondary)] whitespace-nowrap">{{ formatDate(row.sold_at) }}</td>
                <td class="p-3 text-[var(--text-secondary)]">{{ row.reference || '—' }}</td>
                <td class="p-3 font-mono text-xs text-[var(--text-secondary)] whitespace-nowrap">
                  {{ row.license_key || '—' }}
                </td>
                <td class="p-3 text-[var(--text-secondary)]">{{ row.recorded_by_display || '—' }}</td>
                <td class="p-3 text-end whitespace-nowrap">
                  <button
                    type="button"
                    class="px-2 py-1 rounded-lg text-xs border border-red-500/40 text-red-400"
                    :disabled="busyId === row.id"
                    @click="deleteSale(row)"
                  >
                    <i class="fas fa-trash" />
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="mt-3 text-sm text-[var(--text-secondary)]">
          {{ $t('ownerConsole.salesTotal', { total: salesTotal }) }}
        </p>
      </template>
    </template>

    <!-- Support channels -->
    <template v-else>
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div class="lg:col-span-2">
          <div class="flex justify-end mb-4">
            <button
              type="button"
              class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
              @click="openChannel(null)"
            >
              <i class="fas fa-plus me-1" />{{ $t('ownerConsole.addChannel') }}
            </button>
          </div>

          <div v-if="loading" class="grid grid-cols-1 gap-4">
            <BaseSkeleton v-for="i in 3" :key="i" variant="card" class="!h-20" />
          </div>
          <div v-else-if="!channels.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
            {{ $t('ownerConsole.noChannels') }}
          </div>
          <div v-else class="grid grid-cols-1 gap-3">
            <BaseCard
              v-for="row in channels"
              :key="row.id"
              variant="glass"
              padding="sm"
              class="border border-[var(--glass-border)]"
            >
              <div class="flex items-center gap-3">
                <i :class="row.icon" class="text-lg text-amber-400 w-6 text-center" />
                <div class="min-w-0 flex-1">
                  <p class="font-semibold text-[var(--text-primary)] truncate">{{ row.label }}</p>
                  <p class="text-xs text-[var(--text-secondary)] truncate" dir="ltr">{{ row.value }}</p>
                </div>
                <span
                  class="shrink-0 rounded-lg px-2 py-1 text-xs font-semibold border"
                  :class="row.is_active
                    ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40'
                    : 'border-[var(--border-card)] text-[var(--text-secondary)]'"
                >
                  {{ row.is_active ? $t('common.active') : $t('common.inactive') }}
                </span>
                <button
                  type="button"
                  class="px-2 py-1 rounded-lg text-xs border border-[var(--border-card)] text-[var(--text-secondary)]"
                  @click="openChannel(row)"
                >
                  <i class="fas fa-pen" />
                </button>
                <button
                  type="button"
                  class="px-2 py-1 rounded-lg text-xs border border-red-500/40 text-red-400"
                  :disabled="busyId === row.id"
                  @click="deleteChannel(row)"
                >
                  <i class="fas fa-trash" />
                </button>
              </div>
            </BaseCard>
          </div>
        </div>

        <!-- What the customer actually sees, rendered by the same component the
             panel footer and the tour use. -->
        <div>
          <p class="text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('ownerConsole.preview') }}
          </p>
          <div class="card-luxury p-4">
            <SupportChannelList :items="activeChannels" />
            <p v-if="!activeChannels.length" class="text-sm text-[var(--text-secondary)]">
              {{ $t('ownerConsole.previewEmpty') }}
            </p>
          </div>
        </div>
      </div>
    </template>

    <BaseModal v-model="saleOpen" :title="$t('ownerConsole.recordSale')">
      <p class="text-sm text-[var(--text-secondary)] mb-4">{{ $t('ownerConsole.saleHint') }}</p>
      <div class="space-y-3">
        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-customer">
            {{ $t('ownerConsole.customer') }}
          </label>
          <select id="sale-customer" v-model="saleForm.customer" class="input-luxury w-full">
            <option :value="null">{{ $t('ownerConsole.pickCustomer') }}</option>
            <option v-for="opt in customerOptions" :key="opt.id" :value="opt.id">
              {{ opt.label }}
            </option>
          </select>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-amount">
              {{ $t('ownerConsole.amount') }}
            </label>
            <input id="sale-amount" v-model="saleForm.amount" type="number" min="0" step="0.01" class="input-luxury w-full" />
          </div>
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-currency">
              {{ $t('ownerConsole.currency') }}
            </label>
            <input id="sale-currency" v-model="saleForm.currency" type="text" maxlength="8" class="input-luxury w-full" />
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-plan">
              {{ $t('ownerConsole.salePlan') }}
            </label>
            <select id="sale-plan" v-model="saleForm.sale_plan" class="input-luxury w-full">
              <option v-for="p in salePlans" :key="p" :value="p">
                {{ $t(`ownerConsole.salePlans.${p}`) }}
              </option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-reference">
              {{ $t('ownerConsole.reference') }}
            </label>
            <input id="sale-reference" v-model="saleForm.reference" type="text" class="input-luxury w-full" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="sale-note">
            {{ $t('ownerConsole.note') }}
          </label>
          <textarea id="sale-note" v-model="saleForm.note" rows="2" class="input-luxury w-full" />
        </div>
      </div>
      <div class="mt-6 flex justify-end gap-2">
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-[var(--border-card)] text-[var(--text-secondary)]"
          @click="saleOpen = false"
        >
          {{ $t('common.cancel') }}
        </button>
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
          :disabled="!saleValid || saving"
          @click="submitSale"
        >
          {{ $t('ownerConsole.recordSale') }}
        </button>
      </div>
    </BaseModal>

    <BaseModal v-model="channelOpen" :title="$t('ownerConsole.channelTitle')">
      <div class="space-y-3">
        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="channel-kind">
            {{ $t('ownerConsole.channelKind') }}
          </label>
          <select id="channel-kind" v-model="channelForm.kind" class="input-luxury w-full">
            <option v-for="k in channelKinds" :key="k" :value="k">
              {{ $t(`support.kinds.${k}`) }}
            </option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="channel-label">
            {{ $t('ownerConsole.channelLabel') }}
          </label>
          <input id="channel-label" v-model="channelForm.label" type="text" class="input-luxury w-full" />
        </div>
        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="channel-value">
            {{ $t('ownerConsole.channelValue') }}
          </label>
          <input id="channel-value" v-model="channelForm.value" type="text" dir="ltr" class="input-luxury w-full" />
          <p class="mt-1 text-xs text-[var(--text-secondary)]">{{ $t('ownerConsole.channelValueHint') }}</p>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-1" for="channel-order">
              {{ $t('ownerConsole.channelOrder') }}
            </label>
            <input id="channel-order" v-model.number="channelForm.sort_order" type="number" min="0" class="input-luxury w-full" />
          </div>
          <label class="flex items-end gap-2 pb-2 text-sm text-[var(--text-secondary)]">
            <input v-model="channelForm.is_active" type="checkbox" class="rounded" />
            {{ $t('common.active') }}
          </label>
        </div>
      </div>
      <div class="mt-6 flex justify-end gap-2">
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-[var(--border-card)] text-[var(--text-secondary)]"
          @click="channelOpen = false"
        >
          {{ $t('common.cancel') }}
        </button>
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
          :disabled="!channelValid || saving"
          @click="submitChannel"
        >
          {{ $t('common.save') }}
        </button>
      </div>
    </BaseModal>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { authApi, fleetApi, settingsApi, getApiErrorDetails } from '@/services/api'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseModal from '@/components/ui/BaseModal.vue'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import SupportChannelList from '@/components/support/SupportChannelList.vue'

const EXTEND_DAYS = 14

const tabs = [
  { key: 'activity', icon: 'fas fa-shield-halved' },
  { key: 'accounts', icon: 'fas fa-building' },
  { key: 'sales', icon: 'fas fa-receipt' },
  { key: 'support', icon: 'fas fa-headset' },
]
const actionTypes = [
  'signup',
  'login_success',
  'login_failed',
  'logout',
  'price_update',
  'bulk_price_update',
  'special_price_update',
  'template_change',
  'finalize',
  'impersonate_start',
  'other',
]
const salePlans = ['one_time', 'lifetime', 'renewal', 'addon']
const channelKinds = ['phone', 'whatsapp', 'telegram', 'email', 'instagram', 'custom']

const { t, locale } = useI18n()
const toast = useToast()
const siteSettings = useSiteSettingsStore()

const tab = ref('activity')
const loading = ref(true)
const saving = ref(false)
const busyId = ref(null)

const activity = ref([])
const accounts = ref([])
const sales = ref([])
const channels = ref([])

const filters = reactive({ q: '', ip: '', action_type: '', date_from: '', date_to: '' })

const saleOpen = ref(false)
const saleForm = reactive({
  customer: null,
  amount: '',
  currency: 'USD',
  sale_plan: 'one_time',
  reference: '',
  note: '',
})

const channelOpen = ref(false)
const channelEditing = ref(null)
const channelForm = reactive({
  kind: 'phone',
  label: '',
  value: '',
  is_active: true,
  sort_order: 0,
})

const activeChannels = computed(() =>
  channels.value.filter((row) => row.is_active).map((row) => ({ ...row })),
)

const customerOptions = computed(() =>
  accounts.value
    .filter((row) => row.owner)
    .map((row) => ({
      id: row.owner.id,
      label: `${row.owner.full_name || row.owner.username} — ${row.name}`,
    })),
)

const salesTotal = computed(() => {
  const byCurrency = sales.value.reduce((acc, row) => {
    const key = row.currency || 'USD'
    acc[key] = (acc[key] || 0) + Number(row.amount || 0)
    return acc
  }, {})
  return Object.entries(byCurrency)
    .map(([currency, amount]) => `${amount.toFixed(2)} ${currency}`)
    .join(' · ')
})

const saleValid = computed(() => Boolean(saleForm.customer) && Number(saleForm.amount) > 0)
const channelValid = computed(
  () => channelForm.label.trim().length > 0 && channelForm.value.trim().length > 0,
)

function formatDate(value) {
  if (!value) return '—'
  return new Date(value).toLocaleDateString(locale.value, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

function formatDateTime(value) {
  if (!value) return '—'
  return new Date(value).toLocaleString(locale.value, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

function actionClass(action) {
  if (action === 'login_failed') return 'bg-red-500/20 text-red-400 border-red-500/40'
  if (action === 'signup' || action === 'login_success') {
    return 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40'
  }
  if (action === 'impersonate_start') return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  return 'border-[var(--border-card)] text-[var(--text-secondary)]'
}

/** The browser and platform out of a user agent — the full string is on hover. */
function deviceLabel(userAgent) {
  if (!userAgent) return '—'
  const browser =
    /Edg\//.test(userAgent) ? 'Edge'
    : /OPR\//.test(userAgent) ? 'Opera'
    : /Chrome\//.test(userAgent) ? 'Chrome'
    : /Firefox\//.test(userAgent) ? 'Firefox'
    : /Safari\//.test(userAgent) ? 'Safari'
    : t('ownerConsole.unknownDevice')
  const platform =
    /Android/.test(userAgent) ? 'Android'
    : /iPhone|iPad/.test(userAgent) ? 'iOS'
    : /Windows/.test(userAgent) ? 'Windows'
    : /Mac OS/.test(userAgent) ? 'macOS'
    : /Linux/.test(userAgent) ? 'Linux'
    : ''
  return platform ? `${browser} · ${platform}` : browser
}

function accountBadgeLabel(row) {
  if (row.owner && !row.owner.is_active) return t('ownerConsole.suspended')
  if (row.is_paid) return t('ownerConsole.paid')
  const days = row.owner?.days_remaining
  if (days == null) return '—'
  if (days < 0) return t('fleet.lapsed')
  if (days === 0) return t('fleet.expiresToday')
  return t('fleet.daysLeft', { days })
}

function accountBadgeClass(row) {
  if (row.owner && !row.owner.is_active) return 'bg-red-500/20 text-red-400 border-red-500/40'
  if (row.is_paid) return 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40'
  const days = row.owner?.days_remaining
  if (days == null || days < 0) return 'bg-red-500/20 text-red-400 border-red-500/40'
  if (days <= 3) return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  return 'border-[var(--border-card)] text-[var(--text-secondary)]'
}

function unwrap(data) {
  return Array.isArray(data) ? data : (data?.results ?? [])
}

async function load() {
  loading.value = true
  try {
    if (tab.value === 'activity') {
      const params = Object.fromEntries(
        Object.entries(filters).filter(([, value]) => value !== ''),
      )
      const { data } = await authApi.activity(params)
      activity.value = unwrap(data)
    } else if (tab.value === 'accounts') {
      const { data } = await fleetApi.accounts()
      accounts.value = unwrap(data)
    } else if (tab.value === 'sales') {
      const [saleRes, accountRes] = await Promise.all([fleetApi.sales(), fleetApi.accounts()])
      sales.value = unwrap(saleRes.data)
      accounts.value = unwrap(accountRes.data)
    } else {
      const { data } = await settingsApi.supportChannels.list()
      channels.value = unwrap(data)
    }
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    loading.value = false
  }
}

function exportCsv() {
  const header = ['email', 'user', 'account', 'action', 'ip', 'user_agent', 'created_at']
  const escape = (value) => `"${String(value ?? '').replace(/"/g, '""')}"`
  const rows = activity.value.map((row) =>
    [
      row.email,
      row.user_display,
      row.account,
      row.action_type,
      row.ip_address,
      row.user_agent,
      row.created_at,
    ]
      .map(escape)
      .join(','),
  )
  const blob = new Blob([[header.join(','), ...rows].join('\n')], {
    type: 'text/csv;charset=utf-8;',
  })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `logins-${new Date().toISOString().slice(0, 10)}.csv`
  link.click()
  URL.revokeObjectURL(url)
}

async function extendTrial(row) {
  busyId.value = row.id
  try {
    await fleetApi.extendTrial(row.owner.id, { days: EXTEND_DAYS })
    toast.success(t('fleet.extended', { days: EXTEND_DAYS }))
    await load()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

async function forceLogout(row) {
  busyId.value = row.id
  try {
    await authApi.users.forceLogout(row.owner.id)
    toast.success(t('ownerConsole.forcedLogout'))
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

async function toggleSuspend(row) {
  busyId.value = row.id
  try {
    await fleetApi.suspendAccount(row.id, !row.owner.is_active)
    toast.success(row.owner.is_active ? t('ownerConsole.suspended') : t('ownerConsole.reinstated'))
    await load()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

function openSale(row) {
  saleForm.customer = row?.owner?.id ?? null
  saleForm.amount = ''
  saleForm.currency = 'USD'
  saleForm.sale_plan = 'one_time'
  saleForm.reference = ''
  saleForm.note = ''
  if (!accounts.value.length) {
    fleetApi
      .accounts()
      .then(({ data }) => {
        accounts.value = unwrap(data)
      })
      .catch((error) => toast.error(getApiErrorDetails(error).message))
  }
  saleOpen.value = true
}

async function submitSale() {
  if (!saleValid.value) return
  saving.value = true
  try {
    await fleetApi.createSale({
      customer: saleForm.customer,
      amount: saleForm.amount,
      currency: saleForm.currency.trim().toUpperCase() || 'USD',
      sale_plan: saleForm.sale_plan,
      reference: saleForm.reference.trim(),
      note: saleForm.note.trim(),
    })
    saleOpen.value = false
    toast.success(t('ownerConsole.saleRecorded'))
    await load()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    saving.value = false
  }
}

async function deleteSale(row) {
  busyId.value = row.id
  try {
    await fleetApi.deleteSale(row.id)
    sales.value = sales.value.filter((r) => r.id !== row.id)
    toast.success(t('ownerConsole.saleDeleted'))
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

function openChannel(row) {
  channelEditing.value = row
  channelForm.kind = row?.kind ?? 'phone'
  channelForm.label = row?.label ?? ''
  channelForm.value = row?.value ?? ''
  channelForm.is_active = row?.is_active ?? true
  channelForm.sort_order = row?.sort_order ?? channels.value.length
  channelOpen.value = true
}

async function submitChannel() {
  if (!channelValid.value) return
  saving.value = true
  const payload = {
    kind: channelForm.kind,
    label: channelForm.label.trim(),
    value: channelForm.value.trim(),
    is_active: channelForm.is_active,
    sort_order: channelForm.sort_order || 0,
  }
  try {
    if (channelEditing.value) {
      await settingsApi.supportChannels.update(channelEditing.value.id, payload)
    } else {
      await settingsApi.supportChannels.create(payload)
    }
    channelOpen.value = false
    toast.success(t('common.saved'))
    await load()
    // The panel footer, the tour and the expiry wall all read this store, so
    // refreshing it makes the change visible without a reload.
    await siteSettings.fetch()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    saving.value = false
  }
}

async function deleteChannel(row) {
  busyId.value = row.id
  try {
    await settingsApi.supportChannels.delete(row.id)
    channels.value = channels.value.filter((r) => r.id !== row.id)
    await siteSettings.fetch()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

watch(tab, load)
onMounted(load)
</script>
