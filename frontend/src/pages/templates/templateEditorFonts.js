/** Map font filename to a safe CSS font-family token (matches injected @font-face). */
export function editorFontFamilyToken(filename) {
  if (!filename || typeof filename !== 'string') return ''
  const safe = filename.replace(/[^a-zA-Z0-9_-]/g, '_')
  return `TE_${safe}`
}

/**
 * Inject @font-face rules for template editor preview (/static/fonts/…).
 * Call once after fetching GET /api/template-editor/fonts/.
 */
export function injectTemplateEditorFontFaces(fontList) {
  if (!Array.isArray(fontList) || !fontList.length) return
  const id = 'template-editor-font-faces'
  let el = document.getElementById(id)
  if (!el) {
    el = document.createElement('style')
    el.id = id
    document.head.appendChild(el)
  }
  const rules = fontList
    .filter((f) => f && f.filename)
    .map((f) => {
      const token = editorFontFamilyToken(f.filename)
      const enc = encodeURIComponent(f.filename)
      return `@font-face{font-family:'${token}';src:url('/static/fonts/${enc}') format('opentype'),url('/static/fonts/${enc}') format('truetype');font-display:swap;}`
    })
  el.textContent = rules.join('\n')
}
