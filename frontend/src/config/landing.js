/**
 * Landing page data that is not copy.
 *
 * Prices, links and phone numbers live here so a change lands in one file
 * instead of seven locale dictionaries. Anything a visitor reads as a sentence
 * belongs in `landing.*` in `src/locales/*.json` instead.
 */

/** Sales line. Shown verbatim, always LTR, and reused for the WhatsApp deep link. */
export const CONTACT_PHONE = '+989916122680'

/** `wa.me` wants the number without `+` or separators. */
const WHATSAPP_NUMBER = CONTACT_PHONE.replace(/\D/g, '')

/**
 * Telegram channel. Placeholder until the real channel is live — change the
 * handle here and the nav link, the channel section and the footer all follow.
 */
export const TELEGRAM_CHANNEL = '@mrexchange'
export const TELEGRAM_URL = `https://t.me/${TELEGRAM_CHANNEL.replace('@', '')}`

export const TEL_HREF = `tel:${CONTACT_PHONE}`

/** Pre-filled WhatsApp message, localised by the caller. */
export function whatsappHref(message) {
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`
}

/** Instant demo: `?demo=1` autologs into the shared demo account (LoginView). */
export const DEMO_URL = '/login?demo=1'
/**
 * Trials are self-serve: the visitor signs up with an email address and lands
 * in their own panel with the clock already running. Kept in sync with the
 * backend's INDIVIDUAL_TRIAL_DAYS — this constant only writes the copy.
 */
export const TRIAL_URL = '/signup'
export const TRIAL_DAYS = 14

/** Bundle price. One-off — the only recurring line is the optional support add-on. */
export const BUNDLE_PRICE = 399

/** Optional monthly support retainer. */
export const SUPPORT_PRICE = 40

/**
 * Ticker rows. Static sample rates: the marketing page must render before any
 * API call, and these are illustrative, not quoted.
 */
export const TICKER_RATES = [
  { pair: 'GBP/EUR', value: '1.185', change: '0.21%', up: true },
  { pair: 'GBP/USD', value: '1.271', change: '0.14%', up: false },
  { pair: 'EUR/USD', value: '1.072', change: '0.08%', up: true },
  { pair: 'GBP/AED', value: '4.668', change: '0.32%', up: true },
  { pair: 'GBP/TRY', value: '41.90', change: '0.55%', up: false },
  { pair: 'USDT/GBP', value: '0.787', change: '0.05%', up: true },
  { pair: 'BTC/GBP', value: '52,140', change: '1.24%', up: true },
  { pair: 'XAU/GBP', value: '1,948', change: '0.31%', up: false },
]

/** Hero mock panel rows. `base` drives the live-price jitter animation. */
export const HERO_RATES = [
  { flag: '🇬🇧', code: 'GBP', buy: 1.25, sell: 1.285 },
  { flag: '🇺🇸', code: 'USD', buy: 0.79, sell: 0.81 },
  { flag: '🇪🇺', code: 'EUR', buy: 0.85, sell: 0.875 },
  { flag: '🇦🇪', code: 'AED', buy: 0.215, sell: 0.225 },
]

/** Channels marquee. `key` resolves to `landing.channels.<key>`. */
export const CHANNELS = [
  { key: 'telegram', icon: '✈️' },
  { key: 'instagram', icon: '📸' },
  { key: 'website', icon: '🌐' },
  { key: 'widget', icon: '🧩' },
  { key: 'bot', icon: '🤖' },
  { key: 'api', icon: '🔌' },
  { key: 'reports', icon: '📊' },
  { key: 'branches', icon: '🏢' },
  { key: 'security', icon: '🔐' },
  { key: 'whatsapp', icon: '💬' },
]

/**
 * Add-on catalogue.
 *
 * `market` is the researched going rate for the same service (agency/freelance,
 * 2026); `price` is ours and is deliberately set below it. Keep that ordering
 * true — the cards render the market figure struck through next to ours.
 *
 * `unit`: 'once' | 'month'. `optional` marks a line the customer can decline.
 * `note` renders a short price qualifier under the card text, resolved from
 * `landing.addons.items.<key>.note` (e.g. "free with the package").
 */
export const ADDONS = [
  { key: 'website', icon: '🌐', price: '$400', market: '$1,200–4,500', unit: 'once' },
  { key: 'mobileApp', icon: '📱', price: '$500', market: '$2,000–8,000', unit: 'once' },
  { key: 'api', icon: '🔌', price: '$30', market: '$150–600', unit: 'once', note: true },
  { key: 'accounting', icon: '🧮', price: '$80', market: '$400–1,500', unit: 'once', note: true },
  { key: 'telegramBot', icon: '🤖', price: '$100', market: '$250–800', unit: 'once' },
  { key: 'whatsapp', icon: '💬', price: '$100', market: '$300–900', unit: 'once' },
  { key: 'widget', icon: '🧩', price: '$100', market: '$250–800', unit: 'once' },
  { key: 'branch', icon: '🏢', price: '$130', market: '$300–900', unit: 'once', note: true },
  { key: 'migration', icon: '📦', price: '$50', market: '$150–600', unit: 'once' },
  { key: 'training', icon: '🎓', price: 'Free', market: '$200–600', unit: 'once', note: true },
  { key: 'domain', icon: '🔒', price: '$50', market: '$150–400', unit: 'once', note: true },
  { key: 'support', icon: '🛠️', price: '$40', market: '$250–550', unit: 'month', optional: true, featured: true },
  { key: 'social', icon: '📣', price: '$150', market: '$400–3,800', unit: 'month', optional: true },
  { key: 'seo', icon: '🔍', price: '$200', market: '$800–2,400', unit: 'month', optional: true },
  { key: 'content', icon: '🖼️', price: '$150', market: '$240–1,200', unit: 'month', optional: true },
  { key: 'hosting', icon: '🖧', price: '$30', market: '$40–400', unit: 'month', optional: true },
  { key: 'rateFeed', icon: '📡', price: '$35', market: '$70–300', unit: 'month', optional: true },
]

/** Rows of the "package features" table. */
export const PACKAGE_FEATURES = [
  'panel',
  'instant',
  'telegram',
  'telegramBot',
  'instagram',
  'website',
  'graphics',
  'widget',
  'reports',
  'alerts',
  'branches',
  'roles',
  'backups',
  'support',
]

/** FAQ entries; copy resolves to `landing.faq.items.<key>.q` / `.a`. */
export const FAQ_KEYS = ['auto', 'telegram', 'instagram', 'branding', 'website', 'branches', 'setup', 'api', 'support']
