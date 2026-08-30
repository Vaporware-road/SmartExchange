<template>
  <div class="mx-auto mb-12 max-w-2xl text-center" data-reveal>
    <p v-if="eyebrow" class="mb-3 text-xs font-semibold uppercase tracking-[0.18em]" style="color: var(--primary)">
      {{ eyebrow }}
    </p>
    <h2 class="text-2xl font-bold leading-snug sm:text-[2rem]">{{ title }}</h2>
    <p v-if="subtitle" class="mt-4 text-[0.95rem] leading-7" style="color: var(--text-secondary)">{{ subtitle }}</p>
  </div>
</template>

<script setup>
defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  subtitle: { type: String, default: '' },
})
</script>
