<template>
  <a class="ws-logo" href="#top">
    <img v-if="showImage && branding.logo" :src="branding.logo" :alt="name" />
    <span v-if="!branding.logo || withName">{{ name }}</span>
  </a>
</template>

<script setup>
import { computed } from 'vue'
import { useSiteContext } from '../composables/useSiteContext.js'

const props = defineProps({
  showImage: { type: Boolean, default: true },
  withName: { type: Boolean, default: false },
})

const { branding, t } = useSiteContext()
const name = computed(() => t(branding.value.business_name) || 'Exchange')
</script>
