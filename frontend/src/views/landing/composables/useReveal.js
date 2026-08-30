import { onBeforeUnmount, onMounted } from 'vue'

const REVEAL_SELECTOR = '[data-reveal]'

/**
 * Adds the `data-revealed` attribute to `[data-reveal]` elements as they scroll
 * into view.
 *
 * A data attribute (not a class) is used deliberately: Vue rewrites `className`
 * wholesale on every class patch, so an imperative `.is-revealed` class would be
 * wiped the moment a component toggles any `:class` (e.g. an accordion) — the
 * element would snap back to `opacity: 0` and stay invisible.
 *
 * No animation library: the transition itself is CSS, this only decides when.
 * Under `prefers-reduced-motion` everything is revealed immediately so the page
 * is never left with invisible content.
 *
 * @param {import('vue').Ref<HTMLElement|null>} rootRef container to scan
 */
export function useReveal(rootRef) {
  let observer = null

  onMounted(() => {
    const root = rootRef.value
    if (!root) return

    const targets = root.querySelectorAll(REVEAL_SELECTOR)
    const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

    if (reduced || typeof IntersectionObserver === 'undefined') {
      targets.forEach((el) => el.setAttribute('data-revealed', ''))
      return
    }

    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return
          entry.target.setAttribute('data-revealed', '')
          observer.unobserve(entry.target)
        })
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.08 },
    )

    targets.forEach((el) => observer.observe(el))
  })

  onBeforeUnmount(() => {
    observer?.disconnect()
    observer = null
  })
}
