<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('fleet.title') }}</h1>

    <div class="flex gap-2 mb-6">
      <button
        v-for="t in tabs"
        :key="t"
        type="button"
        class="px-4 py-2 rounded-lg text-sm font-medium border transition-colors"
        :class="tab === t
          ? 'bg-amber-500/20 text-amber-400 border-amber-500/40'
          : 'border-[var(--border-card)] text-[var(--text-secondary)]'"
        @click="tab = t"
      >
        <i :class="t === 'trials' ? 'fas fa-hourglass-half' : 'fas fa-key'" class="me-1" />
        {{ $t(`fleet.tabs.${t}`) }}
      </button>
    </div>

    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <BaseSkeleton v-for="i in 4" :key="i" variant="card" class="!h-44" />
    </div>

    <!-- Trial customers: live from the shared database, so days remaining is exact. -->
    <template v-else-if="tab === 'trials'">
      <div v-if="!trials.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
        {{ $t('fleet.noTrials') }}
      </div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <BaseCard
          v-for="row in trials"
          :key="row.id"
          variant="glass"
          padding="sm"
          class="border border-[var(--glass-border)]"
        >
          <div class="flex items-start justify-between gap-3">
            <div class="min-w-0">
              <p class="font-semibold text-[var(--text-primary)] truncate">
                {{ row.full_name || row.username }}
              </p>
              <p class="text-sm text-[var(--text-secondary)] truncate">
                {{ row.exchange_name || row.username }}
              </p>
              <p v-if="row.deployment" class="text-xs text-[var(--text-secondary)] mt-1 truncate">
                <i class="fas fa-globe me-1" />{{ row.deployment.domain }}
              </p>
            </div>
            <span
              class="shrink-0 rounded-lg px-2 py-1 text-xs font-semibold border"
              :class="remainingClass(row.days_remaining)"
            >
              {{ remainingLabel(row.days_remaining) }}
            </span>
          </div>

          <dl class="mt-3 grid grid-cols-2 gap-x-4 gap-y-1 text-xs text-[var(--text-secondary)]">
            <div>
              <dt class="inline">{{ $t('fleet.expires') }}:</dt>
              <dd class="inline ms-1">{{ formatDate(row.trial_expires_at) }}</dd>
            </div>
            <div>
              <dt class="inline">{{ $t('fleet.status') }}:</dt>
              <dd class="inline ms-1">
                {{ row.deployment ? $t(`fleet.statuses.${row.deployment.status}`) : $t('fleet.noStack') }}
              </dd>
            </div>
            <div>
              <dt class="inline">{{ $t('fleet.plan') }}:</dt>
              <dd class="inline ms-1">{{ $t(`programmerHub.plans.${row.plan}`) }}</dd>
            </div>
            <div>
              <dt class="inline">{{ $t('fleet.reminded') }}:</dt>
              <dd class="inline ms-1">
                {{ row.trial_expiry_notified_at ? formatDate(row.trial_expiry_notified_at) : '—' }}
              </dd>
            </div>
          </dl>

          <div class="mt-3 flex flex-wrap gap-2">
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-[var(--border-card)] text-[var(--text-secondary)]"
              :disabled="busyId === row.id"
              @click="extend(row)"
            >
              <i class="fas fa-clock me-1" />{{ $t('fleet.extend', { days: extendDays }) }}
            </button>
            <button
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-amber-500/40 bg-amber-500/20 text-amber-400"
              :disabled="busyId === row.id"
              @click="openConvert(row)"
            >
              <i class="fas fa-arrow-right me-1" />{{ $t('fleet.convert') }}
            </button>
            <button
              v-if="!row.deployment || row.deployment.status === 'failed'"
              type="button"
              class="px-3 py-1.5 rounded-lg text-xs font-medium border border-[var(--border-card)] text-[var(--text-secondary)]"
              :disabled="busyId === row.id"
              @click="provision(row)"
            >
              <i class="fas fa-server me-1" />{{ $t('fleet.provision') }}
            </button>
          </div>
        </BaseCard>
      </div>
    </template>

    <!-- Licensed customers: their installs are isolated, so this is check-in data only. -->
    <template v-else>
      <div v-if="!deployments.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
        {{ $t('fleet.noDeployments') }}
      </div>
      <div v-else class="card-luxury p-0 overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="text-start text-xs uppercase text-[var(--text-secondary)]">
              <th class="p-3 text-start">{{ $t('fleet.customer') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.domain') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.plan') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.renews') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.lastCheckin') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.version') }}</th>
              <th class="p-3 text-start">{{ $t('fleet.license') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="row in deployments"
              :key="row.id"
              class="border-t border-[var(--border-card)]"
            >
              <td class="p-3">
                <p class="text-[var(--text-primary)]">{{ row.exchange_name || row.customer_name }}</p>
                <p class="text-xs text-[var(--text-secondary)]">{{ row.customer_username }}</p>
              </td>
              <td class="p-3 text-[var(--text-secondary)]">{{ row.domain }}</td>
              <td class="p-3 text-[var(--text-secondary)]">{{ $t(`programmerHub.plans.${row.plan}`) }}</td>
              <td class="p-3 text-[var(--text-secondary)]">{{ formatDate(row.renews_at) }}</td>
              <td class="p-3" :class="checkinClass(row.last_checkin_at)">
                {{ row.last_checkin_at ? formatDate(row.last_checkin_at) : $t('fleet.neverCheckedIn') }}
              </td>
              <td class="p-3 text-[var(--text-secondary)]">{{ row.installed_version || '—' }}</td>
              <td class="p-3">
                <code class="text-xs text-[var(--text-secondary)]">{{ row.license_key }}</code>
                <button
                  type="button"
                  class="ms-2 px-2 py-1 rounded-lg text-xs border border-[var(--border-card)] text-[var(--text-secondary)]"
                  :disabled="busyId === row.id"
                  @click="reissue(row)"
                >
                  <i class="fas fa-rotate me-1" />{{ $t('fleet.reissue') }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <BaseModal v-model="convertOpen" :title="$t('fleet.convertTitle')">
      <p class="text-sm text-[var(--text-secondary)] mb-4">{{ $t('fleet.convertHint') }}</p>
      <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2" for="fleet-domain">
        {{ $t('fleet.domain') }}
      </label>
      <input
        id="fleet-domain"
        v-model="convertDomain"
        type="text"
        class="input-luxury w-full"
        placeholder="panel.customer.example"
        @keyup.enter="submitConvert"
      />
      <div class="mt-6 flex justify-end gap-2">
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-[var(--border-card)] text-[var(--text-secondary)]"
          @click="convertOpen = false"
        >
          {{ $t('common.cancel') }}
        </button>
        <button
          type="button"
          class="px-4 py-2 rounded-lg text-sm border border-amber-500/40 bg-amber-500/20 text-amber-400"
          :disabled="!convertDomain.trim() || converting"
          @click="submitConvert"
        >
          {{ $t('fleet.convert') }}
        </button>
      </div>
    </BaseModal>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { fleetApi, getApiErrorDetails } from '@/services/api'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseModal from '@/components/ui/BaseModal.vue'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const STALE_CHECKIN_HOURS = 48
const extendDays = 14

const { t, locale } = useI18n()
const toast = useToast()

const tabs = ['trials', 'licensed']
const tab = ref('trials')
const loading = ref(true)
const busyId = ref(null)
const trials = ref([])
const deployments = ref([])

const convertOpen = ref(false)
const converting = ref(false)
const convertDomain = ref('')
const convertRow = ref(null)

function formatDate(value) {
  if (!value) return '—'
  return new Date(value).toLocaleDateString(locale.value, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

function remainingLabel(days) {
  if (days == null) return '—'
  if (days < 0) return t('fleet.lapsed')
  if (days === 0) return t('fleet.expiresToday')
  return t('fleet.daysLeft', { days })
}

function remainingClass(days) {
  if (days == null || days < 0) return 'bg-red-500/20 text-red-400 border-red-500/40'
  if (days <= 3) return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  return 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40'
}

function checkinClass(value) {
  if (!value) return 'text-red-400'
  const hours = (Date.now() - new Date(value).getTime()) / 3_600_000
  return hours > STALE_CHECKIN_HOURS ? 'text-amber-400' : 'text-[var(--text-secondary)]'
}

function unwrap(data) {
  return Array.isArray(data) ? data : (data?.results ?? [])
}

async function load() {
  loading.value = true
  try {
    if (tab.value === 'trials') {
      const { data } = await fleetApi.trials()
      trials.value = unwrap(data)
    } else {
      const { data } = await fleetApi.deployments()
      deployments.value = unwrap(data)
    }
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    loading.value = false
  }
}

async function extend(row) {
  busyId.value = row.id
  try {
    const { data } = await fleetApi.extendTrial(row.id, { days: extendDays })
    trials.value = trials.value.map((r) => (r.id === row.id ? data : r))
    toast.success(t('fleet.extended', { days: extendDays }))
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

async function provision(row) {
  busyId.value = row.id
  try {
    await fleetApi.provisionTrial(row.id)
    toast.success(t('fleet.provisionQueued'))
    await load()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

function openConvert(row) {
  convertRow.value = row
  convertDomain.value = ''
  convertOpen.value = true
}

async function submitConvert() {
  if (!convertDomain.value.trim()) return
  converting.value = true
  try {
    const { data } = await fleetApi.convertTrial(convertRow.value.id, {
      domain: convertDomain.value.trim(),
    })
    convertOpen.value = false
    toast.success(t('fleet.converted', { key: data.license_key }))
    await load()
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    converting.value = false
  }
}

async function reissue(row) {
  busyId.value = row.id
  try {
    const { data } = await fleetApi.reissueLicense(row.id)
    deployments.value = deployments.value.map((r) => (r.id === row.id ? data : r))
    toast.success(t('fleet.reissued'))
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    busyId.value = null
  }
}

watch(tab, load)
onMounted(load)
</script>
