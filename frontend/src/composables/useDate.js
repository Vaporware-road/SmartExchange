import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { format as jalaliFormat } from 'date-fns-jalali'

export function useDate() {
  const { locale } = useI18n()

  const isJalali = computed(() => locale.value === 'fa')

  function formatDate(dateInput, pattern) {
    if (!dateInput) return '—'
    const d = typeof dateInput === 'string' ? new Date(dateInput) : dateInput
    if (isNaN(d.getTime())) return '—'

    if (isJalali.value) {
      return jalaliFormat(d, pattern || 'yyyy/MM/dd')
    }
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
  }

  function formatDateTime(dateInput) {
    if (!dateInput) return '—'
    const d = typeof dateInput === 'string' ? new Date(dateInput) : dateInput
    if (isNaN(d.getTime())) return '—'

    const time = d.toLocaleTimeString(isJalali.value ? 'fa-IR' : 'en-US', {
      hour: '2-digit',
      minute: '2-digit',
    })

    if (isJalali.value) {
      return `${jalaliFormat(d, 'yyyy/MM/dd')} ${time}`
    }
    return `${d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })} ${time}`
  }

  function formatTime(dateInput) {
    if (!dateInput) return '—'
    const d = typeof dateInput === 'string' ? new Date(dateInput) : dateInput
    if (isNaN(d.getTime())) return '—'

    return d.toLocaleTimeString(isJalali.value ? 'fa-IR' : 'en-US', {
      hour: '2-digit',
      minute: '2-digit',
    })
  }

  function formatRelative(dateInput) {
    if (!dateInput) return '—'
    const d = typeof dateInput === 'string' ? new Date(dateInput) : dateInput
    if (isNaN(d.getTime())) return '—'

    const now = new Date()
    const diffMs = now - d
    const diffMin = Math.floor(diffMs / 60000)
    const diffHour = Math.floor(diffMs / 3600000)
    const diffDay = Math.floor(diffMs / 86400000)

    if (isJalali.value) {
      if (diffMin < 1) return 'همین الان'
      if (diffMin < 60) return `${diffMin} دقیقه پیش`
      if (diffHour < 24) return `${diffHour} ساعت پیش`
      if (diffDay < 7) return `${diffDay} روز پیش`
      return jalaliFormat(d, 'yyyy/MM/dd')
    }

    if (diffMin < 1) return 'Just now'
    if (diffMin < 60) return `${diffMin}m ago`
    if (diffHour < 24) return `${diffHour}h ago`
    if (diffDay < 7) return `${diffDay}d ago`
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
  }

  return { isJalali, formatDate, formatDateTime, formatTime, formatRelative }
}
