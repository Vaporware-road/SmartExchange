<template>
  <div class="ws-page ws-splitpage">
    <component :is="header.component" v-if="header" :content="header.content" />

    <div class="ws-splitpage__frame">
      <!-- The opening section stays put while the rest of the page moves past
           it, which is the whole point of this layout. -->
      <div v-if="lead" class="ws-splitpage__lead">
        <component :is="lead.component" :content="lead.content" />
      </div>
      <main class="ws-splitpage__scroll">
        <component
          :is="section.component"
          v-for="section in rest"
          :key="key(section)"
          :content="section.content"
        />
      </main>
    </div>

    <component :is="footer.component" v-if="footer" :content="footer.content" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { sectionKey as key, usePageSections } from './_chrome.js'

const { header, footer, body } = usePageSections()
const lead = computed(() => body.value[0] || null)
const rest = computed(() => body.value.slice(1))
</script>

<style scoped>
.ws-splitpage__frame {
  display: grid;
  grid-template-columns: minmax(0, 0.92fr) minmax(0, 1.08fr);
  align-items: start;
}

.ws-splitpage__lead {
  position: sticky;
  top: 0;
  min-height: 100vh;
  display: grid;
  align-items: center;
  background: var(--ws-bg-alt);
  border-inline-end: 1px solid var(--ws-border);
}

.ws-splitpage__scroll {
  min-width: 0;
}

@container ws (max-width: 1000px) {
  .ws-splitpage__frame {
    grid-template-columns: minmax(0, 1fr);
  }

  .ws-splitpage__lead {
    position: static;
    min-height: 0;
    border-inline-end: 0;
    border-bottom: 1px solid var(--ws-border);
  }
}
</style>
