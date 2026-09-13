<template>
  <section class="ws-section ws-section--tight ws-cta-banner">
    <div class="ws-container ws-cta-banner__inner">
      <div class="ws-stack">
        <h2 v-if="t(content.title)" class="ws-h2">{{ t(content.title) }}</h2>
        <p v-if="body" class="ws-lead">{{ body }}</p>
      </div>
      <WsButton v-if="label" :href="content.cta_href">{{ label }}</WsButton>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import WsButton from '../../primitives/WsButton.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const body = computed(() => t(props.content.body))
const label = computed(() => t(props.content.cta_label))
</script>

<style scoped>
.ws-cta-banner {
  background: var(--ws-bg-alt);
  border-block: 1px solid var(--ws-border);
}

.ws-cta-banner__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  flex-wrap: wrap;
}
</style>
