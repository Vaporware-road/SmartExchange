<template>
  <section id="product" class="py-20">
    <div class="lp-container">
      <LandingSectionHead
        :eyebrow="t('landing.features.eyebrow')"
        :title="t('landing.features.title')"
        :subtitle="t('landing.features.subtitle')"
      />

      <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <article v-for="(item, i) in FEATURES" :key="item.key" class="lp-card p-6" data-reveal :style="{ transitionDelay: `${i * 60}ms` }">
          <span class="text-2xl">{{ item.icon }}</span>
          <h3 class="mt-3 text-base font-semibold">{{ t(`landing.features.items.${item.key}.title`) }}</h3>
          <p class="mt-2 text-sm leading-7" style="color: var(--text-secondary)">
            {{ t(`landing.features.items.${item.key}.desc`) }}
          </p>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import LandingSectionHead from './LandingSectionHead.vue'

const { t } = useI18n()

/**
 * Six, not twelve. The long grid was the bulk of the old page's clutter; the
 * rest of the capability list now lives in the package table further down.
 */
const FEATURES = [
  { key: 'panel', icon: '🖥️' },
  { key: 'instant', icon: '⚡' },
  { key: 'telegram', icon: '✈️' },
  { key: 'instagram', icon: '📸' },
  { key: 'branding', icon: '🎨' },
  { key: 'security', icon: '🔐' },
]
</script>
