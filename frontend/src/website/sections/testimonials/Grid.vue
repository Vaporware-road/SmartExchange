<template>
  <WsSection anchor="testimonials" :title="t(content.title)" center>
    <div class="ws-grid" :style="{ '--ws-cols': cols }">
      <figure v-for="(item, i) in items" :key="i" class="ws-card ws-quote-card">
        <WsStars :rating="item.rating" />
        <blockquote>{{ t(item.quote) }}</blockquote>
        <figcaption>
          <img v-if="item.avatar" :src="item.avatar" :alt="item.author" />
          <span>
            <strong>{{ item.author }}</strong>
            <small v-if="item.role">{{ t(item.role) }}</small>
          </span>
        </figcaption>
      </figure>
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsStars from '../../primitives/WsStars.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
const cols = computed(() => Math.min(items.value.length || 3, 3))
</script>

<style scoped>
.ws-quote-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
  text-align: start;
}

blockquote {
  margin: 0;
  color: var(--ws-text);
  white-space: pre-line;
}

figcaption {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: auto;
}

figcaption img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
}

figcaption span {
  display: flex;
  flex-direction: column;
}

figcaption strong {
  color: var(--ws-heading);
  font-size: 0.95rem;
}

figcaption small {
  color: var(--ws-text-muted);
}
</style>
