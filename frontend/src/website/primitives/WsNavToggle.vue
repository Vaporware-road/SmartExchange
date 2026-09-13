<template>
  <button
    type="button"
    class="ws-burger"
    :aria-expanded="String(modelValue)"
    :aria-label="modelValue ? 'Close menu' : 'Open menu'"
    @click="$emit('update:modelValue', !modelValue)"
  >
    <i :class="modelValue ? 'fas fa-xmark' : 'fas fa-bars'" />
  </button>
</template>

<script setup>
defineProps({ modelValue: { type: Boolean, default: false } })
defineEmits(['update:modelValue'])
</script>

<style scoped>
.ws-burger {
  display: none;
  margin-inline-start: auto;
  background: transparent;
  border: 1px solid var(--ws-border);
  border-radius: var(--ws-radius-sm);
  color: var(--ws-heading);
  width: 42px;
  height: 42px;
  font-size: 1.05rem;
  cursor: pointer;
}

@container ws (max-width: 860px) {
  .ws-burger {
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
