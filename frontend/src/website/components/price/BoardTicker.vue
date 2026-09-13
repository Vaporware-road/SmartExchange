<template>
  <div class="ws-ticker" :class="{ 'ws-ticker--still': !animated }">
    <div class="ws-ticker__track" :style="trackStyle">
      <span v-for="(row, index) in marquee" :key="`${row.key}-${index}`" class="ws-ticker__item">
        <img v-if="iconFor(row)" class="ws-ticker__icon" :src="iconFor(row)" alt="" />
        <span class="ws-ticker__name">{{ row.name || `${row.from}/${row.to}` }}</span>
        <PriceQuote v-if="row.buy" :quote="row.buy" side="buy" v-bind="quoteProps" />
        <PriceQuote v-if="row.sell" :quote="row.sell" side="sell" v-bind="quoteProps" />
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import PriceQuote from './PriceQuote.vue'
import { getCurrencyIconByCode } from '@/utils/categoryIcons.js'

const props = defineProps({
  groups: { type: Array, default: () => [] },
  config: { type: Object, default: () => ({}) },
  labels: { type: Object, required: true },
  locale: { type: String, default: 'en' },
})

const rows = computed(() => props.groups.flatMap((group) => group.rows))
/* Doubled so the loop has something to scroll into; a single copy would gap. */
const marquee = computed(() => (rows.value.length ? [...rows.value, ...rows.value] : []))
const animated = computed(() => rows.value.length > 2)
const trackStyle = computed(() => ({ '--ws-ticker-duration': `${Math.max(rows.value.length * 5, 20)}s` }))
const quoteProps = computed(() => ({ decimals: props.config.decimals ?? 2, locale: props.locale }))

function iconFor(row) {
  return props.config.show_currency_icons === false ? null : getCurrencyIconByCode(row.from)
}
</script>

<style scoped>
.ws-ticker {
  overflow: hidden;
  border-block: 1px solid var(--ws-border);
  background: var(--ws-surface);
  padding-block: 14px;
  /* Fade the ends so items enter and leave instead of being sliced off. */
  mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent);
}

.ws-ticker__track {
  display: flex;
  gap: 44px;
  width: max-content;
  animation: ws-ticker-scroll var(--ws-ticker-duration, 30s) linear infinite;
}

.ws-ticker--still .ws-ticker__track {
  animation: none;
  width: 100%;
  justify-content: center;
}

.ws-ticker__item {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  white-space: nowrap;
}

.ws-ticker__icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
}

.ws-ticker__name {
  font-weight: 600;
  color: var(--ws-heading);
}

.ws-ticker:hover .ws-ticker__track {
  animation-play-state: paused;
}

@keyframes ws-ticker-scroll {
  from {
    transform: translateX(0);
  }
  to {
    /* Half, because the list is doubled — one full pass of the real items. */
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ws-ticker__track {
    animation: none;
  }
  .ws-ticker {
    overflow-x: auto;
  }
}
</style>
