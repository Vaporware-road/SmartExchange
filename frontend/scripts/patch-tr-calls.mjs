import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const file = path.join(__dirname, '../src/views/users/UserManagementView.vue')
let c = fs.readFileSync(file, 'utf8')
c = c.replace(/tr\('([^']+)',\s*'(?:[^'\\]|\\.)*',\s*'(?:[^'\\]|\\.)*'\)/g, "t('$1')")
c = c.replace(/function tr\(key, faText, enText\) \{[\s\S]*?\}\n\n/, '')
c = c.replace(/const \{ t, te, locale \} = useI18n\(\)/, 'const { t } = useI18n()')
fs.writeFileSync(file, c)
console.log('patched UserManagementView')
