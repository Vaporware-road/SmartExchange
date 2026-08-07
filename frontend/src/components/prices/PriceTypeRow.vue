<template>
  <article class="group grid grid-cols-[minmax(0,1fr)_auto_auto] gap-3 rounded-lg bg-[var(--bg-card)]/80 px-3 py-2.5 transition hover:bg-[var(--bg-hover)]">
    <div class="min-w-0">
      <p class="truncate text-sm font-semibold text-[var(--text-primary)]" :title="priceType.name">
        {{ priceType.name }}
      </p>
      <p class="truncate text-xs text-[var(--text-secondary)]">
        {{ sourceCode }} / {{ targetCode }} • {{ (priceType.slug || '').toUpperCase() || '—' }}
      </p>
    </div>

    <div class="justify-self-end text-right">
      <InlinePriceInput
        v-if="isEditing"
        :model-value="priceType.latest_price"
        :saving="saving"
        @save="(val) => $emit('save', val)"
        @cancel="$emit('cancel')"
      />
      <button
        v-else
        type="button"
        class="font-mono text-lg font-bold text-gold tabular-nums transition hover:text-yellow-300"
        :title="$t('common.edit')"
        @click="$emit('edit')"
      >
        {{ formattedPrice }}
      </button>
      <p class="mt-1 text-[11px] text-[var(--text-secondary)]">
        {{ relativeUpdatedAt }}
      </p>
    </div>

    <div class="flex items-center gap-2 justify-self-end self-center">
      <span class="rounded-full px-2 py-0.5 text-xs font-medium" :class="trendClass">
        <i class="fas mr-1" :class="trendIcon"></i>
        {{ trendText }}
      </span>
      <router-link
        :to="`/prices/category/${categoryId}/update`"
        class="opacity-100 md:opacity-0 md:group-hover:opacity-100 rounded-md border border-[var(--border-color)] px-2 py-1 text-xs text-[var(--text-secondary)] transition hover:text-gold"
      >
        <i class="fas fa-sliders-h"></i>
      </router-link>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import InlinePriceInput from '@/components/prices/InlinePriceInput.vue'
import { formatAppNumber, formatAppDecimal } from '@/utils/localeFormat.js'

const { locale } = useI18n()

const props = defineProps({
  categoryId: {
    type: [Number, String],
    required: true,
  },
  priceType: {
    type: Object,
    required: true,
  },
  isEditing: {
    type: Boolean,
    default: false,
  },
  saving: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['edit', 'save', 'cancel'])

const sourceCode = computed(() =>
  props.priceType?.source_currency?.code ?? props.priceType?.source_currency ?? '—'
)
const targetCode = computed(() =>
  props.priceType?.target_currency?.code ?? props.priceType?.target_currency ?? '—'
)

const appLoc = computed(() => (locale.value === 'fa' ? 'fa' : 'en'))

const formattedPrice = computed(() => {
  const value = Number(props.priceType?.latest_price)
  if (!Number.isFinite(value)) return '—'
  return formatAppNumber(appLoc.value, value, { maximumFractionDigits: 0 })
})

const changePercent = computed(() => {
  const value = Number(props.priceType?.change_percent)
  return Number.isFinite(value) ? value : null
})

const trendIcon = computed(() => {
  if (changePercent.value == null) return 'fa-minus'
  if (changePercent.value > 0) return 'fa-arrow-up'
  if (changePercent.value < 0) return 'fa-arrow-down'
  return 'fa-minus'
})

const trendClass = computed(() => {
  if (changePercent.value == null) return 'bg-slate-500/15 text-slate-700 dark:text-slate-300'
  if (changePercent.value > 0) return 'bg-emerald-500/15 text-emerald-300'
  if (changePercent.value < 0) return 'bg-rose-500/15 text-rose-300'
  return 'bg-slate-500/15 text-slate-700 dark:text-slate-300'
})

const trendText = computed(() => {
  if (changePercent.value == null) return '—'
  const sign = changePercent.value > 0 ? '+' : ''
  return `${sign}${formatAppDecimal(appLoc.value, changePercent.value, 1)}%`
})

const relativeUpdatedAt = computed(() => {
  const raw = props.priceType?.latest_price_at
  if (!raw) return '—'
  const date = new Date(raw)
  if (Number.isNaN(date.getTime())) return '—'
  const now = Date.now()
  const diffMs = Math.max(now - date.getTime(), 0)
  const diffMin = Math.floor(diffMs / 60000)
  const loc = appLoc.value
  if (loc === 'fa') {
    if (diffMin < 1) return 'همین الان'
    if (diffMin < 60) return `${formatAppNumber('fa', diffMin)} دقیقه پیش`
    const diffHours = Math.floor(diffMin / 60)
    if (diffHours < 24) return `${formatAppNumber('fa', diffHours)} ساعت پیش`
    const diffDays = Math.floor(diffHours / 24)
    return `${formatAppNumber('fa', diffDays)} روز پیش`
  }
  if (diffMin < 1) return 'Just now'
  if (diffMin < 60) return `${formatAppNumber('en', diffMin)}m ago`
  const diffHours = Math.floor(diffMin / 60)
  if (diffHours < 24) return `${formatAppNumber('en', diffHours)}h ago`
  const diffDays = Math.floor(diffHours / 24)
  return `${formatAppNumber('en', diffDays)}d ago`
})
</script>
