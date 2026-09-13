<template>
  <header class="ws-nav" :class="{ 'ws-nav--sticky': content.sticky !== false }">
    <div class="ws-container ws-navs">
      <nav class="ws-navs__side ws-navs__side--start">
        <a v-for="(link, i) in leftLinks" :key="i" :href="link.href">{{ t(link.label) }}</a>
      </nav>
      <WsLogo v-if="content.show_logo !== false" with-name class="ws-navs__logo" />
      <nav class="ws-navs__side ws-navs__side--end">
        <a v-for="(link, i) in rightLinks" :key="i" :href="link.href">{{ t(link.label) }}</a>
        <WsLanguage v-if="content.show_language !== false" />
        <WsButton v-if="cta" :href="content.cta_href">{{ cta }}</WsButton>
      </nav>
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
/* The logo sits in the middle, so the links divide around it. */
const half = computed(() => Math.ceil(links.value.length / 2))
const leftLinks = computed(() => links.value.slice(0, half.value))
const rightLinks = computed(() => links.value.slice(half.value))
const cta = computed(() => t(props.content.cta_label))
</script>

<style scoped>
.ws-navs {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 20px;
  padding-block: 18px;
}

.ws-navs__side {
  display: flex;
  align-items: center;
  gap: 22px;
  font-size: 0.92rem;
}

.ws-navs__side--end {
  justify-content: flex-end;
}

.ws-navs__side a {
  color: var(--ws-text-muted);
}

.ws-navs__side a:hover {
  color: var(--ws-primary);
}

.ws-navs__logo {
  font-size: 1.25rem;
}

@container ws (max-width: 860px) {
  .ws-navs {
    grid-template-columns: auto 1fr;
  }
  .ws-navs__side {
    display: none;
  }
}
</style>
