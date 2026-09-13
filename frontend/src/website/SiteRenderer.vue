<template>
  <div v-if="snapshot" class="ws-shell">
    <div class="ws-root" :style="style" :dir="dir" :lang="activeLocale" v-bind="attrs">
      <component :is="chrome" />
    </div>
  </div>

  <div v-else class="ws-root ws-root--empty">
    <slot name="empty">
      <p>{{ $t('website.renderer.nothingToShow') }}</p>
    </slot>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { layoutComponent } from './registry.js'
import { ensureFonts, styleAttrs, tokenStyle } from './tokens.js'
import { directionFor } from './localize.js'
import { provideSiteContext } from './composables/useSiteContext.js'
import './website.css'

/**
 * Draws a site from its snapshot — the same component for the published page,
 * the builder's live preview and the authenticated preview route.
 *
 * Everything variable arrives as data: the theme as custom properties on this
 * wrapper, the arrangement as a chrome component, the words as localized
 * content. Nothing about a particular desk is compiled in.
 */
const props = defineProps({
  snapshot: { type: Object, default: null },
  /** Overrides the visitor's language, used by the builder's language tabs. */
  locale: { type: String, default: '' },
  /** Names the desk for the price feed when the URL cannot (preview, builder). */
  accountSlug: { type: String, default: '' },
  isEditing: { type: Boolean, default: false },
})

const chosenLocale = ref('')

const snapshotRef = computed(() => props.snapshot)
const primaryLocale = computed(() => props.snapshot?.primary_locale || 'en')
const activeLocale = computed(
  () => props.locale || chosenLocale.value || primaryLocale.value,
)
const theme = computed(() => props.snapshot?.theme || {})
const style = computed(() => tokenStyle(theme.value))
const attrs = computed(() => styleAttrs(theme.value))
const dir = computed(() => directionFor(activeLocale.value))
const chrome = computed(() =>
  layoutComponent(props.snapshot?.layout, props.snapshot?.chrome),
)

provideSiteContext({
  snapshot: snapshotRef,
  locale: activeLocale,
  accountSlug: computed(() => props.accountSlug || props.snapshot?.slug || ''),
  isEditing: computed(() => props.isEditing),
  setLocale: (code) => {
    chosenLocale.value = code
  },
})

watch(
  () => theme.value.font_families,
  (families) => ensureFonts(families),
  { immediate: true },
)
</script>

<style scoped>
.ws-root--empty {
  display: grid;
  place-items: center;
  min-height: 260px;
  color: var(--ws-text-muted, #6b7280);
  padding: 40px;
  text-align: center;
}
</style>
