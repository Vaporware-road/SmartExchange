<template>
  <WsSection anchor="gallery" :title="t(content.title)" center>
    <div class="ws-masonry">
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
/* CSS columns rather than a grid: a masonry wall should keep each image's own
   proportions, which a row-based grid cannot do without cropping. */
.ws-masonry {
  columns: 3;
  column-gap: var(--ws-block-gap);
}

.ws-masonry figure {
  margin: 0 0 var(--ws-block-gap);
  break-inside: avoid;
  border-radius: var(--ws-radius);
  overflow: hidden;
  border: 1px solid var(--ws-border);
  background: var(--ws-surface);
}

.ws-masonry img {
  width: 100%;
}

figcaption {
  padding: 10px 14px;
  font-size: 0.85rem;
  color: var(--ws-text-muted);
}

@container ws (max-width: 900px) {
  .ws-masonry {
    columns: 2;
  }
}

@container ws (max-width: 560px) {
  .ws-masonry {
    columns: 1;
  }
}
</style>
