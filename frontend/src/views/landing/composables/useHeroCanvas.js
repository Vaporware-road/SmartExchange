import { onBeforeUnmount, onMounted } from 'vue'

const LINK_DISTANCE = 130
const DENSITY = 14000

/**
 * Hero background: a drifting particle network drawn on a `<canvas>`.
 *
 * Kept hand-rolled rather than pulled from a library — it is ~60 lines and the
 * panel bundle should not grow for one decorative background. Colours come from
 * `--primary` so it follows the active theme.
 *
 * @param {import('vue').Ref<HTMLCanvasElement|null>} canvasRef
 */
export function useHeroCanvas(canvasRef) {
  let frame = 0
  let particles = []
  let ctx = null
  let resizeObserver = null

  function accent() {
    const value = getComputedStyle(document.documentElement).getPropertyValue('--primary').trim()
    return value || '#ffd700'
  }

  function seed(width, height) {
    const count = Math.min(90, Math.round((width * height) / DENSITY))
    particles = Array.from({ length: count }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      r: Math.random() * 1.6 + 0.6,
    }))
  }

  function resize() {
    const canvas = canvasRef.value
    if (!canvas) return
    const dpr = Math.min(window.devicePixelRatio || 1, 2)
    const { clientWidth: w, clientHeight: h } = canvas
    canvas.width = w * dpr
    canvas.height = h * dpr
    ctx = canvas.getContext('2d')
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    seed(w, h)
  }

  function draw() {
    const canvas = canvasRef.value
    if (!canvas || !ctx) return
    const w = canvas.clientWidth
    const h = canvas.clientHeight
    const color = accent()

    ctx.clearRect(0, 0, w, h)

    for (const p of particles) {
      p.x += p.vx
      p.y += p.vy
      if (p.x < 0 || p.x > w) p.vx *= -1
      if (p.y < 0 || p.y > h) p.vy *= -1
    }

    ctx.strokeStyle = color
    for (let i = 0; i < particles.length; i += 1) {
      for (let j = i + 1; j < particles.length; j += 1) {
        const dx = particles[i].x - particles[j].x
        const dy = particles[i].y - particles[j].y
        const dist = Math.hypot(dx, dy)
        if (dist > LINK_DISTANCE) continue
        ctx.globalAlpha = (1 - dist / LINK_DISTANCE) * 0.18
        ctx.beginPath()
        ctx.moveTo(particles[i].x, particles[i].y)
        ctx.lineTo(particles[j].x, particles[j].y)
        ctx.stroke()
      }
    }

    ctx.fillStyle = color
    ctx.globalAlpha = 0.5
    for (const p of particles) {
      ctx.beginPath()
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
      ctx.fill()
    }
    ctx.globalAlpha = 1

    frame = requestAnimationFrame(draw)
  }

  onMounted(() => {
    const canvas = canvasRef.value
    if (!canvas) return
    if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return

    resize()
    resizeObserver = new ResizeObserver(resize)
    resizeObserver.observe(canvas)
    frame = requestAnimationFrame(draw)
  })

  onBeforeUnmount(() => {
    cancelAnimationFrame(frame)
    resizeObserver?.disconnect()
    resizeObserver = null
    particles = []
    ctx = null
  })
}
