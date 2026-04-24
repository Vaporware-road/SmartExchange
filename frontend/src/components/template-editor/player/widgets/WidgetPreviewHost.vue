<template>
  <component :is="comp" v-if="comp" :widget="widget" />
  <div v-else class="flex h-full w-full items-center justify-center text-xs text-[var(--text-secondary)]">
    {{ widget?.type || '?' }}
  </div>
</template>

<script setup>
import { computed } from 'vue'
import TextWidgetPreview from './TextWidgetPreview.vue'
import ImageWidgetPreview from './ImageWidgetPreview.vue'
import PriceBoardWidget from './PriceBoardWidget.vue'

const props = defineProps({
  widget: { type: Object, required: true },
})

const comp = computed(() => {
  switch (props.widget?.type) {
    case 'text':
    case 'marquee':
    case 'date':
    case 'clock':
    case 'weekday':
      return TextWidgetPreview
    case 'image':
    case 'video':
      return ImageWidgetPreview
    case 'price_board':
      return PriceBoardWidget
    default:
      return TextWidgetPreview
  }
})
</script>
