import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const localesDir = path.join(__dirname, '../src/locales')

function getByPath(obj, keyPath) {
  return keyPath.split('.').reduce((o, k) => (o == null ? undefined : o[k]), obj)
}

function setByPath(obj, keyPath, value) {
  const keys = keyPath.split('.')
  let cur = obj
  for (let i = 0; i < keys.length - 1; i++) {
    const k = keys[i]
    if (!cur[k] || typeof cur[k] !== 'object' || Array.isArray(cur[k])) cur[k] = {}
    cur = cur[k]
  }
  cur[keys[keys.length - 1]] = value
}

function allKeys(obj, prefix = '') {
  const out = []
  for (const [k, v] of Object.entries(obj)) {
    const full = prefix ? `${prefix}.${k}` : k
    if (v && typeof v === 'object' && !Array.isArray(v)) out.push(...allKeys(v, full))
    else out.push(full)
  }
  return out
}

const en = JSON.parse(fs.readFileSync(path.join(localesDir, 'en.json'), 'utf8'))
const enKeys = allKeys(en)

for (const loc of ['fa', 'ar', 'es']) {
  const file = path.join(localesDir, `${loc}.json`)
  const data = JSON.parse(fs.readFileSync(file, 'utf8'))
  const locKeys = new Set(allKeys(data))
  let added = 0
  for (const key of enKeys) {
    if (!locKeys.has(key)) {
      const val = getByPath(en, key)
      if (val !== undefined) {
        setByPath(data, key, val)
        added++
      }
    }
  }
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8')
  console.log(`${loc}: added ${added} keys from en fallback`)
}
