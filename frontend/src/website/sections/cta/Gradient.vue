<template>
  <section class="ws-section ws-cta-gradient">
    <div class="ws-cta-gradient__glow" aria-hidden="true" />
    <div class="ws-container ws-cta-gradient__inner">
      <h2 v-if="t(content.title)" class="ws-h2">{{ t(content.title) }}</h2>
      <p v-if="body" class="ws-lead">{{ body }}</p>
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
.ws-cta-gradient {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  background: var(--ws-bg-alt);
}

.ws-cta-gradient__glow {
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(34rem 20rem at 20% 0%, color-mix(in srgb, var(--ws-primary) 32%, transparent), transparent 62%),
    radial-gradient(30rem 18rem at 84% 100%, color-mix(in srgb, var(--ws-accent) 28%, transparent), transparent 60%);
}

.ws-cta-gradient__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px;
}

.ws-cta-gradient__inner .ws-lead {
  margin-inline: auto;
}
</style>
