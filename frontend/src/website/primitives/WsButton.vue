<template>
  <a v-if="href" class="ws-btn" :class="{ 'ws-btn--ghost': ghost }" :href="href" :target="external ? '_blank' : null" :rel="external ? 'noopener' : null">
    <slot />
  </a>
  <button v-else type="button" class="ws-btn" :class="{ 'ws-btn--ghost': ghost }">
    <slot />
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  href: { type: String, default: '' },
  ghost: { type: Boolean, default: false },
})

/** An owner pasting a full URL means "somewhere else"; an anchor means "here". */
const external = computed(() => /^https?:\/\//i.test(props.href))
</script>
