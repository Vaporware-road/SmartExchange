<template>
  <div class="wb-panel">
    <p class="wb-panel__note">
      <i class="fas fa-circle-info" /> {{ $t('website.builder.designNote') }}
    </p>

    <div class="wb-designs">
      <button
        v-for="(manifest, slug) in layouts"
        :key="slug"
        type="button"
        class="wb-design"
        :class="{ 'is-active': slug === store.layoutSlug }"
        :disabled="store.saving"
        @click="choose(slug)"
      >
        <LayoutThumb :layout="manifest" :theme="themes[manifest.default_theme]" />
        <span class="wb-design__meta">
          <strong>{{ $t(`website.layouts.${slug}.name`) }}</strong>
          <small>{{ $t(`website.layouts.${slug}.blurb`) }}</small>
        </span>
        <i v-if="slug === store.layoutSlug" class="fas fa-circle-check wb-design__tick" />
      </button>
    </div>
  </div>
</template>

<script setup>
import layouts from '@catalog/layouts.json'
import themes from '@catalog/themes.json'
import LayoutThumb from '../LayoutThumb.vue'
import { useWebsiteStore } from '@/stores/website'

/** Ten designs, one click apart. Content is carried across by the API. */
const store = useWebsiteStore()

async function choose(slug) {
  if (slug === store.layoutSlug) return
  await store.applyLayout(slug)
}
</script>

<style scoped>
.wb-designs {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(148px, 1fr));
  gap: 12px;
}

.wb-design {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 10px;
  border: 1px solid var(--border-card);
  border-radius: 13px;
  background: var(--bg-card);
  cursor: pointer;
  text-align: start;
  transition: border-color 0.18s ease, transform 0.18s ease;
}

.wb-design:hover:not(:disabled) {
  border-color: var(--primary);
  transform: translateY(-2px);
}

.wb-design.is-active {
  border-color: var(--primary);
  box-shadow: 0 0 0 1px var(--primary);
}

.wb-design:disabled {
  opacity: 0.6;
  cursor: wait;
}

.wb-design__meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.wb-design__meta strong {
  font-size: 0.9rem;
  color: var(--text-primary);
}

.wb-design__meta small {
  font-size: 0.75rem;
  color: var(--text-secondary);
  line-height: 1.4;
}

.wb-design__tick {
  position: absolute;
  top: 8px;
  inset-inline-end: 10px;
  color: var(--primary);
}
</style>
