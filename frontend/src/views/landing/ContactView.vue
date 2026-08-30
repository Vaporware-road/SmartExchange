<template>
  <div ref="root" class="lp">
    <LandingNav />

    <main>
      <section class="lp-contact-hero py-20 sm:py-24">
        <div class="lp-container relative text-center">
          <div class="flex justify-center" data-reveal>
            <span class="lp-contact-mark lp-float">
              <LandingLogo :size="46" eager />
            </span>
          </div>

          <p class="mt-8 text-xs font-semibold uppercase tracking-[0.18em]" style="color: var(--primary)" data-reveal>
            {{ t('landing.contactPage.eyebrow') }}
          </p>

          <h1 class="mt-3 text-3xl font-extrabold leading-tight sm:text-[2.6rem]" data-reveal>
            {{ t('landing.contactPage.title') }}
            <span class="lp-accent">{{ t('landing.contactPage.titleAccent') }}</span>
          </h1>

          <p
            class="mx-auto mt-5 max-w-2xl text-sm leading-8 sm:text-[0.95rem]"
            style="color: var(--text-secondary)"
            data-reveal
          >
            {{ t('landing.contactPage.subtitle') }}
          </p>

          <!-- Arrived from a "start free trial" button: say what happens next. -->
          <div v-if="wantsTrial" class="lp-card mx-auto mt-8 max-w-2xl p-6 text-start" data-reveal>
            <p class="text-xs font-semibold uppercase tracking-[0.18em]" style="color: var(--primary)">
              {{ t('landing.contactPage.trial.eyebrow') }}
            </p>
            <h2 class="mt-2 text-lg font-bold">{{ t('landing.contactPage.trial.title') }}</h2>
            <p class="mt-3 text-sm leading-8" style="color: var(--text-secondary)">
              {{ t('landing.contactPage.trial.text') }}
            </p>
          </div>
        </div>
      </section>

      <section class="pb-4">
        <div class="lp-container grid gap-5 md:grid-cols-3">
          <a
            v-for="channel in channels"
            :key="channel.key"
            :href="channel.href"
            :dir="channel.ltr ? 'ltr' : undefined"
            :target="channel.external ? '_blank' : undefined"
            :rel="channel.external ? 'noopener' : undefined"
            class="lp-card lp-contact-card p-7"
            :style="{ '--lp-brand': channel.brand }"
            data-reveal
          >
            <span class="lp-contact-card__icon" aria-hidden="true" v-html="channel.icon" />

            <h2 class="mt-5 text-base font-bold">{{ t(`landing.contactPage.channels.${channel.key}.name`) }}</h2>
            <p class="mt-2 text-xs leading-6" style="color: var(--text-secondary)">
              {{ t(`landing.contactPage.channels.${channel.key}.desc`) }}
            </p>

            <span class="lp-contact-card__handle" dir="ltr">{{ channel.handle }}</span>

            <span class="lp-contact-card__action">
              {{ t(`landing.contactPage.channels.${channel.key}.action`) }}
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
                <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </span>
          </a>
        </div>
      </section>

      <section class="py-14">
        <div class="lp-container grid gap-5 sm:grid-cols-3">
          <div v-for="fact in FACTS" :key="fact" class="lp-card p-6" data-reveal>
            <h3 class="text-sm font-semibold">{{ t(`landing.contactPage.facts.${fact}.title`) }}</h3>
            <p class="mt-2 text-xs leading-6" style="color: var(--text-secondary)">
              {{ t(`landing.contactPage.facts.${fact}.value`) }}
            </p>
          </div>
        </div>
      </section>

      <section class="pb-24">
        <div class="lp-container">
          <div class="lp-card mx-auto max-w-3xl p-8 text-center sm:p-12" data-reveal>
            <h2 class="text-2xl font-bold leading-snug sm:text-[1.9rem]">{{ t('landing.contactPage.ctaTitle') }}</h2>
            <p class="mx-auto mt-4 max-w-xl text-sm leading-8" style="color: var(--text-secondary)">
              {{ t('landing.contactPage.ctaText') }}
            </p>

            <div class="mt-8 flex flex-wrap justify-center gap-3">
              <a :href="DEMO_URL" class="lp-btn lp-btn--primary">{{ t('landing.hero.ctaDemo') }}</a>
              <RouterLink :to="{ name: 'landing', hash: '#package' }" class="lp-btn lp-btn--ghost">
                {{ t('landing.nav.package') }}
              </RouterLink>
            </div>
          </div>
        </div>
      </section>
    </main>

    <LandingFooter />
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { RouterLink, useRoute } from 'vue-router'
import LandingFooter from './components/LandingFooter.vue'
import LandingLogo from './components/LandingLogo.vue'
import LandingNav from './components/LandingNav.vue'
import { useReveal } from './composables/useReveal.js'
import {
  CONTACT_PHONE,
  DEMO_URL,
  TELEGRAM_CHANNEL,
  TELEGRAM_URL,
  TEL_HREF,
  whatsappHref,
} from '@/config/landing.js'
import './landing.css'

const { t } = useI18n()

const route = useRoute()
const wantsTrial = computed(() => route.query.intent === 'trial')

const root = ref(null)
useReveal(root)

/** Reassurance row under the channels; copy is `landing.contactPage.facts.<key>`. */
const FACTS = ['hours', 'languages', 'onboarding']

const ICONS = {
  telegram:
    '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M21.94 4.3 18.7 19.6c-.24 1.08-.88 1.35-1.79.84l-4.94-3.64-2.38 2.29c-.27.27-.5.5-1.01.5l.36-5.07 9.24-8.35c.4-.36-.09-.56-.62-.2L6.13 12.16 1.26 10.64c-1.06-.33-1.08-1.06.22-1.57l19.1-7.36c.88-.32 1.65.2 1.36 2.59z"/></svg>',
  whatsapp:
    '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>',
  phone:
    '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.46.57 3.6a1 1 0 0 1-.25 1z"/></svg>',
}

/** The WhatsApp greeting follows the visitor's language, so the chat opens in it. */
const channels = computed(() => [
  {
    key: 'telegram',
    href: TELEGRAM_URL,
    handle: TELEGRAM_CHANNEL,
    icon: ICONS.telegram,
    brand: '#229ed9',
    external: true,
  },
  {
    key: 'whatsapp',
    href: whatsappHref(t('landing.contact.whatsappMessage')),
    handle: CONTACT_PHONE,
    icon: ICONS.whatsapp,
    brand: '#25d366',
    external: true,
  },
  {
    key: 'phone',
    href: TEL_HREF,
    handle: CONTACT_PHONE,
    icon: ICONS.phone,
    brand: 'var(--primary)',
    ltr: true,
  },
])

onMounted(() => {
  document.title = t('landing.contactPage.metaTitle')
})
</script>
