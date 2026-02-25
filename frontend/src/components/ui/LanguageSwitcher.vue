<template>
  <button
    class="inline-flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-xl text-sm font-medium transition-all duration-300 ease-in-out border hover:scale-105"
    style="background: var(--bg-card); border-color: var(--border-color); color: var(--primary);"
    :title="nextLabel"
    @click="toggle"
  >
    <i class="fas fa-globe text-xs" />
    <span>{{ currentLabel }}</span>
  </button>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { setLocale } from '@/i18n'

const { locale } = useI18n()

const currentLabel = computed(() => locale.value === 'fa' ? 'FA' : 'EN')
const nextLabel = computed(() => locale.value === 'fa' ? 'English' : 'فارسی')

function toggle() {
  setLocale(locale.value === 'fa' ? 'en' : 'fa')
}
</script>
