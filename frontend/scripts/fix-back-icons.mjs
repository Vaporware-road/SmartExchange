import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const files = [
  'views/categories/CategoryFormView.vue',
  'views/categories/TelegramStudioView.vue',
  'views/prices/BulkUpdateView.vue',
  'views/finalize/FinalizeCategoryView.vue',
  'views/finalize/FinalizeSpecialPriceView.vue',
  'views/special-prices/SpecialPriceFormView.vue',
  'views/settings/LogsView.vue',
  'views/special-prices/UpdateSpecialPriceView.vue',
  'views/special-prices/SpecialPriceHistoryView.vue',
]

for (const rel of files) {
  const file = path.join(__dirname, '../src', rel)
  let c = fs.readFileSync(file, 'utf8')
  c = c.replace(/:class="isRtl \? 'fa-arrow-right' : 'fa-arrow-left icon-back'"/g, "class=\"fas fa-arrow-left icon-back me-2\"")
  c = c.replace(/<i class="fas" :class="isRtl \? 'fa-arrow-right' : 'fa-arrow-left icon-back'" \/>/g, '<i class="fas fa-arrow-left icon-back me-2" />')
  c = c.replace(/:class="\$i18n\.locale && \['fa', 'ar'\]\.includes\(\$i18n\.locale\) \? 'fa-arrow-right' : 'fa-arrow-left icon-back'"/g, "class=\"fas fa-arrow-left icon-back me-2\"")
  c = c.replace(/<i class="fas me-2" :class="\$i18n\.locale[^"]*"/g, '<i class="fas fa-arrow-left icon-back me-2"')
  c = c.replace(/<i class="fas" :class="'fa-arrow-left icon-back'" \/>/g, '<i class="fas fa-arrow-left icon-back me-2" />')
  fs.writeFileSync(file, c)
  console.log('fixed', rel)
}
