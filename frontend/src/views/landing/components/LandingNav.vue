<template>
  <header
    class="sticky top-0 z-50 border-b transition-colors duration-300"
    :class="scrolled ? 'backdrop-blur-xl' : 'border-transparent'"
    :style="scrolled ? { background: 'var(--glass-bg)', borderColor: 'var(--border-card)' } : { background: 'transparent' }"
  >
    <div class="lp-container flex h-16 items-center gap-4">
      <RouterLink :to="{ name: 'landing', hash: '#top' }" class="shrink-0" aria-label="MrExchange">
        <LandingLogo :size="30" eager />
      </RouterLink>

      <nav class="hidden flex-1 items-center justify-center gap-7 lg:flex" :aria-label="t('landing.nav.label')">
        <RouterLink
          v-for="link in LINKS"
          :key="link.labelKey"
          :to="link.to"
          class="lp-navlink"
          :class="{ 'lp-navlink--active': isActive(link) }"
        >{{ t(link.labelKey) }}</RouterLink>
      </nav>

      <div class="ms-auto flex items-center gap-2 lg:ms-0">
        <LandingLangMenu />

        <!-- `.lp-btn` sets `display: inline-flex`, which ties with Tailwind's
             `hidden` on specificity. The breakpoint toggle therefore lives on a
             wrapper with no display rule of its own, where `hidden` wins. -->
        <span class="hidden sm:block">
          <a :href="DEMO_URL" class="lp-btn lp-btn--primary !px-4 !py-2 !text-[0.82rem]">
            {{ t('landing.nav.cta') }}
          </a>
        </span>

        <span class="block lg:hidden">
          <button
            type="button"
            class="lp-btn lp-btn--ghost !p-2"
            :aria-label="t('landing.nav.menu')"
            :aria-expanded="open"
            aria-controls="lp-mobile-nav"
            @click="open = !open"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path v-if="!open" d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round" />
              <path v-else d="M6 6l12 12M18 6L6 18" stroke-linecap="round" />
            </svg>
          </button>
        </span>
      </div>
    </div>

    <div
      v-show="open"
      id="lp-mobile-nav"
      class="border-t lg:hidden"
      style="background: var(--bg-card); border-color: var(--border-card)"
    >
      <nav class="lp-container flex flex-col py-3" :aria-label="t('landing.nav.label')">
        <RouterLink
          v-for="link in LINKS"
          :key="link.labelKey"
          :to="link.to"
          class="py-2.5 text-sm font-medium"
          style="color: var(--text-primary)"
          @click="open = false"
        >{{ t(link.labelKey) }}</RouterLink>
        <a :href="TEL_HREF" dir="ltr" class="py-2.5 text-sm font-semibold" style="color: var(--primary)">
          {{ CONTACT_PHONE }}
        </a>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { RouterLink, useRoute } from 'vue-router'
import LandingLangMenu from './LandingLangMenu.vue'
import LandingLogo from './LandingLogo.vue'
import { CONTACT_PHONE, DEMO_URL, TEL_HREF } from '@/config/landing.js'

const { t } = useI18n()
const route = useRoute()

/**
 * Four destinations, deliberately. The old nav carried seven links plus a phone
 * number and a language button, which is what made it read as clutter; the
 * phone moved to the contact page and the mobile drawer.
 *
 * The section links are router targets rather than bare `#hash` hrefs because
 * this nav also renders on /contact, where the sections do not exist — routing
 * to the landing page with a hash works from either page.
 */
const LINKS = [
  { to: { name: 'landing', hash: '#product' }, labelKey: 'landing.nav.product' },
  { to: { name: 'landing', hash: '#services' }, labelKey: 'landing.nav.services' },
  { to: { name: 'landing', hash: '#package' }, labelKey: 'landing.nav.package' },
  { to: { name: 'contact' }, labelKey: 'landing.nav.contact' },
]

/** Only the whole-page destinations light up; hashes are positions, not pages. */
function isActive(link) {
  return !link.to.hash && route.name === link.to.name
}

const open = ref(false)
const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 12
}

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})

onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>
