<template>
  <div
    class="grid grid-cols-1 sm:grid-cols-[minmax(7rem,9rem)_1fr] gap-1 sm:gap-3 py-2 border-b text-sm"
    style="border-color: var(--border-card);"
  >
    <dt class="text-[var(--text-secondary)] font-medium">{{ label }}</dt>
    <dd
      class="text-[var(--text-primary)] break-words"
      :class="{ 'font-mono text-xs': mono }"
      :dir="dir"
    >
      {{ value || '—' }}
    </dd>
  </div>
</template>

<script setup>
defineProps({
  label: { type: String, required: true },
  value: { type: [String, Number], default: '' },
  dir: { type: String, default: undefined },
  mono: { type: Boolean, default: false },
})
</script>
