<template>
  <div class="template-editor-workspace flex h-[100dvh] max-h-[100dvh] min-h-0 min-w-0 flex-1 flex-col text-[var(--text-primary)]">
    <header
      class="sticky top-0 z-20 flex shrink-0 items-center gap-3 border-b border-[var(--border-card)] bg-[var(--bg-card)]/95 px-3 py-2.5 backdrop-blur-md sm:px-4"
    >
      <div class="flex w-28 shrink-0 items-center">
        <router-link
          to="/templates"
          class="inline-flex items-center gap-2 rounded-lg px-2 py-1.5 text-sm text-[var(--text-secondary)] transition-colors hover:bg-[var(--bg-hover)] hover:text-[var(--primary)]"
        >
          <i class="fas fa-arrow-left" />
          <span>Back</span>
        </router-link>
      </div>
      <div class="min-w-0 flex-1 text-center">
        <h1 v-if="template" class="truncate text-sm font-semibold text-[var(--primary)] sm:text-base" :title="template.name">
          {{ template.name }}
        </h1>
        <span v-else class="text-sm text-[var(--text-secondary)]">Template</span>
      </div>
      <div class="flex w-48 shrink-0 items-center justify-end gap-2">
        <div class="flex flex-col items-end gap-0.5">
          <span class="inline-flex items-center gap-1.5 rounded-full border border-[var(--border-card)] bg-[var(--bg-input)]/80 px-2 py-1 text-[11px] text-[var(--text-secondary)]">
            <span
              class="h-2 w-2 rounded-full"
              :class="saveIndicatorClass"
            />
            {{ saveStatusLabel }}
          </span>
          <span v-if="lastSavedAt" class="text-[10px] text-[var(--text-secondary)]">
            {{ `Last save: ${lastSavedAt.toLocaleTimeString()}` }}
          </span>
        </div>
        <button type="button" class="btn-luxury py-1.5 px-4 text-sm" :disabled="isSaving" @click="save">
          {{ isSaving ? 'Saving…' : 'Save' }}
        </button>
      </div>
    </header>

    <div v-if="loadError" class="p-8 text-center text-red-600 dark:text-red-300">{{ loadError }}</div>
    <div v-else-if="loading" class="flex flex-1 items-center justify-center p-8 text-[var(--text-secondary)]">Loading…</div>

    <div v-else class="flex min-h-0 min-w-0 flex-1 gap-2 overflow-hidden p-2 sm:p-3">
      <WidgetLibraryPanel :category-id="template?.category ?? null" />
      <main
        class="relative flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden rounded-xl border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)]"
      >
        <div
          class="flex shrink-0 items-center justify-between gap-2 border-b border-[var(--border-card)] bg-[var(--bg-input)]/80 px-3 py-2 text-xs"
        >
          <span class="text-[var(--text-secondary)]">Canvas {{ canvasW }}×{{ canvasH }}</span>
          <div class="flex items-center gap-1">
            <button
              type="button"
              class="rounded-md border border-[var(--border-card)] px-2 py-0.5 text-[var(--text-primary)] hover:bg-[var(--bg-hover)]"
              @click="zoomOut"
            >
              −
            </button>
            <span class="w-11 text-center tabular-nums text-[var(--text-secondary)]">{{ Math.round(scale * 100) }}%</span>
            <button
              type="button"
              class="rounded-md border border-[var(--border-card)] px-2 py-0.5 text-[var(--text-primary)] hover:bg-[var(--bg-hover)]"
              @click="zoomIn"
            >
              +
            </button>
            <button
              type="button"
              class="rounded-md border border-[var(--border-card)] px-2 py-0.5 text-[var(--text-primary)] hover:bg-[var(--bg-hover)]"
              @click="fitZoom"
            >
              Fit
            </button>
          </div>
        </div>
        <div
          ref="viewportRef"
          class="relative flex min-h-0 flex-1 items-center justify-center overflow-hidden bg-[var(--editor-workspace-bg)] p-1 sm:p-2"
        >
          <div
            class="relative overflow-visible"
            :style="{
              width: `${canvasW * scale}px`,
              height: `${canvasH * scale}px`,
            }"
          >
            <div
              class="absolute left-0 top-0 overflow-visible"
              :style="{ transform: `scale(${scale})`, transformOrigin: 'top left' }"
            >
              <div
                ref="canvasRootRef"
                class="relative overflow-hidden rounded-md border border-[var(--editor-canvas-border)] bg-white shadow-[var(--editor-canvas-shadow)]"
                :style="{
                  width: canvasW + 'px',
                  height: canvasH + 'px',
                  backgroundColor: backgroundColor,
                }"
                @mousedown.self="clearSelection"
              >
                  <img
                    v-if="imageUrl"
                    :src="imageUrl"
                    alt=""
                    class="pointer-events-none absolute inset-0 h-full w-full object-contain opacity-100"
                    draggable="false"
                    @load="onBaseImageLoad"
                  />
                  <div
                    v-for="item in sortedWidgets"
                    :key="item.id"
                    :ref="(el) => setWidgetEl(item.id, el)"
                    class="absolute box-border will-change-transform"
                    :class="[selectedId === item.id ? 'ring-2 ring-inset ring-[var(--primary)]/80' : '']"
                    :style="widgetDomStyle(item)"
                    :data-wid="item.id"
                    @mousedown.stop="selectWidget(item.id)"
                  >
                    <div :class="widgetInnerChromeClass(item.type)">
                      <WidgetPreviewHost :widget="item" />
                    </div>
                  </div>
              </div>
              <Moveable
                v-if="moveableTarget"
                :key="selectedId || 'none'"
                class="pointer-events-auto"
                :target="moveableTarget"
                :pass-drag-area="true"
                :draggable="true"
                :resizable="true"
                :rotatable="true"
                :origin="false"
                :zoom="1 / scale"
                :throttle-drag="0"
                @drag="onDrag"
                @resize="onResize"
                @rotate="onRotate"
                @dragEnd="onDragEnd"
                @resizeEnd="onResizeEnd"
                @rotateEnd="onRotateEnd"
              />
            </div>
          </div>
          <div v-if="!imageUrl" class="pointer-events-none absolute inset-0 z-10 flex items-center justify-center">
            <button
              type="button"
              class="pointer-events-auto flex w-[min(92vw,520px)] flex-col items-center gap-3 rounded-2xl border-2 border-dashed border-[var(--primary)]/80 bg-white/95 px-10 py-8 text-center text-base font-semibold text-[#0f172a] shadow-[var(--editor-canvas-shadow)] transition-all hover:-translate-y-0.5 hover:border-[var(--primary)] hover:shadow-[var(--shadow-card-hover)]"
              @click="openBackgroundPicker"
            >
              <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-[var(--primary)]/15 text-[var(--primary)]">
                <i class="fas fa-image text-2xl" />
              </span>
              <span class="text-lg leading-tight">Upload background image</span>
              <span class="text-sm font-medium leading-relaxed text-slate-600">Start your design by setting a base canvas image.</span>
            </button>
          </div>
        </div>
      </main>
      <TemplateInspectorPanel />
    </div>
    <input
      ref="backgroundFileInput"
      type="file"
      accept="image/jpeg,image/png,image/gif,image/webp"
      class="hidden"
      @change="onBackgroundFile"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import Moveable from 'vue3-moveable'
