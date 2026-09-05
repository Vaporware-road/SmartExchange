<template>
  <div ref="root" class="lp">
    <LandingNav />

    <main class="py-16 sm:py-20">
      <div class="lp-container">
        <LandingSectionHead
          :eyebrow="t('landing.nav.tutorials')"
          :title="t('landing.tutorials.title')"
          :subtitle="t('landing.tutorials.subtitle')"
        />

        <div class="grid gap-6 sm:grid-cols-2">
          <RouterLink
            v-for="post in TUTORIALS"
            :key="post.slug"
            :to="{ name: 'tutorial', params: { slug: post.slug } }"
            class="lp-card group block overflow-hidden !p-0"
            data-reveal
          >
            <img
              :src="GIF_BASE + post.gif"
              :alt="t(`landing.tutorials.posts.${post.slug}.title`)"
              class="aspect-video w-full object-cover"
              loading="lazy"
              decoding="async"
            />
            <div class="p-6">
              <p class="text-xs font-semibold uppercase tracking-[0.18em]" style="color: var(--primary)">
                {{ post.icon }} {{ t('landing.tutorials.minutes', { count: post.minutes }) }}
              </p>
              <h3 class="mt-3 text-lg font-bold leading-snug">
                {{ t(`landing.tutorials.posts.${post.slug}.title`) }}
              </h3>
              <p class="mt-3 text-sm leading-7" style="color: var(--text-secondary)">
                {{ t(`landing.tutorials.posts.${post.slug}.summary`) }}
              </p>
              <p class="mt-4 text-sm font-semibold" style="color: var(--primary)">
                {{ t('landing.tutorials.readMore') }} →
              </p>
            </div>
          </RouterLink>
        </div>

        <div class="mt-14 text-center">
          <a :href="TRIAL_URL" class="lp-btn lp-btn--primary">{{ t('landing.hero.ctaTrial') }}</a>
        </div>
      </div>
    </main>

    <LandingFooter />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { RouterLink } from 'vue-router'
import LandingFooter from './components/LandingFooter.vue'
import LandingNav from './components/LandingNav.vue'
import LandingSectionHead from './components/LandingSectionHead.vue'
import { useReveal } from './composables/useReveal.js'
import { GIF_BASE, TUTORIALS } from '@/content/tutorials'
import { TRIAL_URL } from '@/config/landing.js'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import './landing.css'

const { t } = useI18n()
const root = ref(null)
useReveal(root)

onMounted(() => {
  useSiteSettingsStore().fetch()
})
</script>
