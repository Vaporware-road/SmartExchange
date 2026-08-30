<template>
  <section id="package" class="py-20">
    <div class="lp-container">
      <!-- Was "compare features". There is one plan, so there is nothing to
           compare — this is simply what the package contains. -->
      <LandingSectionHead :title="t('landing.package.title')" :subtitle="t('landing.package.subtitle')" />

      <div class="lp-card mx-auto max-w-3xl overflow-hidden" data-reveal>
        <ul class="divide-y" style="border-color: var(--border-card)">
          <li
            v-for="key in PACKAGE_FEATURES"
            :key="key"
            class="flex items-center justify-between gap-4 px-5 py-3.5 text-sm"
            style="border-color: var(--border-card)"
          >
            <span>{{ t(`landing.package.rows.${key}`) }}</span>
            <span
              class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-xs font-bold"
              style="background: var(--primary-muted); color: var(--primary)"
              :aria-label="t('landing.package.included')"
            >✓</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import LandingSectionHead from './LandingSectionHead.vue'
import { PACKAGE_FEATURES } from '@/config/landing.js'

const { t } = useI18n()
</script>