import { formatDrfError, templateEditorApi } from '@/services/api'
import { injectTemplateEditorFontFaces } from './templateEditorFonts.js'
import { useTemplatesStore } from '@/stores/templatesEditor'
import { provideTemplateEditor } from './templateEditorInjectionKey.js'
import WidgetLibraryPanel from './WidgetLibraryPanel.vue'
import TemplateInspectorPanel from './TemplateInspectorPanel.vue'
import WidgetPreviewHost from '@/components/template-editor/player/widgets/WidgetPreviewHost.vue'
import { fitFontSizeToWidgetBox } from '@/utils/fitTextToBox.js'

const route = useRoute()
const toast = useToast()
const templatesStore = useTemplatesStore()

const loading = ref(true)
const loadError = ref('')
const saveState = ref('saved')
const hasLoadedOnce = ref(false)
const lastSavedAt = ref(null)
const template = ref(null)
const backgroundFileInput = ref(null)

const canvasW = ref(1920)
const canvasH = ref(1080)
const backgroundColor = ref('#ffffff')

const widgets = ref([])
const selectedId = ref(null)
const priceBindingPreviewMap = ref({})

const viewportRef = ref(null)
const canvasRootRef = ref(null)
const widgetEls = new Map()

const scale = ref(0.35)

const selectedWidget = computed(() => widgets.value.find((w) => w.id === selectedId.value) || null)
const isSaving = computed(() => templatesStore.saving || saveState.value === 'saving')
const saveStatusLabel = computed(() => {
  if (saveState.value === 'error') return 'Save failed'
  if (isSaving.value) return 'Saving'
  if (saveState.value === 'dirty') return 'Unsaved changes'
  return 'Saved'
})
const saveIndicatorClass = computed(() => {
  if (saveState.value === 'error') return 'bg-red-500'
  if (isSaving.value) return 'bg-amber-400'
  if (saveState.value === 'dirty') return 'bg-sky-500'
  return 'bg-emerald-500'
})

