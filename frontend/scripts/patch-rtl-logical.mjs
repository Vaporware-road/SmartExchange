import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const srcRoot = path.join(__dirname, '../src')

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    const p = path.join(dir, name)
    const st = fs.statSync(p)
    if (st.isDirectory()) walk(p, out)
    else if (/\.vue$/.test(name)) out.push(p)
  }
  return out
}

const files = walk(srcRoot)
let total = 0

for (const file of files) {
  let c = fs.readFileSync(file, 'utf8')
  const orig = c

  c = c.replace(/\btext-left\b/g, 'text-start')
  c = c.replace(/\btext-right\b/g, 'text-end')
  c = c.replace(/\bmr-2\b/g, 'me-2')
  c = c.replace(/\bml-2\b/g, 'ms-2')
  c = c.replace(/\bml-1\b/g, 'ms-1')
  c = c.replace(/\bmr-1\b/g, 'me-1')
  c = c.replace(/\bml-8\b/g, 'ms-8')
  c = c.replace(/\bpr-24 rtl:pr-4 rtl:pl-24\b/g, 'pe-24')
  c = c.replace(/\btop-4 right-4\b/g, 'top-4 end-4')
  c = c.replace(/\btop-3 right-3\b/g, 'top-3 end-3')
  c = c.replace(/fa-arrow-left(?![\w-])/g, (m, offset, str) => {
    const before = str.slice(Math.max(0, offset - 20), offset)
    if (before.includes('icon-back')) return m
  // skip if already has rtl:rotate-180 nearby
    const after = str.slice(offset, offset + 40)
    if (after.includes('rtl:rotate-180')) return m
    return 'fa-arrow-left icon-back'
  })
  c = c.replace(/fa-chevron-left(?![\w-])/g, (m, offset, str) => {
    const after = str.slice(offset, offset + 40)
    if (after.includes('rtl:') || str.slice(offset - 15, offset).includes('icon-back')) return m
    return 'fa-chevron-left icon-back'
  })
  c = c.replace(/\$i18n\.locale && \['fa', 'ar'\]\.includes\(\$i18n\.locale\) \? 'fa-arrow-right' : 'fa-arrow-left'/g, "'fa-arrow-left icon-back'")

  if (c !== orig) {
    fs.writeFileSync(file, c)
    total++
    console.log('patched', path.relative(srcRoot, file))
  }
}

console.log(`done: ${total} files`)
