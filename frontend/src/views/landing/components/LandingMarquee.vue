<template>
  <div class="lp-marquee" :class="{ 'lp-marquee--reverse': reverse }" :style="{ '--lp-marquee-duration': `${duration}s` }">
    <!-- The list is rendered twice; the -50% keyframe therefore ends on a frame
         identical to the first, so the loop is continuous with no snap-back.
         The second pass is decorative and hidden from assistive tech. -->
    <div class="lp-marquee__track">
      <div class="flex shrink-0 items-center">
        <template v-for="(item, i) in items" :key="`a-${i}`"><slot :item="item" /></template>
      </div>
      <div class="flex shrink-0 items-center" aria-hidden="true">
        <template v-for="(item, i) in items" :key="`b-${i}`"><slot :item="item" /></template>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  items: { type: Array, required: true },
  /** Seconds for one full pass of a single copy. Longer = slower. */
  duration: { type: Number, default: 44 },
  reverse: { type: Boolean, default: false },
})
</script>
