import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'

/**
 * Live finalized rates for the public site.
 *
 * Three behaviours matter more than the fetch itself:
 *  - it polls, because a desk finalizes prices all day and a visitor who left
 *    the tab open must not be quoted this morning's rate;
 *  - it pauses while the tab is hidden, so an abandoned tab is not a slow
 *    denial-of-service on the desk's own server;
 *  - a failed refresh keeps the last good numbers on screen instead of blanking
 *    the board, and backs off so a backend blip does not turn into a hammer.
 */
const MIN_INTERVAL = 15
const MAX_BACKOFF = 8

export function useSitePrices(options) {
  const snapshot = ref(null)
  const loading = ref(true)
  const failed = ref(false)
  let timer = 0
  let backoff = 1
  let inFlight = null

  const accountSlug = computed(() => options.accountSlug?.value || '')
  const interval = computed(() => {
    const seconds = Number(options.refreshSeconds?.value ?? 60)
    return Number.isFinite(seconds) ? Math.max(seconds, MIN_INTERVAL) : 60
  })

  function endpoint() {
    const slug = accountSlug.value
    return slug
      ? `/api/public/website/prices/?account=${encodeURIComponent(slug)}`
      : '/api/public/website/prices/'
  }

  async function load() {
    if (inFlight) return inFlight
    inFlight = (async () => {
      try {
        const response = await fetch(endpoint(), { headers: { Accept: 'application/json' } })
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        snapshot.value = await response.json()
        failed.value = false
        backoff = 1
      } catch {
        failed.value = true
        backoff = Math.min(backoff * 2, MAX_BACKOFF)
      } finally {
        loading.value = false
        inFlight = null
      }
    })()
    return inFlight
  }

  function schedule() {
    clearTimeout(timer)
    if (typeof document !== 'undefined' && document.hidden) return
    timer = setTimeout(async () => {
      await load()
      schedule()
    }, interval.value * 1000 * backoff)
  }

  function onVisibility() {
    if (document.hidden) {
      clearTimeout(timer)
      return
    }
    load().then(schedule)
  }

  onMounted(() => {
    load().then(schedule)
    document.addEventListener('visibilitychange', onVisibility)
  })

  onBeforeUnmount(() => {
    clearTimeout(timer)
    document.removeEventListener('visibilitychange', onVisibility)
  })

  watch([accountSlug, interval], () => {
    load().then(schedule)
  })

  return { snapshot, loading, failed, reload: load }
}

/**
 * Fold a price snapshot into the rows a board shows.
 *
 * The panel stores one row per direction, but an exchange board reads as one
 * line per currency pair with a buy and a sell column, so matching directions
 * are paired back up here rather than in five separate widget variants.
 */
export function buildRateGroups(snapshot, config = {}) {
  if (!snapshot) return []
  const source = config.source || 'categories'
  const categoryIds = new Set((config.category_ids || []).map(Number))
  const priceTypeIds = new Set((config.price_type_ids || []).map(Number))
  const groups = []

  if (source === 'categories' || source === 'both') {
    for (const category of snapshot.categories || []) {
      if (categoryIds.size && !categoryIds.has(Number(category.id))) continue
      const types = (category.price_types || []).filter(
        (type) =>
          type.is_active !== false &&
          type.latest_price != null &&
          (!priceTypeIds.size || priceTypeIds.has(Number(type.id))),
      )
      if (!types.length) continue
      groups.push({ id: `c${category.id}`, name: category.name, rows: pairRows(types) })
    }
  }

  if (source === 'special' || source === 'both') {
    for (const special of snapshot.special_prices || []) {
      const pairs = (special.pairs || []).filter((pair) => pair.latest_price != null)
      if (!pairs.length) continue
      groups.push({ id: `s${special.id}`, name: special.name, rows: pairRows(pairs), special: true })
    }
  }

  return groups
}

function pairRows(entries) {
  const byPair = new Map()
  for (const entry of entries) {
    const from = entry.source_currency?.code || ''
    const to = entry.target_currency?.code || ''
    const key = `${from}>${to}` || entry.name
    if (!byPair.has(key)) {
      byPair.set(key, {
        key,
        name: entry.name,
        from,
        to,
        fromSymbol: entry.source_currency?.symbol || '',
        toSymbol: entry.target_currency?.symbol || '',
        buy: null,
        sell: null,
        updatedAt: null,
      })
    }
    const row = byPair.get(key)
    const quote = {
      price: entry.latest_price,
      at: entry.latest_price_effective_at || entry.latest_price_created_at,
      notes: entry.notes || '',
      name: entry.name,
    }
    if (entry.trade_type === 'sell') row.sell = quote
    else row.buy = quote
    if (quote.at && (!row.updatedAt || quote.at > row.updatedAt)) row.updatedAt = quote.at
    // A one-direction pair still needs a label, and the price type's own name is
    // more meaningful than the currency codes when a desk names it "Cash USD".
    if (!row.buy || !row.sell) row.name = entry.name
  }
  return [...byPair.values()]
}

/** Format a decimal string for display without losing trailing precision. */
export function formatPrice(value, decimals = 2, locale = 'en') {
  if (value == null || value === '') return '—'
  const number = Number(value)
  if (!Number.isFinite(number)) return String(value)
  return number.toLocaleString(locale === 'fa' ? 'en-US' : locale, {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  })
}

/** "Updated 3 minutes ago", in whatever language the visitor is reading. */
export function formatUpdatedAt(iso, locale = 'en') {
  if (!iso) return ''
  const then = new Date(iso)
  if (Number.isNaN(then.getTime())) return ''
  const seconds = Math.round((Date.now() - then.getTime()) / 1000)
  const formatter = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' })
  if (seconds < 60) return formatter.format(-seconds, 'second')
  if (seconds < 3600) return formatter.format(-Math.round(seconds / 60), 'minute')
  if (seconds < 86400) return formatter.format(-Math.round(seconds / 3600), 'hour')
  return formatter.format(-Math.round(seconds / 86400), 'day')
}
