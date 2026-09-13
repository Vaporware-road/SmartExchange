<template>
  <WsSection anchor="gallery" :title="t(content.title)" alt>
    <div class="ws-carousel" role="region" tabindex="0">
      <figure v-for="(item, i) in items" :key="i">
        <img :src="item.image" :alt="t(item.caption)" loading="lazy" decoding="async" />
        <figcaption v-if="t(item.caption)">{{ t(item.caption) }}</figcaption>
      </figure>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => (props.content.items || []).filter((item) => item.image))
</script>

<style scoped>
/* Native scroll-snap, so it works with a trackpad, a touch swipe and a keyboard
   without a carousel library or a single line of drag maths. */
.ws-carousel {
  display: flex;
  gap: var(--ws-block-gap);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding-bottom: 10px;
  scrollbar-width: thin;
}

.ws-carousel figure {
  margin: 0;
  flex: 0 0 clamp(260px, 34%, 420px);
  scroll-snap-align: start;
  border-radius: var(--ws-radius);
  overflow: hidden;
  border: 1px solid var(--ws-border);
  background: var(--ws-surface);
}

.ws-carousel img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

figcaption {
  padding: 10px 14px;
  font-size: 0.85rem;
  color: var(--ws-text-muted);
}
</style>
