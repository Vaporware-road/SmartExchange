<template>
  <BaseModal
    :model-value="modelValue"
    :title="$t('orders.detailTitle')"
    :aria-label="$t('orders.detailTitle')"
    panel-class="max-w-2xl"
    @update:model-value="$emit('update:modelValue', $event)"
  >
    <div v-if="order" class="space-y-6">
      <section>
        <h3 class="text-sm font-semibold text-gold mb-3 flex items-center gap-2">
          <i class="fas fa-info-circle" />
          {{ $t('orders.sectionStatus') }}
        </h3>
        <dl class="detail-grid">
          <DetailRow :label="$t('common.status')" :value="$t(`orders.status.${order.status}`)" />
          <DetailRow :label="$t('orders.platform')" :value="platformLabel" />
          <DetailRow :label="$t('common.date')" :value="formatDate(order.created_at)" />
          <DetailRow v-if="order.reviewed_at" :label="$t('orders.reviewedAt')" :value="formatDate(order.reviewed_at)" />
        </dl>
      </section>

      <section>
        <h3 class="text-sm font-semibold text-gold mb-3 flex items-center gap-2">
          <i class="fas fa-user" />
          {{ $t('orders.sectionCustomer') }}
        </h3>
        <dl class="detail-grid">
          <DetailRow :label="$t('common.name')" :value="order.customer_name || '—'" />
          <DetailRow
            v-if="order.contact_phone || order.customer_phone"
            :label="$t('webapp.customerPhone')"
            :value="order.contact_phone || order.customer_phone"
            dir="ltr"
          />
          <DetailRow
            v-if="order.telegram_chat_id"
            :label="$t('orders.telegramChatId')"
            :value="String(order.telegram_chat_id)"
            dir="ltr"
          />
          <DetailRow
            v-if="telegramUsername"
            :label="$t('orders.telegramUsername')"
            :value="telegramUsername"
            dir="ltr"
          />
          <DetailRow
            v-if="order.customer_uuid"
            :label="$t('orders.customerId')"
            :value="order.customer_uuid"
            dir="ltr"
            mono
          />
        </dl>
      </section>

      <section>
        <h3 class="text-sm font-semibold text-gold mb-3 flex items-center gap-2">
          <i class="fas fa-shopping-cart" />
          {{ $t('orders.sectionOrder') }}
        </h3>
        <dl class="detail-grid">
          <DetailRow
            :label="$t('webapp.tradeType')"
            :value="order.trade_type === 'buy' ? $t('webapp.buy') : $t('webapp.sell')"
          />
          <DetailRow :label="$t('common.category')" :value="order.category_name" />
          <DetailRow
            v-if="order.price_type_name"
            :label="$t('webapp.priceType')"
            :value="order.price_type_name"
          />
          <DetailRow
            :label="$t('webapp.amount')"
            :value="amountLabel"
            dir="ltr"
          />
          <DetailRow
            v-if="order.customer_note"
            :label="$t('webapp.note')"
            :value="order.customer_note"
          />
        </dl>
      </section>

      <section v-if="extraMetadataRows.length">
        <h3 class="text-sm font-semibold text-gold mb-3 flex items-center gap-2">
          <i class="fas fa-database" />
          {{ $t('orders.sectionMetadata') }}
        </h3>
        <dl class="detail-grid">
          <DetailRow
            v-for="row in extraMetadataRows"
            :key="row.key"
            :label="row.label"
            :value="row.value"
            :dir="row.dir"
            :mono="row.mono"
          />
        </dl>
      </section>

      <section v-if="order.status === 'pending'">
        <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
          {{ $t('orders.adminNote') }}
        </label>
        <textarea
          v-model="adminNote"
          class="input-luxury w-full min-h-[80px]"
          rows="3"
          :placeholder="$t('orders.adminNotePlaceholder')"
        />
        <div class="flex flex-wrap gap-2 mt-4">
          <button
            type="button"
            class="btn-luxury flex-1 min-w-[120px]"
            :disabled="reviewing"
            @click="$emit('review', { order, status: 'approved', admin_note: adminNote })"
          >
            <i class="fas fa-check me-2" />
            {{ $t('orders.approve') }}
          </button>
          <button
            type="button"
            class="px-4 py-2.5 rounded-xl border text-sm flex-1 min-w-[120px] border-red-500/40 text-red-400 hover:bg-red-500/10 transition"
            :disabled="reviewing"
            @click="$emit('review', { order, status: 'rejected', admin_note: adminNote })"
          >
            <i class="fas fa-times me-2" />
            {{ $t('orders.reject') }}
          </button>
        </div>
      </section>

      <section v-else-if="order.admin_note">
        <h3 class="text-sm font-semibold text-gold mb-2">{{ $t('orders.adminNote') }}</h3>
        <p class="text-sm opacity-80">{{ order.admin_note }}</p>
      </section>

      <section class="pt-2 border-t" style="border-color: var(--border-card);">
        <button
          type="button"
          class="w-full px-4 py-2.5 rounded-xl border text-sm border-red-500/40 text-red-400 hover:bg-red-500/10 transition"
          :disabled="reviewing || deleting"
          @click="$emit('delete', order)"
        >
          <i class="fas fa-trash-alt me-2" />
          {{ $t('orders.deleteOrder') }}
        </button>
      </section>
    </div>
  </BaseModal>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import BaseModal from '@/components/ui/BaseModal.vue'
