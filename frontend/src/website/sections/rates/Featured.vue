<template>
  <WsSection
    anchor="rates"
    :title="t(content.title)"
    :subtitle="t(content.subtitle)"
    alt
  >
    <PriceWidget variant="featured" :config="content" />
    <p v-if="note" class="ws-muted ws-rates__note">{{ note }}</p>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import PriceWidget from '../../components/PriceWidget.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/** The board the desk is really here for; the widget does the work. */
const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const note = computed(() => t(props.content.note))
</script>

<style scoped>
.ws-rates__note {
  margin: 20px 0 0;
  font-size: 0.85rem;
}
</style>
