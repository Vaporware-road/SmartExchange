<template>
  <span class="inline-flex items-center gap-2">
    <!--
      `Mr Exchange.png` is a green mark followed by a WHITE wordmark, drawn for a
      dark background: on the light theme the wordmark is invisible. So the image
      is cropped to the mark alone (it occupies the leftmost ~28% of the 1218×390
      artwork) and the wordmark is set in text, which follows the theme.
    -->
    <img
      :src="logo"
      alt=""
      aria-hidden="true"
      class="w-[0.92em] shrink-0 object-cover object-left"
      :style="{ height: '1em', fontSize: `${size}px` }"
      :width="size"
      :height="size"
      :loading="eager ? 'eager' : 'lazy'"
      :fetchpriority="eager ? 'high' : undefined"
    />
    <span class="font-latin font-extrabold tracking-tight" :style="{ fontSize: `${size * 0.62}px` }">
      MrExchange
    </span>
  </span>
</template>

<script setup>
defineProps({
  /** Mark height in px; the wordmark is sized from it. */
  size: { type: Number, default: 32 },
  eager: { type: Boolean, default: false },
})

const logo = '/static/landing/images/Mr Exchange.png'
</script>
