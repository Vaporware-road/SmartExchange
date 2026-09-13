<template>
  <div v-if="src" class="ws-media" :class="{ 'ws-media--ratio': ratio }">
    <img :src="src" :alt="alt" loading="lazy" decoding="async" />
  </div>
  <div v-else-if="placeholder" class="ws-media ws-media--ratio ws-media--empty" aria-hidden="true">
    <span><i class="fas fa-image" /></span>
  </div>
</template>

<script setup>
defineProps({
  src: { type: String, default: '' },
  alt: { type: String, default: '' },
  ratio: { type: Boolean, default: true },
  /** Draw an empty frame when there is no image — useful while editing. */
  placeholder: { type: Boolean, default: false },
})
</script>

<style scoped>
.ws-media--empty {
  display: grid;
  place-items: center;
  color: var(--ws-text-muted);
  font-size: 1.6rem;
  background: var(--ws-surface-alt);
}
</style>