const sortedWidgets = computed(() => [...widgets.value].sort((a, b) => (a.zIndex || 0) - (b.zIndex || 0)))

const imageUrl = computed(() => {
  return normalizeTemplateImageUrl(template.value?.image)
})

function normalizeTemplateImageUrl(rawUrl) {
  if (!rawUrl || typeof rawUrl !== 'string') return ''
  const u = rawUrl.trim()
  if (!u) return ''
  if (u.startsWith('/')) return u
  if (!u.startsWith('http://') && !u.startsWith('https://')) return ''
  try {
    const parsed = new URL(u)
    if (parsed.pathname.startsWith('/media/')) {
      return `${parsed.pathname}${parsed.search}${parsed.hash}`
    }
    return u
  } catch {
    return ''
  }
}

const moveableTarget = computed(() => {
  if (!selectedId.value) return null
  return widgetEls.get(selectedId.value) || null
})

function setWidgetEl(id, el) {
  if (el) widgetEls.set(id, el)
  else widgetEls.delete(id)
}

function widgetDomStyle(w) {
  return {
    width: `${w.width}px`,
    height: `${w.height}px`,
    transform: `translate(${w.x}px, ${w.y}px) rotate(${w.rotation || 0}deg)`,
    zIndex: w.zIndex ?? 1,
  }
}

function clampWidgetToCanvas(w) {
  if (!w) return
  w.width = Math.max(24, Math.min(w.width || 0, canvasW.value))
  w.height = Math.max(24, Math.min(w.height || 0, canvasH.value))
  const maxX = Math.max(0, canvasW.value - w.width)
  const maxY = Math.max(0, canvasH.value - w.height)
  w.x = Math.min(maxX, Math.max(0, w.x || 0))
  w.y = Math.min(maxY, Math.max(0, w.y || 0))
}

const TEXT_LIKE_WIDGETS = new Set(['text', 'marquee', 'date', 'clock', 'weekday'])

/** Editor-only frame: text-like widgets show raw text; image keeps a light frame. */
function widgetInnerChromeClass(type) {
  if (TEXT_LIKE_WIDGETS.has(type)) {
    return 'h-full min-h-0 w-full min-w-0 overflow-hidden rounded-none bg-transparent'
  }
  return 'h-full w-full overflow-hidden rounded-md border border-[var(--border-card)] bg-[var(--bg-input)]/50 dark:border-white/10 dark:bg-black/25'
}

function selectWidget(id) {
  selectedId.value = id
}

function clearSelection() {
  selectedId.value = null
}

function nextZIndex() {
  const zs = widgets.value.map((w) => w.zIndex || 0)
  return (zs.length ? Math.max(...zs) : 0) + 1
}

function defaultName(type) {
  const map = {
    text: 'Text',
    image: 'Image',
    date: 'Date',
    weekday: 'Weekday',
    clock: 'Clock',
  }
  return map[type] || type
}

