<template>
  <WsSection anchor="testimonials" :title="t(content.title)" center alt>
    <div v-if="items.length" class="ws-slider">
      <figure class="ws-card ws-slider__slide">
        <WsStars :rating="current.rating" />
        <blockquote>{{ t(current.quote) }}</blockquote>
        <figcaption>
          <img v-if="current.avatar" :src="current.avatar" :alt="current.author" />
          <span>
            <strong>{{ current.author }}</strong>
            <small v-if="current.role">{{ t(current.role) }}</small>
          </span>
        </figcaption>
      </figure>

      <div v-if="items.length > 1" class="ws-slider__dots">
        <button
          v-for="(item, i) in items"
          :key="i"
          type="button"
          :class="{ 'is-active': i === index }"
          :aria-label="`${i + 1}`"
          @click="go(i)"
        />
      </div>
    </div>
  </WsSection>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsStars from '../../primitives/WsStars.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const items = computed(() => props.content.items || [])
const index = ref(0)
const current = computed(() => items.value[index.value] || {})
let timer = 0

function go(next) {
  index.value = next
  restart()
}

function restart() {
  clearInterval(timer)
  if (items.value.length < 2) return
  // Stopped entirely under reduced motion: an auto-advancing quote is exactly
  // the kind of movement that setting asks us not to make.
  if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return
  timer = setInterval(() => {
    index.value = (index.value + 1) % items.value.length
  }, 7000)
}

onMounted(restart)
onBeforeUnmount(() => clearInterval(timer))
</script>

<style scoped>
.ws-slider {
  max-width: 760px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.ws-slider__slide {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  text-align: center;
  padding: calc(var(--ws-block-gap) * 1.3);
}

blockquote {
  margin: 0;
  font-size: 1.12rem;
  color: var(--ws-text);
  white-space: pre-line;
}

figcaption {
  display: flex;
  align-items: center;
  gap: 12px;
}

figcaption img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
}

figcaption span {
  display: flex;
  flex-direction: column;
  text-align: start;
}

figcaption strong {
  color: var(--ws-heading);
}

figcaption small {
  color: var(--ws-text-muted);
}

.ws-slider__dots {
  display: flex;
  justify-content: center;
  gap: 8px;
}

.ws-slider__dots button {
  width: 9px;
  height: 9px;
  padding: 0;
  border: 0;
  border-radius: 50%;
  background: var(--ws-border-strong);
  cursor: pointer;
  transition: background 0.2s ease, width 0.2s ease;
}

.ws-slider__dots button.is-active {
  background: var(--ws-primary);
  width: 26px;
  border-radius: 999px;
}
</style>
