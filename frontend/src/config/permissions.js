/**
 * Central permission config — single source of truth for roles and access.
 *
 * کارمند (employee): اجازهٔ کامل مثل مدیر و ادمین، به‌جز «تغییر و اضافه کردن ادمین».
 * تنها محدودیت: مدیریت کاربران (User Center) — فقط super_admin و management.
 */

export const ROLES = {
  SUPER_ADMIN: 'super_admin',
  MANAGEMENT: 'management',
  DEVELOPER: 'developer',
  EMPLOYEE: 'employee',
}

/** All roles that can use the panel. */
export const ALL_PANEL_ROLES = Object.values(ROLES)

/** Only these roles can manage users (add/edit/remove admins, activity log). */
const ADMIN_MANAGEMENT_ROLES = [ROLES.SUPER_ADMIN, ROLES.MANAGEMENT]

/**
 * Which roles can access each feature.
 * کارمند = همه اجازه‌ها به‌جز adminManagement
 */
export const PERMISSIONS = {
  /** تحلیل و نمودارها — همه */
  analysis: ALL_PANEL_ROLES,
  /** نهایی‌سازی و انتشار به تلگرام — همه */
  finalize: ALL_PANEL_ROLES,
  /** تنظیمات پنل (سایت، ربات، کانال، لاگ‌ها) — همه */
  settings: ALL_PANEL_ROLES,
  /** حذف آیتم‌ها (دسته‌بندی، قالب و غیره) — همه */
  deleteItems: ALL_PANEL_ROLES,
  /** مدیریت کاربران / ادمین‌ها (اضافه، ویرایش، حذف، لاگ فعالیت) — فقط super_admin و management */
  adminManagement: ADMIN_MANAGEMENT_ROLES,
}

function normalizeRole(role) {
  const key = String(role ?? '').trim().toLowerCase().replaceAll('-', '_')
  if (key === 'superadmin') return ROLES.SUPER_ADMIN
  return key
}

/**
 * @param {string|null} role
 * @param {string} permission - key of PERMISSIONS
 * @returns {boolean}
 */
export function can(role, permission) {
  const normalizedRole = normalizeRole(role)
  if (!normalizedRole) return false
  const allowed = PERMISSIONS[permission]
  return Array.isArray(allowed) && allowed.includes(normalizedRole)
}

export default { ROLES, PERMISSIONS, ALL_PANEL_ROLES, can }
