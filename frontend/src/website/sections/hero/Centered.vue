<template>
  <section id="top" class="ws-section ws-hero">
    <WsBackground />
    <div class="ws-container ws-hero__inner">
      <p v-if="eyebrow" class="ws-eyebrow">{{ eyebrow }}</p>
      <h1 class="ws-display">{{ title }}</h1>
      <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
      <div v-if="primaryLabel || secondaryLabel" class="ws-actions ws-hero__actions">
        <WsButton v-if="primaryLabel" :href="content.primary_cta_href">{{ primaryLabel }}</WsButton>
        <WsButton v-if="secondaryLabel" ghost :href="content.secondary_cta_href">{{ secondaryLabel }}</WsButton>
      </div>
      <div v-if="badges.length" class="ws-actions ws-hero__actions">
        <span v-for="(badge, i) in badges" :key="i" class="ws-pill">
          <i v-if="badge.icon" :class="`fas fa-${badge.icon}`" aria-hidden="true" />
          {{ t(badge.label) }}
        </span>
      </div>
      <WsImage v-if="content.image" :src="content.image" :alt="imageAlt" :ratio="false" class="ws-hero__shot" />
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
.ws-hero {
  padding-block: calc(var(--ws-section-gap) * 1.2);
}

.ws-hero__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px;
}

.ws-hero__inner .ws-lead {
  margin-inline: auto;
}

.ws-hero__actions {
  justify-content: center;
}

.ws-hero__shot {
  margin-top: 26px;
  width: min(100%, 960px);
  box-shadow: var(--ws-shadow-lg);
}
</style>
