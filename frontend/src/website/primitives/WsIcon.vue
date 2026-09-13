<template>
  <span class="ws-icon" aria-hidden="true">
    <i :class="resolved" />
  </span>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  name: { type: String, default: '' },
})

/**
 * Owners type icon names, not class strings, so a bare name is expanded to the
 * Font Awesome class the shell already loads. A full class string is respected.
 */
const resolved = computed(() => {
  const name = (props.name || '').trim()
  if (!name) return 'fas fa-circle-notch'
  if (name.includes('fa-')) return name
  return `fas fa-${name}`
})
</script>
