<template>
  <section id="top" class="ws-section ws-hero-stacked">
    <WsBackground />
    <div class="ws-container">
      <div class="ws-hero-stacked__top">
        <div class="ws-stack">
          <p v-if="eyebrow" class="ws-eyebrow">{{ eyebrow }}</p>
          <h1 class="ws-display">{{ title }}</h1>
        </div>
        <div class="ws-stack ws-hero-stacked__aside">
          <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
          <div v-if="primaryLabel || secondaryLabel" class="ws-actions">
            <WsButton v-if="primaryLabel" :href="content.primary_cta_href">{{ primaryLabel }}</WsButton>
            <WsButton v-if="secondaryLabel" ghost :href="content.secondary_cta_href">{{ secondaryLabel }}</WsButton>
          </div>
        </div>
      </div>

      <WsImage v-if="content.image" :src="content.image" :alt="imageAlt" class="ws-hero-stacked__shot" />

      <ul v-if="badges.length" class="ws-hero-stacked__badges">
        <li v-for="(badge, i) in badges" :key="i">
          <i v-if="badge.icon" :class="`fas fa-${badge.icon}`" aria-hidden="true" />
          {{ t(badge.label) }}
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup>
import WsBackground from '../../primitives/WsBackground.vue'
import WsButton from '../../primitives/WsButton.vue'
import WsImage from '../../primitives/WsImage.vue'
import { useHero } from './_hero.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t, eyebrow, title, subtitle, primaryLabel, secondaryLabel, imageAlt, badges } = useHero(props)
</script>

<style scoped>
.ws-hero-stacked {
  padding-block: calc(var(--ws-section-gap) * 1.05);
}

.ws-hero-stacked__top {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr);
  gap: calc(var(--ws-block-gap) * 1.4);
  align-items: end;
}

.ws-hero-stacked__shot {
  margin-top: calc(var(--ws-block-gap) * 1.6);
  aspect-ratio: 21 / 9;
}

.ws-hero-stacked__badges {
  list-style: none;
  margin: calc(var(--ws-block-gap) * 1.2) 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 14px 40px;
  border-top: 1px solid var(--ws-border);
  padding-top: 22px;
}

.ws-hero-stacked__badges li {
  display: inline-flex;
  align-items: center;
  gap: 0.6em;
  color: var(--ws-text-muted);
  font-weight: 500;
}

.ws-hero-stacked__badges i {
  color: var(--ws-primary);
}

@container ws (max-width: 900px) {
  .ws-hero-stacked__top {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
