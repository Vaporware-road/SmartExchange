import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const root = path.join(__dirname, '../src')

function patch(rel, pairs) {
  const file = path.join(root, rel)
  let c = fs.readFileSync(file, 'utf8')
  let n = 0
  for (const [from, to] of pairs) {
    if (!c.includes(from)) {
      console.warn(`[${rel}] missing:`, from.slice(0, 70))
      continue
    }
    c = c.replace(from, to)
    n++
  }
  fs.writeFileSync(file, c)
  console.log(`patched ${rel} (${n})`)
}

patch('views/templates/TemplatesDashboardView.vue', [
  ['<i class="fas fa-plus"></i> Add Template', '<i class="fas fa-plus"></i> {{ $t(\'templates.addTemplate\') }}'],
  ["{{ $t('emptyState.noTemplates') || 'No templates yet.' }}", "{{ $t('emptyState.noTemplates') }}"],
  ['{{ t.name ?? `Template ${t.id}` }}', "{{ t.name ?? $t('templates.templateNumber', { id: t.id }) }}"],
  ['<i class="fas fa-edit"></i> Editor', "<i class=\"fas fa-edit\"></i> {{ $t('templates.openEditor') }}"],
  ["{{ deletingId === t.id ? 'Deleting...' : 'Delete' }}", "{{ deletingId === t.id ? $t('common.deleting') : $t('common.delete') }}"],
  ["return 'Unassigned'", "return t('templates.unassigned')"],
  ['import { ref, onMounted } from \'vue\'', "import { ref, onMounted } from 'vue'\nimport { useI18n } from 'vue-i18n'"],
  ['const toast = useToast()', "const { t } = useI18n()\nconst toast = useToast()"],
  ['`Are you sure you want to delete "${name}"?\\nThis action cannot be undone.`', "t('templates.deleteConfirm')"],
  ["toast.success('Template deleted successfully.')", "toast.success(t('templates.deleteSuccess'))"],
])

patch('views/templates/TemplateFormView.vue', [
  ["|| 'Creating template for category'", ''],
  ["toast.error('Please enter a template name.')", "toast.error(t('templates.nameRequired'))"],
  ["toast.error('A category is required to create a template.')", "toast.error(t('templates.categoryRequired'))"],
  ["|| 'Create failed'", "|| t('templates.createFailed')"],
  ["'Category'", "$t('common.category')"],
  ["'Select category'", "$t('categories.selectCategory')"],
])

patch('views/templates/TemplateMediaLibraryView.vue', [
  ['JPG, PNG, GIF, WebP — copy URLs', "{{ $t('templateMedia.formatHint') }}"],
  ["'Upload images'", "$t('templateMedia.uploadImages')"],
  ['Copy link', "{{ $t('common.copyLink') }}"],
  ["toast.success('Link copied')", "toast.success(t('toast.linkCopied'))"],
  ["toast.error('Could not copy')", "toast.error(t('toast.copyFailed'))"],
  ["toast.success(`Uploaded: ${file.name}`)", "toast.success(t('templateMedia.uploadSuccess', { name: file.name }))"],
])

patch('views/templates/HeadlessTemplateRenderer.vue', [
  ['Loading…', "{{ $t('common.loading') }}"],
  ["loadError.value = 'Missing render token'", "loadError.value = t('templateRenderer.missingToken')"],
  ["loadError.value = 'Failed to load render context'", "loadError.value = t('templateRenderer.loadFailed')"],
])

patch('views/auth/LandingView.vue', [
  ['Access Panel', "{{ $t('landing.accessPanel') }}"],
])

patch('components/layout/AppFooter.vue', [
  ['Powered by Siavash', "{{ $t('footer.poweredBy') }}"],
])

patch('components/layout/AppSidebar.vue', [
  ['aria-label="Toggle sidebar"', ":aria-label=\"$t('a11y.toggleSidebar')\""],
])

patch('components/layout/AppBreadcrumb.vue', [
  ['aria-label="Breadcrumb"', ":aria-label=\"$t('a11y.breadcrumb')\""],
])

patch('components/ui/ThemeToggle.vue', [
  ['aria-label="Toggle theme"', ":aria-label=\"$t('a11y.toggleTheme')\""],
])

patch('components/ui/AlertMessage.vue', [
  ['aria-label="Dismiss"', ":aria-label=\"$t('a11y.dismiss')\""],
])

patch('views/prices/PricesView.vue', [
  ['>Price Type<', ">{{ $t('prices.columns.priceType') }}<"],
  ['>Category<', ">{{ $t('prices.columns.category') }}<"],
  ['>Pair<', ">{{ $t('prices.columns.pair') }}<"],
  ['>Latest Price<', ">{{ $t('prices.columns.latestPrice') }}<"],
  ['>Actions<', ">{{ $t('prices.columns.actions') }}<"],
])

patch('views/prices/PriceHistoryView.vue', [
  ['>Price<', ">{{ $t('priceHistory.columns.price') }}<"],
  ['>Date<', ">{{ $t('priceHistory.columns.date') }}<"],
  ['>Notes<', ">{{ $t('priceHistory.columns.notes') }}<"],
])

patch('views/prices/UpdatePriceView.vue', [
  ['Back to Prices', "{{ $t('prices.backToList') }}"],
  ['New Price', "{{ $t('prices.newPrice') }}"],
  ['Notes (optional)', "{{ $t('prices.notesOptional') }}"],
  ['placeholder="Optional notes"', ":placeholder=\"$t('prices.notesPlaceholder')\""],
])

patch('views/special-prices/SpecialPriceHistoryView.vue', [
  ['>Price<', ">{{ $t('priceHistory.columns.price') }}<"],
  ['>Date<', ">{{ $t('priceHistory.columns.date') }}<"],
])

patch('components/template-editor/player/widgets/ImageWidgetPreview.vue', [
  ['Image URL', "{{ $t('templateEditor.inspector.imageUrl') }}"],
])
