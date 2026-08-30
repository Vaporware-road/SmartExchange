<template>
  <section id="faq" class="border-y py-20" style="background: var(--bg-navbar); border-color: var(--border-card)">
    <div class="lp-container">
      <LandingSectionHead :title="t('landing.faq.title')" :subtitle="t('landing.faq.subtitle')" />

      <div class="mx-auto max-w-3xl space-y-3">
        <div
          v-for="key in FAQ_KEYS"
          :key="key"
          class="lp-faq lp-card overflow-hidden"
          :class="{ 'is-open': openKey === key }"
          data-reveal
        >
          <button
            type="button"
            class="flex w-full items-center justify-between gap-4 px-5 py-4 text-start text-sm font-semibold"
            :aria-expanded="openKey === key"
            @click="toggle(key)"
          >
            <span>{{ t(`landing.faq.items.${key}.q`) }}</span>
            <svg class="lp-faq__chevron shrink-0" width="14" height="9" viewBox="0 0 14 9" fill="none" aria-hidden="true">
              <path d="M1 1l6 6 6-6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
            </svg>
          </button>

          <div class="lp-faq__answer">
            <div>
              <p class="px-5 pb-4 text-sm leading-8" style="color: var(--text-secondary)">
                {{ t(`landing.faq.items.${key}.a`) }}
              </p>
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
import LandingSectionHead from './LandingSectionHead.vue'
import { FAQ_KEYS } from '@/config/landing.js'

const { t } = useI18n()

const openKey = ref(FAQ_KEYS[0])

function toggle(key) {
  openKey.value = openKey.value === key ? null : key
}
</script>
