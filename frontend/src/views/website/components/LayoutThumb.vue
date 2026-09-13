<template>
  <span class="wb-thumb" :style="style" :data-chrome="layout.chrome">
    <span class="wb-thumb__nav" :data-variant="layout.defaults.header" />
    <span class="wb-thumb__hero" :data-variant="layout.defaults.hero" />
    <span class="wb-thumb__rates" :data-variant="layout.defaults.rates" />
    <span class="wb-thumb__rows"><i /><i /><i /></span>
  </span>
</template>

<script setup>
import { computed } from 'vue'

/**
 * A wireframe of what a layout actually arranges, painted in that layout's
 * default theme colours.
 *
 * Drawn rather than screenshotted so adding a layout needs no image pipeline
 * and no stale PNG when a design is tweaked.
 */
const props = defineProps({
  layout: { type: Object, required: true },
  theme: { type: Object, default: null },
})

const style = computed(() => {
  const tokens = props.theme?.tokens || {}
  return {
    '--t-bg': tokens['--ws-bg'] || '#111',
    '--t-surface': tokens['--ws-surface'] || '#222',
    '--t-primary': tokens['--ws-primary'] || '#888',
    '--t-text': tokens['--ws-text-muted'] || '#666',
  }
})
</script>

<style scoped>
.wb-thumb {
  display: block;
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: 9px;
  overflow: hidden;
  background: var(--t-bg);
  padding: 7px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.wb-thumb__nav {
  height: 8px;
  border-radius: 3px;
  background: var(--t-surface);
  flex: none;
}

.wb-thumb__nav[data-variant='floating'] {
  border-radius: 999px;
  margin-inline: 14%;
}

.wb-thumb__nav[data-variant='centered'] {
  height: 12px;
}

.wb-thumb__hero {
  flex: 1.5;
  border-radius: 5px;
  background: linear-gradient(135deg, var(--t-primary), var(--t-surface));
  opacity: 0.9;
}

.wb-thumb__hero[data-variant='split-image'] {
  background: linear-gradient(90deg, var(--t-surface) 52%, var(--t-primary) 52%);
}

.wb-thumb__hero[data-variant='rates-first'] {
  background: linear-gradient(90deg, var(--t-primary) 46%, var(--t-surface) 46%);
}

.wb-thumb__hero[data-variant='centered'] {
  background: radial-gradient(circle at 50% 40%, var(--t-primary), var(--t-surface) 70%);
}

.wb-thumb__rates {
  flex: 1;
  border-radius: 5px;
  background: var(--t-surface);
  border: 1px solid color-mix(in srgb, var(--t-primary) 40%, transparent);
}

.wb-thumb__rates[data-variant='ticker'] {
  flex: 0 0 7px;
}

.wb-thumb__rows {
  display: flex;
  gap: 5px;
  flex: 0.8;
}

.wb-thumb__rows i {
  flex: 1;
  border-radius: 4px;
  background: var(--t-surface);
  opacity: 0.75;
}

/* The two chromes that are structurally different get their own silhouette. */
.wb-thumb[data-chrome='sidebar'] {
  padding-inline-start: 26%;
}

.wb-thumb[data-chrome='sidebar']::before {
  content: '';
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  width: 22%;
  background: var(--t-surface);
}

.wb-thumb[data-chrome='split'] .wb-thumb__hero {
  background: linear-gradient(90deg, var(--t-surface) 48%, var(--t-primary) 48%);
}
</style>
