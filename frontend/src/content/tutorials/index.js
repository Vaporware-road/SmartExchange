/**
 * Tutorial hub content.
 *
 * Posts are release-managed files, not database rows: they ship with the
 * screenshots they describe, so a post and the build it documents can never
 * drift apart. Copy lives in `landing.tutorials.posts.<slug>.*` in the locale
 * files; only the structure — order, artwork, step ids — is here.
 *
 * `gif` names a file under `backend/static/landing/gifs/`, recorded by
 * `scripts/record_gifs.py` against the running dev app.
 */
export const TUTORIALS = [
  {
    slug: 'publish-prices',
    icon: '💱',
    gif: 'publish-prices.gif',
    minutes: 3,
    steps: ['open', 'enter', 'finalize', 'publish'],
  },
  {
    slug: 'template-editor',
    icon: '🎨',
    gif: 'template-editor.gif',
    minutes: 4,
    steps: ['open', 'drag', 'bind', 'preview'],
  },
  {
    slug: 'telegram-bot',
    icon: '🤖',
    gif: 'telegram-bot.gif',
    minutes: 5,
    steps: ['token', 'channel', 'settings', 'test'],
  },
  {
    slug: 'signup-tour',
    icon: '🚀',
    gif: 'signup-tour.gif',
    minutes: 2,
    steps: ['signup', 'code', 'tour', 'trial'],
  },
]

export const GIF_BASE = '/static/landing/gifs/'

export function findTutorial(slug) {
  return TUTORIALS.find((post) => post.slug === slug) ?? null
}
