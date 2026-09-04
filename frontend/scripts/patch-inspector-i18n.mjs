import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const file = path.join(__dirname, '../src/pages/templates/TemplateInspectorPanel.vue')
let c = fs.readFileSync(file, 'utf8')

const replacements = [
  ['>Inspector<', ">{{ $t('templateEditor.inspector.title') }}<"],
  ['>Template settings<', ">{{ $t('templateEditor.inspector.templateSettings') }}<"],
  ['>Template name<', ">{{ $t('templateEditor.inspector.templateName') }}<"],
  ['>Width<', ">{{ $t('templateEditor.inspector.width') }}<"],
  ['>Height<', ">{{ $t('templateEditor.inspector.height') }}<"],
  ['>Canvas background<', ">{{ $t('templateEditor.inspector.canvasBackground') }}<"],
  ['          Upload background image\n', "          {{ $t('templateEditor.inspector.uploadBackground') }}\n"],
  ['Select a widget to edit style, typography and data bindings.', "{{ $t('templateEditor.inspector.selectWidget') }}"],
  ['>Name<', ">{{ $t('common.name') }}<"],
  ['>Type<', ">{{ $t('common.type') }}<"],
  ['>PriceType binding<', ">{{ $t('templateEditor.inspector.priceTypeBinding') }}<"],
  ['>Select PriceType<', ">{{ $t('templateEditor.inspector.selectPriceType') }}<"],
  ['Stable key:', "{{ $t('templateEditor.inspector.stableKey') }}"],
  ['Preview source:', "{{ $t('templateEditor.inspector.previewSource') }}"],
  [' | Value: ', " | {{ $t('templateEditor.inspector.previewValue') }} "],
  ['Fallback value (used when live value is unavailable)', "{{ $t('templateEditor.inspector.fallbackValue') }}"],
  ['Uses <code class="font-mono">time</code> from server data.', "{{ $t('templateEditor.inspector.clockUsesServerTime') }}"],
  ['>Typography<', ">{{ $t('templateEditor.inspector.typography') }}<"],
  ['>Font size<', ">{{ $t('templateEditor.inspector.fontSize') }}<"],
  ['>Text color<', ">{{ $t('templateEditor.inspector.textColor') }}<"],
  ['title="Pick color"', ":title=\"$t('templateEditor.inspector.pickColor')\""],
  ['>Font file (PNG export)<', ">{{ $t('templateEditor.inspector.fontFile') }}<"],
  ['>Default (server)<', ">{{ $t('templateEditor.inspector.defaultServerFont') }}<"],
  ['>Align<', ">{{ $t('templateEditor.inspector.align') }}<"],
  ['>Vertical (in box)<', ">{{ $t('templateEditor.inspector.verticalAlign') }}<"],
  ['>Weight<', ">{{ $t('templateEditor.inspector.weight') }}<"],
  ['>Line height (optional)<', ">{{ $t('templateEditor.inspector.lineHeight') }}<"],
  ['placeholder="e.g. 1.2 or 32"', ":placeholder=\"$t('templateEditor.inspector.lineHeightPlaceholder')\""],
  ['>Plain text on export (no outline / shadow)<', ">{{ $t('templateEditor.inspector.plainTextExport') }}<"],
  ['>Drop shadow (PNG)<', ">{{ $t('templateEditor.inspector.dropShadow') }}<"],
  ['>Text outline (PNG)<', ">{{ $t('templateEditor.inspector.textOutline') }}<"],
  ['>Snap to background image<', ">{{ $t('templateEditor.inspector.snapToBackground') }}<"],
  ['Moves the widget box to the edges of the visible image (letterboxing excluded).', "{{ $t('templateEditor.inspector.snapHelp') }}"],
  ["alignWidgetToBackground('left')\">Left<", "alignWidgetToBackground('left')\">{{ $t('templateEditor.inspector.snapLeft') }}<"],
  ["alignWidgetToBackground('center-h')\">H mid<", "alignWidgetToBackground('center-h')\">{{ $t('templateEditor.inspector.snapHMid') }}<"],
  ["alignWidgetToBackground('right')\">Right<", "alignWidgetToBackground('right')\">{{ $t('templateEditor.inspector.snapRight') }}<"],
  ["alignWidgetToBackground('top')\">Top<", "alignWidgetToBackground('top')\">{{ $t('templateEditor.inspector.snapTop') }}<"],
  ["alignWidgetToBackground('center-v')\">V mid<", "alignWidgetToBackground('center-v')\">{{ $t('templateEditor.inspector.snapVMid') }}<"],
  ["alignWidgetToBackground('bottom')\">Bottom<", "alignWidgetToBackground('bottom')\">{{ $t('templateEditor.inspector.snapBottom') }}<"],
  ['>Image URL<', ">{{ $t('templateEditor.inspector.imageUrl') }}<"],
  ['placeholder="https://… or /media/…"', ":placeholder=\"$t('templateEditor.inspector.imageUrlPlaceholder')\""],
  ["{{ uploading ? 'Uploading…' : 'Upload image' }}", "{{ uploading ? $t('common.uploading') : $t('templateEditor.inspector.uploadImage') }}"],
  ['          Open media library\n', "          {{ $t('templateEditor.inspector.openMediaLibrary') }}\n"],
  ['>Opacity (editor + PNG)<', ">{{ $t('templateEditor.inspector.opacity') }}<"],
  ['>z-index<', ">{{ $t('templateEditor.inspector.zIndex') }}<"],
  ['>Rotation<', ">{{ $t('templateEditor.inspector.rotation') }}<"],
  ['        Delete widget\n', "        {{ $t('templateEditor.inspector.deleteWidget') }}\n"],
  ["toast.success('Image uploaded')", "toast.success(t('templateEditor.inspector.imageUploaded'))"],
  ["{ id: 'appearance', label: 'Appearance' }", "{ id: 'appearance', label: t('templateEditor.inspector.tabs.appearance') }"],
  ["{ id: 'typography', label: 'Font' }", "{ id: 'typography', label: t('templateEditor.inspector.tabs.typography') }"],
  ["{ id: 'data', label: 'Data' }", "{ id: 'data', label: t('templateEditor.inspector.tabs.data') }"],
  ['const inspectorTabs = [', 'const inspectorTabs = computed(() => ['],
  [']\n\nconst isTextLikeWidget', '])\n\nconst isTextLikeWidget'],
  ['<option value="left">Left</option>', '<option value="left">{{ $t(\'templateEditor.inspector.alignLeft\') }}</option>'],
  ['<option value="center">Center</option>', '<option value="center">{{ $t(\'templateEditor.inspector.alignCenter\') }}</option>'],
  ['<option value="right">Right</option>', '<option value="right">{{ $t(\'templateEditor.inspector.alignRight\') }}</option>'],
  ['<option value="middle">Middle</option>', '<option value="middle">{{ $t(\'templateEditor.inspector.valignMiddle\') }}</option>'],
  ['<option value="top">Top</option>', '<option value="top">{{ $t(\'templateEditor.inspector.valignTop\') }}</option>'],
  ['<option value="bottom">Bottom</option>', '<option value="bottom">{{ $t(\'templateEditor.inspector.valignBottom\') }}</option>'],
  ['<option value="normal">Normal</option>', '<option value="normal">{{ $t(\'templateEditor.inspector.weightNormal\') }}</option>'],
  ['<option value="bold">Bold</option>', '<option value="bold">{{ $t(\'templateEditor.inspector.weightBold\') }}</option>'],
]

for (const [from, to] of replacements) {
  if (!c.includes(from)) {
    console.warn('missing:', from.slice(0, 60))
    continue
  }
  c = c.replace(from, to)
}

if (!c.includes("import { ref, computed, onMounted, nextTick }")) {
  c = c.replace("import { ref, onMounted, nextTick }", "import { ref, computed, onMounted, nextTick }")
}

fs.writeFileSync(file, c)
console.log('patched TemplateInspectorPanel')
