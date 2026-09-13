<template>
  <header class="ws-nav ws-nav--floating">
    <div class="ws-container ws-navf">
      <WsLogo v-if="content.show_logo !== false" with-name />
      <nav class="ws-navf__links">
        <a v-for="(link, i) in links" :key="i" :href="link.href">{{ t(link.label) }}</a>
      </nav>
      <div class="ws-navf__end">
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
.ws-navf {
  display: flex;
  align-items: center;
  gap: 22px;
  padding-block: 10px;
}

.ws-navf__links {
  display: flex;
  gap: 24px;
  margin-inline: auto;
  font-size: 0.92rem;
}

.ws-navf__links a {
  color: var(--ws-text-muted);
}

.ws-navf__links a:hover {
  color: var(--ws-primary);
}

.ws-navf__end {
  display: flex;
  align-items: center;
  gap: 10px;
}

@container ws (max-width: 860px) {
  .ws-navf__links,
  .ws-navf__end {
    display: none;
  }
}
</style>