function addWidget(type, extra = null) {
  const cw = canvasW.value
  const ch = canvasH.value
  const id = globalThis.crypto?.randomUUID?.() || `widget-${Date.now()}-${Math.random().toString(16).slice(2)}`
  const base = {
    id,
    type,
    name: defaultName(type),
    x: cw * 0.08,
    y: ch * 0.08,
    width: Math.min(520, cw * 0.35),
    height: Math.min(200, ch * 0.18),
    rotation: 0,
    zIndex: nextZIndex(),
    visible: true,
    content: '',
    style: {},
  }
  if (extra && typeof extra === 'object') {
    if (extra.name) base.name = extra.name
    if (extra.content != null) base.content = extra.content
    if (typeof extra.x === 'number') base.x = extra.x
    if (typeof extra.y === 'number') base.y = extra.y
    if (typeof extra.width === 'number') base.width = extra.width
    if (typeof extra.height === 'number') base.height = extra.height
    if (extra.style && typeof extra.style === 'object') {
      base.style = { ...base.style, ...extra.style }
    }
  }
  if (type === 'text' || type === 'marquee') {
    base.width = Math.min(640, cw * 0.45)
    base.height = Math.min(120, ch * 0.12)
    base.content = 'Sample text'
    base.style = { fontSize: 28 }
  } else if (type === 'image') {
    base.width = Math.min(480, cw * 0.35)
    base.height = Math.min(320, ch * 0.35)
  } else if (type === 'date') {
    base.width = 280
    base.height = 72
    base.content = ''
    base.style = {
      ...base.style,
      fontSize: base.style.fontSize ?? 26,
      dateKey: base.style.dateKey || base.style.date_key || 'date_fa',
    }
    delete base.style.date_key
  } else if (type === 'weekday') {
    base.width = 280
    base.height = 72
    base.content = ''
    base.style = {
      ...base.style,
      fontSize: base.style.fontSize ?? 26,
      dateKey: base.style.dateKey || base.style.date_key || 'farsi_weekday',
    }
    delete base.style.date_key
  } else if (type === 'clock') {
    base.width = 280
    base.height = 72
    base.content = '12:00'
    base.style = { fontSize: 26 }
  }
  widgets.value.push(base)
  clampWidgetToCanvas(base)
  selectedId.value = id
  if (FONT_AUTOSCALE_TYPES.has(type)) {
    nextTick(() => fitFontSizeToWidgetBox(base))
  }
}

async function loadPriceBindingPreviewValues() {
  const categoryId = template.value?.category
  if (categoryId == null || categoryId === '') {
    priceBindingPreviewMap.value = {}
    return
  }
  try {
    const { data } = await templateEditorApi.priceBindingsPreview({ category: categoryId })
    const rows = Array.isArray(data) ? data : []
    const mapped = {}
    for (const row of rows) {
      const key = String(row?.key || '').trim()
      if (!key) continue
      const entry = {
        value: row?.previous_price != null ? String(row.previous_price) : '',
        source: row?.source || 'none',
        hasValue: Boolean(row?.has_value),
        label: row?.label || key,
        bindingKey: key,
      }
      mapped[key] = entry
      const ptid = row?.price_type_id
      if (ptid != null && ptid !== '') {
        mapped[`price_type__${ptid}`] = entry
      }
    }
    priceBindingPreviewMap.value = mapped
  } catch {
    priceBindingPreviewMap.value = {}
  }
}

function onBaseImageLoad(ev) {
  const el = ev?.target
  if (!el?.naturalWidth || !template.value) return
  const nw = el.naturalWidth
  const nh = el.naturalHeight
  if (nw < 1 || nh < 1) return
  if (nw === canvasW.value && nh === canvasH.value) return
  canvasW.value = nw
  canvasH.value = nh
  const cj = template.value.config_json && typeof template.value.config_json === 'object' ? template.value.config_json : {}
  backgroundColor.value = cj.backgroundColor || backgroundColor.value
  loadWidgetsFromConfigJson(cj)
  nextTick(() => {
    fitZoom()
    refitAllTextWidgets()
  })
}

function deleteWidget(id) {
  widgets.value = widgets.value.filter((w) => w.id !== id)
  widgetEls.delete(id)
  if (selectedId.value === id) selectedId.value = null
}

function parseTransform(target) {
  const tf = target.style.transform || ''
  const tr = tf.match(/translate\(([-0-9.]+)px,\s*([-0-9.]+)px\)/)
  const rr = tf.match(/rotate\(([-0-9.]+)deg\)/)
  return {
    x: tr ? parseFloat(tr[1]) : 0,
    y: tr ? parseFloat(tr[2]) : 0,
    rotation: rr ? parseFloat(rr[1]) : 0,
  }
}

const FONT_AUTOSCALE_TYPES = new Set(['text', 'marquee', 'date', 'weekday', 'clock'])

function refitSelectedTextWidget() {
  const sw = selectedWidget.value
  if (sw && FONT_AUTOSCALE_TYPES.has(sw.type)) fitFontSizeToWidgetBox(sw)
}

function refitAllTextWidgets() {
  widgets.value.forEach((w) => {
    if (FONT_AUTOSCALE_TYPES.has(w.type)) fitFontSizeToWidgetBox(w)
  })
}

function syncWidgetFromTarget(target) {
  const id = target.dataset.wid
  const w = widgets.value.find((x) => x.id === id)
  if (!w) return
  const { x, y, rotation } = parseTransform(target)
  w.x = x
  w.y = y
  w.rotation = rotation
  const width = parseFloat(target.style.width)
  const height = parseFloat(target.style.height)
  if (!Number.isNaN(width) && width > 0) w.width = width
  if (!Number.isNaN(height) && height > 0) w.height = height
  clampWidgetToCanvas(w)
}

