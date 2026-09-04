import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    const p = path.join(dir, name)
    if (fs.statSync(p).isDirectory()) walk(p, out)
    else if (/\.vue$/.test(name)) out.push(p)
  }
  return out
}

for (const file of walk(path.join(__dirname, '../src'))) {
  let c = fs.readFileSync(file, 'utf8')
  const o = c
  c = c.replace(/<i class="fas" class="fas fa-arrow-left icon-back me-2" \/>/g, '<i class="fas fa-arrow-left icon-back me-2" />')
  c = c.replace(/<i class="fas me-2" class="fas fa-arrow-left icon-back me-2"><\/i>/g, '<i class="fas fa-arrow-left icon-back me-2"></i>')
  c = c.replace(/ icon-back text-xs text-\[var\(--text-secondary\)\] rtl:rotate-180/g, ' icon-back text-xs text-[var(--text-secondary)]')
  if (c !== o) {
    fs.writeFileSync(file, c)
    console.log('fixed', path.relative(path.join(__dirname, '../src'), file))
  }
}
