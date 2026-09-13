<template>
  <span v-if="count" class="ws-stars" :aria-label="`${count} / 5`">
    <i v-for="n in 5" :key="n" :class="n <= count ? 'fas fa-star' : 'far fa-star'" aria-hidden="true" />
  </span>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({ rating: { type: [Number, String], default: 0 } })
const count = computed(() => {
  const value = Number(props.rating)
  return Number.isFinite(value) ? Math.min(Math.max(Math.round(value), 0), 5) : 0
})
</script>

<style scoped>
.ws-stars {
  display: inline-flex;
  gap: 3px;
  color: var(--ws-accent);
  font-size: 0.85rem;
}
</style>
