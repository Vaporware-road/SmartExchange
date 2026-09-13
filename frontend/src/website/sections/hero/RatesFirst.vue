<template>
  <section id="top" class="ws-section ws-hero-rates">
    <WsBackground />
    <div class="ws-container ws-hero-rates__inner">
      <div class="ws-stack ws-hero-rates__copy">
        <p v-if="eyebrow" class="ws-eyebrow">{{ eyebrow }}</p>
        <h1 class="ws-display">{{ title }}</h1>
        <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
        <div v-if="primaryLabel || secondaryLabel" class="ws-actions">
          <WsButton v-if="primaryLabel" :href="content.primary_cta_href">{{ primaryLabel }}</WsButton>
          <WsButton v-if="secondaryLabel" ghost :href="content.secondary_cta_href">{{ secondaryLabel }}</WsButton>
        </div>
      </div>
      <div class="ws-card ws-hero-rates__board">
        <PriceWidget variant="table" :config="ratesConfig" />
      </div>
    </div>
  </section>
</template>

<script setup>
import WsBackground from '../../primitives/WsBackground.vue'
import WsButton from '../../primitives/WsButton.vue'
import PriceWidget from '../../components/PriceWidget.vue'
import { useRatesConfig } from '../../composables/useRatesConfig.js'
import { useHero } from './_hero.js'

/** For desks whose rates *are* the pitch: the board opens the page. */
const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { eyebrow, title, subtitle, primaryLabel, secondaryLabel } = useHero(props)
const ratesConfig = useRatesConfig({ columns: 2, show_updated_at: true })
</script>

<style scoped>
.ws-hero-rates {
  padding-block: calc(var(--ws-section-gap) * 1.05);
}

.ws-hero-rates__inner {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: calc(var(--ws-block-gap) * 1.6);
  align-items: center;
}

.ws-hero-rates__board {
  padding: 10px;
}

@container ws (max-width: 960px) {
  .ws-hero-rates__inner {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