/** Resolve widget root (Moveable usually sets event.target to the :target element). */
function getMoveableDomTarget(e) {
  const t = e?.target
  if (!t) return null
  if (t.dataset?.wid) return t
  const el = typeof t.closest === 'function' ? t.closest('[data-wid]') : null
  return el || null
}

function onDrag(e) {
  const t = getMoveableDomTarget(e) || e?.target
  if (t) t.style.transform = e.transform
}

function onResize(e) {
  const target = getMoveableDomTarget(e) || e?.target
  if (!target?.dataset?.wid) return
  target.style.width = `${e.width}px`
  target.style.height = `${e.height}px`
  target.style.transform = e.drag.transform

  const id = target.dataset?.wid
  const w = id ? widgets.value.find((x) => x.id === id) : null
  if (!w || !FONT_AUTOSCALE_TYPES.has(w.type)) return
  w.width = e.width
  w.height = e.height
  fitFontSizeToWidgetBox(w)
}

function onRotate(e) {
  const t = getMoveableDomTarget(e) || e?.target
  if (t) t.style.transform = e.drag.transform
}

function onDragEnd(e) {
  const target = getMoveableDomTarget(e) || e?.target
  if (target?.dataset?.wid) syncWidgetFromTarget(target)
}

function onResizeEnd(e) {
  const target = getMoveableDomTarget(e) || e?.target
  if (target?.dataset?.wid) syncWidgetFromTarget(target)
}

function onRotateEnd(e) {
  const target = getMoveableDomTarget(e) || e?.target
  if (target?.dataset?.wid) syncWidgetFromTarget(target)
}

function pxToPct(px, total) {
  if (!total) return '0%'
  return `${((Number(px) / total) * 100).toFixed(4)}%`
}

function pctToPx(val, total) {
  if (val == null) return 0
  if (typeof val === 'number' && !Number.isNaN(val)) return (val / 100) * total
  const s = String(val).trim().replace('%', '')
  const n = parseFloat(s)
  if (Number.isNaN(n)) return 0
  return (n / 100) * total
}

function widgetsToPercentPayload() {
  const cw = canvasW.value
  const ch = canvasH.value
  return widgets.value.map((w) => ({
    id: w.id,
    type: w.type,
    name: w.name,
    x: pxToPct(w.x, cw),
    y: pxToPct(w.y, ch),
    width: pxToPct(w.width, cw),
    height: pxToPct(w.height, ch),
    rotation: w.rotation || 0,
    zIndex: w.zIndex ?? 1,
    visible: w.visible !== false,
    content: w.content ?? '',
    style: w.style && typeof w.style === 'object' ? { ...w.style } : {},
  }))
}

function loadWidgetsFromConfigJson(cj) {
  const cw = canvasW.value
  const ch = canvasH.value
  const list = Array.isArray(cj?.widgets) ? cj.widgets : []
  widgets.value = list.map((raw) => ({
    id: String(raw.id),
    type: raw.type || 'text',
    name: raw.name || defaultName(raw.type || 'text'),
    x: pctToPx(raw.x, cw),
    y: pctToPx(raw.y, ch),
    width: pctToPx(raw.width, cw),
    height: pctToPx(raw.height, ch),
    rotation: Number(raw.rotation) || 0,
    zIndex: Number(raw.zIndex) || 1,
    visible: raw.visible !== false,
    content: raw.content ?? '',
    style: raw.style && typeof raw.style === 'object' ? { ...raw.style } : {},
  }))
}

async function save() {
  if (!template.value) return
  saveState.value = 'saving'
  try {
    const config_json = {
      backgroundColor: backgroundColor.value,
      widgets: widgetsToPercentPayload(),
    }
    await templatesStore.saveConfigJsonOnly(template.value.id, {
      config_json,
      canvas_width: canvasW.value,
      canvas_height: canvasH.value,
    })
    template.value = templatesStore.current
    await loadPriceBindingPreviewValues()
    lastSavedAt.value = new Date()
    saveState.value = 'saved'
    const categoryLabel = template.value?.category_name || (template.value?.category ? `#${template.value.category}` : 'No category')
    toast.success(`Template saved (${categoryLabel})`)
  } catch (e) {
    saveState.value = 'error'
    toast.error(formatDrfError(e.response?.data) || 'Save failed')
  }
}

function openBackgroundPicker() {
  backgroundFileInput.value?.click()
}

