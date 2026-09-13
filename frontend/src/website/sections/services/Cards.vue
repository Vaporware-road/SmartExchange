<template>
  <WsSection anchor="services" :title="t(content.title)" :subtitle="t(content.subtitle)" alt>
    <div class="ws-grid" :style="{ '--ws-cols': cols }">
      <component
        :is="item.href ? 'a' : 'article'"
        v-for="(item, i) in items"
        :key="i"
        :href="item.href || null"
        class="ws-card ws-card--hover ws-service-card"
      >
        <WsIcon :name="item.icon" />
        <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
        <p class="ws-body">{{ t(item.body) }}</p>
        <span v-if="item.href" class="ws-service-card__more" aria-hidden="true">
          <i class="fas fa-arrow-right" />
        </span>
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
.ws-service-card {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ws-service-card__more {
  color: var(--ws-primary);
  margin-top: auto;
  padding-top: 6px;
}

[dir='rtl'] .ws-service-card__more {
  transform: scaleX(-1);
}
</style>
