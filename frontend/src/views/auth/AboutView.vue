<template>
  <main class="vapor-about">
    <div class="vapor-about__space" aria-hidden="true" />
    <div class="vapor-about__nebula" aria-hidden="true" />
    <div class="vapor-about__stars" aria-hidden="true" />
    <div class="vapor-about__grid" aria-hidden="true" />
    <div class="vapor-about__crt" aria-hidden="true" />
    <div class="vapor-about__scan" aria-hidden="true" />

    <div class="vapor-about__frame">
      <p class="vapor-about__tag">
        Every product is an opportunity to leave a lasting mark.
      </p>

      <GlitchTitle text="Vaporware-Road" />

      <nav class="vapor-about__links">
        <a :href="githubOrg" target="_blank" rel="noopener noreferrer">
          GitHub // Vaporware-road
        </a>
        <router-link to="/login">{{ $t('common.accessPanel') }}</router-link>
        <router-link to="/panel">{{ $t('common.backToApp') }}</router-link>
      </nav>
    </div>
  </main>
</template>

<script setup>
import GlitchTitle from '@/components/ui/GlitchTitle.vue'
import { VAPORWARE_GITHUB_ORG } from '@/constants/branding.js'

const githubOrg = VAPORWARE_GITHUB_ORG
</script>
