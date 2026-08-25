/**
 * Sidebar / drawer / bottom-nav entries.
 * Developer panel (not impersonating) uses a shorter list.
 */
export const staffNavLinks = [
  { to: '/', labelKey: 'sidebar.dashboard', icon: 'fas fa-tachometer-alt', exact: true, activeColor: 'gold' },
  { to: '/update', labelKey: 'sidebar.priceHub', icon: 'fas fa-dollar-sign', exact: false, activeColor: 'buy' },
  { to: '/finalize', labelKey: 'sidebar.finalize', icon: 'fas fa-check-circle', exact: false, permission: 'finalize', activeColor: 'buy' },
  { to: '/categories', labelKey: 'sidebar.categories', icon: 'fas fa-tags', exact: false, activeColor: 'gold' },
  { to: '/analysis', labelKey: 'sidebar.analysis', icon: 'fas fa-chart-line', exact: false, permission: 'analysis', activeColor: 'info' },
  { to: '/telegram/send', labelKey: 'sidebar.telegram', icon: 'fab fa-telegram', exact: false, activeColor: 'info' },
  { to: '/instagram', labelKey: 'sidebar.instagramHub', icon: 'fab fa-instagram', exact: false, activeColor: 'gold' },
  { to: '/templates', labelKey: 'sidebar.templates', icon: 'fas fa-file-image', exact: false, activeColor: 'template' },
  { to: '/users', labelKey: 'sidebar.adminManagement', icon: 'fas fa-user-shield', exact: false, permission: 'adminManagement', activeColor: 'gold' },
  { to: '/settings', labelKey: 'sidebar.settings', icon: 'fas fa-cog', exact: false, permission: 'settings', activeColor: 'gold' },
]

export const developerNavLinks = [
  { to: '/programmer', labelKey: 'sidebar.userManagement', icon: 'fas fa-users', exact: true, permission: 'programmerHub', activeColor: 'gold' },
  { to: '/programmer/register', labelKey: 'sidebar.registerUser', icon: 'fas fa-user-plus', exact: true, permission: 'programmerHub', activeColor: 'gold' },
  { to: '/programmer/templates', labelKey: 'sidebar.plans', icon: 'fas fa-medal', exact: false, permission: 'programmerHub', activeColor: 'gold' },
  { to: '/programmer/fleet', labelKey: 'sidebar.fleet', icon: 'fas fa-server', exact: false, permission: 'programmerHub', activeColor: 'gold' },
  { to: '/analysis', labelKey: 'sidebar.analysis', icon: 'fas fa-chart-line', exact: false, permission: 'analysis', activeColor: 'info' },
  { to: '/telegram/send', labelKey: 'sidebar.telegram', icon: 'fab fa-telegram', exact: false, activeColor: 'info' },
  { to: '/instagram', labelKey: 'sidebar.instagramHub', icon: 'fab fa-instagram', exact: false, activeColor: 'gold' },
  { to: '/templates', labelKey: 'sidebar.templates', icon: 'fas fa-file-image', exact: false, activeColor: 'template' },
  { to: '/users', labelKey: 'sidebar.adminManagement', icon: 'fas fa-user-shield', exact: false, permission: 'adminManagement', activeColor: 'gold' },
  { to: '/settings', labelKey: 'sidebar.settings', icon: 'fas fa-cog', exact: false, permission: 'settings', activeColor: 'gold' },
]

export function navLinkIsActive(route, link) {
  if (link.exact) return route.path === link.to
  if (link.to === '/update') {
    return route.path === '/update' ||
      (route.path.startsWith('/prices/category/') && route.path.endsWith('/update')) ||
      (route.path.startsWith('/prices/special/') && route.path.endsWith('/update'))
  }
  return route.path.startsWith(link.to)
}

export function visibleNavLinks(auth) {
  const links = auth.shouldOpenProgrammerHub ? developerNavLinks : staffNavLinks
  return links.filter((link) => {
    if (!link.permission) return true
    return auth.can(link.permission)
  })
}
