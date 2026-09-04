import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const file = path.join(__dirname, '../src/views/categories/TelegramStudioView.vue')
let c = fs.readFileSync(file, 'utf8')
c = c.replace(/\s*\|\|\s*'(?:[^'\\]|\\.)*'/g, '')
c = c.replace(/\s*\|\|\s*"(?:[^"\\]|\\.)*"/g, '')
fs.writeFileSync(file, c)
console.log('removed telegram studio fallbacks')
