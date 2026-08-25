import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import Layout from '@/layouts/AppLayout.vue'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('@/views/auth/LandingView.vue'),
    meta: { public: true },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: { public: true },
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/auth/AboutView.vue'),
    meta: { public: true },
  },
  {
    path: '/error/404',
    name: 'error-404',
    component: () => import('@/views/errors/ErrorView.vue'),
    props: { code: 404 },
    meta: { public: true },
  },
  {
    path: '/error/500',
    name: 'error-500',
    component: () => import('@/views/errors/ErrorView.vue'),
    props: { code: 500 },
    meta: { public: true },
  },
  {
    path: '/error/403',
    name: 'error-403',
    component: () => import('@/views/errors/ErrorView.vue'),
    props: { code: 403 },
    meta: { public: true },
  },
  {
    path: '/panel',
    component: Layout,
    meta: { requiresAuth: true, titleKey: 'breadcrumb.home' },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/views/dashboard/DashboardView.vue'),
        meta: { titleKey: 'routes.dashboard' },
      },
      {
        path: 'programmer',
        name: 'programmer',
        component: () => import('@/views/programmer/ProgrammerHubView.vue'),
        meta: {
          titleKey: 'routes.programmerHub',
          roles: ['super_admin', 'developer'],
        },
      },
      {
        path: 'programmer/register',
        name: 'programmer-register',
        component: () => import('@/views/programmer/ProgrammerRegisterView.vue'),
        meta: {
          titleKey: 'routes.programmerRegister',
          roles: ['super_admin', 'developer'],
        },
      },
      {
        path: 'programmer/users/:id',
        name: 'programmer-user',
        component: () => import('@/views/programmer/ProgrammerUserDetailView.vue'),
        meta: {
          titleKey: 'routes.programmerUser',
          roles: ['super_admin', 'developer'],
        },
      },
      {
        path: 'programmer/fleet',
        name: 'programmer-fleet',
        component: () => import('@/views/programmer/ProgrammerFleetView.vue'),
        meta: {
          titleKey: 'routes.programmerFleet',
          roles: ['super_admin', 'developer'],
        },
      },
      {
        path: 'programmer/templates',
        name: 'programmer-templates',
        component: () => import('@/views/programmer/ProgrammerTemplatesView.vue'),
        meta: {
          titleKey: 'routes.programmerTemplates',
          roles: ['super_admin', 'developer'],
        },
      },
      {
        path: 'update',
        name: 'update',
        component: () => import('@/views/prices/PriceManagementView.vue'),
        meta: { titleKey: 'routes.priceHub' },
      },
      {
        path: 'prices',
        name: 'prices',
        redirect: { path: '/update' },
      },
      {
        path: 'prices/category/:id/update',
        name: 'bulk-update',
        component: () => import('@/views/prices/BulkUpdateView.vue'),
        meta: { titleKey: 'routes.bulkUpdate' },
      },
      {
        path: 'prices/special/:id/update',
        name: 'update-special-price',
        component: () => import('@/views/special-prices/UpdateSpecialPriceView.vue'),
        meta: { titleKey: 'routes.updateSpecialPrice' },
      },
      {
        path: 'prices/:id/history',
        name: 'price-history',
        component: () => import('@/views/prices/PriceHistoryView.vue'),
        meta: { titleKey: 'routes.priceHistory' },
      },
      {
        path: 'special-prices',
        name: 'special-prices',
        redirect: { path: '/update' },
      },
      {
        path: 'special-prices/new',
        name: 'special-price-new',
        component: () => import('@/views/special-prices/SpecialPriceFormView.vue'),
        meta: { titleKey: 'routes.specialPriceNew' },
      },
      {
        path: 'special-prices/:id/update',
        name: 'update-special-price-legacy',
        redirect: (to) => ({ path: `/prices/special/${to.params.id}/update` }),
      },
      {
        path: 'special-prices/:id/template',
        name: 'special-price-template',
        component: () => import('@/views/special-prices/SpecialPriceTemplateRedirectView.vue'),
        meta: { titleKey: 'routes.templateEditor' },
      },
      {
        path: 'special-prices/:id/telegram-studio',
        name: 'special-price-telegram-studio',
        component: () => import('@/views/special-prices/SpecialPriceTelegramRedirectView.vue'),
        meta: { titleKey: 'routes.telegramStudio' },
      },
      {
        path: 'special-prices/:id/history',
        name: 'special-price-history',
        component: () => import('@/views/special-prices/SpecialPriceHistoryView.vue'),
        meta: { titleKey: 'routes.specialPriceHistory' },
      },
      {
        path: 'finalize',
        name: 'finalize',
        component: () => import('@/views/finalize/FinalizeDashboardView.vue'),
        meta: { titleKey: 'routes.finalize' },
      },
      {
        path: 'finalize/category/:id',
        name: 'finalize-category',
        component: () => import('@/views/finalize/FinalizeCategoryView.vue'),
        meta: { titleKey: 'routes.finalizeCategory' },
      },
      {
        path: 'finalize/special-price/:id',
        name: 'finalize-special-price',
        component: () => import('@/views/finalize/FinalizeSpecialPriceView.vue'),
        meta: { titleKey: 'routes.finalizeSpecialPrice' },
      },
      {
        path: 'categories',
        name: 'categories',
        component: () => import('@/views/categories/CategoriesView.vue'),
        meta: { titleKey: 'routes.categories' },
      },
      {
        path: 'categories/new',
        name: 'category-new',
        component: () => import('@/views/categories/CategoryFormView.vue'),
        meta: { titleKey: 'routes.categoryNew' },
      },
      {
        path: 'categories/create',
        redirect: { name: 'category-new' },
      },
      {
        path: 'categories/:id/edit',
        name: 'category-edit',
        component: () => import('@/views/categories/CategoryFormView.vue'),
        meta: { titleKey: 'routes.categoryEdit' },
      },
      {
        path: 'categories/:id/price-types/new',
        name: 'price-type-new',
        component: () => import('@/views/categories/PriceTypeFormView.vue'),
        meta: { titleKey: 'routes.priceTypeNew' },
      },
      {
        path: 'categories/:id/price-types/:priceTypeId/edit',
        name: 'price-type-edit',
        component: () => import('@/views/categories/PriceTypeFormView.vue'),
        meta: { titleKey: 'routes.priceTypeNew' },
      },
      {
        path: 'categories/:id/template',
        name: 'category-template',
        component: () => import('@/views/categories/CategoryTemplateRedirectView.vue'),
        meta: { titleKey: 'routes.templateEditor' },
      },
      {
        path: 'categories/:id/telegram-studio',
        name: 'telegram-studio',
        component: () => import('@/views/categories/TelegramStudioView.vue'),
        meta: { titleKey: 'routes.telegramStudio' },
      },
      {
        path: 'categories/:id/template',
        name: 'category-template',
        component: () => import('@/views/categories/CategoryTemplateRedirectView.vue'),
        meta: { titleKey: 'routes.templateEditor' },
      },
      {
        path: 'settings',
        name: 'settings',
        component: () => import('@/views/settings/SettingsView.vue'),
        meta: { titleKey: 'routes.settings' },
      },
      {
        path: 'users',
        name: 'users',
        component: () => import('@/views/users/UserManagementView.vue'),
        meta: {
          titleKey: 'routes.userCenter',
          requiresAuth: true,
          roles: ['super_admin', 'management'],
        },
      },
      {
        path: 'settings/logs',
        name: 'logs',
        component: () => import('@/views/settings/LogsView.vue'),
        meta: { titleKey: 'routes.logs' },
      },
      {
        path: 'analysis',
        name: 'analysis',
        component: () => import('@/views/analysis/AnalyticsView.vue'),
        meta: { titleKey: 'routes.analysis' },
      },
      {
        path: 'telegram/send',
        name: 'telegram-send',
        component: () => import('@/views/telegram/TelegramMessageView.vue'),
        meta: { titleKey: 'routes.telegramSend' },
      },
      {
        path: 'telegram/bots/new',
        name: 'telegram-bot-new',
        component: () => import('@/views/telegram/BotFormView.vue'),
        meta: { titleKey: 'telegram.botSetup.newBotTitle' },
      },
      {
        path: 'telegram/bots/:id/edit',
        name: 'telegram-bot-edit',
        component: () => import('@/views/telegram/BotFormView.vue'),
        meta: { titleKey: 'telegram.botSetup.editBot' },
      },
      {
        path: 'telegram/settings',
        name: 'telegram-settings',
        component: () => import('@/views/telegram/TelegramSettingsView.vue'),
        meta: { titleKey: 'routes.telegramSettings' },
      },
      {
        path: 'templates',
        name: 'templates',
        component: () => import('@/views/templates/TemplatesDashboardView.vue'),
        meta: { titleKey: 'routes.templates' },
      },
      {
        path: 'instagram',
        name: 'instagram',
        component: () => import('@/views/instagram/InstagramHubView.vue'),
        meta: { titleKey: 'routes.instagramHub' },
      },
      {
        path: 'templates/new',
        name: 'template-new',
        component: () => import('@/views/templates/TemplateFormView.vue'),
        meta: { titleKey: 'routes.templateNew' },
      },
      {
        path: 'templates/media',
        name: 'template-media-library',
        component: () => import('@/views/templates/TemplateMediaLibraryView.vue'),
        meta: { titleKey: 'routes.templateMediaLibrary' },
      },
      {
        path: 'templates/:id/editor',
        name: 'template-editor',
        component: () => import('@/pages/templates/TemplateEditor.vue'),
        meta: { titleKey: 'routes.templateEditor', templateEditorLayout: true },
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/errors/ErrorView.vue'),
    props: { code: 404 },
    meta: { public: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, from, next) => {
  const auth = useAuthStore()
  await auth.ensureInitialized()

  if (to.meta.public) {
    if (auth.isAuthenticated && to.name === 'login') {
      next({ name: 'dashboard' })
    } else {
      next()
    }
  } else if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else {
    // Permission-based access: finalize and settings require super_admin or management
    const path = to.path
    if (path.startsWith('/finalize') && !auth.can('finalize')) {
      next({ name: 'error-403' })
    } else if ((path === '/settings' || path.startsWith('/settings/')) && !auth.can('settings')) {
      next({ name: 'error-403' })
    } else if (to.meta.roles && !to.meta.roles.includes(auth.role)) {
      next({ name: 'error-403' })
    } else if (to.name === 'dashboard' && auth.shouldOpenProgrammerHub) {
      next({ name: 'programmer' })
    } else if (
      (to.name === 'programmer' ||
        to.name === 'programmer-fleet' ||
        to.name === 'programmer-templates' ||
        to.name === 'programmer-register' ||
        to.name === 'programmer-user') &&
      auth.isImpersonating
    ) {
      next({ name: 'dashboard' })
    } else {
      next()
    }
  }
})

export default router
