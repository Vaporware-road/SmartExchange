<template>
  <span
    v-if="displayCount"
    :class="[
      'inline-flex items-center justify-center font-bold leading-none text-white bg-sell',
      inline ? 'min-w-[1.25rem] h-5 px-1.5 text-[11px] rounded-full' : 'absolute -top-1.5 -end-1.5 min-w-[1.125rem] h-[1.125rem] px-1 text-[10px] rounded-full ring-2 ring-[var(--bg-navbar)]',
    ]"
    :aria-label="ariaLabel"
  >
    {{ displayCount }}
  </span>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useOrdersQueueStore } from '@/stores/ordersQueue'

defineProps({
  inline: { type: Boolean, default: false },
})

const { t } = useI18n()
const store = useOrdersQueueStore()

const displayCount = computed(() => {
  const n = store.pendingCount
  if (!n || n <= 0) return ''
  return n > 99 ? '99+' : String(n)
})

const ariaLabel = computed(() =>
  t('orders.pendingBadge', { count: store.pendingCount }),
)
</script>
