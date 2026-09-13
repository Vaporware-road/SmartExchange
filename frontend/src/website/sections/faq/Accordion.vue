<template>
  <WsSection anchor="faq" :title="t(content.title)" :subtitle="t(content.subtitle)" center>
    <div class="ws-faq">
      <details v-for="(item, i) in items" :key="i" :open="i === 0">
        <summary>
          <span>{{ t(item.question) }}</span>
          <i class="fas fa-plus" aria-hidden="true" />
        </summary>
        <p class="ws-body">{{ t(item.answer) }}</p>
      </details>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/* Native <details>: keyboard support, find-in-page and no-JS all come free. */
const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
</script>

<style scoped>
.ws-faq {
  max-width: 800px;
  margin-inline: auto;
  border-top: 1px solid var(--ws-border);
}

details {
  border-bottom: 1px solid var(--ws-border);
}

summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 20px 4px;
  cursor: pointer;
  font-weight: 600;
  color: var(--ws-heading);
  list-style: none;
}

summary::-webkit-details-marker {
  display: none;
}

summary i {
  color: var(--ws-primary);
  transition: transform 0.22s ease;
  flex: none;
}

details[open] summary i {
  transform: rotate(45deg);
}

details p {
  padding: 0 4px 20px;
}
</style>
