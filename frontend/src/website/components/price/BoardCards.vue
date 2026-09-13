<template>
  <div class="ws-board-cards">
    <div v-for="group in groups" :key="group.id" class="ws-board-cards__group">
      <h3 v-if="showGroupNames" class="ws-h3 ws-board-cards__caption">{{ group.name }}</h3>
      <div class="ws-grid" :style="{ '--ws-cols': columns }">
        <article v-for="row in group.rows" :key="row.key" class="ws-card ws-card--hover ws-rate">
          <PricePair :row="row" :show-icon="config.show_currency_icons !== false" />
          <div class="ws-rate__quotes">
            <div v-if="row.buy" class="ws-rate__quote">
              <span class="ws-rate__label">{{ labels.buy }}</span>
              <PriceQuote :quote="row.buy" side="buy" v-bind="quoteProps" />
            </div>
            <div v-if="row.sell" class="ws-rate__quote">
              <span class="ws-rate__label">{{ labels.sell }}</span>
              <PriceQuote :quote="row.sell" side="sell" v-bind="quoteProps" />
            </div>
          </div>
          <p v-if="config.show_updated_at && row.updatedAt" class="ws-rate__time">
            {{ since(row.updatedAt) }}
          </p>
        </article>
      </div>
    </div>
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

const columns = computed(() => props.config.columns || 3)
const showGroupNames = computed(() => props.groups.length > 1)
const quoteProps = computed(() => ({ decimals: props.config.decimals ?? 2, locale: props.locale }))

function since(iso) {
  return formatUpdatedAt(iso, props.locale)
}
</script>

<style scoped>
.ws-board-cards {
  display: flex;
  flex-direction: column;
  gap: calc(var(--ws-block-gap) * 1.4);
}

.ws-board-cards__caption {
  margin-bottom: 16px;
}

.ws-rate {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ws-rate__quotes {
  display: flex;
  gap: 10px;
}

.ws-rate__quote {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 12px 14px;
  border-radius: var(--ws-radius-sm);
  background: var(--ws-surface-alt);
  border: 1px solid var(--ws-border);
}

.ws-rate__label {
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ws-text-muted);
}

.ws-rate__time {
  margin: 0;
  font-size: 0.78rem;
  color: var(--ws-text-muted);
}
</style>
