<template>
  <div class="ws-grid ws-board-grid" :style="{ '--ws-cols': columns }">
    <article v-for="row in rows" :key="row.key" class="ws-board-grid__tile">
      <PricePair :row="row" :show-icon="config.show_currency_icons !== false" />
      <div class="ws-board-grid__values">
        <PriceQuote v-if="row.buy" :quote="row.buy" side="buy" v-bind="quoteProps" />
        <span v-if="row.buy && row.sell" class="ws-board-grid__sep">/</span>
        <PriceQuote v-if="row.sell" :quote="row.sell" side="sell" v-bind="quoteProps" />
      </div>
      <span v-if="config.show_updated_at && row.updatedAt" class="ws-board-grid__time">
        {{ since(row.updatedAt) }}
      </span>
    </article>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import PricePair from './PricePair.vue'
import PriceQuote from './PriceQuote.vue'
import { formatUpdatedAt } from '../../composables/useSitePrices.js'

const props = defineProps({
  groups: { type: Array, default: () => [] },
  config: { type: Object, default: () => ({}) },
  labels: { type: Object, required: true },
  locale: { type: String, default: 'en' },
})

/* A grid reads as one flat board, so the category split is dropped here. */
const rows = computed(() => props.groups.flatMap((group) => group.rows))
const columns = computed(() => props.config.columns || 4)
const quoteProps = computed(() => ({ decimals: props.config.decimals ?? 2, locale: props.locale }))

function since(iso) {
  return formatUpdatedAt(iso, props.locale)
}
</script>

<style scoped>
.ws-board-grid__tile {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 20px;
  border-radius: var(--ws-radius);
  border: 1px solid var(--ws-border);
  background: var(--ws-surface);
  transition: border-color 0.2s ease, transform 0.2s ease;
}

.ws-board-grid__tile:hover {
  border-color: var(--ws-primary);
  transform: translateY(-3px);
}

.ws-board-grid__values {
  display: flex;
  align-items: baseline;
  gap: 0.5em;
  flex-wrap: wrap;
}

.ws-board-grid__sep {
  color: var(--ws-border-strong);
}

.ws-board-grid__time {
  font-size: 0.76rem;
  color: var(--ws-text-muted);
}
</style>
