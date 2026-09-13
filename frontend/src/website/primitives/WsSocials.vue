<template>
  <div v-if="links.length" class="ws-socials">
    <a v-for="link in links" :key="link.key" :href="link.href" target="_blank" rel="noopener" :aria-label="link.key">
      <i :class="link.icon" aria-hidden="true" />
    </a>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useSiteContext } from '../composables/useSiteContext.js'

const { branding } = useSiteContext()

const ICONS = {
  telegram: 'fab fa-telegram',
  instagram: 'fab fa-instagram',
  twitter: 'fab fa-x-twitter',
  linkedin: 'fab fa-linkedin',
}

const links = computed(() =>
  Object.entries(branding.value.socials || {})
    .filter(([, href]) => href)
    .map(([key, href]) => ({ key, href, icon: ICONS[key] || 'fas fa-link' })),
)
</script>

<style scoped>
.ws-socials {
  display: flex;
  gap: 10px;
}

.ws-socials a {
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border-radius: var(--ws-radius-sm);
  border: 1px solid var(--ws-border);
  color: var(--ws-text-muted);
  transition: color 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
}

.ws-socials a:hover {
  color: var(--ws-primary);
  border-color: var(--ws-primary);
  transform: translateY(-2px);
}
</style>
