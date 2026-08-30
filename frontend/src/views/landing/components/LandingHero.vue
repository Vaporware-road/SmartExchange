<template>
  <section id="top" class="relative overflow-hidden">
    <canvas ref="canvas" class="pointer-events-none absolute inset-0 h-full w-full" aria-hidden="true" />

    <div class="lp-container relative grid items-center gap-12 py-16 lg:grid-cols-[1.05fr_0.95fr] lg:py-24">
      <div data-reveal>
        <span
          class="lp-pulse inline-flex items-center rounded-full border px-3.5 py-1.5 text-xs font-medium"
          style="border-color: var(--border-color); color: var(--text-secondary)"
        >
          {{ t('landing.hero.badge') }}
        </span>

        <h1 class="mt-5 text-[2.1rem] font-extrabold leading-[1.25] sm:text-5xl">
          {{ t('landing.hero.title') }}<br />
          <span class="lp-accent">{{ t('landing.hero.titleAccent') }}</span>
        </h1>

        <p class="mt-5 max-w-xl text-base leading-8" style="color: var(--text-secondary)">
          {{ t('landing.hero.subtitle') }}
        </p>

        <div class="mt-8 flex flex-wrap gap-3">
          <a :href="DEMO_URL" class="lp-btn lp-btn--primary">{{ t('landing.hero.ctaDemo') }}</a>
          <a :href="TRIAL_URL" class="lp-btn lp-btn--ghost">{{ t('landing.hero.ctaTrial') }}</a>
        </div>

        <p class="mt-4 text-xs" style="color: var(--text-secondary)">{{ t('landing.hero.note') }}</p>
      </div>

      <div class="relative" data-reveal>
        <div
          v-for="(chip, i) in chips"
          :key="chip.key"
          class="lp-glass lp-float absolute z-10 hidden items-center gap-2 px-3 py-2 text-xs font-medium shadow-lg sm:flex"
          :class="chip.position"
          :style="{ animationDelay: `${i * 0.7}s` }"
        >
          <span>{{ chip.icon }}</span>
          <span>{{ t(`landing.channels.${chip.key}`) }}</span>
        </div>

        <div class="lp-glass overflow-hidden p-4 shadow-2xl sm:p-5">
          <div class="mb-3 flex items-center justify-between">
            <span class="text-sm font-semibold">{{ t('landing.hero.panelTitle') }}</span>
            <span class="lp-pulse text-[0.7rem] font-medium" style="color: var(--text-secondary)">
              {{ t('landing.hero.live') }}
            </span>
          </div>

          <div class="divide-y" style="border-color: var(--border-card)">
            <div
              v-for="row in rows"
              :key="row.code"
              class="lp-rate-row flex items-center justify-between gap-3 rounded-lg px-2 py-3"
              :class="{ 'is-flashing': row.flash }"
              style="border-color: var(--border-card)"
            >
              <span class="flex items-center gap-2 text-sm font-medium">
                <span class="text-lg leading-none">{{ row.flag }}</span>
                <span dir="ltr">{{ row.code }}</span>
              </span>
              <span class="flex items-center gap-4 font-latin text-sm" dir="ltr">
                <span class="flex flex-col items-end">
                  <span class="text-[0.62rem] uppercase" style="color: var(--text-secondary)">{{ t('landing.hero.buy') }}</span>
                  <span :class="row.buyUp ? 'lp-up' : 'lp-down'">£{{ formatRate(row.buy) }}</span>
                </span>
                <span class="flex flex-col items-end">
                  <span class="text-[0.62rem] uppercase" style="color: var(--text-secondary)">{{ t('landing.hero.sell') }}</span>
                  <span :class="row.sellUp ? 'lp-up' : 'lp-down'">£{{ formatRate(row.sell) }}</span>
                </span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useHeroCanvas } from '../composables/useHeroCanvas.js'
import { formatRate, useLivePrices } from '../composables/useLivePrices.js'
import { DEMO_URL, HERO_RATES, TRIAL_URL } from '@/config/landing.js'

const { t } = useI18n()

const canvas = ref(null)
useHeroCanvas(canvas)

const { rows } = useLivePrices(HERO_RATES)

const chips = [
  { key: 'telegram', icon: '✈️', position: '-top-4 start-2' },
  { key: 'instagram', icon: '📸', position: 'top-1/3 -start-6' },
  { key: 'website', icon: '🌐', position: '-bottom-4 end-6' },
]
</script>
