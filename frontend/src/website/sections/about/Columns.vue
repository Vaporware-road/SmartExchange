<template>
  <WsSection anchor="about" :title="t(content.title)" alt>
    <div class="ws-about-cols">
      <p v-if="body" class="ws-body ws-about-cols__body">{{ body }}</p>
      <ul v-if="points.length" class="ws-grid" :style="{ '--ws-cols': 2 }">
        <li v-for="(point, i) in points" :key="i" class="ws-card">
          <i class="fas fa-circle-check" aria-hidden="true" />
          <span>{{ t(point.text) }}</span>
        </li>
      </ul>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const body = computed(() => t(props.content.body))
const points = computed(() => props.content.points || [])
</script>

<style scoped>
.ws-about-cols {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr);
  gap: calc(var(--ws-block-gap) * 1.4);
  align-items: start;
}

.ws-about-cols__body {
  font-size: 1.05rem;
}

.ws-about-cols ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.ws-about-cols li {
  display: flex;
  align-items: flex-start;
  gap: 0.8em;
}

.ws-about-cols i {
  color: var(--ws-primary);
  margin-top: 0.25em;
}

@container ws (max-width: 900px) {
  .ws-about-cols {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
