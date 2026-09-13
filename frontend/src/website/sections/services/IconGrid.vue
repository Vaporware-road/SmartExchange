<template>
  <WsSection anchor="services" :title="t(content.title)" :subtitle="t(content.subtitle)" center>
    <div class="ws-grid" :style="{ '--ws-cols': cols }">
      <component
        :is="item.href ? 'a' : 'div'"
        v-for="(item, i) in items"
        :key="i"
        :href="item.href || null"
        class="ws-service"
      >
        <WsIcon :name="item.icon" />
        <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
        <p class="ws-body">{{ t(item.body) }}</p>
      </component>
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
.ws-service {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 14px;
}
</style>
