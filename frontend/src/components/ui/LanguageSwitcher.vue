<template>
  <div ref="rootRef" class="relative">
    <button
      class="inline-flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-xl text-sm font-medium transition-all duration-300 ease-in-out border hover:scale-105 min-w-[3.75rem]"
      style="background: var(--bg-card); border-color: var(--border-color); color: var(--primary);"
      :title="$t('lang.' + locale)"
      @click="open = !open"
    >
      <i class="fas fa-globe text-xs" />
      <span>{{ localeLabel(locale) }}</span>
    </button>
    <Transition name="fade-slide">
      <div
        v-if="open"
        class="absolute end-0 top-full mt-2 z-50 min-w-[8rem] rounded-xl border py-1 shadow-lg"
        style="background: var(--bg-card); border-color: var(--border-color);"
      >
        <button
          v-for="loc in locales"
          :key="loc"
          class="flex w-full items-center gap-2 px-3 py-2 text-sm transition-colors hover:bg-[var(--bg-hover)] ltr:text-left rtl:text-right"
          :class="locale === loc ? 'text-[var(--primary)] font-semibold' : 'text-[var(--text-secondary)]'"
          @click="selectLocale(loc)"
        >
          <span>{{ $t('lang.' + loc) }}</span>
          <i v-if="locale === loc" class="fas fa-check text-xs ms-auto" />
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useI18n } from 'vue-i18n'
import { SUPPORTED_LOCALES } from '@/i18n'
import { setLocale } from '@/i18n'

const { locale } = useI18n({ useScope: 'global' })
const locales = SUPPORTED_LOCALES
const open = ref(false)
const rootRef = ref(null)

function localeLabel(code) {
  return code.toUpperCase()
}

function selectLocale(code) {
  setLocale(code)
  open.value = false
}

function onDocumentClick(e) {
  if (rootRef.value && !rootRef.value.contains(e.target)) {
    open.value = false
  }
}

onMounted(() => document.addEventListener('click', onDocumentClick))
onBeforeUnmount(() => document.removeEventListener('click', onDocumentClick))
</script>