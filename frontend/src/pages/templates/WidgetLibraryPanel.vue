<template>
  <aside class="flex w-64 shrink-0 flex-col gap-2 overflow-hidden rounded-xl border border-[var(--border-card)] bg-[var(--bg-card)] text-sm sm:w-64">
    <h2 class="shrink-0 px-2 pt-2 text-xs font-semibold uppercase tracking-wide text-[var(--text-secondary)]">
      {{ $t('templateEditor.widgetLibrary.title') }}
    </h2>

    <div class="min-h-0 flex-1 space-y-2 overflow-y-auto px-2 pb-2">
      <section
        v-for="sec in sections"
        :key="sec.id"
        class="rounded-lg border border-[var(--border-card)] bg-[var(--bg-input)]/70"
      >
        <button
          type="button"
          class="flex w-full items-center justify-between gap-2 px-3 py-2.5 text-start text-sm font-medium text-[var(--text-primary)] transition-colors hover:bg-[var(--bg-hover)]"
          @click="toggle(sec.id)"
        >
          <span class="flex min-w-0 items-center gap-2">
            <i :class="['fas shrink-0 text-[var(--primary)]', sec.icon]" />
            <span class="truncate">{{ sec.title }}</span>
          </span>
          <i
            class="fas fa-chevron-down shrink-0 text-xs text-[var(--text-secondary)] transition-transform"
            :class="open[sec.id] ? '-rotate-180' : ''"
          />
        </button>
        <div v-show="open[sec.id]" class="space-y-2 border-t border-[var(--border-card)] px-2 pb-2 pt-2">
          <button
            v-for="w in sec.widgets"
            :key="w.type + (w.label || '')"
            type="button"
            class="group flex w-full items-start gap-2 rounded-lg border border-[var(--border-card)] bg-[var(--bg-card)] px-2 py-2 text-start transition-all hover:-translate-y-0.5 hover:border-[var(--primary)]/45 hover:shadow-[var(--shadow-card)]"
            @click="add(w.type, w.extra)"
          >
            <div
              class="relative flex h-10 w-14 shrink-0 items-center justify-center overflow-hidden rounded-md border border-[var(--border-card)] bg-[var(--bg-input)]/80"
              :title="$t('templateEditor.widgetLibrary.widgetPreview', { label: w.label })"
            >
              <span class="pointer-events-none absolute inset-0 opacity-45" :class="w.thumbClass" />
              <i :class="['fas relative z-10 text-sm text-[var(--primary)]', w.icon]" />
            </div>
            <span class="min-w-0">
              <span class="block truncate text-xs font-semibold text-[var(--text-primary)]">{{ w.label }}</span>
              <span class="block truncate text-[10px] text-[var(--text-secondary)]">{{ w.hint }}</span>
            </span>
          </button>
        </div>
      </section>

      <section
        v-if="priceBindings.length"
        class="rounded-lg border border-[var(--border-card)] bg-[var(--bg-input)]/70"
      >
        <button
          type="button"
          class="flex w-full items-center justify-between gap-2 px-3 py-2.5 text-start text-sm font-medium text-[var(--text-primary)] transition-colors hover:bg-[var(--bg-hover)]"
          @click="toggle('prices')"
        >
          <span class="flex min-w-0 items-center gap-2">
            <i class="fas fa-coins shrink-0 text-[var(--primary)]" />
            <span class="truncate">{{ $t('templateEditor.widgetLibrary.priceBindings') }}</span>
          </span>
          <i
            class="fas fa-chevron-down shrink-0 text-xs text-[var(--text-secondary)] transition-transform"
            :class="open.prices ? '-rotate-180' : ''"
          />
        </button>
        <div v-show="open.prices" class="max-h-48 space-y-1 overflow-y-auto border-t border-[var(--border-card)] px-2 pb-2 pt-1">
          <button
            v-for="row in priceBindings"
            :key="`${row.key}-${row.price_type_id ?? ''}`"
            type="button"
            class="btn-luxury-outline flex w-full flex-col items-start gap-0.5 py-2 text-start text-xs"
            @click="addPriceBinding(row)"
          >
            <span class="font-mono text-[10px] text-[var(--text-secondary)]">{{ row.key }}</span>
            <span class="truncate">{{ row.description }}</span>
          </button>
        </div>
      </section>

      <section class="rounded-lg border border-[var(--border-card)] bg-[var(--bg-input)]/70">
        <button
          type="button"
          class="flex w-full items-center justify-between gap-2 px-3 py-2.5 text-start text-sm font-medium text-[var(--text-primary)] transition-colors hover:bg-[var(--bg-hover)]"
          @click="toggle('media_lib')"
        >
          <span class="flex min-w-0 items-center gap-2">
            <i class="fas fa-folder-open shrink-0 text-[var(--primary)]" />
            <span class="truncate">{{ $t('templateEditor.widgetLibrary.mediaLibrary') }}</span>
          </span>
          <i
            class="fas fa-chevron-down shrink-0 text-xs text-[var(--text-secondary)] transition-transform"
            :class="open.media_lib ? '-rotate-180' : ''"
          />
        </button>
        <div v-show="open.media_lib" class="space-y-2 border-t border-[var(--border-card)] px-2 pb-2 pt-2">
          <button
            type="button"
            class="group flex w-full items-center gap-2 rounded-lg border border-dashed border-[var(--primary)]/50 bg-[var(--bg-card)] px-2 py-2 text-start transition hover:border-[var(--primary)]"
            @click="te.openBackgroundPicker?.()"
          >
            <span class="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-md bg-[var(--primary)]/10 text-[var(--primary)]">
              <i class="fas fa-image" />
            </span>
            <span>
              <span class="block text-xs font-semibold text-[var(--text-primary)]">{{ $t('templateEditor.widgetLibrary.uploadBaseImage') }}</span>
              <span class="block text-[10px] text-[var(--text-secondary)]">{{ $t('templateEditor.widgetLibrary.setCanvasBackgroundFirst') }}</span>
            </span>
          </button>
          <p v-if="mediaLoading" class="px-1 py-2 text-xs text-[var(--text-secondary)]">{{ $t('common.loading') }}</p>
          <p v-else-if="!mediaItems.length" class="px-1 py-2 text-xs text-[var(--text-secondary)]">{{ $t('templateEditor.widgetLibrary.noUploads') }}</p>
          <div v-else class="grid max-h-40 grid-cols-3 gap-1 overflow-y-auto">
            <button
              v-for="m in mediaItems"
              :key="m.url"
              type="button"
              class="relative aspect-square overflow-hidden rounded border border-[var(--border-card)] hover:ring-2 hover:ring-[var(--primary)]"
              :title="m.name"
              @click="insertMediaUrl(m.url)"
            >
              <img :src="m.url" alt="" class="h-full w-full object-cover" />
            </button>
          </div>
        </div>
      </section>
    </div>
  </aside>
