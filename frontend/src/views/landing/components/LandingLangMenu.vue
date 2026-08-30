<template>
  <!-- `relative` on the wrapper is the whole fix for the old switcher: the menu
       is anchored to the button inside the header instead of being positioned
       against the page, which is why it used to spill outside the bar. -->
  <div ref="root" class="relative">
    <button
      type="button"
      class="lp-btn lp-btn--ghost !px-3 !py-2 !text-[0.8rem]"
      :aria-label="t('landing.nav.language')"
      :aria-expanded="open"
      aria-haspopup="listbox"
      @click="open = !open"
    >
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
        <circle cx="12" cy="12" r="9" />
        <path d="M3 12h18M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18" />
      </svg>
      <span class="hidden sm:inline">{{ current.label }}</span>
    </button>

    <transition name="lp-fade">
      <ul
        v-if="open"
        class="absolute end-0 top-[calc(100%+0.5rem)] z-50 min-w-[9.5rem] overflow-hidden rounded-xl border py-1 shadow-lg"
        style="background: var(--bg-card); border-color: var(--border-card)"
        role="listbox"
      >
        <li v-for="option in options" :key="option.code">
          <button
            type="button"
            class="flex w-full items-center justify-between px-3.5 py-2 text-start text-sm transition-colors"
            :style="option.code === locale
              ? { color: 'var(--primary)', background: 'var(--primary-muted)' }
              : { color: 'var(--text-primary)' }"
            role="option"
            :aria-selected="option.code === locale"
            @click="choose(option.code)"
          >
            <span>{{ option.label }}</span>
            <span class="text-[0.7rem] uppercase" style="color: var(--text-secondary)">{{ option.code }}</span>
          </button>
        </li>
      </ul>
    </transition>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { setLocale, SUPPORTED_LOCALES } from '@/i18n'

const { t, locale } = useI18n()

/** Endonyms — a visitor looking for their language recognises it in its own script. */
const LABELS = {
  en: 'English',
  fa: 'فارسی',
  ar: 'العربية',
  tr: 'Türkçe',
  de: 'Deutsch',
  fr: 'Français',
  es: 'Español',
}

const options = SUPPORTED_LOCALES.map((code) => ({ code, label: LABELS[code] ?? code }))
const current = computed(() => options.find((o) => o.code === locale.value) ?? options[0])

const open = ref(false)
const root = ref(null)

function choose(code) {
  setLocale(code)
  open.value = false
}

function onDocumentPointer(event) {
  if (!open.value || root.value?.contains(event.target)) return
  open.value = false
}

function onKeydown(event) {
  if (event.key === 'Escape') open.value = false
}

onMounted(() => {
  document.addEventListener('click', onDocumentPointer)
  document.addEventListener('keydown', onKeydown)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onDocumentPointer)
  document.removeEventListener('keydown', onKeydown)
})
</script>

<style scoped>
.lp-fade-enter-active,
.lp-fade-leave-active {
  transition: opacity 0.18s ease, transform 0.18s ease;
}
.lp-fade-enter-from,
.lp-fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
