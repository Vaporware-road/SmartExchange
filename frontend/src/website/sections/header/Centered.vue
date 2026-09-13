<template>
  <header class="ws-nav" :class="{ 'ws-nav--sticky': content.sticky !== false }">
    <div class="ws-container ws-navc">
      <div class="ws-navc__top">
        <WsLanguage v-if="content.show_language !== false" />
        <WsLogo v-if="content.show_logo !== false" with-name class="ws-navc__logo" />
        <WsButton v-if="cta" :href="content.cta_href">{{ cta }}</WsButton>
        <WsNavToggle v-model="open" />
      </div>
      <nav v-if="links.length" class="ws-navc__links">
        <a v-for="(link, i) in links" :key="i" :href="link.href">{{ t(link.label) }}</a>
      </nav>
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
.ws-navc {
  padding-block: 16px;
}

.ws-navc__top {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
}

.ws-navc__logo {
  justify-self: center;
  font-size: 1.3rem;
}

.ws-navc__top > :last-child {
  justify-self: end;
}

.ws-navc__links {
  display: flex;
  justify-content: center;
  gap: 30px;
  padding-top: 14px;
  margin-top: 14px;
  border-top: 1px solid var(--ws-border);
  font-size: 0.93rem;
}

.ws-navc__links a {
  color: var(--ws-text-muted);
}

.ws-navc__links a:hover {
  color: var(--ws-primary);
}

@container ws (max-width: 860px) {
  .ws-navc__links {
    display: none;
  }
  .ws-navc__top {
    grid-template-columns: auto 1fr auto;
  }
  .ws-navc__logo {
    justify-self: start;
  }
}
</style>
