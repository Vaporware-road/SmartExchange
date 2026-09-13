<template>
  <WsSection anchor="about" tight>
    <blockquote class="ws-statement">
      <p v-if="t(content.title)" class="ws-statement__text">{{ t(content.title) }}</p>
      <p v-if="body" class="ws-lead ws-statement__body">{{ body }}</p>
    </blockquote>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/** One large claim, centred. Used by layouts that want a pause, not a wall. */
const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const body = computed(() => t(props.content.body))
</script>

<style scoped>
.ws-statement {
  margin: 0;
  max-width: 900px;
  margin-inline: auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.ws-statement__text {
  margin: 0;
  font-family: var(--ws-font-heading);
  font-weight: var(--ws-heading-weight);
  letter-spacing: var(--ws-heading-tracking);
  color: var(--ws-heading);
  font-size: clamp(1.5rem, 1.05rem + 2cqi, 2.6rem);
  line-height: 1.3;
  text-wrap: balance;
}

.ws-statement__body {
  margin-inline: auto;
  white-space: pre-line;
}
</style>
