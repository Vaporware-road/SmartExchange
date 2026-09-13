<template>
  <div v-if="locales.length > 1" class="ws-lang">
    <button
      v-for="code in locales"
      :key="code"
      type="button"
      class="ws-lang__btn"
      :class="{ 'is-active': code === locale }"
      @click="setLocale(code)"
    >
      {{ code.toUpperCase() }}
    </button>
  </div>
</template>

<script setup>
import { useSiteContext } from '../composables/useSiteContext.js'

/** Only rendered when the desk actually publishes in more than one language. */
const { locales, locale, setLocale } = useSiteContext()
</script>

<style scoped>
.ws-lang {
  display: inline-flex;
  border: 1px solid var(--ws-border);
  border-radius: 999px;
  overflow: hidden;
}

.ws-lang__btn {
  border: 0;
  background: transparent;
  color: var(--ws-text-muted);
  font: inherit;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  padding: 0.42em 0.85em;
  cursor: pointer;
  transition: background 0.18s ease, color 0.18s ease;
}

.ws-lang__btn.is-active {
  background: var(--ws-primary);
  color: var(--ws-on-primary);
}
</style>
