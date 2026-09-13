<template>
  <span v-if="!quote" class="ws-quote ws-quote--empty">—</span>
  <span v-else class="ws-quote ws-num" :class="side ? `ws-quote--${side}` : null">
    <span class="ws-quote__value">{{ formatted }}</span>
    <span v-if="symbol" class="ws-quote__symbol">{{ symbol }}</span>
  </span>
</template>

<script setup>
import { computed } from 'vue'
import { formatPrice } from '../../composables/useSitePrices.js'

const props = defineProps({
  quote: { type: Object, default: null },
  decimals: { type: Number, default: 2 },
  locale: { type: String, default: 'en' },
  symbol: { type: String, default: '' },
  side: { type: String, default: '' },
})

const formatted = computed(() => formatPrice(props.quote?.price, props.decimals, props.locale))
</script>

<style scoped>
.ws-quote {
  display: inline-flex;
  align-items: baseline;
  gap: 0.28em;
  font-weight: 700;
  font-size: 1.05em;
  color: var(--ws-heading);
}

.ws-quote--buy {
  color: var(--ws-buy);
}

.ws-quote--sell {
  color: var(--ws-sell);
}

.ws-quote--empty {
  color: var(--ws-text-muted);
  font-weight: 500;
}

.ws-quote__symbol {
  font-size: 0.72em;
  font-weight: 500;
  color: var(--ws-text-muted);
}
</style>
