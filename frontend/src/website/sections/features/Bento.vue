<template>
  <WsSection anchor="features" :title="t(content.title)" :subtitle="t(content.subtitle)" alt>
    <div class="ws-bento">
      <article
        v-for="(item, i) in items"
        :key="i"
        class="ws-card ws-bento__tile"
        :class="{ 'ws-bento__tile--wide': isWide(i) }"
      >
        <WsIcon v-if="item.icon" :name="item.icon" />
        <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
        <p class="ws-body">{{ t(item.body) }}</p>
        <WsImage v-if="item.image" :src="item.image" :alt="t(item.title)" class="ws-bento__shot" />
      </article>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsIcon from '../../primitives/WsIcon.vue'
import WsImage from '../../primitives/WsImage.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])

/* First and fourth run wide, which is what gives a bento its uneven look
   without asking the owner to think about grid spans. */
function isWide(index) {
  return index % 3 === 0
}
</script>

<style scoped>
.ws-bento {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--ws-block-gap);
}

.ws-bento__tile {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ws-bento__tile--wide {
  grid-column: span 2;
}

.ws-bento__shot {
  margin-top: auto;
  aspect-ratio: 16 / 9;
}

@container ws (max-width: 900px) {
  .ws-bento {
    grid-template-columns: minmax(0, 1fr);
  }
  .ws-bento__tile--wide {
    grid-column: auto;
  }
}
</style>
