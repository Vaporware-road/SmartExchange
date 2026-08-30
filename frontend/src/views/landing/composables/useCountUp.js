import { onBeforeUnmount, onMounted, ref } from 'vue'

const DURATION = 1400

/**
 * Counts a number up from zero the first time it scrolls into view.
 *
 * Non-numeric stats (the "∞" channel count) pass `target: null` and are
 * rendered as-is; the observer still fires so they reveal in step with the rest.
 *
 * @param {import('vue').Ref<HTMLElement|null>} rootRef
 * @param {Array<{target: number|null}>} stats
 */
export function useCountUp(rootRef, stats) {
  const values = ref(stats.map((s) => (s.target == null ? null : 0)))
  let observer = null
  let frame = 0

  function settle() {
    stats.forEach((s, i) => {
      values.value[i] = s.target
    })
  }

  function run() {
    const start = performance.now()
    const step = (now) => {
      const p = Math.min((now - start) / DURATION, 1)
      // easeOutCubic: fast first, settles on the real figure rather than drifting past it.
      const eased = 1 - (1 - p) ** 3
      stats.forEach((s, i) => {
        if (s.target == null) return
        values.value[i] = Math.round(s.target * eased)
      })
      if (p < 1) frame = requestAnimationFrame(step)
    }
    frame = requestAnimationFrame(step)
  }

  onMounted(() => {
    const root = rootRef.value
    if (!root) return
    const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
    if (reduced || typeof IntersectionObserver === 'undefined') {
      settle()
      return
    }
    observer = new IntersectionObserver(
      (entries) => {
        if (!entries.some((e) => e.isIntersecting)) return
        observer.disconnect()
        observer = null
        run()
      },
      { threshold: 0.35 },
    )
    observer.observe(root)
  })

  onBeforeUnmount(() => {
    cancelAnimationFrame(frame)
    observer?.disconnect()
    observer = null
  })

  return { values }
}
