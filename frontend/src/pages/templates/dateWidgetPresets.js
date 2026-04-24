/** Keys supported by backend `dynamic_data._dates_from_timestamp` for `date` widgets (ordered). */
export const DATE_WIDGET_DATE_KEYS = [
  'date_fa',
  'farsi_date',
  'date_fa_slash',
  'date_fa_slash_short',
  'date_fa_iso',
  'date_en',
  'english_date',
  'date_en_iso',
  'date_en_dmy',
  'date_en_mdy',
  'date_en_short',
  'date_en_weekday_long',
  'tether_date',
  'tether_year',
]

/** Keys for `weekday` widgets (same `style.dateKey` field as date). */
export const WEEKDAY_WIDGET_KEYS = ['farsi_weekday', 'english_weekday']

/** Date keys that should render RTL with Persian-friendly bidi (editor + logical order). */
export const PERSIAN_DATE_KEYS = new Set([
  'date_fa',
  'farsi_date',
  'date_fa_slash',
  'date_fa_slash_short',
  'date_fa_iso',
  'farsi_weekday',
])

export function resolvedDateKey(widget) {
  const t = widget?.type
  if (t !== 'date' && t !== 'weekday') return ''
  const k =
    widget?.style?.dateKey ||
    widget?.style?.date_key ||
    (t === 'weekday' ? 'farsi_weekday' : 'date_fa')
  return String(k || '').trim()
}

export function isPersianDateKey(key) {
  return PERSIAN_DATE_KEYS.has(String(key || '').trim())
}

/** Sample text in editor preview (aligned with backend `get_default_sample_value`). */
export const DATE_PREVIEW_SAMPLES = {
  date_fa: '۲۱ فروردین ۱۴۰۴',
  farsi_date: '۲۱ فروردین ۱۴۰۴',
  date_fa_slash: '۱۴۰۴/۰۱/۲۱',
  date_fa_slash_short: '۱۴۰۴/۱/۲۱',
  date_fa_iso: '۱۴۰۴-۰۱-۲۱',
  date_en: 'April 21, 2026',
  english_date: 'April 21, 2026',
  date_en_iso: '2026-04-21',
  date_en_dmy: '21/04/2026',
  date_en_mdy: '04/21/2026',
  date_en_short: '21 Apr 2026',
  date_en_weekday_long: 'Tuesday, April 21, 2026',
  farsi_weekday: 'سه‌شنبه',
  english_weekday: 'Tuesday',
  tether_date: '21 apr',
  tether_year: '2026',
  time: '14:30',
}

export function previewTextForDateWidget(widget) {
  const t = widget?.type
  if (t !== 'date' && t !== 'weekday') return null
  const key =
    widget?.style?.dateKey ||
    widget?.style?.date_key ||
    (t === 'weekday' ? 'farsi_weekday' : 'date_fa')
  const k = String(key || '').trim()
  if (DATE_PREVIEW_SAMPLES[k] != null) return DATE_PREVIEW_SAMPLES[k]
  return `[${k}]`
}
