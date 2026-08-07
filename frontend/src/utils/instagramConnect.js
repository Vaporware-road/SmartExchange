/**
 * Instagram OAuth is started by Django at this path (browser navigation).
 * Use a same-origin path so Vite dev proxies to the API host instead of opening
 * a bare http://127.0.0.1:8000/... URL from the JSON API response.
 */
export const INSTAGRAM_OAUTH_CONNECT_PATH = '/instagram-hub/connect/'

/**
 * @param {boolean} hasAppId — from GET /api/instagram-hub/config/ (App ID configured).
 * @returns {string} href for <a> or empty when OAuth cannot start yet.
 */
export function instagramConnectHref(hasAppId) {
  return hasAppId ? INSTAGRAM_OAUTH_CONNECT_PATH : ''
}
