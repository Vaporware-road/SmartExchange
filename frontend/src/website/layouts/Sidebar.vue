<template>
  <div class="ws-page ws-sidebar">
    <aside class="ws-sidebar__rail">
      <WsLogo with-name />
      <nav v-if="links.length" class="ws-sidebar__nav">
        <a v-for="(link, i) in links" :key="i" :href="link.href">{{ t(link.label) }}</a>
      </nav>
      <div class="ws-sidebar__foot">
        <WsSocials />
        <WsLanguage />
      </div>
    </aside>

    <div class="ws-sidebar__body">
      <!-- On a narrow screen the rail cannot stay beside the content, so the
           layout's own header stands in for it. -->
      <component :is="header.component" v-if="header" :content="header.content" class="ws-sidebar__mobile-nav" />
      <main>
        <component
          :is="section.component"
          v-for="section in body"
          :key="key(section)"
          :content="section.content"
        />
      </main>
      <component :is="footer.component" v-if="footer" :content="footer.content" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import WsLogo from '../primitives/WsLogo.vue'
import WsSocials from '../primitives/WsSocials.vue'
import WsLanguage from '../primitives/WsLanguage.vue'
import { useSiteContext } from '../composables/useSiteContext.js'
import { sectionKey as key, usePageSections } from './_chrome.js'

const { header, footer, body } = usePageSections()
const { t } = useSiteContext()
const links = computed(() => header.value?.content?.nav_links || [])
</script>

<style scoped>
.ws-sidebar {
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  min-height: 100vh;
}

.ws-sidebar__rail {
  position: sticky;
  top: 0;
  align-self: start;
  height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 28px;
  padding: 34px 26px;
  border-inline-end: 1px solid var(--ws-border);
  background: var(--ws-bg-alt);
}

.ws-sidebar__nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ws-sidebar__nav a {
  color: var(--ws-text-muted);
  padding: 8px 12px;
  border-radius: var(--ws-radius-sm);
  transition: background 0.18s ease, color 0.18s ease;
}

.ws-sidebar__nav a:hover {
  background: color-mix(in srgb, var(--ws-primary) 12%, transparent);
  color: var(--ws-primary);
}

.ws-sidebar__foot {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ws-sidebar__body {
  min-width: 0;
}

.ws-sidebar__mobile-nav {
  display: none;
}

@container ws (max-width: 1000px) {
  .ws-sidebar {
    grid-template-columns: minmax(0, 1fr);
  }

  .ws-sidebar__rail {
    display: none;
  }

  .ws-sidebar__mobile-nav {
    display: block;
  }
}
</style>
