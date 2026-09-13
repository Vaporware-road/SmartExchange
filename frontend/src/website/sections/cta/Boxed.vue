<template>
  <WsSection tight>
    <div class="ws-card ws-cta-boxed">
      <div class="ws-stack">
        <h2 v-if="t(content.title)" class="ws-h2">{{ t(content.title) }}</h2>
        <p v-if="body" class="ws-lead">{{ body }}</p>
        <WsButton v-if="label" :href="content.cta_href" class="ws-cta-boxed__btn">{{ label }}</WsButton>
      </div>
      <WsImage v-if="content.image" :src="content.image" :alt="t(content.title)" />
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsButton from '../../primitives/WsButton.vue'
import WsImage from '../../primitives/WsImage.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const body = computed(() => t(props.content.body))
const label = computed(() => t(props.content.cta_label))
</script>

<style scoped>
.ws-cta-boxed {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
  gap: calc(var(--ws-block-gap) * 1.5);
  align-items: center;
  padding: calc(var(--ws-block-gap) * 1.5);
}

.ws-cta-boxed__btn {
  align-self: flex-start;
  margin-top: 8px;
}

@container ws (max-width: 860px) {
  .ws-cta-boxed {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
