import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { isRtlLocale } from '@/constants/locales.js'

/** UI direction helpers — prefer logical CSS (ms/me/ps/pe, start/end) in templates when possible. */
export function useAppDirection() {
  const { locale } = useI18n()

  const isRtl = computed(() => isRtlLocale(locale.value))

  const backIcon = computed(() => (isRtl.value ? 'fa-arrow-right' : 'fa-arrow-left'))

  const breadcrumbChevron = computed(() => (isRtl.value ? 'fa-chevron-left' : 'fa-chevron-right'))

  return { isRtl, backIcon, breadcrumbChevron }
}
