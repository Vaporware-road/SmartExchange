<template>
  <div class="ws-board-table">
    <div v-for="group in groups" :key="group.id" class="ws-board-table__group">
      <h3 v-if="showGroupNames" class="ws-h3 ws-board-table__caption">{{ group.name }}</h3>
      <div class="ws-board-table__scroll">
        <table>
          <thead>
            <tr>
              <th scope="col">{{ labels.currency }}</th>
              <th v-if="twoSided" scope="col" class="ws-t-end">{{ labels.buy }}</th>
              <th v-if="twoSided" scope="col" class="ws-t-end">{{ labels.sell }}</th>
              <th v-else scope="col" class="ws-t-end">{{ labels.price }}</th>
              <th v-if="config.show_updated_at" scope="col" class="ws-t-end">{{ labels.updated }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in group.rows" :key="row.key">
              <td><PricePair :row="row" :show-icon="config.show_currency_icons !== false" /></td>
              <template v-if="twoSided">
                <td class="ws-t-end"><PriceQuote :quote="row.buy" side="buy" v-bind="quoteProps" /></td>
                <td class="ws-t-end"><PriceQuote :quote="row.sell" side="sell" v-bind="quoteProps" /></td>
              </template>
              <td v-else class="ws-t-end">
                <PriceQuote :quote="row.buy || row.sell" v-bind="quoteProps" />
              </td>
              <td v-if="config.show_updated_at" class="ws-t-end ws-board-table__time">
                {{ since(row.updatedAt) }}
              </td>
            </tr>
          </tbody>
        </table>
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

const twoSided = computed(
  () => props.config.show_buy_sell !== false && props.groups.some((g) => g.rows.some((r) => r.buy && r.sell)),
)
const showGroupNames = computed(() => props.groups.length > 1)
const quoteProps = computed(() => ({ decimals: props.config.decimals ?? 2, locale: props.locale }))

function since(iso) {
  return formatUpdatedAt(iso, props.locale)
}
</script>

<style scoped>
.ws-board-table {
  display: flex;
  flex-direction: column;
  gap: calc(var(--ws-block-gap) * 1.2);
}

.ws-board-table__caption {
  margin-bottom: 12px;
}

/* Tables are the one thing allowed to scroll sideways on a phone. */
.ws-board-table__scroll {
  overflow-x: auto;
  border: 1px solid var(--ws-border);
  border-radius: var(--ws-radius);
  background: var(--ws-surface);
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 420px;
}

th {
  text-align: start;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ws-text-muted);
  padding: 14px 18px;
  border-bottom: 1px solid var(--ws-border);
  background: var(--ws-surface-alt);
  white-space: nowrap;
}

td {
  padding: 14px 18px;
  border-bottom: 1px solid var(--ws-border);
  vertical-align: middle;
}

tbody tr:last-child td {
  border-bottom: 0;
}

tbody tr:hover {
  background: color-mix(in srgb, var(--ws-primary) 6%, transparent);
}

.ws-t-end {
  text-align: end;
}

.ws-board-table__time {
  font-size: 0.8rem;
  color: var(--ws-text-muted);
  white-space: nowrap;
}
</style>
