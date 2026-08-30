<template>
  <section class="border-y py-20" style="background: var(--bg-navbar); border-color: var(--border-card)">
    <div class="lp-container">
      <LandingSectionHead :title="t('landing.flow.title')" :subtitle="t('landing.flow.subtitle')" />

      <ol class="relative grid gap-8 md:grid-cols-3">
        <!-- The connecting rail is the animation: a gradient sweeps left to right
             once the steps are on screen, reading as the rate travelling out. -->
        <span class="lp-flow-rail" aria-hidden="true" />

        <li v-for="(key, i) in STEPS" :key="key" class="relative text-center" data-reveal :style="{ transitionDelay: `${i * 140}ms` }">
          <span
            class="mx-auto flex h-12 w-12 items-center justify-center rounded-full border-2 font-latin text-lg font-bold"
            style="background: var(--bg-card); border-color: var(--primary); color: var(--primary)"
          >{{ i + 1 }}</span>
          <h3 class="mt-4 text-base font-semibold">{{ t(`landing.flow.steps.${key}.title`) }}</h3>
          <p class="mx-auto mt-2 max-w-xs text-sm leading-7" style="color: var(--text-secondary)">
            {{ t(`landing.flow.steps.${key}.desc`) }}
          </p>
        </li>
      </ol>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import LandingSectionHead from './LandingSectionHead.vue'

const { t } = useI18n()

const STEPS = ['enter', 'render', 'publish']
</script>

<style scoped>
.lp-flow-rail {
  display: none;
}

@media (min-width: 768px) {
  .lp-flow-rail {
    display: block;
    position: absolute;
    inset-inline: 16%;
    top: 1.5rem;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    background-size: 220% 100%;
    animation: lp-rail 4.5s linear infinite;
  }

  @keyframes lp-rail {
    from {
      background-position: 100% 0;
    }
    to {
      background-position: -120% 0;
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .lp-flow-rail {
    animation: none;
  }
}
</style>
