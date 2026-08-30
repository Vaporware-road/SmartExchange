<template>
  <section class="py-20">
    <div class="lp-container">
      <div class="lp-card grid items-center gap-8 p-6 sm:p-8 lg:grid-cols-[0.9fr_1.1fr]" data-reveal>
        <div>
          <h2 class="text-2xl font-bold leading-snug">{{ t('landing.demo.title') }}</h2>
          <p class="mt-4 text-sm leading-8" style="color: var(--text-secondary)">{{ t('landing.demo.text') }}</p>
          <div class="mt-6 flex flex-wrap gap-3">
            <a :href="DEMO_URL" class="lp-btn lp-btn--primary">{{ t('landing.demo.cta') }}</a>
            <a :href="TRIAL_URL" class="lp-btn lp-btn--ghost">{{ t('landing.hero.ctaTrial') }}</a>
          </div>
          <p class="mt-4 text-xs" style="color: var(--text-secondary)">{{ t('landing.demo.note') }}</p>
        </div>

        <!--
          preload="none": Demo.mp4 is ~41 MB. Anything more makes every visitor
          pay for bytes they may never watch; the poster carries the visual.
        -->
        <video
          class="w-full rounded-2xl border"
          style="border-color: var(--border-card)"
          controls
          playsinline
          preload="none"
          :poster="poster"
          width="1280"
          height="720"
        >
          <source :src="video" type="video/mp4" />
        </video>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { DEMO_URL, TRIAL_URL } from '@/config/landing.js'

const { t } = useI18n()

const video = '/static/landing/Demo.mp4'
const poster = '/static/landing/images/Mr Exchange.png'
</script>
