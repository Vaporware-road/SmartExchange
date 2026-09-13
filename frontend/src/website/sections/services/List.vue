<template>
  <WsSection anchor="services" :title="t(content.title)" :subtitle="t(content.subtitle)">
    <ul class="ws-service-list">
      <li v-for="(item, i) in items" :key="i">
        <span class="ws-service-list__index ws-num">{{ String(i + 1).padStart(2, '0') }}</span>
        <div class="ws-service-list__body">
          <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
          <p class="ws-body">{{ t(item.body) }}</p>
        </div>
        <a v-if="item.href" class="ws-service-list__link" :href="item.href" aria-hidden="true">
          <i class="fas fa-arrow-right" />
        </a>
      </li>
    </ul>
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
.ws-service-list {
  list-style: none;
  margin: 0;
  padding: 0;
  border-top: 1px solid var(--ws-border);
}

.ws-service-list li {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  gap: 26px;
  align-items: start;
  padding-block: 26px;
  border-bottom: 1px solid var(--ws-border);
}

.ws-service-list__index {
  font-family: var(--ws-font-heading);
  font-size: 1.05rem;
  color: var(--ws-primary);
  padding-top: 0.2em;
}

.ws-service-list__body {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ws-service-list__link {
  color: var(--ws-text-muted);
  padding-top: 0.3em;
}

[dir='rtl'] .ws-service-list__link {
  transform: scaleX(-1);
}
</style>
