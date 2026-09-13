import { computed, inject, provide } from 'vue'
import { localize as resolveLocalized, isBlank } from '../localize.js'

const SITE_CONTEXT = Symbol('ws-site-context')

/**
 * The site a section is being drawn inside: its snapshot, the locale in view,
 * and the account slug the price widget needs.
 *
 * Provided once by `SiteRenderer` so no section has to be handed the same four
 * props through three levels of layout.
 */
export function provideSiteContext(context) {
  provide(SITE_CONTEXT, context)
}

export function useSiteContext() {
  const context = inject(SITE_CONTEXT, null)
  const snapshot = computed(() => context?.snapshot?.value || {})
  const locale = computed(() => context?.locale?.value || snapshot.value.primary_locale || 'en')
  const primaryLocale = computed(() => snapshot.value.primary_locale || 'en')

  /** Resolve a localized field down to one string for the current locale. */
  function t(value) {
    return resolveLocalized(value, locale.value, primaryLocale.value)
  }

  return {
    snapshot,
    locale,
    primaryLocale,
    t,
    isBlank,
    branding: computed(() => snapshot.value.branding || {}),
    accountSlug: computed(() => context?.accountSlug?.value || snapshot.value.slug || ''),
    isEditing: computed(() => Boolean(context?.isEditing?.value)),
    sections: computed(() => snapshot.value.sections || []),
    locales: computed(() => snapshot.value.locales || [primaryLocale.value]),
    setLocale: context?.setLocale || (() => {}),
  }
}
