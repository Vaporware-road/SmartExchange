import { computed } from 'vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/**
 * The five hero variants differ in arrangement, not in what they say, so the
 * content unpacking lives here once instead of five times.
 */
export function useHero(props) {
  const { t, branding } = useSiteContext()
  const content = computed(() => props.content || {})

  return {
    t,
    eyebrow: computed(() => t(content.value.eyebrow)),
    title: computed(() => t(content.value.title) || t(branding.value.business_name)),
    subtitle: computed(() => t(content.value.subtitle) || t(branding.value.tagline)),
    primaryLabel: computed(() => t(content.value.primary_cta_label)),
    secondaryLabel: computed(() => t(content.value.secondary_cta_label)),
    imageAlt: computed(() => t(content.value.image_alt)),
    badges: computed(() => content.value.badges || []),
  }
}
