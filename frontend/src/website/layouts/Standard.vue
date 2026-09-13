<template>
  <div class="ws-page">
    <component :is="header.component" v-if="header" :content="header.content" />
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
</template>

<script setup>
import { sectionKey as key, usePageSections } from './_chrome.js'

/** The plain stacked page. Most layouts use it; the variants do the work. */
const { header, footer, body } = usePageSections()
</script>