import DetailRow from '@/components/orders/OrderDetailRow.vue'

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  order: { type: Object, default: null },
  reviewing: { type: Boolean, default: false },
  deleting: { type: Boolean, default: false },
})

defineEmits(['update:modelValue', 'review', 'delete'])

const { t } = useI18n()
const adminNote = ref('')

watch(
  () => props.order,
  (o) => {
    adminNote.value = o?.admin_note || ''
  },
  { immediate: true },
)

const platformLabel = computed(() => {
  const map = {
    telegram: t('orders.platformTelegram'),
    whatsapp: t('orders.platformWhatsapp'),
    web: t('orders.platformWeb'),
  }
  return map[props.order?.platform] || props.order?.platform || '—'
})

const telegramUsername = computed(() => {
  const u =
    props.order?.customer_username ||
    props.order?.source_metadata?.telegram_username
  if (!u) return null
  return u.startsWith('@') ? u : `@${u}`
})

const amountLabel = computed(() => {
  if (!props.order) return '—'
  const code = props.order.currency_code ? ` ${props.order.currency_code}` : ''
  return `${props.order.amount}${code}`
})

const METADATA_LABELS = {
  source: 'orders.metaSource',
  customer_name: 'common.name',
  customer_phone: 'webapp.customerPhone',
  telegram_chat_id: 'orders.telegramChatId',
  telegram_username: 'orders.telegramUsername',
  user_agent: 'orders.metaUserAgent',
}

const SKIP_METADATA_KEYS = new Set([
  'customer_name',
  'customer_phone',
  'telegram_chat_id',
  'telegram_username',
])

const extraMetadataRows = computed(() => {
  const meta = props.order?.source_metadata
  if (!meta || typeof meta !== 'object') return []
  return Object.entries(meta)
    .filter(([key, value]) => value != null && value !== '' && !SKIP_METADATA_KEYS.has(key))
    .map(([key, value]) => ({
      key,
      label: METADATA_LABELS[key] ? t(METADATA_LABELS[key]) : key,
      value: typeof value === 'object' ? JSON.stringify(value) : String(value),
      dir: key.includes('phone') || key.includes('id') ? 'ltr' : undefined,
      mono: key === 'user_agent',
    }))
})

function formatDate(iso) {
  if (!iso) return '—'
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}
</script>

<style scoped>
.detail-grid {
  display: grid;
  gap: 0.5rem;
}
</style>
