<template>
  <div class="ws-board-featured" :class="{ 'ws-board-featured--solo': !rest.length }">
    <article v-if="lead" class="ws-card ws-board-featured__lead">
      <span class="ws-eyebrow">{{ labels.featured }}</span>
      <PricePair :row="lead" :show-icon="config.show_currency_icons !== false" />
      <div class="ws-board-featured__big">
        <div v-if="lead.buy" class="ws-board-featured__cell">
          <span class="ws-board-featured__label">{{ labels.buy }}</span>
          <PriceQuote :quote="lead.buy" side="buy" v-bind="quoteProps" />
        </div>
        <div v-if="lead.sell" class="ws-board-featured__cell">
          <span class="ws-board-featured__label">{{ labels.sell }}</span>
          <PriceQuote :quote="lead.sell" side="sell" v-bind="quoteProps" />
        </div>
      </div>
      <p v-if="config.show_updated_at && lead.updatedAt" class="ws-muted ws-board-featured__time">
        {{ labels.updated }} · {{ since(lead.updatedAt) }}
      </p>
    </article>

    <ul v-if="rest.length" class="ws-board-featured__rest">
      <li v-for="row in rest" :key="row.key">
        <PricePair :row="row" :show-icon="config.show_currency_icons !== false" />
        <span class="ws-board-featured__values">
          <PriceQuote v-if="row.buy" :quote="row.buy" side="buy" v-bind="quoteProps" />
          <PriceQuote v-if="row.sell" :quote="row.sell" side="sell" v-bind="quoteProps" />
        </span>
      </li>
    </ul>
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

const rows = computed(() => props.groups.flatMap((group) => group.rows))
/* The desk's headline pair leads; the rest queue beside it. */
const lead = computed(() => rows.value[0] || null)
const rest = computed(() => rows.value.slice(1, 9))
const quoteProps = computed(() => ({ decimals: props.config.decimals ?? 2, locale: props.locale }))

function since(iso) {
  return formatUpdatedAt(iso, props.locale)
}
</script>

<style scoped>
.ws-board-featured {
  display: grid;
  /* With only one pair to show there is no second column to fill. */
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: var(--ws-block-gap);
  align-items: start;
}

.ws-board-featured__lead {
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: calc(var(--ws-block-gap) * 1.2);
}

.ws-board-featured__big {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
}

.ws-board-featured__big :deep(.ws-quote) {
  font-size: clamp(1.6rem, 1.1rem + 1.8cqi, 2.6rem);
}

.ws-board-featured__cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ws-board-featured__label {
  font-size: 0.74rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ws-text-muted);
}

.ws-board-featured__time {
  font-size: 0.8rem;
  margin: 0;
}

.ws-board-featured__rest {
  list-style: none;
  margin: 0;
  padding: 0;
  border: 1px solid var(--ws-border);
  border-radius: var(--ws-radius);
  overflow: hidden;
  background: var(--ws-surface);
}

.ws-board-featured__rest li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--ws-border);
}

.ws-board-featured__rest li:last-child {
  border-bottom: 0;
}

.ws-board-featured__values {
  display: flex;
  gap: 16px;
  white-space: nowrap;
}

.ws-board-featured--solo {
  grid-template-columns: minmax(0, 1fr);
  max-width: 640px;
}

@container ws (max-width: 900px) {
  .ws-board-featured {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
