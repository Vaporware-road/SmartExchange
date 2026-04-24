<template>
  <div
    class="flex h-full min-h-0 w-full min-w-0 overflow-hidden px-2 font-medium leading-tight text-[var(--text-primary)]"
    :class="isPersianDate ? '' : 'text-center'"
    :style="containerStyle"
  >
    <span :style="textStyle" :dir="textDirAttr">{{ display }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { editorFontFamilyToken } from '@/pages/templates/templateEditorFonts.js'
import { useTemplateEditorInjected } from '@/pages/templates/templateEditorInjectionKey.js'
import {
  previewTextForDateWidget,
  resolvedDateKey,
  isPersianDateKey,
} from '@/pages/templates/dateWidgetPresets.js'

const props = defineProps({
  widget: { type: Object, required: true },
})
const te = useTemplateEditorInjected()

const display = computed(() => {
  const w = props.widget
  const bk = w?.style?.bindingKey || w?.style?.binding_key
  if (bk) {
    const resolved = te.priceBindingPreviewMap?.value?.[String(bk).trim()]
    const fromPreview = resolved?.value != null ? String(resolved.value).trim() : ''
    if (fromPreview) return fromPreview
    const fallback = w?.content != null ? String(w.content).trim() : ''
    return fallback || `[${bk}]`
  }
  const t = w?.type
  if (t === 'date' || t === 'weekday') {
    return previewTextForDateWidget(w)
  }
  if (t === 'clock') return '14:30'
  const c = w?.content
  if (c && String(c).trim()) return String(c)
  return 'Text'
})

const align = computed(() => {
  const a = String(props.widget?.style?.align || 'center').toLowerCase()
  if (a === 'left' || a === 'start') return 'left'
  if (a === 'right' || a === 'end') return 'right'
  return 'center'
})

const isPersianDate = computed(() => {
  const t = props.widget?.type
  if (t !== 'date' && t !== 'weekday') return false
  return isPersianDateKey(resolvedDateKey(props.widget))
})

const textDirAttr = computed(() => (isPersianDate.value ? 'rtl' : undefined))

/** Single-line box fit in editor (matches canvas measure in fitTextToBox). */
const useSingleLineFit = computed(() => {
  const t = props.widget?.type
  return t === 'text' || t === 'marquee' || t === 'date' || t === 'weekday' || t === 'clock'
})

const containerStyle = computed(() => {
  const a = align.value
  const persian = isPersianDate.value
  let justify
  if (persian) {
    if (a === 'left') justify = 'flex-start'
    else if (a === 'right') justify = 'flex-end'
    else justify = 'flex-end'
  } else {
    justify = a === 'left' ? 'flex-start' : a === 'right' ? 'flex-end' : 'center'
  }
  return {
    justifyContent: justify,
    alignItems: 'center',
  }
})

const textStyle = computed(() => {
  const s = props.widget?.style || {}
  const file = s.font || s.fontFilename || s.font_filename
  const token = file ? editorFontFamilyToken(String(file)) : ''
  const fontStack = token
    ? `'${token}', Vazirmatn, 'Segoe UI', system-ui, sans-serif`
    : 'Vazirmatn, Inter, system-ui, sans-serif'
  const persian = isPersianDate.value
  const ta = persian ? (align.value === 'left' ? 'left' : align.value === 'right' ? 'right' : 'right') : align.value
  const style = {
    fontSize: `${s.fontSize ?? 24}px`,
    fontFamily: s.fontFamily || fontStack,
    textAlign: ta,
    maxWidth: '100%',
    wordBreak: useSingleLineFit.value ? 'normal' : 'break-word',
    display: 'block',
    width: persian ? '100%' : undefined,
    direction: persian ? 'rtl' : undefined,
    unicodeBidi: persian ? 'plaintext' : undefined,
  }
  if (useSingleLineFit.value) {
    style.whiteSpace = 'nowrap'
    style.overflow = 'hidden'
    if (s.lineHeight == null || s.lineHeight === '') {
      style.lineHeight = 1.18
    }
  }
  const fw = s.fontWeight || s.weight
  if (fw) style.fontWeight = fw === 'bold' || fw === 700 ? '700' : String(fw)
  if (s.color) style.color = s.color
  if (s.lineHeight != null && s.lineHeight !== '') {
    const lh = Number(s.lineHeight)
    style.lineHeight = Number.isFinite(lh) ? String(lh) : String(s.lineHeight)
  }
  if (s.letterSpacing != null && s.letterSpacing !== '') style.letterSpacing = String(s.letterSpacing)
  return style
})
</script>
