<template>
  <section id="telegram" class="py-16">
    <div class="lp-container">
      <div
        class="relative overflow-hidden rounded-2xl border p-8 sm:p-10"
        style="background: var(--bg-card); border-color: var(--border-card)"
        data-reveal
      >
        <span class="lp-tg-glow" aria-hidden="true" />

        <div class="relative grid items-center gap-8 lg:grid-cols-[1.2fr_0.8fr]">
          <div>
            <span
              class="inline-flex items-center gap-2 rounded-full px-3 py-1 text-xs font-semibold"
              style="background: rgba(34, 158, 217, 0.14); color: #229ed9"
            >
              ✈️ {{ t('landing.telegram.eyebrow') }}
            </span>
            <h2 class="mt-4 text-2xl font-bold leading-snug">{{ t('landing.telegram.title') }}</h2>
            <p class="mt-3 max-w-xl text-sm leading-8" style="color: var(--text-secondary)">
              {{ t('landing.telegram.subtitle') }}
            </p>

            <div class="mt-6 flex flex-wrap items-center gap-3">
              <a :href="TELEGRAM_URL" target="_blank" rel="noopener" class="lp-btn lp-btn--telegram">
                {{ t('landing.telegram.cta') }}
              </a>
              <span class="font-latin text-sm" dir="ltr" style="color: var(--text-secondary)">{{ TELEGRAM_CHANNEL }}</span>
            </div>
          </div>

          <ul class="grid gap-3">
            <li
              v-for="key in PERKS"
              :key="key"
              class="flex items-start gap-2.5 rounded-xl border px-4 py-3 text-sm"
              style="border-color: var(--border-card)"
            >
              <span style="color: var(--primary)">✓</span>
              <span>{{ t(`landing.telegram.perks.${key}`) }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { TELEGRAM_CHANNEL, TELEGRAM_URL } from '@/config/landing.js'

const { t } = useI18n()

const PERKS = ['rates', 'releases', 'tips']
</script>

<style scoped>
.lp-tg-glow {
  position: absolute;
  inset-block-start: -40%;
  inset-inline-end: -10%;
  width: 26rem;
  height: 26rem;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(34, 158, 217, 0.22), transparent 65%);
  animation: lp-tg-drift 9s ease-in-out infinite;
  pointer-events: none;
}

@keyframes lp-tg-drift {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  50% {
    transform: translate(-6%, 8%) scale(1.08);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lp-tg-glow {
    animation: none;
  }
}
</style>
