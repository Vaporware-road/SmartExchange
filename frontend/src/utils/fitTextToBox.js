import { previewTextForDateWidget } from '@/pages/templates/dateWidgetPresets.js'
import { editorFontFamilyToken } from '@/pages/templates/templateEditorFonts.js'

/** String used to estimate rendered width/height for a widget. */
export function getWidgetTextForMeasure(w) {
  if (!w) return 'M'
  const bk = w.style?.bindingKey || w.style?.binding_key
  const t = w.type
  if (t === 'text' || t === 'marquee') {
    if (bk) return `[${String(bk).trim()}]`
    const c = w.content
    return c && String(c).trim() ? String(c).trim() : 'Sample text'
  }
  if (t === 'date' || t === 'weekday') return previewTextForDateWidget(w) || '۲۱ فروردین ۱۴۰۴'
  if (t === 'clock') return '99:99'
  return 'M'
}

export function fontStackForWidgetMeasure(w) {
  const s = w?.style || {}
  const file = s.font || s.fontFilename || s.font_filename
  const token = file ? editorFontFamilyToken(String(file)) : ''
  return token
    ? `'${token}', Vazirmatn, "Segoe UI", system-ui, sans-serif`
    : 'Vazirmatn, Inter, system-ui, sans-serif'
}

/**
 * Largest font size (px) so a single line fits inside the box (canvas measureText).
 */
export function measureMaxFontSize(
  boxW,
  boxH,
  text,
  { fontFamily = 'Vazirmatn, sans-serif', fontWeight = 'normal', min = 8, max = 220 } = {},
) {
  const line = String(text || 'M').split('\n')[0] || 'M'
  const bw = Math.max(4, Number(boxW) || 0)
  const bh = Math.max(4, Number(boxH) || 0)
  if (typeof document === 'undefined') {
    return Math.min(max, Math.max(min, Math.round(bh * 0.55)))
  }
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  if (!ctx) return Math.min(max, Math.max(min, Math.round(bh * 0.55)))
  const weightPrefix = fontWeight === 'bold' || fontWeight === 700 || fontWeight === '700' ? 'bold ' : ''
  let lo = min
  let hi = max
  let best = min
  while (lo <= hi) {
    const mid = (lo + hi) >> 1
    ctx.font = `${weightPrefix}${mid}px ${fontFamily}`
    let tw = 0
    try {
      tw = ctx.measureText(line).width
    } catch {
      tw = line.length * mid * 0.62
    }
    const lineH = mid * 1.18
    if (tw <= bw && lineH <= bh) {
      best = mid
      lo = mid + 1
    } else {
      hi = mid - 1
    }
  }
  return Math.max(min, Math.min(max, best))
}

export function fitFontSizeToWidgetBox(w) {
  if (!w?.style || typeof w.style !== 'object') w.style = {}
  const padX = 16
  const padY = 8
  const fw = Math.max(8, (Number(w.width) || 0) - padX)
  const fh = Math.max(8, (Number(w.height) || 0) - padY)
  const txt = getWidgetTextForMeasure(w)
  const fam = fontStackForWidgetMeasure(w)
  const fwgt = w.style.fontWeight || w.style.weight || 'normal'
  w.style.fontSize = measureMaxFontSize(fw, fh, txt, { fontFamily: fam, fontWeight: fwgt })
}
