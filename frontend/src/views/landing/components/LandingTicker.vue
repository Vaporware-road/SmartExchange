<template>
  <div class="border-y" style="background: var(--bg-navbar); border-color: var(--border-card)">
    <LandingMarquee :items="TICKER_RATES" :duration="38" v-slot="{ item }">
      <span class="lp-tick">
        {{ item.pair }}
        <b>{{ item.value }}</b>
        <i :class="item.up ? 'lp-up' : 'lp-down'">{{ item.up ? '▲' : '▼' }} {{ item.change }}</i>
      </span>
    </LandingMarquee>
  </div>
</template>

<script setup>
import LandingMarquee from './LandingMarquee.vue'
import { TICKER_RATES } from '@/config/landing.js'
</script>
