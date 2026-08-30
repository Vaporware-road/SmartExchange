<template>
  <section ref="root" class="border-y py-10" style="background: var(--bg-navbar); border-color: var(--border-card)">
    <div class="lp-container grid grid-cols-2 gap-8 text-center lg:grid-cols-4">
      <div v-for="(stat, i) in STATS" :key="stat.key">
        <div class="font-latin text-3xl font-extrabold sm:text-4xl" style="color: var(--primary)">
          <!-- The channel count is deliberately unbounded rather than a number:
               the panel fans out to as many outputs as the customer connects. -->
          {{ values[i] == null ? '∞' : values[i] }}<span class="text-xl">{{ stat.suffix }}</span>
        </div>
        <p class="mt-2 text-sm" style="color: var(--text-secondary)">{{ t(`landing.stats.${stat.key}`) }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useCountUp } from '../composables/useCountUp.js'

const { t } = useI18n()

const STATS = [
  { key: 'saved', target: 2, suffix: 'h+' },
  { key: 'automation', target: 100, suffix: '%' },
  { key: 'channels', target: null, suffix: '' },
  { key: 'uptime', target: 99, suffix: '.9%' },
]

const root = ref(null)
const { values } = useCountUp(root, STATS)
</script>
