import { computed } from 'vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/** Footer text, with a sensible copyright when the owner never wrote one. */
export function useFooter(props) {
  const { t, branding } = useSiteContext()
  const content = computed(() => props.content || {})

  return {
    t,
    about: computed(() => t(content.value.about) || t(branding.value.tagline)),
    disclaimer: computed(() => t(content.value.disclaimer)),
    columns: computed(() => content.value.columns || []),
    copyright: computed(() => {
      const own = t(content.value.copyright)
      if (own) return own
      const name = t(branding.value.business_name)
      return `© ${new Date().getFullYear()}${name ? ` ${name}` : ''}`
    }),
  }
}
