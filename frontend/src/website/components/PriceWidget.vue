<template>
  <div class="ws-widget">
    <div v-if="loading" class="ws-widget__state">
      <span class="ws-widget__spinner" aria-hidden="true" />
      <span>{{ labels.loading }}</span>
    </div>

    <p v-else-if="!groups.length" class="ws-widget__state ws-muted">
      {{ failed ? labels.unavailable : labels.empty }}
    </p>

    <template v-else>
      <component
        :is="board"
        :groups="groups"
        :config="config"
        :labels="labels"
        :locale="locale"
      />
      <p v-if="failed" class="ws-widget__stale">{{ labels.stale }}</p>
    </template>
  </div>
</template>

<script setup>
import { computed, toRef } from 'vue'
import { useI18n } from 'vue-i18n'
import BoardCards from './price/BoardCards.vue'
import BoardFeatured from './price/BoardFeatured.vue'
import BoardGrid from './price/BoardGrid.vue'
import BoardTable from './price/BoardTable.vue'
import BoardTicker from './price/BoardTicker.vue'
import { buildRateGroups, useSitePrices } from '../composables/useSitePrices.js'
import { useSiteContext } from '../composables/useSiteContext.js'

/**
 * The exchange-rate board, shared by every layout.
 *
 * One component, five looks, and no colours of its own: it inherits the site's
 * tokens like any other section, which is why a desk can change design without
 * the board suddenly clashing with the page around it.
 */
const props = defineProps({
  variant: { type: String, default: 'cards' },
  config: { type: Object, default: () => ({}) },
})

const BOARDS = {
  cards: BoardCards,
  table: BoardTable,
  ticker: BoardTicker,
  grid: BoardGrid,
  featured: BoardFeatured,
}

const { t: translate } = useI18n()
const { locale, accountSlug } = useSiteContext()

const { snapshot, loading, failed } = useSitePrices({
  accountSlug,
  refreshSeconds: computed(() => props.config.refresh_seconds ?? 60),
})

const board = computed(() => BOARDS[props.variant] || BoardCards)
const groups = computed(() => buildRateGroups(snapshot.value, props.config))

const labels = computed(() => ({
  buy: translate('website.widget.buy'),
  sell: translate('website.widget.sell'),
  price: translate('website.widget.price'),
  currency: translate('website.widget.currency'),
  updated: translate('website.widget.updated'),
  featured: translate('website.widget.featured'),
  loading: translate('website.widget.loading'),
  empty: translate('website.widget.empty'),
  unavailable: translate('website.widget.unavailable'),
  stale: translate('website.widget.stale'),
}))
</script>

<style scoped>
.ws-widget__state {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 48px 20px;
  color: var(--ws-text-muted);
  border: 1px dashed var(--ws-border);
  border-radius: var(--ws-radius);
  margin: 0;
}

.ws-widget__spinner {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2px solid var(--ws-border-strong);
  border-top-color: var(--ws-primary);
  animation: ws-spin 0.8s linear infinite;
}

.ws-widget__stale {
  margin: 12px 0 0;
  font-size: 0.8rem;
  color: var(--ws-text-muted);
  text-align: center;
}

@keyframes ws-spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
