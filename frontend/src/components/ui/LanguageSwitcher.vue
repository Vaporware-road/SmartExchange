<template>
  <div ref="rootRef" class="relative">
    <button
      ref="triggerRef"
      type="button"
      class="inline-flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-xl text-sm font-medium transition-all duration-300 ease-in-out border hover:scale-105"
      style="background: var(--bg-card); border-color: var(--border-color); color: var(--primary);"
      :aria-expanded="open ? 'true' : 'false'"
      :aria-label="$t('header.selectLanguage')"
      @click="toggleOpen"
    >
      <i class="fas fa-globe text-xs" />
      <span>{{ currentMeta.shortLabel }}</span>
      <i
        class="fas fa-chevron-down text-[10px] opacity-70 transition-transform"
        :class="{ 'rotate-180': open }"
      />
    </button>

    <Teleport to="body">
      <div
        v-if="open"
        ref="panelRef"
        class="fixed z-[120] min-w-[168px] rounded-xl border border-[var(--border-card)] bg-[var(--bg-card)] p-1.5 shadow-lg"
        :style="panelStyle"
      >
        <ul role="listbox" :aria-label="$t('header.selectLanguage')">
          <li v-for="item in LOCALES" :key="item.code" role="option" :aria-selected="item.code === locale">
            <button
              type="button"
              class="flex w-full items-center gap-2 rounded-lg px-3 py-2 text-sm transition-colors"
              :class="item.code === locale
                ? 'bg-primary-muted text-[var(--primary)] font-medium'
                : 'text-[var(--text-secondary)] hover:bg-[var(--bg-hover)] hover:text-[var(--text-primary)]'"
              @click="pick(item.code)"
            >
              <span class="w-7 text-xs font-semibold opacity-70">{{ item.shortLabel }}</span>
              <span class="flex-1 text-start">{{ item.label }}</span>
              <i v-if="item.code === locale" class="fas fa-check text-xs text-[var(--primary)]" />
            </button>
          </li>
        </ul>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { setLocale } from '@/i18n'
import { getLocaleMeta, LOCALES } from '@/constants/locales.js'

const { locale } = useI18n({ useScope: 'global' })

const rootRef = ref(null)
const triggerRef = ref(null)
const panelRef = ref(null)
const open = ref(false)
const panelStyle = ref({})

const currentMeta = computed(() => getLocaleMeta(locale.value))

function toggleOpen() {
  open.value ? close() : show()
}

function show() {
  open.value = true
  nextTick(updatePanelPosition)
}

function close() {
  open.value = false
}

function pick(code) {
  setLocale(code)
  close()
}

function onWindowClick(event) {
  if (!open.value) return
  if (rootRef.value?.contains(event.target)) return
  if (panelRef.value?.contains(event.target)) return
  close()
}

function updatePanelPosition() {
  const trigger = triggerRef.value
  if (!trigger) return

  const rect = trigger.getBoundingClientRect()
  const viewportW = window.innerWidth
  const viewportH = window.innerHeight
  const sidePadding = 12
  const gap = 8
  const width = 180

  let left = rect.right - width
  if (left < sidePadding) left = sidePadding
  if (left + width > viewportW - sidePadding) left = viewportW - sidePadding - width

  const spaceBelow = viewportH - rect.bottom - sidePadding
  const spaceAbove = rect.top - sidePadding
  const openUp = spaceBelow < 200 && spaceAbove > spaceBelow
  const top = openUp
    ? Math.max(sidePadding, rect.top - gap)
    : Math.min(viewportH - sidePadding, rect.bottom + gap)

  panelStyle.value = {
    width: `${width}px`,
    left: `${left}px`,
    top: `${top}px`,
    transform: openUp ? 'translateY(-100%)' : 'none',
  }
}

function onViewportChange() {
  if (!open.value) return
  updatePanelPosition()
}

onMounted(() => {
  window.addEventListener('click', onWindowClick)
  window.addEventListener('resize', onViewportChange)
  window.addEventListener('scroll', onViewportChange, true)
})

onBeforeUnmount(() => {
  window.removeEventListener('click', onWindowClick)
  window.removeEventListener('resize', onViewportChange)
  window.removeEventListener('scroll', onViewportChange, true)
})

watch(open, (isOpen) => {
  if (!isOpen) return
  nextTick(updatePanelPosition)
})
</script>
