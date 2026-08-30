<template>
  <section id="contact" class="py-20">
    <div class="lp-container">
      <div class="lp-card mx-auto max-w-3xl p-8 text-center sm:p-12" data-reveal>
        <h2 class="text-2xl font-bold leading-snug sm:text-[1.9rem]">{{ t('landing.contact.title') }}</h2>
        <p class="mx-auto mt-4 max-w-xl text-sm leading-8" style="color: var(--text-secondary)">
          {{ t('landing.contact.subtitle') }}
        </p>

        <div class="mt-8 flex flex-wrap justify-center gap-3">
          <a :href="TEL_HREF" dir="ltr" class="lp-btn lp-btn--ghost">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.46.57 3.6a1 1 0 0 1-.25 1z" />
            </svg>
            {{ CONTACT_PHONE }}
          </a>

          <a :href="whatsappLink" target="_blank" rel="noopener" class="lp-btn lp-btn--whatsapp">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z" />
            </svg>
            {{ t('landing.contact.whatsapp') }}
          </a>

          <a :href="TELEGRAM_URL" target="_blank" rel="noopener" class="lp-btn lp-btn--telegram">
            ✈️ {{ t('landing.contact.telegram') }}
          </a>

          <a :href="DEMO_URL" class="lp-btn lp-btn--primary">{{ t('landing.hero.ctaDemo') }}</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { CONTACT_PHONE, DEMO_URL, TELEGRAM_URL, TEL_HREF, whatsappHref } from '@/config/landing.js'

const { t } = useI18n()

/** The greeting follows the visitor's language, so the chat opens in it too. */
const whatsappLink = computed(() => whatsappHref(t('landing.contact.whatsappMessage')))
</script>
