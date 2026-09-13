<template>
  <WsSection anchor="features" :title="t(content.title)" :subtitle="t(content.subtitle)">
    <div class="ws-alt">
      <!-- Every other row flips, so a long list reads as a rhythm rather than
           a column of identical blocks. -->
      <div
        v-for="(item, i) in items"
        :key="i"
        class="ws-split ws-alt__row"
        :class="{ 'ws-alt__row--flip': i % 2 === 1 }"
      >
        <div class="ws-stack">
          <WsIcon v-if="item.icon" :name="item.icon" />
          <h3 class="ws-h2 ws-alt__title">{{ t(item.title) }}</h3>
          <p class="ws-body">{{ t(item.body) }}</p>
        </div>
        <WsImage :src="item.image" :alt="t(item.title)" placeholder />
      </div>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsIcon from '../../primitives/WsIcon.vue'
import WsImage from '../../primitives/WsImage.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
</script>

<style scoped>
.ws-alt {
  display: flex;
  flex-direction: column;
  gap: calc(var(--ws-block-gap) * 2);
}

.ws-alt__row--flip > :first-child {
  order: 2;
}

.ws-alt__title {
  font-size: clamp(1.4rem, 1.1rem + 1.1cqi, 2rem);
}

@container ws (max-width: 760px) {
  .ws-alt__row--flip > :first-child {
    order: 0;
  }
}
</style>
