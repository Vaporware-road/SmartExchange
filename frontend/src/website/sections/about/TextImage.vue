<template>
  <WsSection anchor="about">
    <div class="ws-split">
      <div class="ws-stack">
        <h2 v-if="t(content.title)" class="ws-h2">{{ t(content.title) }}</h2>
        <p v-if="body" class="ws-body">{{ body }}</p>
        <ul v-if="points.length" class="ws-points">
          <li v-for="(point, i) in points" :key="i">
            <i class="fas fa-check" aria-hidden="true" />{{ t(point.text) }}
          </li>
        </ul>
      </div>
      <WsImage :src="content.image" :alt="t(content.image_alt)" placeholder />
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsImage from '../../primitives/WsImage.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const body = computed(() => t(props.content.body))
const points = computed(() => props.content.points || [])
</script>

<style scoped>
.ws-points {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ws-points li {
  display: flex;
  align-items: flex-start;
  gap: 0.7em;
  color: var(--ws-text-muted);
}

.ws-points i {
  color: var(--ws-primary);
  margin-top: 0.35em;
  font-size: 0.85em;
}
</style>
