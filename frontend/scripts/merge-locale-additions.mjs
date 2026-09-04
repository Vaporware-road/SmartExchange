import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const localesDir = path.join(__dirname, '../src/locales')
const additions = JSON.parse(fs.readFileSync(path.join(__dirname, 'locale-additions.json'), 'utf8'))

function deepMerge(target, source) {
  for (const [key, value] of Object.entries(source)) {
    if (
      value &&
      typeof value === 'object' &&
      !Array.isArray(value) &&
      target[key] &&
      typeof target[key] === 'object' &&
      !Array.isArray(target[key])
    ) {
      deepMerge(target[key], value)
    } else if (target[key] === undefined) {
      target[key] = value
    }
  }
  return target
}

for (const locale of ['en', 'fa', 'ar', 'es']) {
  const file = path.join(localesDir, `${locale}.json`)
  const data = JSON.parse(fs.readFileSync(file, 'utf8'))
  deepMerge(data, additions[locale] || {})
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8')
  console.log(`merged ${locale}.json`)
}
