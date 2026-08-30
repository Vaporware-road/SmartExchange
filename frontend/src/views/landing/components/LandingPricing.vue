<template>
  <section id="services" class="border-y py-20" style="background: var(--bg-navbar); border-color: var(--border-card)">
    <div class="lp-container">
      <LandingSectionHead
        :eyebrow="t('landing.pricing.eyebrow')"
        :title="t('landing.pricing.title')"
        :subtitle="t('landing.pricing.subtitle')"
      />

      <div class="mx-auto grid max-w-4xl gap-5 md:grid-cols-[1.25fr_0.75fr]">
        <div class="lp-card relative overflow-hidden p-7" style="border-color: var(--primary)" data-reveal>
          <span
            class="absolute end-0 top-0 px-3 py-1 text-[0.68rem] font-bold uppercase tracking-wider"
            style="background: var(--primary); color: var(--text-on-primary); border-end-start-radius: 0.9rem"
          >{{ t('landing.pricing.bundle.badge') }}</span>

          <h3 class="text-lg font-bold">{{ t('landing.pricing.bundle.name') }}</h3>

          <p class="mt-3 flex items-baseline gap-2 font-latin" dir="ltr">
            <span class="text-4xl font-extrabold" style="color: var(--primary)">${{ BUNDLE_PRICE }}</span>
            <!-- One-off, not a subscription: the only recurring line we sell is
                 the optional support retainer in the card beside this one. -->
            <span class="text-sm font-medium" style="color: var(--text-secondary)">{{ t('landing.pricing.oneOff') }}</span>
          </p>
          <p class="mt-2 text-xs" style="color: var(--text-secondary)">{{ t('landing.pricing.bundle.note') }}</p>

          <ul class="mt-6 grid gap-2.5 sm:grid-cols-2">
            <li v-for="key in HIGHLIGHTS" :key="key" class="flex items-start gap-2 text-sm">
              <span style="color: var(--primary)">✓</span>
              <span>{{ t(`landing.package.rows.${key}`) }}</span>
            </li>
          </ul>

          <a href="#contact" class="lp-btn lp-btn--primary mt-7 w-full">{{ t('landing.pricing.bundle.cta') }}</a>
        </div>

        <div class="lp-card p-7" data-reveal>
          <span
            class="inline-flex rounded-full border px-2.5 py-1 text-[0.68rem] font-semibold uppercase tracking-wider"
            style="border-color: var(--border-color); color: var(--text-secondary)"
          >{{ t('landing.pricing.optional') }}</span>

          <h3 class="mt-3 text-lg font-bold">{{ t('landing.addons.items.support.title') }}</h3>

          <p class="mt-3 flex items-baseline gap-1.5 font-latin" dir="ltr">
            <span class="text-3xl font-extrabold">${{ SUPPORT_PRICE }}</span>
            <span class="text-sm" style="color: var(--text-secondary)">/ {{ t('landing.pricing.perMonth') }}</span>
          </p>

          <p class="mt-3 text-sm leading-7" style="color: var(--text-secondary)">
            {{ t('landing.addons.items.support.desc') }}
          </p>

          <p class="mt-4 text-xs" style="color: var(--text-secondary)">
            {{ t('landing.pricing.supportNote') }}
          </p>
        </div>
      </div>

      <!-- Add-ons -->
      <div class="mt-16">
        <h3 class="text-center text-xl font-bold" data-reveal>{{ t('landing.addons.title') }}</h3>
        <p class="mx-auto mt-3 max-w-2xl text-center text-sm leading-7" style="color: var(--text-secondary)" data-reveal>
          {{ t('landing.addons.subtitle') }}
        </p>

        <div v-for="group in GROUPS" :key="group.unit" class="mt-10">
          <h4 class="mb-4 text-xs font-semibold uppercase tracking-[0.16em]" style="color: var(--text-secondary)" data-reveal>
            {{ t(`landing.addons.groups.${group.unit}`) }}
          </h4>

          <div class="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            <article
              v-for="(addon, i) in group.items"
              :key="addon.key"
              class="lp-card flex flex-col p-5"
              :style="addon.featured ? { borderColor: 'var(--primary)', transitionDelay: `${i * 40}ms` } : { transitionDelay: `${i * 40}ms` }"
              data-reveal
            >
              <div class="flex items-start justify-between gap-3">
                <span class="text-xl">{{ addon.icon }}</span>
                <span
                  v-if="addon.optional"
                  class="rounded-full px-2 py-0.5 text-[0.62rem] font-semibold uppercase tracking-wide"
                  style="background: var(--primary-muted); color: var(--primary)"
                >{{ t('landing.pricing.optional') }}</span>
              </div>

              <h5 class="mt-3 text-sm font-semibold">{{ t(`landing.addons.items.${addon.key}.title`) }}</h5>
              <p class="mt-1.5 flex-1 text-xs leading-6" style="color: var(--text-secondary)">
                {{ t(`landing.addons.items.${addon.key}.desc`) }}
              </p>
              <p v-if="addon.note" class="mt-2 text-[0.68rem] font-semibold" style="color: var(--primary)">
                {{ t(`landing.addons.items.${addon.key}.note`) }}
              </p>

              <div class="mt-4 flex items-end justify-between gap-2 font-latin" dir="ltr">
                <span class="text-lg font-bold" style="color: var(--primary)">
                  {{ addon.price }}<span v-if="addon.unit === 'month'" class="text-xs font-medium">/mo</span>
                </span>
                <!-- Market figure is the researched going rate for the same
                     service in 2026; ours sits under it by design. -->
                <span class="text-[0.68rem] line-through" style="color: var(--text-secondary)">{{ addon.market }}</span>
              </div>
            </article>
          </div>
        </div>

        <p class="mt-8 text-center text-xs" style="color: var(--text-secondary)" data-reveal>
          {{ t('landing.addons.disclaimer') }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import LandingSectionHead from './LandingSectionHead.vue'
import { ADDONS, BUNDLE_PRICE, SUPPORT_PRICE } from '@/config/landing.js'

const { t } = useI18n()

/** The bundle card shows a readable subset; the full list is the package table. */
const HIGHLIGHTS = ['panel', 'instant', 'telegram', 'instagram', 'website', 'graphics', 'branches', 'roles']

const GROUPS = computed(() => [
  { unit: 'once', items: ADDONS.filter((a) => a.unit === 'once') },
  { unit: 'month', items: ADDONS.filter((a) => a.unit === 'month') },
])
</script>
