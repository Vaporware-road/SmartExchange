<template>
  <WsSection :title="t(content.title)" center tight>
    <dl class="ws-grid" :style="{ '--ws-cols': cols }">
      <div v-for="(item, i) in items" :key="i" class="ws-card ws-stat-card">
        <dt class="ws-num">{{ item.value }}<span v-if="item.suffix">{{ item.suffix }}</span></dt>
        <dd>{{ t(item.label) }}</dd>
      </div>
    </dl>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
const cols = computed(() => Math.min(items.value.length || 4, 4))
</script>

<style scoped>
.ws-stat-card {
  text-align: center;
}

dl {
  margin: 0;
}

dt {
  font-family: var(--ws-font-heading);
  font-weight: var(--ws-heading-weight);
  color: var(--ws-heading);
  font-size: clamp(1.6rem, 1.2rem + 1.6cqi, 2.4rem);
}

dd {
  margin: 8px 0 0;
  color: var(--ws-text-muted);
  font-size: 0.9rem;
}
</style>
