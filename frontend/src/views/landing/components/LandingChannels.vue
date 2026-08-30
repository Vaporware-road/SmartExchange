<template>
  <section class="pt-16 pb-8">
    <div class="lp-container">
      <LandingSectionHead :title="t('landing.channelsSection.title')" :subtitle="t('landing.channelsSection.subtitle')" />
    </div>

    <LandingMarquee :items="CHANNELS" :duration="34" v-slot="{ item }">
      <span
        class="mx-2 inline-flex items-center gap-2 rounded-full border px-5 py-2.5 text-sm font-medium"
        style="background: var(--bg-card); border-color: var(--border-card)"
      >
        <span>{{ item.icon }}</span>
        <span>{{ t(`landing.channels.${item.key}`) }}</span>
      </span>
    </LandingMarquee>

    <LandingMarquee class="mt-3" :items="CHANNELS" :duration="34" reverse v-slot="{ item }">
      <span
        class="mx-2 inline-flex items-center gap-2 rounded-full border px-5 py-2.5 text-sm font-medium"
        style="background: var(--bg-card); border-color: var(--border-card)"
      >
        <span>{{ item.icon }}</span>
        <span>{{ t(`landing.channels.${item.key}`) }}</span>
      </span>
    </LandingMarquee>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import LandingMarquee from './LandingMarquee.vue'
import LandingSectionHead from './LandingSectionHead.vue'
import { CHANNELS } from '@/config/landing.js'

const { t } = useI18n()
</script>
