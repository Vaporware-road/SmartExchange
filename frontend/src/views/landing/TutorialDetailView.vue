<template>
  <div ref="root" class="lp">
    <LandingNav />

    <main class="py-16 sm:py-20">
      <div class="lp-container max-w-3xl">
        <RouterLink :to="{ name: 'tutorials' }" class="lp-navlink text-sm">
          ← {{ t('landing.tutorials.backToIndex') }}
        </RouterLink>

        <template v-if="post">
          <h1 class="mt-6 text-2xl font-bold leading-snug sm:text-[2rem]">{{ copy('title') }}</h1>
          <p class="mt-3 text-xs font-semibold uppercase tracking-[0.18em]" style="color: var(--primary)">
            {{ post.icon }} {{ t('landing.tutorials.minutes', { count: post.minutes }) }}
          </p>
          <p class="mt-5 text-[0.95rem] leading-7" style="color: var(--text-secondary)">{{ copy('intro') }}</p>

          <img
            :src="GIF_BASE + post.gif"
            :alt="copy('title')"
            class="lp-card mt-8 w-full !p-0"
            loading="lazy"
            decoding="async"
          />

          <h2 class="mt-12 text-xl font-bold">{{ t('landing.tutorials.steps') }}</h2>
          <ol class="mt-6 space-y-6">
            <li v-for="(step, index) in post.steps" :key="step" class="flex gap-4" data-reveal>
              <span
                class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-sm font-bold"
                style="background: var(--glass-bg); color: var(--primary); border: 1px solid var(--border-card)"
              >{{ index + 1 }}</span>
              <div>
                <h3 class="font-semibold">{{ copy(`steps.${step}.title`) }}</h3>
                <p class="mt-2 text-sm leading-7" style="color: var(--text-secondary)">
                  {{ copy(`steps.${step}.body`) }}
                </p>
              </div>
            </li>
          </ol>

          <div class="lp-card mt-12 text-center">
            <p class="text-[0.95rem] leading-7">{{ copy('outro') }}</p>
            <a :href="TRIAL_URL" class="lp-btn lp-btn--primary mt-6">{{ t('landing.hero.ctaTrial') }}</a>
          </div>

          <nav v-if="others.length" class="mt-14">
            <h2 class="text-xl font-bold">{{ t('landing.tutorials.more') }}</h2>
            <ul class="mt-4 space-y-2">
              <li v-for="other in others" :key="other.slug">
                <RouterLink :to="{ name: 'tutorial', params: { slug: other.slug } }" class="lp-navlink">
                  {{ other.icon }} {{ t(`landing.tutorials.posts.${other.slug}.title`) }}
                </RouterLink>
              </li>
            </ul>
          </nav>
        </template>

        <p v-else class="mt-10 text-[0.95rem]" style="color: var(--text-secondary)">
          {{ t('landing.tutorials.notFound') }}
        </p>
      </div>
    </main>

    <LandingFooter />
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { RouterLink, useRoute } from 'vue-router'
import LandingFooter from './components/LandingFooter.vue'
import LandingNav from './components/LandingNav.vue'
import { useReveal } from './composables/useReveal.js'
import { findTutorial, GIF_BASE, TUTORIALS } from '@/content/tutorials'
import { TRIAL_URL } from '@/config/landing.js'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import './landing.css'

const { t } = useI18n()
const route = useRoute()
const root = ref(null)
useReveal(root)

const post = computed(() => findTutorial(route.params.slug))
const others = computed(() => TUTORIALS.filter((row) => row.slug !== route.params.slug))

function copy(suffix) {
  return t(`landing.tutorials.posts.${post.value.slug}.${suffix}`)
}

onMounted(() => {
  useSiteSettingsStore().fetch()
})
</script>
