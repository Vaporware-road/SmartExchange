<template>
  <WsSection anchor="steps" :title="t(content.title)" :subtitle="t(content.subtitle)">
    <ol class="ws-timeline">
      <li v-for="(item, i) in items" :key="i">
        <span class="ws-timeline__marker">
          <i v-if="item.icon" :class="`fas fa-${item.icon}`" aria-hidden="true" />
          <span v-else class="ws-num">{{ i + 1 }}</span>
        </span>
        <div class="ws-timeline__body">
          <h3 v-if="t(item.title)" class="ws-h3">{{ t(item.title) }}</h3>
          <p class="ws-body">{{ t(item.body) }}</p>
        </div>
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
</script>

<style scoped>
.ws-timeline {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.ws-timeline li {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 22px;
  padding-bottom: 34px;
  position: relative;
}

/* The connecting rail, drawn on every step but the last. */
.ws-timeline li:not(:last-child)::before {
  content: '';
  position: absolute;
  inset-inline-start: 23px;
  top: 48px;
  bottom: 6px;
  width: 2px;
  background: var(--ws-border);
}

.ws-timeline li:last-child {
  padding-bottom: 0;
}

.ws-timeline__marker {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: var(--ws-surface);
  border: 1px solid var(--ws-border-strong);
  color: var(--ws-primary);
  font-weight: 700;
  flex: none;
}

.ws-timeline__body {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 8px;
}
</style>
