import { computed } from 'vue'
import { useSiteContext } from './useSiteContext.js'

/**
 * The desk's price-widget settings, wherever a board is drawn.
 *
 * A hero that leads with rates and the rates section itself must agree about
 * which categories to show and how often to refresh, so both read the one
 * `rates` section the owner configured rather than carrying separate copies.
 */
export function useRatesConfig(fallback = {}) {
  const { sections } = useSiteContext()
  return computed(() => {
    const rates = sections.value.find((section) => section.type === 'rates')
    return { ...fallback, ...(rates?.content || {}) }
  })
}
