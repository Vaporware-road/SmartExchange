<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between flex-wrap gap-3">
      <h1 class="text-2xl font-bold text-gold">{{ $t('orders.queueTitle') }}</h1>
      <button type="button" class="btn-luxury-outline" :disabled="loading" @click="loadOrders">
        <i class="fas fa-sync-alt" :class="{ 'fa-spin': loading }" />
        {{ $t('common.refresh') }}
      </button>
    </div>

    <div class="card-luxury space-y-3">
      <div class="flex items-start gap-3">
        <i class="fas fa-link text-gold mt-1" />
        <div class="flex-1 min-w-0">
          <h2 class="font-semibold text-gold">{{ $t('orders.customerLinkTitle') }}</h2>
          <p class="text-sm opacity-70 mt-1">{{ $t('orders.customerLinkHint') }}</p>
        </div>
      </div>
      <div class="flex flex-col sm:flex-row gap-2 sm:items-center">
        <code
          class="flex-1 text-xs sm:text-sm break-all rounded-xl border px-3 py-3 min-h-[48px] flex items-center"
          style="border-color: var(--glass-border); background: var(--bg-input);"
        >
          {{ customerOrderUrl }}
        </code>
        <button
          type="button"
          class="btn-luxury shrink-0 min-h-[48px] px-4"
          @click="copyCustomerLink"
        >
          <i class="fas fa-copy me-2" />
          {{ copyLabel }}
        </button>
        <a
          :href="customerOrderUrl"
          target="_blank"
          rel="noopener noreferrer"
          class="btn-luxury-outline shrink-0 min-h-[48px] px-4 inline-flex items-center justify-center"
        >
          <i class="fas fa-external-link-alt me-2" />
          {{ $t('orders.openLink') }}
        </a>
      </div>
    </div>

    <div class="flex gap-2 flex-wrap">
      <button
        v-for="f in statusFilters"
        :key="f.value"
        type="button"
        class="px-4 py-2 rounded-lg text-sm border transition"
        :class="statusFilter === f.value ? 'border-gold text-gold' : 'border-gray-600'"
        @click="setFilter(f.value)"
      >
        {{ f.label }}
      </button>
    </div>

    <div v-if="loading" class="flex justify-center py-12">
      <LoadingSpinner class="w-8 h-8" />
    </div>

    <div v-else-if="!orders.length" class="card-luxury text-center py-12 text-gray-400">
      {{ $t('orders.empty') }}
    </div>

    <div v-else class="space-y-4">
      <div
        v-for="order in orders"
        :key="order.uuid"
        class="card-luxury"
      >
        <div class="flex flex-wrap items-start justify-between gap-4">
          <div>
            <div class="flex items-center gap-2 mb-2">
              <span
                class="text-xs px-2 py-1 rounded"
                :class="statusClass(order.status)"
              >
                {{ $t(`orders.status.${order.status}`) }}
              </span>
              <span class="text-xs opacity-60">{{ order.platform }}</span>
            </div>
            <p class="font-medium">
              {{ order.trade_type === 'buy' ? $t('webapp.buy') : $t('webapp.sell') }}
              — {{ order.category_name }}
            </p>
            <p class="text-sm opacity-80 mt-1">
              {{ $t('webapp.amount') }}: {{ order.amount }}
              <span v-if="order.currency_code"> ({{ order.currency_code }})</span>
            </p>
            <p v-if="order.customer_name" class="text-sm opacity-70 mt-1">
              {{ order.customer_name }}
              <span v-if="order.contact_phone || order.customer_phone">
                — {{ order.contact_phone || order.customer_phone }}
              </span>
              <span v-else-if="order.telegram_chat_id" class="opacity-60">
                — TG: {{ order.telegram_chat_id }}
              </span>
            </p>
            <p v-if="order.customer_note" class="text-sm mt-2 opacity-70">
              {{ order.customer_note }}
            </p>
            <p class="text-xs opacity-50 mt-2">{{ formatDate(order.created_at) }}</p>
          </div>

          <button
            type="button"
            class="btn-luxury-outline shrink-0 min-h-[40px] px-4 text-sm"
            @click="openDetail(order)"
          >
            <i class="fas fa-eye me-2" />
            {{ $t('orders.viewDetails') }}
          </button>
        </div>
      </div>
    </div>

    <OrderIntakeDetailModal
      v-model="detailOpen"
      :order="selectedOrder"
      :reviewing="Boolean(reviewing)"
      :deleting="Boolean(deleting)"
      @review="onModalReview"
      @delete="onModalDelete"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import OrderIntakeDetailModal from '@/components/orders/OrderIntakeDetailModal.vue'
