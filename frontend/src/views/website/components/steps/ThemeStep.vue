<template>
  <div class="wb-panel">
    <section>
      <h3 class="wb-panel__title">{{ $t('website.builder.themeTitle') }}</h3>
      <div class="wb-themes">
        <button
          v-for="(theme, slug) in themes"
          :key="slug"
          type="button"
          class="wb-theme"
          :class="{ 'is-active': slug === store.themeSlug }"
          @click="store.patchSite({ theme_slug: slug }, { immediate: true })"
        >
          <span class="wb-theme__swatch" :style="swatch(theme)">
            <i /><i /><i />
          </span>
          <span>{{ $t(`website.themes.${slug}`) }}</span>
        </button>
      </div>
    </section>

    <section v-for="group in groups" :key="group">
      <h3 class="wb-panel__title">{{ $t(`website.builder.style.${group}`) }}</h3>
      <div class="wb-chips">
        <button
          v-for="option in optionsFor(group)"
          :key="option"
          type="button"
          class="wb-chip"
          :class="{ 'is-active': current(group) === option }"
          @click="setStyle(group, option)"
        >
          {{ $t(`website.styles.${group}.${option}`) }}
        </button>
      </div>
    </section>

    <section>
      <h3 class="wb-panel__title">{{ $t('website.builder.style.brand_color') }}</h3>
      <div class="wb-brand">
        <input
          type="color"
          :value="brandColor"
          @input="store.patchSite({ theme_overrides: { ...store.overrides, brand_color: $event.target.value } })"
        />
        <span class="wb-brand__value ws-num">{{ brandColor }}</span>
        <button
          v-if="store.overrides.brand_color"
          type="button"
          class="btn-luxury-outline wb-brand__reset"
          @click="clearBrand"
        >
          {{ $t('website.builder.useThemeColor') }}
        </button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import themes from '@catalog/themes.json'
import styles from '@catalog/styles.json'
import { useWebsiteStore } from '@/stores/website'

/**
 * Theme first, then the handful of knobs that change a theme's personality.
 *
 * Each knob is a token group, so any combination stays coherent — the owner
 * cannot build something unreadable by mixing a pill button with a sharp card.
 */
const store = useWebsiteStore()
const groups = ['button', 'card', 'background', 'corner', 'density', 'font_pair']

function optionsFor(group) {
  return Object.keys(styles[group] || {})
}

/** A blank override means "whatever this theme suggests". */
function current(group) {
  return store.overrides[group] || themes[store.themeSlug]?.defaults?.[group]
}

function setStyle(group, option) {
  store.patchSite(
    { theme_overrides: { ...store.overrides, [group]: option } },
    { immediate: true },
  )
}

const brandColor = computed(
  () => store.overrides.brand_color || themes[store.themeSlug]?.tokens?.['--ws-primary'] || '#4f7cff',
)

function clearBrand() {
  const next = { ...store.overrides }
  delete next.brand_color
  store.patchSite({ theme_overrides: next }, { immediate: true })
}

function swatch(theme) {
  return {
    '--s1': theme.tokens['--ws-bg'],
    '--s2': theme.tokens['--ws-primary'],
    '--s3': theme.tokens['--ws-accent'],
  }
}
</script>

<style scoped>
.wb-themes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(124px, 1fr));
  gap: 10px;
}

.wb-theme {
  display: flex;
  flex-direction: column;
  gap: 7px;
  padding: 8px;
  border: 1px solid var(--border-card);
  border-radius: 11px;
  background: var(--bg-card);
  cursor: pointer;
  font-size: 0.8rem;
  color: var(--text-primary);
}

.wb-theme.is-active {
  border-color: var(--primary);
  box-shadow: 0 0 0 1px var(--primary);
}

.wb-theme__swatch {
  display: flex;
  height: 38px;
  border-radius: 7px;
  overflow: hidden;
}

.wb-theme__swatch i:nth-child(1) {
  flex: 2;
  background: var(--s1);
}

.wb-theme__swatch i:nth-child(2) {
  flex: 1;
  background: var(--s2);
}

.wb-theme__swatch i:nth-child(3) {
  flex: 1;
  background: var(--s3);
}

.wb-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.wb-chip {
  border: 1px solid var(--border-card);
  background: var(--bg-input);
  color: var(--text-secondary);
  border-radius: 999px;
  padding: 6px 14px;
  font: inherit;
  font-size: 0.82rem;
  cursor: pointer;
  transition: background 0.16s ease, color 0.16s ease, border-color 0.16s ease;
}

.wb-chip.is-active {
  background: var(--primary);
  border-color: var(--primary);
  color: var(--text-on-primary, #fff);
}

.wb-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.wb-brand input[type='color'] {
  width: 52px;
  height: 38px;
  border: 1px solid var(--border-card);
  border-radius: 9px;
  background: transparent;
  cursor: pointer;
  padding: 3px;
}

.wb-brand__value {
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.wb-brand__reset {
  margin-inline-start: auto;
  font-size: 0.8rem;
  padding: 6px 12px;
}
</style>