</template>

<script setup>
import { computed, reactive, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { templateEditorApi, formatDrfError } from '@/services/api'
import { useTemplateEditorInjected } from './templateEditorInjectionKey.js'

const props = defineProps({
  categoryId: { type: [Number, String], default: null },
})

const te = useTemplateEditorInjected()
const { t } = useI18n()
const toast = useToast()

const sections = computed(() => [
  {
    id: 'text_time',
    title: t('templateEditor.widgetLibrary.sections.textTime'),
    icon: 'fa-font',
    widgets: [
      { type: 'text', label: t('templateEditor.widgetLibrary.widgets.text'), icon: 'fa-pen-nib', hint: t('templateEditor.widgetLibrary.widgets.textHint'), thumbClass: 'bg-gradient-to-r from-slate-300/60 to-transparent', extra: null },
      { type: 'date', label: t('templateEditor.widgetLibrary.widgets.date'), icon: 'fa-calendar-alt', hint: t('templateEditor.widgetLibrary.widgets.dateHint'), thumbClass: 'bg-gradient-to-b from-slate-300/50 to-transparent', extra: { style: { dateKey: 'date_fa' } } },
      {
        type: 'weekday',
        label: t('templateEditor.widgetLibrary.widgets.weekday'),
        icon: 'fa-calendar-day',
        hint: t('templateEditor.widgetLibrary.widgets.weekdayHint'),
        thumbClass: 'bg-gradient-to-br from-slate-300/45 to-transparent',
        extra: { style: { dateKey: 'farsi_weekday' } },
      },
      { type: 'clock', label: t('templateEditor.widgetLibrary.widgets.clock'), icon: 'fa-clock', hint: t('templateEditor.widgetLibrary.widgets.clockHint'), thumbClass: 'bg-[radial-gradient(circle_at_50%_50%,rgba(148,163,184,0.45),transparent_65%)]', extra: null },
    ],
  },
  {
    id: 'media',
    title: t('templateEditor.widgetLibrary.sections.media'),
    icon: 'fa-photo-video',
    widgets: [{ type: 'image', label: t('templateEditor.widgetLibrary.widgets.image'), icon: 'fa-image', hint: t('templateEditor.widgetLibrary.widgets.imageHint'), thumbClass: 'bg-[linear-gradient(135deg,rgba(59,130,246,0.35),rgba(16,185,129,0.3))]', extra: null }],
  },
])

const open = reactive({
  text_time: false,
  media: false,
  prices: false,
  media_lib: false,
})

const priceBindings = ref([])
const mediaItems = ref([])
const mediaLoading = ref(false)

function toggle(id) {
  open[id] = !open[id]
}

function add(type, extra) {
  te.addWidget(type, extra || undefined)
}

async function loadPriceBindings() {
  priceBindings.value = []
  if (props.categoryId == null || props.categoryId === '') return
  try {
    const { data } = await templateEditorApi.variables({ category: props.categoryId })
    const list = Array.isArray(data) ? data : []
    priceBindings.value = list
      .filter((v) => v.key && String(v.key).startsWith('price__'))
      .map((v) => ({
        key: v.key,
        description: v.description || v.key,
        price_type_id: v.price_type_id,
      }))
  } catch {
    priceBindings.value = []
  }
}

async function loadMedia() {
  mediaLoading.value = true
  try {
    const { data } = await templateEditorApi.listMedia()
    mediaItems.value = Array.isArray(data?.results) ? data.results : []
  } catch (e) {
    mediaItems.value = []
    toast.error(formatDrfError(e.response?.data) || t('templateEditor.widgetLibrary.mediaLoadFailed'))
  } finally {
    mediaLoading.value = false
  }
}

function addPriceBinding(row) {
  const cw = te.canvasWidth?.value ?? 1920
  const ch = te.canvasHeight?.value ?? 1080
  const fs = Math.min(96, Math.max(28, Math.round(ch * 0.09)))
  const idKey = row.price_type_id != null ? `price_type__${row.price_type_id}` : ''
  const previewValue =
    (idKey && te.priceBindingPreviewMap?.value?.[idKey]?.value) ||
    te.priceBindingPreviewMap?.value?.[row.key]?.value
  const fallbackPrice = String(previewValue || '').trim() || '123,456'
  const style = {
    bindingKey: row.key,
    fontSize: fs,
      color: '#0f172a',
      align: 'center',
      fontWeight: 'normal',
      plainText: true,
    textShadow: false,
    textOutline: false,
  }
  if (row.price_type_id != null && row.price_type_id !== '') {
    style.priceTypeId = row.price_type_id
  }
  te.addWidget('text', {
    name: row.description || row.key,
    style,
    content: fallbackPrice,
    width: Math.min(cw * 0.85, 900),
    height: Math.min(ch * 0.14, fs + 36),
    x: cw * 0.075,
    y: ch * 0.35,
  })
}

function insertMediaUrl(url) {
  te.addWidget('image', {
    content: url,
    name: 'Image',
  })
  toast.success(t('templateEditor.widgetLibrary.imageWidgetAdded'))
}

watch(
  () => props.categoryId,
  () => {
    loadPriceBindings()
  },
  { immediate: true }
)

watch(
  () => open.media_lib,
  (v) => {
    if (v && !mediaItems.value.length && !mediaLoading.value) loadMedia()
  }
)
</script>
