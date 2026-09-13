<template>
  <section id="rates" class="ws-section ws-section--tight ws-rates-ticker">
    <div v-if="title || subtitle" class="ws-container ws-head ws-head--center">
      <h2 v-if="title" class="ws-h2">{{ title }}</h2>
      <p v-if="subtitle" class="ws-lead">{{ subtitle }}</p>
    </div>
    <!-- Full-bleed on purpose: a ticker that stops at the container edge reads
         as a broken table rather than a running feed. -->
    <PriceWidget variant="ticker" :config="content" />
    <p v-if="note" class="ws-container ws-muted ws-rates-ticker__note">{{ note }}</p>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import PriceWidget from '../../components/PriceWidget.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const title = computed(() => t(props.content.title))
const subtitle = computed(() => t(props.content.subtitle))
const note = computed(() => t(props.content.note))
</script>

<style scoped>
.ws-rates-ticker__note {
  margin: 18px auto 0;
  font-size: 0.85rem;
  text-align: center;
}
</style>
