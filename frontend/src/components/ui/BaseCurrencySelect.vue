<template>
  <div ref="rootRef" class="relative w-full">
    <button
      ref="triggerRef"
      type="button"
      class="input-luxury flex w-full items-center justify-between gap-2 text-left"
      :class="{ 'opacity-60 cursor-not-allowed': disabled }"
      :disabled="disabled"
      :aria-expanded="open ? 'true' : 'false'"
      @click="toggleOpen"
    >
      <span class="inline-flex min-w-0 items-center gap-2">
        <span class="inline-flex h-6 w-6 shrink-0 items-center justify-center overflow-hidden rounded-md border border-[var(--border-card)] bg-[var(--bg-card)]">
          <img
            v-if="selectedIcon"
            :src="selectedIcon"
            :alt="selected?.code || 'currency'"
            class="h-4 w-4 object-contain"
          />
          <span v-else class="text-[10px] font-semibold text-[var(--text-secondary)]">
            {{ selected?.code?.slice(0, 2) || '--' }}
          </span>
        </span>
        <span v-if="selected" class="truncate text-[var(--text-primary)]">
          {{ selected.code }} - {{ selected.name }}
        </span>
        <span v-else class="truncate text-[var(--text-secondary)]">
          {{ placeholder }}
        </span>
      </span>
      <i class="fas fa-chevron-down text-xs text-[var(--text-secondary)] transition-transform" :class="{ 'rotate-180': open }" />
    </button>

    <Teleport to="body">
      <div
        v-if="open"
        ref="panelRef"
        class="fixed z-[120] rounded-xl border border-[var(--border-card)] bg-[var(--bg-card)] p-2 shadow-lg"
        :style="panelStyle"
      >
        <div class="mb-2">
          <input
            ref="searchRef"
            v-model.trim="search"
            type="text"
            class="input-luxury !py-2 text-sm"
            :placeholder="searchPlaceholder"
            @keydown.down.prevent="moveActive(1)"
            @keydown.up.prevent="moveActive(-1)"
            @keydown.enter.prevent="selectActive"
            @keydown.esc.prevent="close"
          />
        </div>

        <ul class="overflow-y-auto" :style="{ maxHeight: panelMaxHeight }">
          <li
            v-for="(item, index) in filteredOptions"
            :key="item.code"
          >
            <button
              type="button"
              class="flex w-full items-center gap-2 rounded-lg px-2 py-2 text-sm transition-colors"
              :class="index === activeIndex ? 'bg-primary-muted text-[var(--text-primary)]' : 'text-[var(--text-secondary)] hover:bg-primary-muted/70 hover:text-[var(--text-primary)]'"
              @mouseenter="activeIndex = index"
              @click="select(item)"
            >
              <span class="inline-flex h-6 w-6 shrink-0 items-center justify-center overflow-hidden rounded-md border border-[var(--border-card)] bg-[var(--bg-input)]">
                <img
                  v-if="iconFor(item.code)"
                  :src="iconFor(item.code)"
                  :alt="item.code"
                  class="h-4 w-4 object-contain"
                />
                <span v-else class="text-[10px] font-semibold">{{ item.code.slice(0, 2) }}</span>
              </span>
              <span class="min-w-0 flex-1 truncate text-left">{{ item.code }} - {{ item.name }}</span>
              <span v-if="item.symbol" class="text-xs opacity-80">{{ item.symbol }}</span>
            </button>
          </li>
          <li v-if="!filteredOptions.length" class="px-2 py-3 text-center text-xs text-[var(--text-secondary)]">
            {{ emptyText }}
          </li>
        </ul>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { getCurrencyIconByCode } from '@/utils/categoryIcons'

const props = defineProps({
  modelValue: {
    type: [String, Number],
    default: '',
  },
  options: {
    type: Array,
    default: () => [],
  },
  valueKey: {
    type: String,
    default: 'id',
  },
  placeholder: {
    type: String,
    default: 'Select currency',
  },
  searchPlaceholder: {
    type: String,
    default: 'Search currency...',
  },
  emptyText: {
    type: String,
    default: 'No currency found',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['update:modelValue'])

const rootRef = ref(null)
const triggerRef = ref(null)
const panelRef = ref(null)
const searchRef = ref(null)
const open = ref(false)
const search = ref('')
const activeIndex = ref(0)
const panelStyle = ref({})
const panelMaxHeight = ref('40vh')

const normalizedOptions = computed(() =>
  (Array.isArray(props.options) ? props.options : [])
    .filter((item) => item && item.code)
    .map((item) => ({ ...item, code: String(item.code).toUpperCase() }))
)

const selected = computed(() => normalizedOptions.value.find((item) => item[props.valueKey] === props.modelValue) ?? null)
const selectedIcon = computed(() => (selected.value ? iconFor(selected.value.code) : null))

const filteredOptions = computed(() => {
  const q = search.value.toLowerCase()
  if (!q) return normalizedOptions.value
  return normalizedOptions.value.filter((item) => {
    const symbol = String(item.symbol ?? '').toLowerCase()
    return item.code.toLowerCase().includes(q) || String(item.name ?? '').toLowerCase().includes(q) || symbol.includes(q)
  })
})

function iconFor(code) {
  return getCurrencyIconByCode(code)
}

function toggleOpen() {
  if (props.disabled) return
  open.value ? close() : show()
}

function show() {
  open.value = true
  search.value = ''
  const idx = filteredOptions.value.findIndex((item) => item[props.valueKey] === props.modelValue)
  activeIndex.value = idx >= 0 ? idx : 0
  nextTick(() => {
    updatePanelPosition()
    searchRef.value?.focus()
  })
}

function close() {
  open.value = false
}

function select(item) {
  emit('update:modelValue', item[props.valueKey])
  close()
}

function moveActive(step) {
  if (!filteredOptions.value.length) return
  const next = activeIndex.value + step
  if (next < 0) {
    activeIndex.value = filteredOptions.value.length - 1
    return
  }
  if (next >= filteredOptions.value.length) {
    activeIndex.value = 0
    return
  }
  activeIndex.value = next
}

function selectActive() {
  const item = filteredOptions.value[activeIndex.value]
  if (item) select(item)
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

  const desiredWidth = rect.width
  const maxWidth = Math.max(260, viewportW - sidePadding * 2)
  const width = Math.min(desiredWidth, maxWidth)
  let left = rect.left
  if (left + width > viewportW - sidePadding) left = viewportW - sidePadding - width
  if (left < sidePadding) left = sidePadding

  const spaceBelow = viewportH - rect.bottom - sidePadding
  const spaceAbove = rect.top - sidePadding
  const openUp = spaceBelow < 260 && spaceAbove > spaceBelow
  const top = openUp ? Math.max(sidePadding, rect.top - gap) : Math.min(viewportH - sidePadding, rect.bottom + gap)

  const maxAvailable = openUp ? Math.max(180, spaceAbove - gap) : Math.max(180, spaceBelow - gap)
  panelMaxHeight.value = `${Math.min(380, Math.max(180, maxAvailable))}px`

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

watch(filteredOptions, (items) => {
  if (!items.length) {
    activeIndex.value = 0
    return
  }
  if (activeIndex.value >= items.length) activeIndex.value = items.length - 1
})

watch(open, (isOpen) => {
  if (!isOpen) return
  nextTick(() => updatePanelPosition())
})
</script>
