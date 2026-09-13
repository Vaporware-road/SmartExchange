<template>
  <WsSection anchor="features" :title="t(content.title)" :subtitle="t(content.subtitle)" center>
    <div class="ws-grid" :style="{ '--ws-cols': cols }">
      <article v-for="(item, i) in items" :key="i" class="ws-card ws-feature">
        <WsIcon :name="item.icon" />
        <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
        <p class="ws-body">{{ t(item.body) }}</p>
      </article>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsIcon from '../../primitives/WsIcon.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
const cols = computed(() => Math.min(items.value.length || 3, 3))
</script>

<style scoped>
.ws-feature {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
</style>
