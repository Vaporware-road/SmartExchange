/**
 * Guided tour shown to visitors exploring the public demo account.
 *
 * One step per thing the panel actually does, in the order a rate desk uses it:
 * quote → publish → brand → measure. `to` is the panel route the step opens;
 * copy resolves to `demo.tour.steps.<key>.title` / `.body` / `.look`.
 *
 * `permission` hides a step the demo role cannot open (see config/permissions).
 */
export const DEMO_TOUR_STEPS = [
  { key: 'dashboard', to: '/panel', icon: 'fas fa-tachometer-alt' },
  { key: 'prices', to: '/update', icon: 'fas fa-dollar-sign' },
  { key: 'finalize', to: '/finalize', icon: 'fas fa-check-circle', permission: 'finalize' },
  { key: 'categories', to: '/categories', icon: 'fas fa-tags' },
  { key: 'templates', to: '/templates', icon: 'fas fa-file-image' },
  { key: 'telegram', to: '/telegram/send', icon: 'fab fa-telegram' },
  { key: 'instagram', to: '/instagram', icon: 'fab fa-instagram' },
  { key: 'analytics', to: '/analysis', icon: 'fas fa-chart-line', permission: 'analysis' },
]

export function visibleTourSteps(auth) {
  return DEMO_TOUR_STEPS.filter((step) => !step.permission || auth.can(step.permission))
}
