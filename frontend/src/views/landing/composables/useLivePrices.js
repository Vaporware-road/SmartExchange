import { onBeforeUnmount, onMounted, ref } from 'vue'

const TICK_MS = 2600
const DRIFT = 0.004

/**
 * Gives the hero mock panel its "live" feel: every few seconds one row nudges
 * by a fraction of a percent and flashes up or down.
 *
 * Purely cosmetic — these are sample rates, never a quote — so it stops
 * entirely under `prefers-reduced-motion`.
 *
 * @param {Array<{code: string, buy: number, sell: number}>} seed
 */
export function useLivePrices(seed) {
  const rows = ref(seed.map((r) => ({ ...r, buyUp: true, sellUp: false, flash: false })))
  let timer = 0

  function drift(value) {
    return value * (1 + (Math.random() - 0.5) * DRIFT)
  }

  function tick() {
    const index = Math.floor(Math.random() * rows.value.length)
    const row = rows.value[index]
    const nextBuy = drift(row.buy)
    const nextSell = drift(row.sell)

    row.buyUp = nextBuy >= row.buy
    row.sellUp = nextSell >= row.sell
    row.buy = nextBuy
    row.sell = nextSell
    row.flash = true
    setTimeout(() => {
      row.flash = false
    }, 600)
  }

  onMounted(() => {
    if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return
    timer = setInterval(tick, TICK_MS)
  })

  onBeforeUnmount(() => clearInterval(timer))

  return { rows }
}

/** Formats a sample rate at the precision the mock panel shows. */
export function formatRate(value) {
  return value.toFixed(3)
}
