<template>
  <div class="ws-page ws-onepage">
    <component :is="header.component" v-if="header" :content="header.content" />

    <nav v-if="body.length > 1" class="ws-onepage__dots" :aria-label="$t('website.chrome.sectionNav')">
      <button
        v-for="(section, i) in body"
        :key="key(section)"
        type="button"
        :class="{ 'is-active': i === active }"
        :aria-label="section.type"
        @click="scrollTo(i)"
      />
    </nav>

    <main>
      <div
        v-for="(section, i) in body"
        :key="key(section)"
        :ref="(el) => setRef(el, i)"
        class="ws-onepage__panel"
      >
        <component :is="section.component" :content="section.content" />
      </div>
    </main>

    <component :is="footer.component" v-if="footer" :content="footer.content" />
  </div>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { sectionKey as key, usePageSections } from './_chrome.js'

/**
 * A scroll-through page with a progress rail.
 *
 * Deliberately not scroll-snapped: a rates board can be taller than the
 * viewport, and snapping would make part of it unreachable.
 */
const { header, footer, body } = usePageSections()
const panels = ref([])
const active = ref(0)
let observer = null

function setRef(el, index) {
  if (el) panels.value[index] = el
}

function scrollTo(index) {
  panels.value[index]?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue
        const index = panels.value.indexOf(entry.target)
        if (index !== -1) active.value = index
      }
    },
    { rootMargin: '-45% 0px -45% 0px' },
  )
  panels.value.forEach((panel) => panel && observer.observe(panel))
})

onBeforeUnmount(() => observer?.disconnect())
</script>

<style scoped>
.ws-onepage__dots {
  position: fixed;
  inset-inline-end: 22px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 15;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ws-onepage__dots button {
  width: 9px;
  height: 9px;
  padding: 0;
  border: 0;
  border-radius: 50%;
  background: var(--ws-border-strong);
  cursor: pointer;
  transition: background 0.2s ease, height 0.2s ease;
}

.ws-onepage__dots button.is-active {
  background: var(--ws-primary);
  height: 24px;
  border-radius: 999px;
}

@container ws (max-width: 900px) {
  .ws-onepage__dots {
    display: none;
  }
}
</style>
