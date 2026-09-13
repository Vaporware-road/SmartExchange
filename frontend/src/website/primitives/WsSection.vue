<template>
  <section :id="anchor" class="ws-section" :class="{ 'ws-section--alt': alt, 'ws-section--tight': tight }">
    <div class="ws-container">
      <header v-if="hasHead" class="ws-head" :class="{ 'ws-head--center': center }">
        <p v-if="eyebrow" class="ws-eyebrow">{{ eyebrow }}</p>
        <h2 v-if="title" class="ws-h2">{{ title }}</h2>
        <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
      </header>
      <slot />
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

/** Section shell: the rhythm, the container and the optional heading block. */
const props = defineProps({
  anchor: { type: String, default: '' },
  eyebrow: { type: String, default: '' },
  title: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  center: { type: Boolean, default: false },
  alt: { type: Boolean, default: false },
  tight: { type: Boolean, default: false },
})

const hasHead = computed(() => Boolean(props.eyebrow || props.title || props.subtitle))
</script>
