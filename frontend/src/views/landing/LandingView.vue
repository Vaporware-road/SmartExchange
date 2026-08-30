<template>
  <div ref="root" class="lp">
    <div class="lp-progress" :style="{ transform: `scaleX(${progress})` }" aria-hidden="true" />

    <LandingNav />
    <LandingTicker />

    <main>
      <LandingHero />
      <LandingStats />
      <LandingFeatures />
      <LandingFlow />
      <LandingChannels />
      <LandingDemo />
      <LandingPricing />
      <LandingPackage />
      <LandingTelegram />
      <LandingFaq />
      <LandingContact />
    </main>

    <LandingFooter />
  </div>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import LandingChannels from './components/LandingChannels.vue'
import LandingContact from './components/LandingContact.vue'
import LandingDemo from './components/LandingDemo.vue'
import LandingFaq from './components/LandingFaq.vue'
import LandingFeatures from './components/LandingFeatures.vue'
import LandingFlow from './components/LandingFlow.vue'
import LandingFooter from './components/LandingFooter.vue'
import LandingHero from './components/LandingHero.vue'
import LandingNav from './components/LandingNav.vue'
import LandingPackage from './components/LandingPackage.vue'
import LandingPricing from './components/LandingPricing.vue'
import LandingStats from './components/LandingStats.vue'
import LandingTelegram from './components/LandingTelegram.vue'
import LandingTicker from './components/LandingTicker.vue'
import { useReveal } from './composables/useReveal.js'
import './landing.css'

const { t } = useI18n()

const root = ref(null)
useReveal(root)

const progress = ref(0)

function onScroll() {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight
  progress.value = scrollable > 0 ? Math.min(window.scrollY / scrollable, 1) : 0
}

onMounted(() => {
  document.title = t('landing.meta.title')
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})

onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>
