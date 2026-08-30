<template>
  <footer class="border-t py-12" style="background: var(--bg-footer); border-color: var(--border-card)">
    <div class="lp-container grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
      <div>
        <LandingLogo :size="34" />
        <p class="mt-4 text-xs leading-6" style="color: var(--text-secondary)">{{ t('landing.footer.about') }}</p>
      </div>

      <div v-for="col in COLUMNS" :key="col.titleKey">
        <h3 class="text-sm font-semibold">{{ t(col.titleKey) }}</h3>
        <ul class="mt-3 space-y-2">
          <li v-for="link in col.links" :key="link.href ?? link.labelKey">
            <RouterLink v-if="link.to" :to="link.to" class="lp-navlink">
              {{ t(link.labelKey) }}
            </RouterLink>
            <a
              v-else
              :href="link.href"
              class="lp-navlink"
              :target="link.external ? '_blank' : undefined"
              :rel="link.external ? 'noopener' : undefined"
              :dir="link.ltr ? 'ltr' : undefined"
            >{{ link.label ?? t(link.labelKey) }}</a>
          </li>
        </ul>
      </div>
    </div>

    <div class="lp-container mt-10 border-t pt-6 text-center text-xs" style="border-color: var(--border-card); color: var(--text-secondary)">
      © {{ year }} {{ t('landing.footer.bottom') }}
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { RouterLink } from 'vue-router'
import LandingLogo from './LandingLogo.vue'
import {
  CONTACT_PHONE,
  DEMO_URL,
  TELEGRAM_URL,
  TEL_HREF,
  TRIAL_URL,
  whatsappHref,
} from '@/config/landing.js'

const { t } = useI18n()

const year = new Date().getFullYear()

const COLUMNS = computed(() => [
  {
    titleKey: 'landing.footer.productTitle',
    links: [
      { to: { name: 'landing', hash: '#product' }, labelKey: 'landing.nav.product' },
      { to: { name: 'landing', hash: '#services' }, labelKey: 'landing.nav.services' },
      { to: { name: 'landing', hash: '#package' }, labelKey: 'landing.nav.package' },
      { to: { name: 'landing', hash: '#faq' }, labelKey: 'landing.footer.faq' },
    ],
  },
  {
    titleKey: 'landing.footer.startTitle',
    links: [
      { href: DEMO_URL, labelKey: 'landing.hero.ctaDemo' },
      { href: TRIAL_URL, labelKey: 'landing.hero.ctaTrial' },
      { href: '/login', labelKey: 'landing.footer.login' },
    ],
  },
  {
    titleKey: 'landing.footer.contactTitle',
    links: [
      { to: { name: 'contact' }, labelKey: 'landing.nav.contact' },
      { href: TEL_HREF, label: CONTACT_PHONE, ltr: true },
      { href: whatsappHref(t('landing.contact.whatsappMessage')), labelKey: 'landing.contact.whatsapp', external: true },
      { href: TELEGRAM_URL, labelKey: 'landing.contact.telegram', external: true },
    ],
  },
])
</script>