import { ordersApi, getApiErrorDetails } from '@/services/api'
import { useOrdersQueueStore } from '@/stores/ordersQueue'
import { useToast } from 'vue-toastification'

const { t } = useI18n()
const toast = useToast()
const ordersQueue = useOrdersQueueStore()

const loading = ref(false)
const reviewing = ref(null)
const deleting = ref(null)
const detailOpen = ref(false)
const selectedOrder = ref(null)
const orders = ref([])
const statusFilter = ref('pending')
const customerOrderUrl = ref('')
const copyLabel = ref(t('orders.copyLink'))

const statusFilters = [
  { value: 'pending', label: t('orders.status.pending') },
  { value: 'approved', label: t('orders.status.approved') },
  { value: 'rejected', label: t('orders.status.rejected') },
  { value: '', label: t('orders.status.all') },
]

function statusClass(status) {
  const map = {
    pending: 'bg-yellow-500/20 text-yellow-400',
    approved: 'bg-green-500/20 text-green-400',
    rejected: 'bg-red-500/20 text-red-400',
    cancelled: 'bg-gray-500/20 text-gray-400',
  }
  return map[status] || map.pending
}

function formatDate(iso) {
  if (!iso) return ''
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}

function setFilter(value) {
  statusFilter.value = value
  loadOrders()
}

async function loadOrders() {
  loading.value = true
  try {
    const params = statusFilter.value ? { status: statusFilter.value } : {}
    const { data } = await ordersApi.list(params)
    orders.value = data
  } catch (e) {
    toast.error(getApiErrorDetails(e).message)
  } finally {
    loading.value = false
  }
  ordersQueue.fetchPendingCount()
}

function openDetail(order) {
  selectedOrder.value = order
  detailOpen.value = true
}

async function onModalDelete(order) {
  if (!order) return
  const ok = window.confirm(t('orders.deleteConfirm', { name: order.customer_name || order.uuid }))
  if (!ok) return
  deleting.value = order.uuid
  try {
    await ordersApi.remove(order.uuid)
    toast.success(t('orders.deleteSuccess'))
    detailOpen.value = false
    selectedOrder.value = null
    await loadOrders()
    ordersQueue.fetchPendingCount()
  } catch (e) {
    toast.error(getApiErrorDetails(e).message || t('toast.serverError'))
  } finally {
    deleting.value = null
  }
}

async function onModalReview({ order, status, admin_note: adminNote }) {
  await review(order, status, adminNote)
  detailOpen.value = false
  selectedOrder.value = null
}

async function review(order, status, adminNote = '') {
  reviewing.value = order.uuid
  try {
    const payload = { status }
    if (adminNote?.trim()) payload.admin_note = adminNote.trim()
    await ordersApi.review(order.uuid, payload)
    toast.success(t('orders.reviewSuccess'))
    await loadOrders()
    ordersQueue.fetchPendingCount()
  } catch (e) {
    toast.error(getApiErrorDetails(e).message)
  } finally {
    reviewing.value = null
  }
}

async function loadIntakeLink() {
  try {
    const { data } = await ordersApi.intakeLink()
    customerOrderUrl.value = data.url || `${window.location.origin}/webapp/order`
  } catch {
    customerOrderUrl.value = `${window.location.origin}/webapp/order`
  }
}

async function copyCustomerLink() {
  if (!customerOrderUrl.value) return
  try {
    await navigator.clipboard.writeText(customerOrderUrl.value)
    copyLabel.value = t('orders.copied')
    setTimeout(() => {
      copyLabel.value = t('orders.copyLink')
    }, 2000)
  } catch {
    toast.error(t('orders.copyFailed'))
  }
}

onMounted(async () => {
  await loadIntakeLink()
  await loadOrders()
})
</script>
