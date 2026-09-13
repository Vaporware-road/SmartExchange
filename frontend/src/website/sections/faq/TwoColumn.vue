<template>
  <WsSection anchor="faq" :title="t(content.title)" :subtitle="t(content.subtitle)" alt>
    <div class="ws-grid" :style="{ '--ws-cols': 2 }">
      <div v-for="(item, i) in items" :key="i" class="ws-faq2">
        <h3 v-if="t(item.question)" class="ws-h3">{{ t(item.question) }}</h3>
        <p class="ws-body">{{ t(item.answer) }}</p>
      </div>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
</script>

<style scoped>
.ws-faq2 {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-inline-start: 18px;
  border-inline-start: 2px solid var(--ws-primary);
}
</style>
