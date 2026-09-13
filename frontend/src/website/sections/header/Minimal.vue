<template>
  <header class="ws-nav ws-nav--minimal" :class="{ 'ws-nav--sticky': content.sticky !== false }">
    <div class="ws-container ws-nav__inner">
      <WsLogo v-if="content.show_logo !== false" with-name />
      <nav class="ws-nav__links">
        <a v-for="(link, i) in links" :key="i" :href="link.href">{{ t(link.label) }}</a>
      </nav>
      <div class="ws-nav__end">
        <WsLanguage v-if="content.show_language !== false" />
        <WsButton v-if="cta" :href="content.cta_href">{{ cta }}</WsButton>
      </div>
      <WsNavToggle v-model="open" />
    </div>
    <WsNavDrawer v-model="open" :links="links" :cta="cta" :cta-href="content.cta_href" />
  </header>
</template>

<script setup>
import { computed, ref } from 'vue'
import WsButton from '../../primitives/WsButton.vue'
import WsLogo from '../../primitives/WsLogo.vue'
import WsLanguage from '../../primitives/WsLanguage.vue'
import WsNavToggle from '../../primitives/WsNavToggle.vue'
import WsNavDrawer from '../../primitives/WsNavDrawer.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const open = ref(false)
const links = computed(() => props.content.nav_links || [])
const cta = computed(() => t(props.content.cta_label))
</script>

<style scoped>
.ws-nav__inner {
  display: flex;
  align-items: center;
  gap: 24px;
  padding-block: 18px;
}

.ws-nav__links {
  display: flex;
  gap: 26px;
  margin-inline-start: auto;
  font-size: 0.95rem;
}

.ws-nav__links a {
  color: var(--ws-text-muted);
  transition: color 0.18s ease;
}

.ws-nav__links a:hover {
  color: var(--ws-primary);
}

.ws-nav__end {
  display: flex;
  align-items: center;
  gap: 12px;
}

@container ws (max-width: 860px) {
  .ws-nav__links,
  .ws-nav__end {
    display: none;
  }
}
</style>
