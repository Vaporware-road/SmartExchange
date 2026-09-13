<template>
  <WsSection anchor="steps" :title="t(content.title)" :subtitle="t(content.subtitle)" center alt>
    <ol class="ws-grid ws-steps-cards" :style="{ '--ws-cols': cols }">
      <li v-for="(item, i) in items" :key="i" class="ws-card">
        <span class="ws-steps-cards__num ws-num">{{ String(i + 1).padStart(2, '0') }}</span>
        <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
        <p class="ws-body">{{ t(item.body) }}</p>
      </li>
    </ol>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
const cols = computed(() => Math.min(items.value.length || 3, 4))
</script>

<style scoped>
.ws-steps-cards {
  list-style: none;
  margin: 0;
  padding: 0;
}

.ws-steps-cards li {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ws-steps-cards__num {
  font-family: var(--ws-font-heading);
  font-size: 2rem;
  font-weight: var(--ws-heading-weight);
  color: color-mix(in srgb, var(--ws-primary) 60%, transparent);
  line-height: 1;
}
</style>
