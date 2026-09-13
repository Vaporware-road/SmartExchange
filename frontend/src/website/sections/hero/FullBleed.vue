<template>
  <section id="top" class="ws-hero-full" :class="{ 'ws-hero-full--bare': !content.image }">
    <img v-if="content.image" class="ws-hero-full__bg" :src="content.image" :alt="imageAlt" />
    <div class="ws-hero-full__scrim" aria-hidden="true" />
    <div class="ws-container ws-hero-full__inner">
      <p v-if="eyebrow" class="ws-eyebrow">{{ eyebrow }}</p>
      <h1 class="ws-display">{{ title }}</h1>
      <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
      <div v-if="primaryLabel || secondaryLabel" class="ws-actions">
        <WsButton v-if="primaryLabel" :href="content.primary_cta_href">{{ primaryLabel }}</WsButton>
        <WsButton v-if="secondaryLabel" ghost :href="content.secondary_cta_href">{{ secondaryLabel }}</WsButton>
      </div>
    </div>
  </section>
</template>

<script setup>
import WsButton from '../../primitives/WsButton.vue'
import { useHero } from './_hero.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { eyebrow, title, subtitle, primaryLabel, secondaryLabel, imageAlt } = useHero(props)
</script>

<style scoped>
.ws-hero-full {
  position: relative;
  min-height: min(86dvh, 760px);
  display: grid;
  align-items: center;
  overflow: hidden;
  isolation: isolate;
}

.ws-hero-full__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -2;
}

/* Without this the headline is unreadable over a photo the owner chose. */
.ws-hero-full__scrim {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(
    100deg,
    color-mix(in srgb, var(--ws-bg) 92%, transparent),
    color-mix(in srgb, var(--ws-bg) 52%, transparent) 62%,
    color-mix(in srgb, var(--ws-bg) 24%, transparent)
  );
}

.ws-hero-full--bare {
  min-height: 0;
}

.ws-hero-full__inner {
  display: flex;
  flex-direction: column;
  gap: 22px;
  max-width: 720px;
  padding-block: calc(var(--ws-section-gap) * 0.9);
}
</style>