async function onBackgroundFile(ev) {
  const file = ev.target?.files?.[0]
  if (ev.target) ev.target.value = ''
  if (!file || !template.value) return
  saveState.value = 'saving'
  try {
    const imgMeta = await readImageNaturalSize(file)
    if (imgMeta.width > 0 && imgMeta.height > 0) {
      canvasW.value = imgMeta.width
      canvasH.value = imgMeta.height
      widgets.value.forEach((w) => clampWidgetToCanvas(w))
    }
    const fd = new FormData()
    fd.append('image', file)
    const { data: updated } = await templateEditorApi.patch(template.value.id, fd)
    template.value = updated
    templatesStore.current = updated
    saveState.value = 'saved'
    lastSavedAt.value = new Date()
    nextTick(() => fitZoom())
    toast.success('Background image uploaded')
  } catch (e) {
    saveState.value = 'error'
    const msg = e?.response?.data ? formatDrfError(e.response.data) : (e?.message || 'Background upload failed')
    toast.error(msg)
  }
}

function readImageNaturalSize(source) {
  return new Promise((resolve) => {
    const img = new Image()
    let objectUrl = ''
    if (source instanceof File) objectUrl = URL.createObjectURL(source)
    img.onload = () => {
      resolve({ width: img.naturalWidth || 0, height: img.naturalHeight || 0 })
      if (objectUrl) URL.revokeObjectURL(objectUrl)
    }
    img.onerror = () => {
      resolve({ width: 0, height: 0 })
      if (objectUrl) URL.revokeObjectURL(objectUrl)
    }
    img.src = objectUrl || source
  })
}

function zoomIn() {
  scale.value = Math.min(2, Math.round((scale.value + 0.05) * 100) / 100)
}
function zoomOut() {
  scale.value = Math.max(0.1, Math.round((scale.value - 0.05) * 100) / 100)
}
function fitZoom() {
  const el = viewportRef.value
  if (!el) return
  const pad = 12
  const rw = (el.clientWidth - pad) / canvasW.value
  const rh = (el.clientHeight - pad) / canvasH.value
  scale.value = Math.max(0.1, Math.min(2, Math.min(rw, rh)))
}

watch([canvasW, canvasH], () => {
  nextTick(() => fitZoom())
})

watch(
  [widgets, backgroundColor, canvasW, canvasH, () => template.value?.name],
  () => {
    if (!hasLoadedOnce.value) return
    if (isSaving.value) return
    if (saveState.value === 'saved') saveState.value = 'dirty'
  },
  { deep: true }
)

watch(selectedId, () => {
  nextTick(() => {})
})

watch(
  () => template.value?.category,
  () => {
    loadPriceBindingPreviewValues()
  }
)

provideTemplateEditor({
  widgets,
  selectedId,
  selectedWidget,
  canvasWidth: canvasW,
  canvasHeight: canvasH,
  addWidget,
  openBackgroundPicker,
  deleteWidget,
  selectWidget,
  refitSelectedWidget: refitSelectedTextWidget,
  template,
  priceBindingPreviewMap,
  backgroundColor,
  saveState,
})

onMounted(async () => {
  const id = route.params.id
  if (!id) {
    loadError.value = 'Missing template id'
    loading.value = false
    return
  }
  try {
    const data = await templatesStore.fetchTemplate(id)
    template.value = data
    canvasW.value = Number(data.canvas_width) || 1920
    canvasH.value = Number(data.canvas_height) || 1080
    const cj = data.config_json && typeof data.config_json === 'object' ? data.config_json : {}
    backgroundColor.value = cj.backgroundColor || '#ffffff'
    loadWidgetsFromConfigJson(cj)
    await loadPriceBindingPreviewValues()
    nextTick(() => {
      fitZoom()
      refitAllTextWidgets()
    })
    try {
      const { data } = await templateEditorApi.fonts()
      injectTemplateEditorFontFaces(Array.isArray(data) ? data : [])
    } catch {
      /* preview falls back to system fonts */
    }
    if (viewportRef.value) {
      ro = new ResizeObserver(() => fitZoom())
      ro.observe(viewportRef.value)
    }
    hasLoadedOnce.value = true
    saveState.value = 'saved'
  } catch (e) {
    loadError.value = e?.response?.data?.detail || 'Failed to load template'
  } finally {
    loading.value = false
  }
})

let ro = null
onBeforeUnmount(() => {
  ro?.disconnect()
  ro = null
  widgetEls.clear()
})
</script>
