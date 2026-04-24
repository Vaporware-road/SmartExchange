<template>
  <div
    class="flex h-full w-full flex-col gap-1 overflow-hidden rounded-md p-2"
    :style="panelStyle"
  >
    <div class="text-center text-xs font-semibold uppercase tracking-wide" :style="{ color: headerTextColor }">
      {{ title }}
    </div>
    <div class="grid flex-1 gap-1 overflow-auto" :style="gridStyle">
      <div
        v-for="(row, i) in rows"
        :key="i"
        class="flex items-center justify-between gap-2 rounded px-2 py-1 text-sm"
        :style="rowStyle"
      >
        <span class="truncate font-medium" :style="{ color: labelColor }">{{ row.label }}</span>
        <span class="inline-flex shrink-0 items-center gap-1 font-mono" :style="{ color: priceColor }">
          <i :class="trendIcon(row)" :style="{ color: trendColor(row) }" />
          <span>{{ row.price }}</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  widget: { type: Object, required: true },
})

const style = computed(() => props.widget?.style || {})

const title = computed(() => style.value.title || 'Prices')

const panelStyle = computed(() => ({
  background: style.value.panelBg ?? 'rgba(15,23,42,0.92)',
  border: `1px solid ${style.value.borderColor ?? 'rgba(212,175,55,0.35)'}`,
}))
const headerTextColor = computed(() => style.value.headerColor ?? '#e2e8f0')
const labelColor = computed(() => style.value.labelColor ?? '#f1f5f9')
const priceColor = computed(() => style.value.priceColor ?? '#f8fafc')

const gridStyle = computed(() => ({
  gridTemplateColumns: `repeat(${Math.max(1, Number(style.value.columns) || 1)}, minmax(0, 1fr))`,
}))

const rowStyle = computed(() => ({
  background: style.value.rowBg ?? 'rgba(30,41,59,0.9)',
}))

function trendOf(row) {
  const trend = String(row?.trend || '').toLowerCase()
  if (trend === 'up' || trend === 'down') return trend
  return 'flat'
}
function trendIcon(row) {
  const trend = trendOf(row)
  if (trend === 'up') return 'fas fa-arrow-trend-up'
  if (trend === 'down') return 'fas fa-arrow-trend-down'
  return 'fas fa-minus'
}
function trendColor(row) {
  const trend = trendOf(row)
  if (trend === 'up') return '#10b981'
  if (trend === 'down') return '#ef4444'
  return '#94a3b8'
}

const rows = computed(() => {
  const rowsRaw = style.value.rows
  if (Array.isArray(rowsRaw) && rowsRaw.length) return rowsRaw
  const mock = style.value.mockRows
  if (Array.isArray(mock) && mock.length) return mock
  return [
    { label: 'USDT / IRR', price: '58,200', trend: 'up' },
    { label: 'EUR / IRR', price: '72,400', trend: 'down' },
    { label: 'GBP / IRR', price: '84,100', trend: 'up' },
  ]
})
</script>
